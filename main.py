import urllib2
from pyquery import PyQuery as pq
from time import sleep

url = "https://shop.bitmain.com/antminer_s9_asic_bitcoin_miner.htm"
selector = ".btn-buy-now"

response = urllib2.urlopen(url)
doc = pq(response.read())
while True:
    if doc(selector).text() == "Coming soon":
        print("Still not available")
        sleep(60)
    else:
        while True:
            winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
            sleep(5)