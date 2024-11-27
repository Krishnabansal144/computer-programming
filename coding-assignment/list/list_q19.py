# find second larrgest element
def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums = [n for n in nums if n != largest]
    return max(nums) if nums else None

# Example usage:
nums = [10, 20, 4, 45, 99, 99]
print(second_largest(nums))  # Output: 45