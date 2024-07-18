def print_character_at_index():

    user_string = input("enter a string:")

    index = int(input("enter an index:"))

    if 0 <= index < len(user_string):

        print(f"the character at index {index} is '{user_string[index]}'")

    else:

        print("index out of range")

print_character_at_index()


    