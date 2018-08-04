#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	Playing with python, writing a net scanner
	(in theory). Reading the book:
		"Violent Python - TJ. O'Connor - 2013"
	And re-writing the book's scripts in python 3.
"""
import socket
import argparse
import os


def retBanner(ip, port):
	"""
		Return the host's response.

		It try to connect to a host with a given port,
		if it can, then will return a banner with
		the answer from host.
	"""

	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)	
		return banner

	except Exception as e:
		print("[-]Error = " + str(e) + '\n')
		return

def checkVulns(banner):
	"""
		It try to find a vulnerability.

		Comparing the banner message with the phrases
		from the vulnerabilities' dictionary.
	"""
	f = open(file_name, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print("[+] Server is vulnerable: " + banner.strip('\n'))		
	
def main():

	parser = argparse.ArgumentParser(description="A scanner concept" 
		"(totaly useless in real life)).")
	parser.add_argument('-d', default='vuln_banners.txt',
		help='pass a dictionary of vulnerabilities')
	parser.add_argument('-i', default='192.168.0.1',
		help='pass a initial ip to start')
	parser.add_argument('-e', default=255, type=int,
		help='pass the last host to evaluate')

	args = parser.parse_args()

	file_name 	= args.d
	ip_base 	= args.i[:10]
	first_host	= int(args.i[10:])
	last_host	= args.e + 1
	portList 	= [21, 22, 25, 80, 110, 443]

	if not os.access(file_name, os.R_OK):
		print("You haven't permission to access " + file_name)
		return

	for x in range(first_host, last_host):
		ip = ip_base + str(x)
		for port in portList:
			print("[+] Trying to reach {} at port {}".format(ip, port))
			banner = retBanner(ip, port)
			if banner:
				print('[+] ' + ip + ': ' + banner.strip('\n'))
				checkVulns(banner) 
	

if __name__ ==  '__main__':
	main()

