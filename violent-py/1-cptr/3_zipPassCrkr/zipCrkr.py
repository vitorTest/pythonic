#!/usr/bin/env python3

import zipfile
from threading import Thread

# hint to ZIP - zip evilPass.zip  secretPassFile -P "secret"

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=str.encode(password)) #Python3: pwd: expected bytes, got str
		return password

	except Exception as e:
		return

def main():
	zFile 		= zipfile.ZipFile("evilPass.zip")
	passFile 	= open('dictPass.txt')

	for line in passFile.readlines():
		password 	= line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()

		if t:
			print("!!! BINGO !!! => The password is " + password)
			exit(0)

if __name__ == '__main__':
	main()
