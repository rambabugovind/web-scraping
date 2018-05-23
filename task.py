
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract


size = 0
html = b''#initialize byte string

# url = 'https://9to5google.com/2018/05/22/youtube-music-premium-launch/'
url = 'https://www.cnn.com/politics/live-news/white-house-press-briefing-05-22-18/index.html'
# url = 'https://gizmodo.com/razers-redesigned-blade-gaming-laptop-gets-bigger-burl-1826216941'
# url = 'https://wordpress.stackexchange.com/questions/240629/how-can-i-link-users-across-multiple-subdomains'
response = requests.get(url, stream=True)

for chunk in response.iter_content():
    size += len(chunk)
    html += chunk

domain = '{}.{}'.format(tldextract.extract(url).domain, tldextract.extract(url).suffix)
print ('Domain: ',domain)

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
links = []
for link in soup.find_all('a'):
    if link.get('href') is not None:
        links.append(link.get('href'))
    print(link.get('href'))

print('--------------')

domain_links = []
for l in links:
    # print(l)
    if domain in urlparse(l)[1] or l.startswith('/'):
        print(l)
        domain_links.append(l)


print('Size: {} bytes'.format(size))
print(len(domain_links))
print(tldextract.extract(url))

def validate_url():
    pass

def get_size():
    pass


def get_links():
    pass


def main():
    pass



if __name__ == '__main__':
    main()