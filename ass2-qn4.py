def get_substring(a, start, end):
    if start < 0 or end > len(a) or start > end:
        return "invalid indices"
    return a[start:end]

def main():

    input_string = input("enter the string: ")
    start_index = int(input("enter the start index: "))
    end_index = int(input("enter the end index: "))

    substring = get_substring(input_string, start_index, end_index)

    print("the substring is:",substring)

if __name__ == "__main__":
    main()