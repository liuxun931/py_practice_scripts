import optparse
import socket
import threading
import os, subprocess
import ipaddress

global port_list, sbnet

port_list= [22,80,257,443,4434,8080,19009]
sbnet = ipaddress.ip_network('10.100.100.0/24')

socket.setdefaulttimeout(1)
screenLock = threading.Semaphore(value = 1)
#os.popen('ulimit -n 5000').read()
subprocess.Popen('#!/bin/bash ulimit -n 6000', shell=True)


def connScan(ip, port):
	'''probe tcp socket connection by given port and ip'''
	connskt = socket.socket(family=socket.AddressFamily.AF_INET, type=socket.SocketKind.SOCK_STREAM, proto=6)
	connskt.settimeout(2)
	#screenLock.acquire()
	try:
		connskt.connect((ip, port))
		connskt.send(b'Hello Python\r\n')
		res = connskt.recv(50)
		#hostname = socket.gethostbyaddr(ip)
		print('port: %d is opening on host %s' %(port, ip))
		#print('result: %s' %res)
		connskt.close()
	except Exception as e: 
		#screenLock.acquire()
		#print(e)
		#print('port: %d is not opened on host %s.' %(port, ip))
		#screenLock.release()
		pass
	finally:
		screenLock.release()
		connskt.close()

def main():
	for i in sbnet:
		for p in port_list: 
			t = threading.Thread(target=connScan, args=(str(i),int(p)))
			t.start()

if __name__ == "__main__":
    main()
