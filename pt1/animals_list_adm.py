#!/usr/bin/env python3
# -*- coding: utf-8 -*-

animals_list = 		[
					'cat', 'dog', 'elephant', 'jaguar', 'leopard', 'monkey', 
					'penguin', 'rat', 'snake', 'tiger', 'unicorn', 'zebra'
					]

choose_msg = 		"What do you want to do? \n"\
					"type 'switch' to switch an animal for another one \n"\
					"type 'add' to add more animals \n"\
					"type 'remove' to remove an animal \n"\
					"and type 'bye' for a polite farewell \n"
					
def display_list():
	"""
		Method to display the animals list.
		Very useful to take a snap on the list after some changes.
	"""

	print( "\nThis is your list of animals: \n" + str(animals_list) + "\n" )

def switch_animal(animal_in_list, new_animal):
	"""
		User take an animal in list and change him by another 
		new choosed animal.
	"""

	if animal_in_list in animals_list:
		
		for index in range(0, len(animals_list)):
			if animals_list[index] == animal_in_list:
				animals_list[index] = new_animal
				break
			print(index)
				
	else:
		print("There is no " + animal_in_list + " in your list")

def remove_animal(animal):
	"""
		A method to remove a given animal.
	"""

	if animal in animals_list:
		animals_list.remove(animal)
	else:
		print("There is no " + animal + " in your list")


display_list()
switch_animal('snake', 'rabbit')
exit()
display_list()
switch_animal('crocodile', 'tuna')

