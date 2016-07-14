import vigenereCipher, itertools,math
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message="Qwtguhexcymwlhtzltjiwyuxethizyetcowqbpgzcwb"
        

keyLength=2 #set the keylength

keywords = [''.join(i) for i in itertools.product(alphabets, repeat = keyLength)] #all possible iterations



myfile = open('randomphrases.txt', 'w')
for key in keywords:	
    #print key
	t=vigenereCipher.decryptMessage(key,message)
	myfile.write(t)
	myfile.write('\n')

myfile.close()
print 'decrypted'