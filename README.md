# Term one Python assignment
## Text encryption using Caesar and Polyalphabetic ciphers

The purpose of this assignment is to create a program that can encrypt and decrypt text files using at least *two* encryption methods. The two encryption methods built into the program are the **Caesar cipher** and **Vigènere cipher** encryption methods. As well as being able to encrypt a text file, the program will also be able to decrypt a text file that has already been encrypted with either one of the above mentioned ciphers. 

These two encryption methods are a relavitvely lightweight and effective way to encrypt files. While not the most secure, they still provide some security and will successfully encrypt any text files (Providing that they contain English text. Punctuation and numbers are also encrypted.).

The features found in this program available to the users are; 
- Ability to encrypt a file by using the Caesar cipher
- Ability to decrypt a file that has already been encrypted using the Caesar cipher. 
- Ability to encrypt a file by using the Vigènere cipher. 
- Ability to decrypt a text file that has already been encrypted using a Vigènere cipher. 
- File dialog UI enabling the user to select a text file without the need of the command line. 

##How to use
1. The first requirement to use the program is to have a text file already written that you wish to encrypt. If a text file has already been encrypted then that can be used as well.
2. Once starting the program, follow the written prompts to select the text file that you want to have encrypted or decrypted. This is done using a GUI file dialog to find the file.
3. The program will then prompt as to whether you would like to display the content of the file, continue, or go back. What these options does is fairly self explanitory. 
4. After selecting continue. You will be asked whether you want **Encrypt** or **Decrypt** the file. 
5. After selecting either encrypting or decrypting, you will be asked if you want to use the **Caesar cipher** or the **Vigènere polyalphabetic cipher**
6. You will then be asked which key or shift you would like to use on the text file. Once this is chosen, a text file will be created in the root directory of the program named either 'Caesar_Encrypted(decrypted)' or 'Poly_encrypted(decrypted)' with the encrypted (Or decrypted, if that was chosen) text. 

Created by [Michael](https://twitter.com/The_Japies) [ Bryant](https://github.com/MichaelJapiesBryant)