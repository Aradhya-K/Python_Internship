def remove_duplicates(input_string):

    input_list = input_string.split(',')

    seen = set()
    result = []

    for item in input_list:

        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

input_string = "6,7,9,9,1,1,5,5"

print(f"original list: {input_string}")

output_list = remove_duplicates(input_string)

print(f"list after removing duplicates : {','.join(output_list)}")