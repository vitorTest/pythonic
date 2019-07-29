import crypt

def testPass(cryptPass, user):
	salt 		= cryptPass[0:2]
	# dictFile	= open('dictionary.txt', 'r')
	dictFile	= open('dicToGen.txt', 'r')

	for word in dictFile.readlines():
		word 		= word.strip('\n')
		cryptWord	= crypt.crypt(word, salt)
		if(cryptPass == cryptWord):
			print("[+] Found Password to user {}: {}\nHash-Password: {}\n".format(user, word, cryptPass))
			return

	print("[-] Password Not Found For Hash: " + cryptPass + '\n')
	return

def main():
	passFile 	= open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user 		= line.split(':')[0]
			# cryptPass	= line.split(':')[1].split('-')[0]
			cryptPass	= line.split(':')[1].strip('\n')
			print("[*] Cracking Password For: " + user)
			testPass(cryptPass, user)

if __name__ == '__main__':
	main()