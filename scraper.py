import requests as req
from bs4 import BeautifulSoup
import threading

class Scraper:
    def __init__(self, types):
        self.https = False
        self.socks4 = False

        if types.http_checked.get() == 1:
            self.https = True

        if types.socks4_checked.get() == 1:
            self.socks4 = True

    def scrape_proxies(self, error_scraping):
        site1 = Site1('https://free-proxy-list.net/')
        site1.get_site_content()
            


class Site1:
    def __init__(self, url):
        self.url = url

    def get_site_content(self):
        page = req.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        print(soup)