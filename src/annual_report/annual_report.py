from typing import List
import re
import lxml
from bs4 import BeautifulSoup
import requests
import random
import csv
import json
import time


class AnnalReport():
    site: str
    result : List[str] = []


    def __init__(self, url) -> None:
        self.site = url


    def get_request(url, query=""):
        headers = {
        'User-Agent': random.choice(
                [
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                ]
            ),
        'content-type': "text/html",
        'uule': 'w+CAIQICIHR2VybWFueQ',
        }

        response = requests.get(url, headers=headers)

        return response
    
    def parse_html(text):
        return BeautifulSoup(text, "lxml")
    

    def save_as_csv(self, name,):
        with open(f"{name}.csv", 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';')
            for el in self.result:
                spamwriter.writerow(el)
        
    def save_with_json(self, name):

        with open(f"{name}.json","w",encoding='utf-8') as flux_json:
            json.dump(self.result, flux_json,indent=4)


    def scraper_with_google(self):
        result = []
        query = f"'annual report' and 2021 site:{self.site} filetype:pdf"
        response = requests.get(f"https://google.com/search?q={query}")
        soup = self.parse_html(response.text)
        for l in soup.find_all(href=lambda a: a and re.compile(r"^/url\?q=(?P<url>.*\.pdf).*").match(a)):
            result.append(re.match(r"^/url\?q=(?P<url>.*\.pdf).*", l.get("href")).group("url"))
        self.result = result
