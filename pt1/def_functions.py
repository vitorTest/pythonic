#/usr/bin/env python3
# -*-coding: utf-8 -*-

list_txt = open('shop_list.txt', 'w')

title   =   "Please, after work bring me that: "

# my_list = 		[
# 				'banana', 'coal', 'cola', 'strawberries',
# 				'soap', 'orange', 'rice', 'oil',
# 				]
my_list = 		[# item, quantity, type
				('banana', 2, 'food'),
				('coal', 1, 'fuel'),
				('cola', 3, 'food'),
				('soap', 4, 'hygiene'),
				('orange', 6, 'food'),
				('rice', 1, 'food'),
				('oil', 1, 'food'),
				]
to_buy 		=   {
				'author': 	"Joana D'arc",
				'data': 	'12/08/2018',
				'urgency':	'low',
				'mall': 	'target',
				}

dict_details = 	{
				'title': 	title,	#This will be passed
				's_list':	my_list, #This will not e passed to *s_list
				'details':	to_buy,	#This will e passed
				}

# (*args, **kwargs)
def shopping_list(title, debug=False, *s_list, **details):
	"""
		A sample to exemplify the pessages of the *argument and **keyWordsArgsments.
	"""

	if debug==True:
		print(title)
		print(s_list)
		print(details)
	else:
		print("There is your list: ")

		for item in s_list:
			print(item)

		print('-' * 40)
		#print(details['Author'])

		for detail in details:
			print(detail, ": ", details[detail])
	

def quick_list_as_txt(file, note, pos_separator, *args):
	"""
		An Arbitrary List Arguments sample.		
	"""
	# print(note, pos_separator, args, sep='\n')
	file.write(note + pos_separator.join(args))

def sort_list_by(choice=0):
	"""
		Only to use lambda
	"""

	my_list.sort(key=lambda item: item[choice])

sort_list_by(0)
print(my_list)

# shopping_list(title, my_list, to_buy) // The two arguments are passed to *args, is an interesting sample to be observed

# shopping_list("Hello darling", True,'waffles', 'juice', 'pepper', 'a new car', 'cookies', 
# 				Author="Ronaldo",
# 				Data="12/03/2019",
# 				Urgency="Medium", 
# 				Mall="Wathever")

#shopping_list(**dict_details, debug=True)

#quick_list_as_txt(list_txt, "Hey, buy me those please!\n", '\n', 'waffles', 'juice', 'pepper', 'a new car', 'cookies')

"""
	An interesting sample that shows some of arg's behavior.
	to use it, comment line 42, and uncomment line 41
"""
#quick_list_as_txt(list_txt, "This is a quick message\n", ['pop-corn', 'meat', 'knife'], ['test1', 'test2', 'test3'])