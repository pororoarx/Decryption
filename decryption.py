# Start of pseudocode

# Ask the user to input a string
input_str = input("Enter an input string: ")

# Create a class called "Decryption"
class Decryption:
    def __init__(self, input_str):
        self.input_str = input_str

    # Inside the class, create and initialize a function "decrypt" that takes an input string
    def decrypt(self):
        # Create a variable called "output_str"
        output_str = ""
        # Loop through each character in the input string
        for i in range(len(self.input_str)):
            # If the character is an asterisk, add "a" to the output_str
            if self.input_str[i] == '*':
                output_str += 'a';
            # If the character is an ampersand, add "e" to the output_str
            elif self.input_str[i] == '&':
                output_str += 'e';
            # If the character is a hash symbol, add "i" to the output_str
            elif self.input_str[i] == '#':
                output_str += 'i';
            # If the character is a plus symbol, add "o" to the output_str
            elif self.input_str[i] == '+':
                output_str += 'o';
            # If the character is an exclamation point, add "u" to the output_str
            elif self.input_str[i] == '!':
                output_str += 'u';
            else:
                output_str += self.input_str[i]
        # Return the output_str
        return output_str.strip()

# Create a new object of the Decryption class and the input string of the user
# Call the decrypt function and create a variable called output_str to get the results or decrypted output

# Print the outpput string
