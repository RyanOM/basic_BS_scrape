import urllib
from BeautifulSoup import *

def main():
    
    url = raw_input('Enter URL:')
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    tags = soup('span')
    total = 0
    
    for tag in tags:
        total += int(tag.contents[0])
    
    print('Count %s' % len(tags))
    print('Sum %s' % total)
    
    
if __name__ == "__main__":
    main()
