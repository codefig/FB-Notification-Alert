#!/usr/bin/python2.7

import mechanize
from bs4 import BeautifulSoup
import pynotify
import time


browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()

# insert custom User-Agent if u  want
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0')]

# yeah yeah I know its a bad programing practice to enclose lottsa stuff in a single "try"
# well..I'll change it someday.
while True:
  try:
    

    # uses m.facebook.com because its easier to parse,light
    # and doesn't change as often as the Desktop version


    browser.open("https://m.facebook.com/")
    time.sleep(4)
    browser.select_form(nr=0)
    

    # set your username and password here
    browser.form['email'] = ''
    browser.form['pass'] = ''
    response = browser.submit()
    

    #runs infinitely and checks for new notifications every 1 min
    while True:
     

     # if you wish to change the frequeny of updation , set the 
     # value you want in seconds here.
     time.sleep(60)
     
     browser.open("https://m.facebook.com/notifications")
     soup=BeautifulSoup(browser.response().read())
     print soup.title.string
     pynotify.init('Notification')
     Is=soup.findAll('div',attrs={ "class" : "acy apm"})
     for s in Is:
        msg=s.get_text()
        print msg
        print ""
        n=pynotify.Notification('Notification',msg)
        n.show()

  except Exception, e:

    pynotify.init('Notification')
    n=pynotify.Notification('Notification',"Connection/Authentication Failure")
    n.show()
    print "Connection/Authentication Failure"
    time.sleep(60)
  
      
