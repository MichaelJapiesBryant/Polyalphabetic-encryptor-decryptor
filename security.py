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