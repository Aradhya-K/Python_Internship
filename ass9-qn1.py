def calculate_stats(*nums):

    if not nums:
        return None, None, None
    min_value = min(nums)
    max_value = max(nums)
    avg = sum(nums) / len(nums)
    return min_value, max_value, avg

user_input = input("enter the numbers separated by commas: ")

input_strings = user_input.split(',')

nums = [float(num) for num in input_strings]

min_val, max_val, avg = calculate_stats(*nums)
if min_val is None:
    print("No numbers were entered")

else:
    print(f"Min: {min_val}, Max: {max_val},Average: {avg:.2f}")