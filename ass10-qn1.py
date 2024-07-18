def is_palindrome(word):

    if len(word) <= 1:
        return True
    
    if word[0] != word[-1]:
        return False
    
    return is_palindrome(word[1:-1])

word = "radar"
print(is_palindrome(word))

word = "world"
print(is_palindrome(word))