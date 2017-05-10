import lxml.cssselect
import lxml.html
import re
import requests


class Book():
    def __init__(self, xml):
        self.xml = xml
        self.title = self.parse_title()
        self.due_date = self.parse_due_date()
        self.call_number = self.parse_call_number()

    def parse_title(self):
        title_sel = lxml.cssselect.CSSSelector('.title > a')
        title = title_sel(self.xml)[0].text_content()
        title = title.strip()
        trailing_slash = re.compile(r'\s*/')
        title = re.sub(trailing_slash, '', title)
        return title

    def parse_due_date(self):
        date_sel = lxml.cssselect.CSSSelector('.date_due > span')
        due_date = ''.join(date_sel(self.xml)[0].xpath('text()')).strip()
        return due_date

    def parse_call_number(self):
        call_number_sel = lxml.cssselect.CSSSelector('.call_no')
        call_number = ''.join(
            call_number_sel(self.xml)[0].xpath('text()')).strip()
        return call_number

    def __lt__(self, other):
        return self.call_number < other.call_number

    def __repr__(self):
        return '<Book "{}" "{}">'.format(self.call_number, self.title)


def report(books):
    result = ''
    due_date = ''
    for book in sorted(books):
        if due_date != book.due_date:
            due_date = book.due_date
            result += due_date + "\n"
        result += '    {:20}  {}\n'.format(book.call_number, book.title)
    result += '\n{} items'.format(len(books))
    return result


def load(xml):
    results = []
    tree = lxml.html.fromstring(xml)
    book_sel = lxml.cssselect.CSSSelector('#checkoutst > tbody > tr')
    [results.append(Book(book_xml)) for book_xml in book_sel(tree)]
    return results


def fetch(url, payload, filename=False):
    response = requests.post(url, payload)
    content = response.content.decode('utf-8')
    if filename:
        with open(filename, 'w') as f:
            f.write(content)
    return content


if __name__ == '__main__':
    import json
    with open('config.json', 'r') as f:
        configs = json.load(f)
    url = ''
    books = []
    for user in configs:
        if 'url' in user and user['url'] != url:
            url = user['url']
        filename = user['filename'] if user['filename'] else False
        payload = {'userid': user['username'], 'password': user['password']}
        xml = fetch(url, payload, filename)
        books.extend(load(xml))
    print(report(books))
