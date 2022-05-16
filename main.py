import sys
from scraper import Scraper


if __name__ == '__main__':
    if len(sys.argv) == 2:
        output_file = sys.argv[1]
        scraper = Scraper(output_file)
        scraper.scrape_proxies()

    else:
        print('Error processing arguments!')