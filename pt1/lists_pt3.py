#! /usr/bin/env python3
# -*- using: utf-8 -*-

from collections import deque #Fastest queue in multi-universes
import random


def list_as_stack(): 
	"""
		To test stacks
	"""
	list_in = ['black', 'extreme', 'thrash', 'power', 'speed', 'classic']
	print("This is the metal list\n {}".format(list_in))

	list_in.append('love')
	print("Appending: \n {}".format(list_in))

	print("popping four times")

	for i in range(0, 4):
		list_in.pop()
		print(list_in)

def list_as_queue():
	"""
		To test queues
	"""
	list_on 	= deque(['Glória', 'Joana'])
	f 			= open("clients_list.txt")

	while list_on:
		caos 		= random.randrange(0, 1024)

		if caos % 2 == 0:
			print("{} was served!".format(list_on[0]))
			list_on.popleft()
			print("queue status: " + str(list_on) + '\n')
		else:
			costumer = f.readline()
			if costumer.strip() != '':
				list_on.append(costumer.strip())
				print("A new costumer in the queue!")
				print("queue status: " + str(list_on) + '\n')

	print("All clients satisfied!")

list_as_queue()




