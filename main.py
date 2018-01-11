import urllib2
import pyglet
import time
import logging
from pyquery import PyQuery as pq

logging.basicConfig(filename="./logs/log.txt", 
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

def get_html():
    url = "https://shop.bitmain.com/antminer_s9_asic_bitcoin_miner.htm"
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except:
        logging.error("Error connecting to website")
        time.sleep(5)

def get_status(html):
    selector = ".btn-buy-now"
    doc = pq(html)
    return doc(selector).text()

while True:
    sleepTime = 60
    try:
        html = get_html()
        if html:
            status = get_status(html)
            if status == "Coming soon":
                logging.info("Still not available")
                time.sleep(60)
            else:
                logging.info("On sale!!!")
                while True:
                    music = pyglet.resource.media("alert.wav")
                    music.play()
                    time.sleep(10)
    except KeyboardInterrupt:
        print "We are all done here"
        exit()
