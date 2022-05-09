import requests

class Checker:
    def __init__(self, timeout):
        self.timeout = timeout

    def check_http(self, proxy):
        schema = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

        try:
            status_code = requests.get('https://www.youtube.com/', timeout=self.timeout/1000, proxies=schema).status_code

            if status_code < 300 and status_code >= 200:
                return 1

            else:
                return 0

        except:
            return 0

    def check_socks4(self, proxy):
        schema = {
            'http': f'socks4://{proxy}',
            'https': f'socks4://{proxy}'
        }
        status_code = requests.get('https://www.google.com/', timeout=self.timeout / 1000, proxies=schema).status_code

        if status_code >= 200 and status_code < 300:
            return 1
        try:
            status_code = requests.get('https://www.google.com/', timeout=self.timeout/1000, proxies=schema).status_code

            if status_code >= 200 and status_code < 300:
                return 1

            else:
                return 0

        except:
            return 0
