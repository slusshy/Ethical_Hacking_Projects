#!/usr/bin/env python

import urllib.parse
import requests
import re

target_url="https://srgcmzn.com"
target_links=[]

def extract_links_from(url):
    response = requests.get(url)
    pattern='(?:href=")(.*?)"'
    return re.findall(pattern.encode(), response.content)

def crawl(url):
    href_links=extract_links_from(url)
    for link in href_links:
        link=urllib.parse.urljoin(url, link.decode())
        if "#" in link:
            link=link.split('#')[0]
        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)