#code to check if string is a palindrome

def is_palindrome(word):
    """Function to check if string is a palindrome or not"""

    return word == word[::-1]

string_input = input("Enter a string ")

#Invoking is_palindrome function
print(is_palindrome(string_input))


