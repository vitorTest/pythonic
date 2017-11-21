#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	A fun script to apply the concepts learned is python's 
	tutorial (https://docs.python.org/3/tutorial/controlflow.html)
	'part 1'.
"""

import os
# import time

# All animals are listeded in alphabetical order and in lower case
animals_list = 		[
					'cat', 'dog', 'elephant', 'jaguar', 'leopard', 'monkey', 
					'penguin', 'rat', 'snake', 'tiger', 'unicorn', 'zebra'
					]

choose_msg =	 	"\nWhat do you want to do? \n"\
					"[=] type 'switch' to switch an animal for another one \n"\
					"[=] type 'add' to add more animals \n"\
					"[=] type 'remove' to remove an animal \n"\
					"[=] type 'display' to see your list\n"\
					"[=] and type 'bye' for a polite farewell \n"\
					"$ "

continue_msg = 		"\npress any key, to continue..."
					
def display_list():
	"""
		Method to display the animals list.

		Very useful to take a snap on the list after some changes.
	"""

	print( "\n[+] This is your current list of animals: \n" + str(animals_list) + "\n" )

def switch_animal(animal, new_animal):
	"""
		User take an animal in list and change him by another new choosed animal.
	"""

	animal_in_list = animal.lower()

	if animal_in_list in animals_list:
		
		for index in range(0, len(animals_list)):
			if animals_list[index] == animal_in_list:
				animals_list[index] = new_animal
				display_list()
				break
	else:
		print("\nThere is no '" + animal_in_list + "' in your list!\n")

	animals_list.sort()

def add_animal(animal):
	"""
		Add an animal in the list, if this is not already in the list.
	"""

	animal = animal.lower()

	if animal in animals_list:
		print("That animal is alredy on the list")
	else:
		animals_list.append(animal)

	animals_list.sort()

def remove_animal(animal):
	"""
		A method to remove a given animal.
	"""

	if animal in animals_list:
		animals_list.remove(animal)
	else:
		print("There is no '" + animal + "'' in your list")

def menu():
	"""
		This method was writed only to exemplify how python sees the switch-case flow. 
	"""

	# "What do you want to do? \n"\
	# "type 'switch' to switch an animal for another one \n"\
	# "type 'add' to add more animals \n"\
	# "type 'remove' to remove an animal \n"\
	# "and type 'bye' for a polite farewell \n"
					
	choice = input(choose_msg).lower()

	if choice in ('s', 'switch'):
		animal_in_list 	= input("Give me an animal that is in the list: ")
		new_animal		= input("Give me a new animal for replacement: ")

		switch_animal(animal_in_list, new_animal)


	elif choice in ('a', 'add'):
		animal			= input("Give me a new animal for attachment: ")

		add_animal(animal)

	elif choice in ('r', 'remove'):
		animal 			= input("Give me an animal in list, to e removed: ")

		remove_animal(animal)

	elif choice in ('d', 'display'):
		display_list()

	elif choice in ('b', 'bye', 'good bye', 'exit'):
		print("\ncheck back often\n")
		exit()

	else:
		print("\nyou wrote a invalid option!\n")


if __name__ == '__main__':

	while True:
		menu()
		input(continue_msg)
		os.system('clear')
	
