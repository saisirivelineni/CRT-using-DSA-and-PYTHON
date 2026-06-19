'''#product of all numbers
n = int(input("Enter n: "))

product = 1
for i in range(1, n + 1):
    product *= i

print(product)'''

'''#factorial 0f a number
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(-4))'''

'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(0))'''

'''#sorting order
nums = [5, 4, 3, 1, 2, 8]

sorted_nums = sorted(nums)

print(sorted_nums)'''

'''nums = [5, 4, 3, 1, 2, 8]

result = [[i] for i in nums]

print(result)'''

'''#split the list
nums = [5, 4, 3, 1, 2, 8]

size = 2

parts = [nums[i:i+size] for i in range(0, len(nums), size)]

print(parts)'''


'''#slicing
nums = [1,2,0,4,3]
def split(nums):
    l = len(nums)
    return nums[:l//2], nums[l//2:l]

print(split(nums))'''

'''nums = [1,2,0,4,3]

mid = len(nums) // 2
left = nums[:mid]
right = nums[mid:]
print("Left part:", left)
print("Right part:", right)'''

'''nums = [1, 2, 0, 4, 3]

for i in nums:
    print(i)'''

'''#merge sort
nums = [5, 4, 3, 1, 2]

def divide(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    print("Left:", left, "Right:", right)

    divide(left)
    divide(right)

divide(nums)'''

'''#Merge two sorted lists
list1 = [1, 3, 4, 6]
list2 = [2, 5, 7, 9]

i = j = 0
result = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

result.extend(list1[i:])
result.extend(list2[j:])

print(result)'''

'''def merge_lists(L1, L2):
    i, j = 0, 0
    res = []

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1

    # remaining elements
    res.extend(L1[i:])
    res.extend(L2[j:])

    return res


ans = merge_lists([1, 5, 6], [2, 3, 5, 7, 8])
print(ans)'''

'''def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res + left[i:] + right[j:]


nums = [5, 4, 1, 2, 3, 6, 8, 0]
print(merge_sort(nums))'''


class Solution(object):
    def sortArray(self, nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[:mid])
        return self.merge_lists(left,right)