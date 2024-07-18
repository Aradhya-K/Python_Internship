def sum_of_digits(num):

    if num < 10:
        return num
    
    return num % 10 + sum_of_digits(num // 10)

num = 16789
print(sum_of_digits(num))