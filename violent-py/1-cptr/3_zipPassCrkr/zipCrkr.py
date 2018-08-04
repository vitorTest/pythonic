#!/usr/bin/env python3

import zipfile

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
		guess 		= extractFile(zFile, password)

		if guess:
			print("!!! BINGO !!! => The password is " + password)
			exit(0)
		
if __name__ == '__main__':
	main()