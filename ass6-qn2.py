def generate_tuples(list1, list2):
    result = [(a,b) for a in list1 for b in list2 if a!= b]
    return result

x = [1,2,3]
y = [1,2,3]

result = generate_tuples(x,y)

print(result)