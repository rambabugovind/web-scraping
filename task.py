#!/usr/bin/env python3.5

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract


def get_links(html):
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.prettify())
    links = []
    for link in soup.find_all('a'):
        if link.get('href') is not None:
            links.append(link.get('href'))
        # print(link.get('href'))
    return links


def main():
    size = 0
    html = b''#initialize byte string

    #Code to get url as a commandline argument
    #usage: ./task.py [url]
    if len(sys.argv) == 2:
        url = sys.argv[1]
    elif len(sys.argv) > 2:
        print('Wrong number of command line arguments')
        print('Usage: ')
        print('./task.py [url]')
    else:
        # url = 'https://www.cnn.com/politics/live-news/white-house-press-briefing-05-22-18/index.html'
        url = 'https://httpstat.us/302'
    
    #Handle errors that may occur while fetching the webpage
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        for chunk in response.iter_content():
            size += len(chunk)
            html += chunk
    except requests.exceptions.HTTPError as err:
        print ('HTTP Error: ',err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print ('Request Exception Error: ',err)
        sys.exit(1)

    #extract domain name
    domain = '{}.{}'.format(tldextract.extract(url).domain, tldextract.extract(url).suffix)
    print ('Domain: ',domain)

    #get all links from the webpage
    links = get_links(html)

    #filter links pointing to the same domain from list of all links in the webpage
    domain_links = []
    print('Links pointing to same domain: ')
    for l in links:
        if domain in urlparse(l)[1] or l.startswith('/'):
            print(l)
            domain_links.append(l)

    print('Number of links pointing to same domain: ',len(domain_links))
    print('Size of the webpage: {} bytes'.format(size))
    # print(tldextract.extract(url))



if __name__ == '__main__':
    main()