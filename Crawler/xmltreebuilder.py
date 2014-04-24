from HTMLParser import HTMLParser
import sys
import urllib
url = "http://iopscience.iop.org/1742-6596/"
urltext = urllib.urlopen(url)
output = urltext.read()
globalstack = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    stack = []
    
    def handle_starttag(self, tag, attrs):
        self.stack.append(tag) 
        
    def handle_endtag(self, tag):
        self.stack.pop()
        
    def handle_data(self, data):
        if data.find("PDF") != -1: 
            print "Reached PDF:", data
            temp = self.stack
            print(temp)
            string = str(temp)
            globalstack.append(string)
        


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(output)

import xml.etree.ElementTree as ET
errorlist = []
root = []
try:
    root.append(ET.fromstring(output))
except:
    errorlist.append(sys.exc_info()[0])
    pass
    
