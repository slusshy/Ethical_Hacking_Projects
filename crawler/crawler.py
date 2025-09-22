#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url="srgcmzn.com"

with open("/root/Downloads/common.txt","r")as wordlist_file:
    for line in wordlist_file:
        word=line.strip()
        test_url = target_url+ "/" + word
        response=request(test_url)
        if response:
            print("[+] Discovered a URL --> " + test_url)