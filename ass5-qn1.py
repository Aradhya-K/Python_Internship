def find_number_in_list(list,num):
    
    return num in list
list = [10,40,60,50,34]

num = 34

if find_number_in_list(list,num):
    print(f"NUMBER {num} IS IN THE LIST.")

else:
    print(f"NUMBER {num} IS NOT IN THE LIST")