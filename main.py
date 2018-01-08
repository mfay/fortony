import urllib2
import pyglet
import time
from pyquery import PyQuery as pq


def log(msg):
    with open('./logs/log.txt', 'a') as f:
        f.write("[%s] %s\n" % (time.strftime("%Y-%m-%d %H:%M"), msg))

url = "https://shop.bitmain.com/antminer_s9_asic_bitcoin_miner.htm"
selector = ".btn-buy-now"

response = urllib2.urlopen(url)
doc = pq(response.read())
while True:
    if doc(selector).text() == "Coming soon":
        log("Still not available")
        time.sleep(60)
    else:
        log("On sale!!!")
        while True:
            music = pyglet.resource.media("alert.wav")
            music.play()
            time.sleep(10)
