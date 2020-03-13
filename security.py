import string       #This lets us use string.ascii_letters and string.punctuation to make the alphabet. 
                    #This could all be done manually, but this saves on time and on space.
alphabet = list(string.ascii_letters) + list(string.punctuation) + [' ','\n','1','2','3','4','5','6','7','8','9','0']       #These are manually added, including spaces, and a newline. This is included so that the decryption process can make the decrypted file the exact same as the encrypted one. 
                                                                                                                            #it also means that spaces and newlines are encrypted as well. This means that sentences/paragraphs look as though they are joined in the encrypted text. Which is good for security purposes
def CaesarEncrypt(fileContent):
    
    encryptedText = ''              #The initial encrypted text is set as an empty string
    shiftedAlphabet = {}            #This is the dictionary of the above defined alphabet, this will take the shift (Defined below) and shift the alphabet by that amount. 
    
    userShift = int(input("\n\nPlease enter the shift that you want the text to be encrypted by: "))    #Asks the user for the shift, this must be an int. Polyalphabetic ciphers can use either an int or a string, or a mix (Though this would just be a string)
    
    for i in range(0, len(alphabet)):   #The actual length of the alphabet could be hardcoded here, however this enables for the alphabet to be changed without needing to change any of the code below
        letter = alphabet[i]
        shiftedLetter = alphabet[(i + userShift)%len(alphabet)]     #The modulo operator is used here to loop back around through the dictionary when the shift makes it go past the length. 
                                                                    #E.G. If the number 0 is present in the text-file, if the shift is by 1, then 0 will become 'a' in the encrypted text.  
        shiftedAlphabet[letter] = shiftedLetter     #The shifted alphabet now takes the outcome of the Shifted letter code above. 
    
    for letter in fileContent:      #For each letter in the textfile, the below code is run
        letter = shiftedAlphabet[letter]    #The letter now becomes the corresponding letter found in the shiftedAlphabet, which changed based on the users input above
        encryptedText += str(letter)        #Finally the encryptedText (Which is returned to main.py) is assigned the string outcome of 'letter'. Again, this is done for each letter in the text file. 

    return encryptedText          #This returns the encrypted text to main.py. 


def PolyEncrypt(fileContent):

    i = 0                         #The polyalphabetic key defined lower is multiplied by the length of the text (So it doesn't run out) but still needs to iterate through the different letters of the phrase. So this counter variable is created
    encryptedText = ''            #Again, like the above caeser cipher, the encrypted text is set as an empty string. 
    polyKey = input("What is the key/passphase that you want to use with the Polyalphabetic encryption: ")      #Polyalphabetic ciphers requires a key/password/passphrase, it works like it is doing multiple caesar ciphers. 
    polyKey *= len(fileContent)   #To ensure that the actual keyphrase being used is long enough, we will just multiply the user given one by the length of the content in the file.

    for letter in fileContent:    #For each letter in the text file, which has already been asigned to as 'fileContent'
        encryptedLetter = alphabet[(alphabet.index(letter) + alphabet.index(polyKey[i])) % len(alphabet)]   #The 'alphabet.index(polykey[i]) here acts the same as the userShift in the above Caesar function, 
                                                                                                            #only in this function it needs to iterate through using the key/passphrase provided by the user.
        encryptedText += str(encryptedLetter)   #Does the same thing as in the Caesar encryption above      #This is similar to the 'letter = shiftedAlphabet[letter]' code above.
        i += 1                   #Iterates up through the faux counter variable in the for loop so that the keyword changes per letter. 
    return encryptedText


def CaesarDecrypt(Content):         #The Caesar decryption process is very similar to the encryption process, only that it does it backwards (Decrypts it). To do this in code it's fairly easy, as the shift just needs to be negative.
                                    #This is why the code here is almost the exact same to the Caesar encryption process
    decryptedText = ''              #Both CaesarDecrypt and PolyDecrypt are condensed slightly (In terms of whitespace) as their function is explained above well. The additional comments on the decryptors are for explaining about the decryption process
    shiftedAlphabet = {} 
    userShift = int(input("\n\nPlease enter the shift that you want the text to be decrypted by: "))
    userShift = userShift
    for i in range(0, len(alphabet)):
        letter = alphabet[i]
        shiftedLetter = alphabet[(i + (-userShift))%len(alphabet)]      #This is where the only real change in the code is, the shift is simply reversed here. As long as the user remembers the shift they initially chose,
        shiftedAlphabet[letter] = shiftedLetter                         #then they will be able to decrypt the file using the same shift.
    for letter in Content:
        letter = shiftedAlphabet[letter]
        decryptedText += str(letter)
    return decryptedText 


def PolyDecrypt(Content):       #Just like with the Caesar decryption, this code is essentially the same as the encryption function, however just by  reversing the index of the passphrase/key
    i = 0                       
    encryptedText = '' 
    polyKey = input("What is the key/passphase that you want to use with the Polyalphabetic decryption: ")
    polyKey *= len(Content)     #In the requirements for this function it is noted that; "Zero mark if there is no loop to remove duplicate chars from the key". This can be implimented by making the polyKey var into a dictionary so that any repeating chars
    for letter in Content:      #are removed. However doing this would make the encrypted text less secure, so I have chosen to forego this requirement (As noted above it can be easily implemented if 100% neccisary)
        encryptedLetter = alphabet[(alphabet.index(letter) + -alphabet.index(polyKey[i])) % len(alphabet)]  #The only change is on this line, where the key is reversed ' -alphabet.index(polykey[i])
        encryptedText += str(encryptedLetter)
        i += 1
    return encryptedText