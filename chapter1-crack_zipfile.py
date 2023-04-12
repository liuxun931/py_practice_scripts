###
import os
import zipfile as zf
import py7zr
import threading

'''need to install py7zr to do unzip on more complicated file'''

def ext_file(zfile, pw):
	try:
		#zfile.extractall(pwd=pw)
		py7zr.unpack_7zarchive(zfile, pw)
		print("Successfully found password: %s \n" %pw)
	except Exception as e:
		print(e)

def main():
	#zfile = zf.ZipFile('crackme.zip')
	zfile = 'crackme.zip'
	plist = os.popen("cat dictionary.txt").read().split('\n')
	plist.pop()
	for p in plist:
		print(p)
		t = threading.Thread(target=ext_file, args=(zfile, p.encode('utf-8')))
		t.start()

if __name__ == '__main__':
	main()
