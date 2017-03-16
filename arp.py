# run script as SUDO
# To discover dash MAC address:
# - push button down for 3 seconds until it pulses blue,
# - connect your computer wifi to "Amazon ConfigureMe",
# - in a web browser, go to: http://192.168.0.1/

# notes: Address Resolution Protoco or ARP is used for mapping a network address to a physical address 
# EXAMPLE:  IP Address to a MAC address

# Change python version system-wide
# python --version
# update-alternatives --list python
# sudo update-alternatives --config python

# Update Raspberry Pi
# sudo apt-get update
# sudo apt-get dist-upgrade

# repurpose: ac:63:be:de:a0:63 (NSS)
# multivitamins: f0:27:2d:4a:96:a9 (NSS)
# wilsonjones: 84:d6:d0:da:43:b4
# MilkBaby: 0c:47:c9:ac:35:56 (not registered)
# Pets: 68:54:fd:38:e1:8c
# The Laundress: 44:65:0d:10:21:a9 (home, but flakey)

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from take_pic import pic
from send_text import SMStext
#import datetime
#import picamera
#from twilio.rest import TwilioRestClient
#import pyimgur
#from time import sleep



def arp_display(pkt):
   
    if pkt[ARP].op == 1: #who-has (request)
        #if pkt[ARP].psrc:
        if pkt[ARP].hwsrc == 'ac:63:be:de:a0:63':
            print("doorbell pressed")
            pic()
            SMStext()

if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)


