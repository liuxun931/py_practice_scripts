import optparse
import socket
import threading
import os

port_list = [22,80,257,443,4434,8080,8088,19009]
socket.setdefaulttimeout(1)
screenLock = threading.Semaphore(value = 1)
os.system('ulimit -n 65535')

def connScan(ip, port):
    
    connskt = socket.socket()
    try:
        connskt.connect((ip, port))
        connskt.send(b'violentPython\r\n')
        res = connskt.recv(50)
        screenLock.acquire()
        hostname = socket.gethostbyaddr(ip)
        print('port: %d is opening on host %s - %s' %(port, hostname, ip))
        print('result: %s' %res)
        connskt.close()
    except: 
        screenLock.acquire()
        print('port: %d is not opened on host %s.' %(port, ip))
    finally:
        screenLock.release()
        connskt.close()


def main():
	port_list = [22,80,257,443,4434,8080,8088,19009]
	ip_prefix = '10.100.100.'
	for i in range(1, 254):
		ip_addr = ip_prefix + str(i)
		for p in port_list:
			t = threading.Thread(target=connScan, args=(ip_addr,int(p)))
			t.start()
			#connScan(ip_addr, p)

if __name__ == "__main__":
    main()
