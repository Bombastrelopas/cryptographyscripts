#This script checks a text file and tries to find phrases which have english words inside
#If it finds a lot of english words in a phrase it prints it.




from random import choice
import string

#The english dictionary
dictionary = set(open('dictionary.txt','r').read().lower().split())
max_len = max(map(len, dictionary)) #longest word in the set of words



with open('dec.txt', 'r') as myfile:
    data=myfile.readlines()




words_found = set() #set of words found, starts empty
numbwords=0
#loop for every phrase

wordlength=raw_input("enter the length of word to hack:")

for phrase in data:
    words_found.clear()
    numbwords=0
    for i in xrange(len(phrase)): #for each possible starting position in the corpus
	    chunk = phrase[i:i+max_len+1] #chunk that is the size of the longest word
	    for j in xrange(1,len(chunk)+1): #loop to check each possible subchunk
	        word = chunk[:j] #subchunk
	        if word in dictionary: #constant time hash lookup if it's in dictionary
	            
	            
	            words_found.add(word)

    
    for wu in words_found:
    	if len(wu)>=int(wordlength):
    		numbwords+=1
    		
    		if numbwords>=4:
    			#print words_found
    			print phrase
	            
	            
	            
	        	
	        	
	        	
	        	
	      	

	            	
	            	






print 'Ended hack'

#print words_found
#print 'long words:'
#print long_words