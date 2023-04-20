## test for hash crack
import crypt
import socket
import threading


def testPass(cryptPass):
	salt = cryptPass[0:2]
	if salt == '$6':
		print("found crypting : SHA512")
		salt = '$6$'
	if salt == '$5':
		print("found crypting: SHA256")
		salt = '$5$'
	if salt == '$1':
		print("found crypting: MD5")
		salt = '$1$'
	dictFile = open('dictionary.txt', 'r')
	for w in dictFile.readlines():
		w = w.strip('\n')
		cryptWord = crypt.crypt(w, salt)
		print(cryptWord)
		if (cryptWord == cryptPass):
			print("[+] Found Password : " + w + "\n")
			return
	print("Password not found in dict file.")
	return

def crackUser(user, key):
	print("cracking pw for user : %s" %user)
	testPass(key)

def main():
    crackUser('admin', '$6$$GI93GOf2RUu53i5mLrIL5RvnDF1sv9IP2Jh8KPt53BcIMCvBGob3jHOuaPx7fM1lJIPuHQceJexCdzOfihtjL/')
	
if __name__ == '__main__':
	main()
