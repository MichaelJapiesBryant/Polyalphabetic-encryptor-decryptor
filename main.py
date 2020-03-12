# In  main.py you need to read a string from the user as the original file name. 
# Then you need to open the file to read all the contents and store the content into a variable. 
# Next you need to check if the user wants to either encrypt or decrypt the file.
import security
from tkinter import Tk
from tkinter.filedialog import askopenfilename  #This enables the user to use a GUI to select the file that is wanted to be encrypted. 
                                                #The reasoning for all of this is outlined in the strategy plan  

Tk().withdraw()             #This stops the baseline tkinter window from appearing. Cleaning up the experience a little bit. 



def main():

    correctFile = False                 #This is a check as to whether or not the file chosen by the user is the correct file or not. Validation isn't needed, but is nice to have. 
    while not correctFile:              #The user selects the file that they want to encrypt or decrypt here. They can choose to either display the content of the file or not. 
        userFile = None                 #Assign the selected file as None for now. Will become the link to the text-file wanted to be encrypted. 
        userFileContent = None          #This is the variable that the text (to be encrypted) will be assigned to.

        input("Please select the file that you want to either encrypt or decrypt\nPress enter to continue\n")

        userFile = open(askopenfilename())  #This is an inbuilt function of tkinter that opens a GUI for the user to open a file. This line saves the link to the file in a variable
        userFileContent = userFile.read()   #The read() function reads from the text file previously selected. This saves the content of the selected file as a vairable. 

        fileValidation = int(input("\n\nThe path to the selected file is: %s\nWould you like to;\n1) Display the contents of the file \n2) Continue\n3) Go back\n"%(userFile.name)))
                                        #fileValidation and the following if statements just confirms with the user whether or not the file is the correct one. 
                                        #Users can choose to either display the content, continue, or if there was a mistake, they can go back and select another file. 

        if fileValidation == 1:    
            print("\n\n\n" + userFileContent)      #This prints the content of the chosen file to the terminal, including linebreaks
            if int(input("\n\nIs this the correct file?\n1) Yes\n2) No\n")) == 1:     #After showing the user, they will again be prompted to see whether or not this is the correct file.
                correctFile = True
                continue                
            else:                       #Similar to the else statement just below, if the user enters anything but 1, this means that it is not the correct file and will prompt the user to try again.
                continue
            
        elif fileValidation == 2:       #This is just for if the user doesn't want to view the content, but HAS selected the correct file
            correctFile = True
            continue

        else:                           #If the selection is 'Go back' or anything else (E.G. a random string/number) it will automatically return to the top of the main function
            continue
    


    #User will decide whether or not to encrypt or decrypt here as well as which method (Caesar or Polyalphabetic) they wish to use 
    encryptOrDecrypt = int(input("\n\n Would you like to;\n1) Encrypt the file\n2) Decrpyt the file\n3) Go back\n"))
    if encryptOrDecrypt == 1:   #If the user wants to encrypt the file, they will then be prompted to choose between the Caesar or Polyalphabetic encryption methods. 
        caesarOrPoly = int(input('\n\nWhich type of encryption would you like to use;\n1) Caesar\n2) Polyalphabetic\n'))
                                        #caesarOrPoly is used for selecting Encryption AND Decryption methods. It is assigned above, so will not break if another file is going to be chosen. 

        if caesarOrPoly == 1:   
            print("User has selected the Caesar Encryption method")
            #security(CaesarEncrypt(userFileContent) This will be added later on when security.py has been written For now it is just commented out. The same thing can be seen below. 
        elif caesarOrPoly == 2:
            print("Poly Encrypt")
            #security(PolyEncrypt(userFileContent))
        else:                           #This goes to the default of going back up to selecting a file. If the user enters 3 or any other input it will default here
            correctFile = False
            main()


    elif encryptOrDecrypt == 2:          #Similar to if the user chooses to Encrypt. The user will be prompted here for which Decryption method they want to use.
        caesarOrPoly = int(input('\n\nWhich type of decryption would you like to use; \n1) Caesar Decryption\n2) Polyalphabetic Decryption\n'))
        if caesarOrPoly == 1:
            print("Caesar Decrypt")
        elif caesarOrPoly == 2:
            print("Poly Decrypt")
        else:
            correctFile = False
            main()


    else:                       #If the user doesn't enter a valid answer (1 or 2) or enters 3, they will be taken to the top and be prompted to choose a file again. 
        correctFile = False
        main()


    
         

if __name__ == "__main__":
    main()