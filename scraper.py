import time

import requests as req
from bs4 import BeautifulSoup
from save_proxies import SaveProxies
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Site1:
    def __init__(self, main_class):
        self.http_proxy_urls = ('https://free-proxy-list.net/', 'https://www.sslproxies.org/', 'https://www.us-proxy.org/')
        self.main = main_class

    def get_http_proxies_site_1(self):
        http_proxies = []
        for url in self.http_proxy_urls:
            soup = self.main.get_site_content(url)

            proxy_list = soup.find(id='list').div.find('tbody')

            for proxy_item in proxy_list:
                proxy_info = proxy_item.find_all('td')

                ip = proxy_info[0].get_text()
                port = proxy_info[1].get_text()

                http_proxies.append(f'{ip}:{port}')

        http_proxies = list(dict.fromkeys(http_proxies))

        for proxy in http_proxies:
            self.main.http_proxies_scraped.append(proxy)


class Site2(Firefox, By):
    def __init__(self, main_class):
        self.main = main_class
        self.proxy_lists = ('https://openproxy.space/list/http',)
        Firefox.__init__(self)

    def get_site_2_http_proxies(self):
        self.get(self.proxy_lists[0])
        time.sleep(2)

        textbox = self.find_element(self.XPATH, '/html/body/div[1]/div/div/div/div[1]/section[4]/textarea')
        proxy_list = textbox.text.rstrip().split('\n')

        for proxy in proxy_list:
            self.main.http_proxies_scraped.append(proxy)

        self.quit()


class Scraper(Site1, Site2, SaveProxies):
    def __init__(self, output_path):
        SaveProxies.__init__(self, output_path)
        Site1.__init__(self, self)
        Site2.__init__(self, self)

        self.http_proxies_scraped = []
        self.output_path = output_path

    def scrape_proxies(self):
        self.get_http_proxies_site_1()
        self.get_site_2_http_proxies()
        self.save_proxies(self.http_proxies_scraped)

    def get_site_content(self, url):
        page = req.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
