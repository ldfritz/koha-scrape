import json
import lxml.cssselect
import lxml.html
import re
import sys


def get_title(book):
    title_sel = lxml.cssselect.CSSSelector('.title > a')
    title = title_sel(book)[0].text_content()
    inner_space = re.compile(r'\s+/?\s*\n?\s*')
    title = re.sub(inner_space, ' ', title).strip()
    return title


def get_due_date(book):
    date_sel = lxml.cssselect.CSSSelector('.date_due > span')
    due_date = ''.join(date_sel(book)[0].xpath('text()')).strip()
    return due_date


def get_call_number(book):
    call_number_sel = lxml.cssselect.CSSSelector('.call_no')
    call_number = ''.join(call_number_sel(book)[0].xpath('text()')).strip()
    return call_number


def book_summary(books):
    summary = ''
    cur_date = ''
    for due_date, call_number, title in sorted(books):
        if cur_date != due_date:
            cur_date = due_date
            summary += cur_date + "\n"
        summary += '    {:20}  {}\n'.format(call_number, title)
    summary += '\n{} items'.format(len(books))
    return summary


def parse(filenames):
    books = []
    for filename in filenames:
        tree = lxml.html.parse(filename)
        book_sel = lxml.cssselect.CSSSelector('#checkoutst > tbody > tr')
        for book in book_sel(tree):
            books.append(
                (get_due_date(book), get_call_number(book), get_title(book)))
    return books

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        configs = json.load(f)
    filenames = [config['filename'] for config in configs]
    books = parse(filenames)
    summary = book_summary(books)
    with open('report.txt', 'w') as f:
        f.write(summary)
    print(summary)
