## test for conn ports

import socket
import threading

def conn_test(ip, port):
	'''try socket conn on given ip and port'''		
	socket.setdefaulttimeout(1)
	s = socket.socket()
	try:
		s.connect((ip, port))
		rcv = s.recv(1024)
		print('%s ssh: %s' %(ip, rcv) )
	except Exception as e:
		#print("Error = " + ip + ":" + str(port) + " conn: " + str(e))
		pass

def main():
	ip = ''
	port = 22
	for i in range(1,254):
		ip = '10.100.100.' + str(i)
		t = threading.Thread(target=conn_test, args=(ip, port))
		t.start()
	
if __name__ == '__main__':
	main()
