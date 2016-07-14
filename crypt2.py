import string

alphabet = string.ascii_uppercase
plaintext =  'Hflyy Lqtuw jel hfy Yxdyt-mqtuw stnyl hfy wmk, Wydyt jel hfy Noglj-xelnw qt hfyql fgxxw ej whety, Tqty jel Ielhgx Iyt neeiyn he nqy, Ety jel hfy Nglm Xeln et fqw nglm hflety, Qt hfy Xgtn ej Ielnel ofyly hfy Wfgneow xqy. Ety Lqtu he lsxy hfyi gxx, Ety Lqtu he jqtn hfyi, Ety Lqtu he rlqtu hfyi gxx gtn qt hfy nglmtyww rqtn hfyi Qt hfy Xgtn ej Ielnel ofyly hfy Wfgneow xqy.'

arrayA=[1,3,5,7,11,13,17,19,23,25]


ciphertext = ""




for keyA in arrayA:
      
      
      for keyB in range(0,26):
            print "KeyA" , keyA
            print "KeyB" , keyB

            for character in plaintext:
                if character.islower():
                     character=character.upper()
                if character in alphabet:  
                     
                    character = alphabet.find(character)
                    ciphertext = ciphertext + alphabet[(keyA * character + keyB) % len(alphabet)]
                else:

                    ciphertext = ciphertext + character
         
            /Users/john/Desktop/Krpt/crypt2.py
            print "Encrypted message : " + ciphertext
            ciphertext=""