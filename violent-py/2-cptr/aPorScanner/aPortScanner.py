#!/usr/bin/env python3

import socket

def main():

	print(socket.gethostbyname("www.google.com"))
	print(socket.gethostbyaddr('157.240.222.35'))


if __name__ == '__main__':
	main()
