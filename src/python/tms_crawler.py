import requests
import bs4
import json
import threading
from constants import BASE_URL
from utility import SerializeableJSON, RowData, TMSClass, Encoder

def get_college_page_sublinks(page):
    sublinks = []
    for child in page.find('table', class_="collegePanel").children:
        if child.find('div'):
            curr = child.find('div')
            while curr > 0:
                anchor = curr.find('a')
                if isinstance(anchor, bs4.element.Tag):
                    sublinks.append((anchor.text, anchor.get('href')))
                curr = curr.next_sibling 
    return sublinks


def get_classes_on_college(page):
    classes = []

    sublinks = get_college_page_sublinks(page)
    for title, link in sublinks:
        c = get_classes_on_page(link)
        print(title)
        classes.append(
            dict(
                classesCategory=title,
                classes=c
            )
        )
    return classes

def get_classes_on_page(page):
    page = BASE_URL + page
    page_request = requests.get(page)
    if page_request.status_code != 200:
        return []
    
    soup = bs4.BeautifulSoup(page_request.text, 'html.parser')
    child_tags = []

    i = 0
    for child in soup.find('tr', class_="tableHeader").parent.children:
        if isinstance(child, bs4.element.Tag):
            data = RowData(child, i)
            child_tags.append(data)
            i += 1

    child_tags = filter(lambda row: row.has_data(), child_tags)
    child_tags = [json.loads(TMSClass(row).toJSON()) for row in child_tags]

    return child_tags

def get_colleges_thread_runner(page_url, class_section, class_list, threaded=False):
    college_page = requests.get(BASE_URL + page_url).text
    college_page = bs4.BeautifulSoup(college_page, 'html.parser')

    if threaded:
        lock = threading.Lock()
        lock.acquire(True)
    print(class_section)
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
    
    # print(json.dumps(class_list, indent=4))
    return class_list

def get_quarters(page):
    ret = []
    links = page.find_all('div', class_='term')
    for link in links:
        l = link.find('a')
        ret.append([l.text, l.get('href')])

    return ret



class Crawler:

    def __init__(self):
        print("Created crawler: {}".format(str(self)))
        self.update()
    
    def update(self):
        page = requests.get('https://termmasterschedule.drexel.edu/webtms_du/app')
        if page.status_code != 200:
            print("Error code: {}".format(page.status_code))
            
        page = bs4.BeautifulSoup(page.text, 'html.parser')

        self.quarters = get_quarters(page)

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

            print(quarter[0])
            for _ in range(3):
                page = requests.get(BASE_URL + quarter[1])

                if page.status_code == 200:
                    break
                else:
                    print(page.status_code)
            else:
                continue
            
            page = bs4.BeautifulSoup(page.text, 'html.parser')

            all_classes = get_colleges_from_side_left(page, threaded=True)

            with open('./{}.json'.format(quarter[0]), 'w') as _file:
                _file.write(json.dumps(all_classes, cls=Encoder, indent=4))
