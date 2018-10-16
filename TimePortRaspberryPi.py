#!/usr/bin/env python3

from time import localtime
import sys
import os
import socket

def bind_port(prt):
	"""Create socket and bind to port.
	"""
	host = '' #bind to all available interfaces
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse port
	s.bind((host, prt))
	s.listen(1)

	return(s)

if __name__ == '__main__':
	port = 55555
	thesocket = bind_port(port)
	time = localtime()
	outdata = (b'\nThe time is %d:%d' %(time[3], time[4]))

	while True:
		connection, peer = thesocket.accept()
		print('Sending data to %s...' % repr(peer), end = '')
		connection.sendall(outdata)
		print('Done.\n')
		connection.shutdown(socket.SHUT_RDWR)

