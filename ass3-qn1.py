def is_alphabet(char):
        if('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            return True
        else:
            return False

def count_alphabet(str):
    alphabet_count = 0

    for char in str:
        if is_alphabet(char):
             alphabet_count=alphabet_count+1

    return alphabet_count

str=input("enter the string:")

count = count_alphabet(str)

print(f"the total number of alphabet={count} in the given string: {str}")
        