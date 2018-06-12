#!env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re


def get_baidu_links(page_url):
    # page_url = "http://www.91baiduyun.com/thread-38640-166-1.html"
    soup = BeautifulSoup(requests.get(page_url).content, "lxml")
    links = [re.findall(r'\https://pan.baidu.com.*', content.text)[0] for content in soup.find_all("td", class_ = "t_f")]
    for link in links:
        print(link)

    

def main():
    url = "http://www.91baiduyun.com/thread-38640-1-1.html"
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    last_page_url = [ a["href"] for a in soup.find("div", class_="pg").find_all("a")][-2]
    get_baidu_links(last_page_url)


if __name__ == '__main__':
    main()
