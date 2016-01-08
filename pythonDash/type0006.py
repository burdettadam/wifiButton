import socket
import struct
import binascii
import urllib2

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
	# returns (<string of results>,< address it came from>)
	packet = rawSocket.recvfrom(2048)
	
	ethernet_header = packet[0][0:14]
	ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

	ethertype = ethernet_detailed[2]
	if ethertype != '\x00\x06':
		continue
	
	#only does work when ethertype 0006 detected, maybe not good enough for bigger applications
	
	detectedMac = ":".join(map(binascii.hexlify, ethernet_detailed[1]))
	#detectedMac = binascii.hexlify(ethernet_detailed[1])

	print "Button push detected from:  ", detectedMac
	
	toHit = "http://kibdev.kobj.net/sky/event/7297153A-5BDC-11E5-A831-22BDE71C24E1/buttoned/dash_button/button_pressed?mac=" + detectedMac
	
	urllib2.urlopen(toHit)
