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

    def scrape_proxies(self):
        site1 = Site1('https://free-proxy-list.net/')
        site1.get_proxies()


class Site1:
    def __init__(self, url):
        self.url = url

    def get_site_content(self):
        page = req.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_proxies(self):
        soup = self.get_site_content()

        proxy_list = soup.find(id='list').div.find('tbody')

        for proxy_item in proxy_list:
            proxy_info = proxy_item.find_all('td')
            ip = proxy_info[0].get_text()
            print(ip)