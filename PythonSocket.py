#!/usr/bin/env python3


import sys
import os 
import socket


def open_connection(ipn, prt):
   """Open TCP connection to ipnum:port.
   """
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   connect_error = s.connect_ex((ipn, prt))

   if connect_error:
      if connect_error == 111:
         usage('Connection refused.  Check address and try again.')
      else:
         usage('Error %d connecting to %s:%d' % (connect_error,ipn,prt))

   return(s)

def receive_data(thesock, nbytes):
   """Attempt to receive nbytes of data from open socket thesock.
   """
   dstring = b''
   rcount = 0  # number of bytes received
   thesock.settimeout(5)
   while rcount < nbytes:
      try:
         somebytes = thesock.recv(min(nbytes - rcount, 2048))
      except socket.timeout:
         print('Connection timed out.', file = sys.stderr)
         break
      if somebytes == b'':
         print('Connection closed.', file = sys.stderr)
         break
      rcount = rcount + len(somebytes)
      dstring = dstring + somebytes

   print('\n%d bytes received.\n' % rcount)

   return(dstring)

if __name__ == '__main__':

   thesocket = open_connection('128.111.17.41', 80)
   thesocket.send(b'GET /~phys129/lipman/ HTTP/1.0\r\nHOST: web.physics.ucsb.edu\r\n\r\n')
   indata = receive_data(thesocket, 4096)
   thesocket.shutdown(socket.SHUT_RDWR)
   thesocket.close()

string = indata.decode()
#pint(string)
start = string.find('"greenss">')
end = string.find('</span></p>')
#pirnt(start)
#print(end)

print()
print('The Physics 129 announcements were last updated on: ', string[start + 10: end])
print()
