def sort_by_first_value(lst):

    sorted_lst = sorted(lst, key=lambda x: x[0])
    return sorted_lst

input_list = [[1,2], [3,4], [0,6], [2,8]]
sorted_list = sort_by_first_value(input_list)

print("sorted output:")
print(sorted_list)