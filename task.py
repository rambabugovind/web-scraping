
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# resp1 = requests.get('http://www.youtube.com')
# print(len(resp1.content))
# resp = requests.head('http://www.ramgov.com')
# print(resp.headers['Content-Length'])

size = 0
html = b''#initialize byte string

# url = 'https://9to5google.com/2018/05/22/youtube-music-premium-launch/'
# url = 'https://www.cnn.com/politics/live-news/white-house-press-briefing-05-22-18/index.html'
url = 'https://gizmodo.com/razers-redesigned-blade-gaming-laptop-gets-bigger-burl-1826216941'
response = requests.get(url, stream=True)
# size = sum(len(chunk) for chunk in response.iter_content())
# print(response.text)
for chunk in response.iter_content():
    size += len(chunk)
    html += chunk

# print(html)
# parsed_uri = urlparse(url)
# domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
domain = urlparse(url)[1]
print ('Domain: ',domain)

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
links = []
for link in soup.find_all('a'):
    if link.get('href') is not None:
        links.append(link.get('href'))
    print(link.get('href'))

# linkstodomain = SoupStrainer('a', href=re.compile(domain))
print('--------------')
# print(linkstodomain)
for l in links:
    # print(l)
    if domain in urlparse(l)[1] or l.startswith('/'):
        print(l)

# with open()

print('Size: {} bytes'.format(size))
# print(html)

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