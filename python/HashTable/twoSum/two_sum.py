def two_sum(nums, target):
    hash_table = {}

    for idx, num in enumerate(nums):
        if num not in hash_table:
            hash_table[num] = idx
        num1 = target - num
        if num1 in hash_table and hash_table[num1] != idx:
            return [hash_table[num1], idx]
    return False

print(two_sum([3, 2, 4], 6))

