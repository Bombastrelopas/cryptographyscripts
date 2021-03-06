
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
      
      myMessage="Qwtguhexcymwlhtzltjiwyuxethizyetcowqbpgzcwb"

      #myMessage="uye bv gmp"
      myKey= "STASSINOPOULOS"

      print decryptMessage(myKey,myMessage)
      #translated=decryptMessage(myKey,myMessage)
      #print translated
      """
      fo=open('randomphrases.txt')
      words=fo.readlines()
      fo.close()
      for word in words:
            #print word.split()[1:2]
            #mykey=word.split()[1:2]
            #print mykey[0]
            print decryptMessage(,myMessage)
            
            """
            






def encryptMessage(key, message):
     return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
     translated = [] # stores the encrypted/decrypted message string

     keyIndex = 0
     key = key.upper()

     for symbol in message: # loop through each character in message
         num = LETTERS.find(symbol.upper())
         if num != -1: # -1 means symbol.upper() was not found in LETTERS
             if mode == 'encrypt':
                 num += LETTERS.find(key[keyIndex]) # add if encrypting
             elif mode == 'decrypt':
                 num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

             num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
             if symbol.isupper():
                translated.append(LETTERS[num])
             elif symbol.islower():
                 translated.append(LETTERS[num].lower())

             keyIndex += 1 # move to the next letter in the key
             if keyIndex == len(key):
                 keyIndex = 0
         else:
             # The symbol was not in LETTERS, so add it to translated as is.
             translated.append(symbol)

     return ''.join(translated)


if __name__ == '__main__':
       main()