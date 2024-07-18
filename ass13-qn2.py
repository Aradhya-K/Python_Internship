def transform_string(s):
    chars = list(s)

    upper_case = ''.join(map(lambda c: c.upper(), chars))
    lower_case = ''.join(map(lambda c: c.lower(), chars))

    return upper_case, lower_case

input_string = "Hiii There! "
upper_case, lower_case = transform_string(input_string)

print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")