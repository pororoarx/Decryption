DECRYPTION

A Python Script that will accept a string as encrypted text and then the program will decrypt it using the following character substitute: 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !. The program was developed by Ken Andrea G. Legaspi for Laboratory Exercise No. 1 in the Object Oriented Programming subject.

======================================================================================================================================================================

Table of Contents

- Installation
- Usage
- Contributing
- Conclusion

======================================================================================================================================================================

- Installation

1. Clone the repository to your local machine: ‘git clone git@github.com:pororoarx/Decryption.git’
2. Install the required ‘pyfiglet’ module: ‘pip install pyfiglet’

- Usage

1. Open Git Bash and go to the project directory.
2. Run the program: ‘decryption.py’
3. Enter a string to decrypt when prompted.
4. The program will output the decrypted string in the module.

- Formulation

This program was formulated using Python. It uses the ‘pyfiglet’ module to display the program title in different font styles and is executed in the GitBash command line interface. The algorithm of the decryption program is all about replacing certain symbols with corresponding vowels:
1. Asterisk (*) is replaced with "a"
2. Ampersand (&) is replaced with "e"
3. Hash (#) is replaced with "i"
4. Plus (+) is replaced with "o"
5. Exclamation point (!) is replaced with "u"

This program employs a ‘Decryption’ class that contains a method called ‘decrypt’ that executes the decryption algorithm. The input_str attribute of the class is initialized with the user’s input during initialization, and the decrypt method outputs the decrypted string.

- Conclusion

This program executes a simple implementation of a substitution cipher using Python. This REAME.md file provides clear instructions for installing and running the program, so feel free to contribute to its development.

======================================================================================================================================================================
