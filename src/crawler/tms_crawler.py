import requests
import bs4
import json
import threading
import datetime
from crawler.constants import BASE_URL, GREEN, RESET, BOLD, BLUE
from crawler.utility import RowData, TMSClass, Encoder


def get_page(page, meta="", retries=3):
    for _ in range(retries):
        response = requests.get(page)

        if response.status_code == 200:
            break
        else:
            print('{}\nLink: {}\nStatus code: {}\n'.format(datetime.datetime.now(), page, response.status_code))
    else:
        return None

    print('{blue}{bold}{}{reset}{green}{}s elapsed{reset}'.format(meta,
                                                                  response.elapsed.total_seconds(),
                                                                  green=GREEN,
                                                                  reset=RESET,
                                                                  bold=BOLD,
                                                                  blue=BLUE))

    return bs4.BeautifulSoup(response.text, 'html.parser')


def get_college_page_sublinks(page):
    sublinks = []
    for child in page.find('table', class_="collegePanel").children:
        if isinstance(child, bs4.element.Tag) and child.find('div'):
            curr = child.find('div')

            while curr is not None:
                anchor = curr.find('a')
                if isinstance(anchor, bs4.element.Tag):
                    sublinks.append((anchor.text, anchor.get('href')))
                curr = curr.next_sibling 
    return sublinks


def get_classes_on_college(page):
    classes = []

    sublinks = get_college_page_sublinks(page)
    for title, link in sublinks:
        c = get_classes_on_page(link, title)
        classes.append(
            dict(
                classesCategory=title,
                classes=c
            )
        )
    return classes


def get_classes_on_page(page, title):
    soup = get_page(BASE_URL + page, meta='{}: '.format(title))

    if soup is None:
        return []

    child_tags = []

    i = 0
    for child in soup.find('tr', class_="tableHeader").parent.children:
        if isinstance(child, bs4.element.Tag):
            data = RowData(child, i)
            child_tags.append(data)
            i += 1

    child_tags = [json.loads(TMSClass(row).toJSON()) for row in list(filter(lambda row: row.has_data(), child_tags))]

    return child_tags


def get_colleges_thread_runner(page_url, class_section, class_list, threaded=True):
    college_page = get_page(BASE_URL + page_url, meta='{}: '.format(class_section))

    if threaded:
        lock = threading.Lock()
        lock.acquire(True)
    class_list.append(
        dict(
            collegeName=class_section, 
            collegeSubcategories=get_classes_on_college(college_page)
        )
    )

    if threaded:
        lock.release()


def get_colleges_from_side_left(page, threaded=False):

    threads = []

    class_list = []
    colleges = page.find(id='sideLeft').find_all('a')
    colleges = [[college.text, college.get('href')] for college in colleges]
    
    for college in colleges:
        if threaded:
            threads.append(threading.Thread(target=get_colleges_thread_runner, args=(college[1], college[0], class_list)))
        else:
            get_colleges_thread_runner(college[1], college[0], class_list, threaded=threaded)

    if threaded:
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    
    return class_list


def get_links_to_terms(page):
    ret = []
    links = page.find_all('div', class_='term')
    for link in links:
        l = link.find('a')
        ret.append([l.text, l.get('href')])

    return ret


class Crawler:

    def __init__(self):
        print("Created crawler: {}".format(str(self)))
        self.quarters = []
        self.update()
    
    def update(self):
        page = get_page('https://termmasterschedule.drexel.edu/webtms_du/app')

        self.quarters = get_links_to_terms(page)

    def crawl(self):
        for quarter in self.quarters:
            quarter[0] = "".join(quarter[0]
                                    .replace('-', '_')
                                    .replace('Quarter', '-Q')
                                    .replace('Semester', '-S')
                                    .replace('Fall', 'Fa')
                                    .replace('Winter', 'Wi')
                                    .replace('Spring', 'Sp')
                                    .replace('Summer', 'Su')
                                    .split(' ')
                                 )

            page = get_page(BASE_URL + quarter[1], meta='{}: '.format(quarter[0]))

            if page is None:
                continue

            all_classes = get_colleges_from_side_left(page, threaded=True)

            with open('./.tmp/{}.json'.format(quarter[0]), 'w') as _file:
                _file.write(json.dumps(all_classes, cls=Encoder, indent=4))
