def count_occurrences(nums, target):
    def binary_search(left_bound):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target or (left_bound and nums[mid] == target):
                left = mid + 1
            else:
                right = mid - 1
        return left
    left_index = binary_search(True)
    right_index = binary_search(False) - 1

    if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
        return right_index - left_index + 1
    return 0
nums = [1,2,3,4,5]
target = 5

print(count_occurrences(nums, target))