from random import choice
import string

dictionary = set(open('dictionary.txt','r').read().lower().split())
max_len = max(map(len, dictionary)) #longest word in the set of words


with open('apokript.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

#print data

data_with_space=data.replace("a","") #Test to see if a letter is put there for no reason


text = data #.join([choice(string.ascii_lowercase) for i in xrange(28000)])
#text += '-'+text[::-1] #append the reverse of the text to itself

words_found = set() #set of words found, starts empty
for i in xrange(len(text)): #for each possible starting position in the corpus
    chunk = text[i:i+max_len+1] #chunk that is the size of the longest word
    for j in xrange(1,len(chunk)+1): #loop to check each possible subchunk
        word = chunk[:j] #subchunk
        if word in dictionary: #constant time hash lookup if it's in dictionary
            words_found.add(word) #add to set of words

long_words =set() #long words set


#Find the long words first 
for w in words_found:
	if len(w)>2:
		long_words.add(w)
#print words_found
print 'long words:'
print long_words