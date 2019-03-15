#!/usr/bin/env python3

import zipfile
import argparse #The book uses optparse... I think that I prefeer to try with argparse
from threading import Thread


# hint to ZIP - zip evilPass.zip  secretPassFile -P "secret"

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=str.encode(password)) #Python3: pwd: expected bytes, got str		
		return password

	except Exception as e:
		return

def main():

    parser = argparse.ArgumentParser(description='A password protected zip file, cracker')

    parser.add_argument('-f', metavar='ZIP_FILE',  help='Give the name of the file')
    parser.add_argument('-d', metavar='DICTIONARY', help='Give a dictionary')
    args = parser.parse_args()

    if not args.f:
        print("You must give me a zip file, -h for help")
        exit(0)
    if not args.d:
        print("You must give me a dictionary, -h for help")
        exit(0)

    zFile = zipfile.ZipFile(args.f)
    passFile = open(args.d)

	# zFile 		= zipfile.ZipFile("evilPass.zip")
	# passFile 	= open('dictPass.txt')

    for line in passFile.readlines():
    	password 	= line.strip('\n')
    	t = Thread(target=extractFile, args=(zFile, password))
    	t.start()

        #I move the password's print here, because when the password is found
        #the program exits and closes, instead of continuing to try to extract.
    	if t:
    		print("!!! BINGO !!! => The password is " + password)
    		exit(0)

if __name__ == '__main__':
	main()
