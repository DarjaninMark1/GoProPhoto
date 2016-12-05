
from HTMLParser import HTMLParser
import re, urllib, os, urllib2, time

GoProUrl = 'http://127.0.0.1:8000/'

repeat = True
while repeat:
    print('take a photo?')
    if raw_input() == "close":
         repeat = False

    print('taking photo')
     #take a photo
    #urllib.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=1').read()

    #create folder on desktop
    newpath = os.path.expanduser("~/Desktop/GoPro_Photos/")
    if not os.path.exists(newpath): os.makedirs(newpath)

    #wait until GoPro make file and save it
    time.sleep(0.5)

    print('searching diectory')
    #find biggest directory
    urlDir = ''
    class MyDIRParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            global urlDir
            for i in attrs:
                if i[0] == 'href' and re.match('.*GOPRO', i[1]):
                    urlDir = i[1]


    parser = MyDIRParser()
    parser.feed(urllib.urlopen(str(GoProUrl)).read())

    #if urlDir != '':
        #print urlDir
    print('searching photo')
    #find biggest/last *.jpg
    url = ''
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            global url
            for i in attrs:
                if i[0] == 'href' and re.match('.*JPG', i[1]):
                    url = i[1]


    parser = MyHTMLParser()
    parser.feed(urllib.urlopen(str(GoProUrl) + str(urlDir)).read())

    #if url != '':
        #print 'taky test' + str(url) + 'test'
    print('downloading' + str(url))
    #save biggest *.jpg
    f = urllib2.urlopen(str(GoProUrl) + str(urlDir) + str(url))
    jpg = open (str(newpath) + 'http://127.0.0.1:8000/102GOPRO/Ferrari003.jpg','w')
    jpg.write(f.read())
    jpg.close()

    print str(url) + ' downloaded'
