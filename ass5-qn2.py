def substring_exists(string,substring):
    len_sub = len(substring)

    for i in range(len(string) - len_sub + 1):
        
        if string[i:i + len_sub] == substring:
            return True
    return False

main_string = "hii there,how are you?"
sub_string = "there"

if substring_exists(main_string , sub_string):
    print(f"substring '{sub_string}' found in the main string. ")

else:
    print(f"substring '{sub_string}' not found in the main string. ")