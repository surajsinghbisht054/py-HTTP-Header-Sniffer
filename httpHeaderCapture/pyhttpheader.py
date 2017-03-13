#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    https://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''

import socket

s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
	data=s.recvfrom(65565)
	try:
		if "HTTP" in data[0][54:]:
				print "[","="*30,']'
				raw=data[0][54:]
				if "\r\n\r\n" in raw:
					line=raw.split('\r\n\r\n')[0]
					print "[*] Header Captured "
					print line[line.find('HTTP'):]
				else:
					print raw
		else:
			#print '[{}]'.format(data)
			pass
	except:
		pass