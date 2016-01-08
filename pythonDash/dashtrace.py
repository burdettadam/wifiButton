import socket
import struct
import binascii

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

count = 0

print ""

while True:

	packet = rawSocket.recvfrom(2048)
	
	ethernet_header = packet[0][0:14]
	ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
	
	MAC_source = ethernet_detailed[1]
	if MAC_source != '\xf0\x27\x2d\xa9\xb3\x75':
		count += 1
		print "\033[F", count
		continue
	
	ethertype = ethernet_detailed[2]
	
	print "Dest MAC:     ", binascii.hexlify(ethernet_detailed[0])
	print "Source MAC:   ", binascii.hexlify(MAC_source)
	print "Type:         ", binascii.hexlify(ethertype)
	print ""
	
	if ethertype == '\x08\x06':
		arp_header = packet[0][14:42]
		arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
		print arp_detailed, "\n"