import requests
import traceback

class Checker:
    def __init__(self, timeout, main_object):
        self.main_object = main_object
        self.timeout = timeout

    def check_http(self, proxy):
        schema = {
            "http": f'http://{proxy}',
            "https": f'http://{proxy}',
        }

        try:
            status_code = requests.get('https://api.ipify.org/?format=json', timeout=float(self.timeout/1000), proxies=schema).status_code
            if status_code < 300 and status_code >= 200:
                if __name__ == '__main__':
                    self.main_object.working_http.append(proxy)

        except Exception as e:
            pass

    def check_socks4(self, proxy):
        schema = {
            'http': f'socks4://{proxy}',
            'https': f'socks4://{proxy}'
        }

        try:
            status_code = requests.get('https://api.ipify.org/?format=json', timeout=float(self.timeout/1000), proxies=schema).status_code

            if status_code < 300 and status_code >= 200:
                self.main_object.working_socks.append(proxy)

            else:
                return 0

        except:
            return 0

