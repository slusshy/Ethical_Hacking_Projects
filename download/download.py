#!/usr/bin/env python

import requests

def download(url):
    get_response=requests.get(url)
    file_name=url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://www.gran-turismo.com/images/c/i1V6C4zrs9MMcSB.jpg")