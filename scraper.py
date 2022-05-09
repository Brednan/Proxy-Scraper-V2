import requests as req
from bs4 import BeautifulSoup
import threading

class Scraper:
    def __init__(self, types, timeout):
        self.https = False
        self.socks4 = False
        self.proxies_scraped = []

        if types.http_checked.get() == 1:
            self.https = True

        if types.socks4_checked.get() == 1:
            self.socks4 = True

    def scrape_proxies(self):
        site1 = Site1(self)
        site1.get_http_proxies()
        site1.get_socks_proxies()
        print(self.proxies_scraped)


class Site1:
    def __init__(self, main_class):
        self.http_proxy_urls = ('https://free-proxy-list.net/', 'https://www.sslproxies.org/', 'https://www.us-proxy.org/')
        self.socks4_url = 'https://www.socks-proxy.net/'
        self.main = main_class

    def get_site_content(self, url):
        page = req.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_http_proxies(self):
        http_proxies = []
        for url in self.http_proxy_urls:
            soup = self.get_site_content(url)

            proxy_list = soup.find(id='list').div.find('tbody')

            for proxy_item in proxy_list:
                proxy_info = proxy_item.find_all('td')

                ip = proxy_info[0].get_text()
                port = proxy_info[1].get_text()

                http_proxies.append(f'{ip}:{port}')

        http_proxies = list(dict.fromkeys(http_proxies))

        for proxy in http_proxies:
            self.main.proxies_scraped.append({
                'proxy': proxy,
                'type': 'http'
            })

    def get_socks_proxies(self):
        socks4_proxies = []
        soup = self.get_site_content(self.socks4_url)

        proxy_list = soup.find(id='list').div.find('tbody')

        for proxy_item in proxy_list:
            proxy_info = proxy_item.find_all('td')

            ip = proxy_info[0].get_text()
            port = proxy_info[1].get_text()

            socks4_proxies.append(f'{ip}:{port}')

        socks4_proxies = list(dict.fromkeys(socks4_proxies))

        for proxy in socks4_proxies:
            self.main.proxies_scraped.append({
                'proxy': proxy,
                'type': 'socks4'
            })
