from flask import Flask, render_template, jsonify
import requests
import bs4
import json
import re
import datetime

BASE_URL = "https://termmasterschedule.drexel.edu"

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SerializeableJSON):
            return obj.toJSON()

        return json.JSONEncoder.default(self, obj)

class SerializeableJSON:
    def toJSON(self):
        return json.dumps(self.__dict__)

class RowData(SerializeableJSON):
    def __init__(self, fields, index):
        self.row = []
        self.index = index
        field = fields.find('td')
        while field is not None:
            if isinstance(field, bs4.element.Tag):
                if field.a is not None:
                    self.row.append([field.text.strip(), str(field.a.get('href'))])
                else:
                    self.row.append(field.text.strip())

            field = field.next_sibling
    def has_data(self):
        return len(self.row) > 0 and len(self.row[0]) > 0

def to_dt(time):
    time = time.split(' ')
    am_pm = time[-1]
    try:
        hours, minutes = time[0].split(':')
    except ValueError:
        return None
    hours = int(hours)
    minutes = int(minutes)
    if am_pm in "PMpmPmpM" and hours != 12:
        hours += 12
    return str(datetime.time(hours, minutes if minutes < 60 else 59, 0, 0))


def get_credits(page):
    page = requests.get(page).text
    page = bs4.BeautifulSoup(page, 'html.parser')
    cred = page.find(class_ = "tableHeader", text="Credits").parent.find(class_ = "even")
    cred = cred.text.strip()
    enroll = page.find(class_ = "tableHeader", text="Enroll").parent.find(class_ = "odd")
    enroll = int(enroll.text.strip())
    max_enroll = page.find(class_ = "tableHeader", text="Max Enroll").parent.find(class_ = "even")
    max_enroll = int(max_enroll.text.strip())
    return [cred, enroll, max_enroll]

def symboltime_to_datatime(time_range):
    time_range = time_range.split(' - ')
    time_range = map(to_dt, time_range)
    return time_range
class TMSClass(SerializeableJSON):
    def __init__(self, row):
        self.index = row.index
        self.SC = row.row[0]
        self.CN = row.row[1]
        self.IT = row.row[2]
        self.IM = row.row[3]
        self.SEC = row.row[4]
        self.CRN = row.row[5]
        if isinstance(self.CRN, list) and len(self.CRN) >= 2:
            self.CRN[1] = (BASE_URL + self.CRN[1])
        self.CT = row.row[6]
        dt = row.row[7].split('\n')
        if len(dt) > 1:
            dt[1] = symboltime_to_datatime(dt[1])
            self.DT = {
                'days': dt[0],
                'times': dt[1]
            }
        else:
            self.DT = dt
        self.IN = row.row[8]
        tmp = None
        try:
            info = get_credits(self.CRN[1])
            tmp = float(info[0])
            self.MAX = info[2]
            self.ENROLL = info[1]
        except:
            tmp = ""

        self.CR = tmp

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
    classes = {}

    sublinks = get_college_page_sublinks(page)
    for title, link in sublinks:
        c = get_classes_on_page(link)
        classes.update({title: c})
    return classes

# page = requests.get("https://termmasterschedule.drexel.edu/webtms_du/app?component=subjectDetails&page=CollegesSubjects&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDCyNToJHhmXlAaYXA0sQiEG1ooWtoCQAiXVdwpgAAAA%3D%3D&sp=SA&sp=SARTH&sp=0")

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

home = "".join(open('./cci_home.html').readlines())
home_soup = bs4.BeautifulSoup(home, 'html.parser')

page = requests.get('https://termmasterschedule.drexel.edu/webtms_du/app?component=collSubj&page=CollegesSubjects&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=5').text

classes = get_classes_on_college(bs4.BeautifulSoup(page, 'html.parser'))

# print(json.dumps(classes, cls=Encoder, indent=4))

with open('./output.json', 'w') as out:
    json.dump(classes, out, cls=Encoder, indent=4)
    # out.write(json.dumps(classes, cls=Encoder, indent=4).replace('\\"', '"').replace('\\\\\\"','"'))

# for section in classes:
#     for tms in section[1]:
#         if isinstance(tms, TMSClass):
#             print(tms.toJSON())

# d = RowData()
# print(d.toJSON())

# print(last_tag.parent)
# print(soup.find(class='.tableHeader'))



app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/output.json')
def get_output():
    # return jsonify(
    return app.response_class(
        response="".join(open('./output.json', 'r').readlines()),
        mimetype='application/json'
    )
    # )
    # return json.dumps("".join(open('./output.json', 'r').readlines()))


if __name__ == '__main__':
    app.run()
