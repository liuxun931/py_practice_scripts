#!_*_encoding:utf-8_*_

import paramiko
import threading,os,time
import ipaddress as ip

#global username, password, mynetwork, filename, port, comm, para
global network, filename, para

mynetwork = ip.ip_network('10.100.100.0/24')
filename = ('ssh_conn_' + time.ctime() + '.txt').replace(" ", "_")

port = 22
username='admin'
password='vpn@123'

#comm = 'ls /home/admin'
comm = 'ip addr| grep net'
para = {"hostname":'', "port":port, "username":username, "password":password, "timeout":3, "comm":comm}

os.system('touch ./%s' %(filename))

def ssh_conn(hostname, port, username, password, timeout, comm):
	conn = paramiko.client.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sceenLock = threading.Semaphore(value=1) 
	try:
		conn.connect(hostname=hostname,port=port, username=username, password=password, timeout=timeout)
		#print("connect to %s success." %hostname)
		row = "%s has connected. " %hostname
		stdin, stdout, stderr = conn.exec_command(comm)
		output = stdout.read().decode()
		conn.close()
		cmd = ('echo %s >> ' %row)+ filename
		print(hostname)
		print(output)
		os.system(cmd)
	except Exception as e:
		sceenLock.release()
		#print("failed to connect to %s ." %hostname)
		#print(hostname + str(e))
		conn.close()
	finally:
		conn.close()
		sceenLock.release()

		
def main():
	for i in mynetwork:
		para['hostname'] = str(i)
		#print(para)
		t = threading.Thread(target=ssh_conn, kwargs=para)
		t.start()
	
if __name__ == "__main__":
	main()
