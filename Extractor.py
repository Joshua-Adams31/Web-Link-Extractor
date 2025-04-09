from urllib.request import urlopen
from html.parser import HTMLParser

import queue;

my_queue = queue.Queue()
invalidURLs = []
hyperlinks = []

# HTML parser that extracts hyperlinks from HTML content
class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for attr in attrs:
                if(attr[0] == "href"):
                    hyperlinks.append(attr[1])
        

parser = MyHTMLParser()

# Get the URLs from the user
my_queue = input("Enter the links seperated by commas: ").split(",")

# Loop through the URLs and extract hyperlinks
while(len(my_queue) > 0):
    url = my_queue.pop(0)
    try:
        response = urlopen(url)
    except:
        invalidURLs.append(url)
        continue
    html = response.read().decode('utf-8')
    parser.feed(html)

    parser.reset()



#print("Invalid URLs:")
#for url in invalidURLs:
    #print(url)

print("Hyperlinks extracted#")
#for link in hyperlinks:
   #print(link)