def is_palindrome(str):
    return str[::-1]
input_string =  input("enter the string:")

res = is_palindrome(input_string)

if res == input_string:
    print("it is a palindrome")
    
else:
    print("it is not a palindrome")