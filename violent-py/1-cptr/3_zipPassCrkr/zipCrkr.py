#!/usr/bin/env python3

import zipfile
import argparse
from threading import Thread

# hint to ZIP - zip evilPass.zip  secretPassFile -P "secret"

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=str.encode(password)) #Python3: pwd: expected bytes, got str
		print("!!! BINGO !!! => The password is " + password)
		
		return password

	except Exception as e:
		return 

def main():

	parser = argparse.ArgumentParser(description='A ZIP decypher')

	zFile 		= zipfile.ZipFile("evilPass.zip")
	passFile 	= open('dictPass.txt')

	for line in passFile.readlines():
		password 	= line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()
