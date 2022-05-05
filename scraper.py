import requests as req
from bs4 import BeautifulSoup
import threading

class Scraper:
    def __init__(self, types):
        self.https = False
        self.socks4 = False
        self.proxies_scraped = []

        if types.http_checked.get() == 1:
            self.https = True

        if types.socks4_checked.get() == 1:
            self.socks4 = True

    def scrape_proxies(self):
        site1 = Site1(self)
        site1.get_proxies()
        print(self.proxies_scraped)


class Site1:
    def __init__(self, main_class):
        self.urls = ('https://free-proxy-list.net/', 'https://www.sslproxies.org/')
        self.main = main_class

    def get_site_content(self, url):
        page = req.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_proxies(self):
        proxies = []
        for url in self.urls:
            soup = self.get_site_content(url)

            proxy_list = soup.find(id='list').div.find('tbody')

            for proxy_item in proxy_list:
                proxy_info = proxy_item.find_all('td')

                ip = proxy_info[0].get_text()
                port = proxy_info[1].get_text()

                proxies.append(f'{ip}:{port}')

        proxies = list(dict.fromkeys(proxies))

        for proxy in proxies:
            proxy = proxy.split(':')

            self.main.proxies_scraped.append({
                'ip': proxy[0],
                'port': proxy[1],
                'type': 'http'
            })
