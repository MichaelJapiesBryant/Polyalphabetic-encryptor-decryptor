import string       #This lets us use string.ascii_letters and string.punctuation to make the alphabet. 
                    #This could all be done manually, but this saves on time and on space.
alphabet = list(string.ascii_letters) + list(string.punctuation) + [' ','\n','1','2','3','4','5','6','7','8','9','0']



def CaesarEncrypt(fileContent):

    encryptedText = ''              #The initial encrypted text is set as an empty string
    shiftedAlphabet = {}            #This is the dictionary of the above defined alphabet, this will take the shift (Defined below) and shift the alphabet by that amount. 
    
    userShift = int(input("\n\nPlease enter the shift that you want the text to be encrypted by: "))
    
    for i in range(0, len(alphabet)):   #The actual length of the alphabet could be hardcoded here, however this enables for the alphabet to be changed without needing to change any of the code below
        letter = alphabet[i]
        shiftedLetter = alphabet[(i + userShift)%len(alphabet)]     #The modulo operator is used here to loop back around through the dictionary when the shift makes it go past the length. 
                                                                    #E.G. If the number 0 is present in the text-file, if the shift is by 1, then 0 will become 'a' in the encrypted text.  
        shiftedAlphabet[letter] = shiftedLetter
    
    for letter in fileContent:
        letter = shiftedAlphabet[letter]
        encryptedText += str(letter)

    return encryptedText          #This returns the encrypted text to main.py. 


def PolyEncrypt(fileContent):

    i = 0                         #The polyalphabetic key defined lower is multiplied by the length of the text (So it doesn't run out) but still needs to iterate through the different letters of the phrase. So this counter variable is created
    encryptedText = ''            #Again, like the above caeser cipher, the encrypted text is set as an empty string. 
    polyKey = input("What is the key/passphase that you want to use with the Polyalphabetic encryption: ")      #Polyalphabetic ciphers requires a key/password/passphrase, it works like it is doing multiple caesar ciphers. 
    polyKey *= len(fileContent)   #To ensure that the actual keyphrase being used is long enough, we will just multiply the user given one by the length of the content in the file.

    for letter in fileContent: 
        encryptedLetter = alphabet[(alphabet.index(letter) + alphabet.index(polyKey[i])) % len(alphabet)]   #The 'alphabet.index(polykey[i]) here acts the same as the userShift in the above Caesar function, 
                                                                                                            #only in this function it needs to iterate through using the key/passphrase provided by the user.
        encryptedText += str(encryptedLetter)
        i += 1                   #Iterates up through the faux counter variable in the for loop so that the keyword changes per letter. 
    return encryptedText