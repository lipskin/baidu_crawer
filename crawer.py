#!env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import pdb

def get_baidu_links(page_url):
    # page_url = "http://www.91baiduyun.com/thread-38640-166-1.html"
    print(page_url)
    soup = BeautifulSoup(requests.get(page_url).content, "lxml")
    try: 
        links = [re.findall(r'\https://pan.baidu.com.*', content.text)[0] for content in soup.find_all("td", class_ = "t_f")]
        for link in links:
            print("<a href='%s'>%s</a><br/>" % (link, link))
    except IndexError:
        print("This page don't have baidu link")

    

def enter_content(url):
    # url = "http://www.91baiduyun.com/thread-38640-1-1.html"
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    last_page_url = [ a["href"] for a in soup.find("div", class_="pg").find_all("a")][-2]
    last_url_id = re.findall(r'\d+', last_page_url)[-2]
    page_urls = [last_page_url]
    page_urls.append(last_page_url.replace(last_url_id, str(int(last_url_id)-1)))
    # page_urls.append(last_page_url.replace(last_url_id, str(int(last_url_id)-2)))
    for page_url in page_urls:
        get_baidu_links(page_url)


def main():
    url = "http://www.91baiduyun.com/forum-37-1.html"
    # soup = BeautifulSoup(requests.get(url, headers={"Content-Type": "text/html; charset=utf-8"}).content, "lxml")
    links = [a for a in re.findall(r'<a.*s xst', requests.get(url).text)]
    content_urls = []
    for link in links:
        if bool(re.search(r'bold', link)):
            continue
        elif bool(re.search(r'http', link)):
            content_urls.append(re.search(r'http://www\.91baiduyun\.com/thread-.*-1\.html', link).group())
        else:
            continue
    for content_url in content_urls[:3]:
        enter_content(content_url)
     


if __name__ == '__main__':
    main()
