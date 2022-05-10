import time
from checker import Checker

def test_func(proxy):
    checker = Checker(timeout=5000)
    print(checker.check_http(proxy))

test_func('169.57.1.85:8123')