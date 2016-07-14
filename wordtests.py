import vigenereCipher
ciphered="Qwtguhexcymwlhtzltjiwyuxethizyetcowqbpgzcwb"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr=[]

keylength=3 #Change this to get different key-lenghts

for let in alphabet:
    print let ,": " ,ciphered.count(let)
#s,p interesting key letters
"""
for letter in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            for letter4 in alphabet:
                for letter5 in alphabet:

                         key=  letter+ letter2 +letter3 +letter4 +letter5 #+letter6
                         #print 'Letter:' , letter ,': ' ,ciphered.count(letter)
                         deciphered= vigenereCipher.decryptMessage(key,ciphered)
                         
                         pos=0
                         for let in alphabet:  #put the number of appearence of each letter to the array
                             arr.append(deciphered.count(let))
                             pos+=1


                         
                         if arr[25]==0 and arr[9]==0 and arr[23]==0:

                            if arr[4]>=3 and arr[19]>=3 and arr[0]>=1:
                                 print key , ": " , deciphered
                                 #print arr
                         del arr[:]
                         key="" #restore key to no value
                         """