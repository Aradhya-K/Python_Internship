def find_char(matrix, char):
    found = False
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    if num_rows ==0 or num_cols == 0:
        print("not found")
        return
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if matrix[row_index][col_index] == char:
                print(f"Row: {row_index}, Column: {col_index}")
                found = True
                break
        if found:
            break
    if not found:
        print("not found")
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h,', 'i']
]
char = input("enter the character to find: ")
find_char(matrix,char)
