import crypt
import random
import string

users_list 		= open('usersList.txt', 'r')
generated_file 	= open('passwords.txt', 'w')

def get_word():
	return random.choice(open('dicToGen.txt', 'r').readlines()).strip('\n')

def get_pass(user):
	salt 	= random.choice(string.ascii_letters).upper()
	salt 	= random.choice(string.ascii_letters).upper() + salt
	word 	= get_word()

	return crypt.crypt(word, salt)

def main():
	
	for line in users_list.readlines():
		user 		= line.split('.')[1].strip('\n')
		password 	= get_pass(user)
		get_pass(user)

		generated_file.writelines('{}:{}\n'.format(user, password))

if __name__ == '__main__':
	main()