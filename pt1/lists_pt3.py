#! /usr/bin/env python3
# -*- using: utf-8 -*-

from collections import deque #Fastest queue in multi-universes
import random

#
#	LISTS COMPREHENSIONS
#

def tst_list_comp():
	list_of_squares = [x**2 for x in range(10)]
	list_of_cubes = list(map(lambda x: x**3, range(10)))
	list_combined = [[x, y] for x in list_of_squares for y in list_of_cubes if x != y]

	# print("Squares: {}".format(list_of_squares))
	# print("Cubes: {}".format(list_of_cubes))
	print("The two lists combined: {}".format(list_combined))

def tst_nest_list():

	matrix = [ 
		[17, 73, 75, 7],
		[11, 22, 33, 44],
		[90, 98, 87, 76],
		[59, 37, 49, 1]
	]		

	#transposed = [[linha[i] for linha in matrix] for i in range(4)]

	#In the real world, you should prefer built-in functions to complex flow statements
	transposed = list(zip(*matrix))
	print(transposed)

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


tst_nest_list()