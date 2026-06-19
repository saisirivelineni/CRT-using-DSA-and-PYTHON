'''#find minimum and maximum value
def find_min_max(arr):
    min_value = arr[0]
    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]

    return min_value, max_value

numbers = [7, 4, 1, 3, 2, 5, 0]
minimum, maximum = find_min_max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)'''

'''nums = input().split()
print(nums)
for i in range(len(nums)):
    nums[i] = int(nums[i])*2

print(nums)'''

'''nums = input().split()
print(nums)
for i in range(len(nums)):
    nums[i] = int(nums[i])**3

print(nums)'''

'''nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if i % 2 == 0:      # even index
        nums[i] = nums[i] * 2
    else:               # odd index
        nums[i] = nums[i] * 3

print(nums)'''

'''nums=list(map(int,input().split()))
for i in range(1,len(nums)):
  if i*i>=len(nums):
       break
  nums[i*i]=nums[i*i]**2
print(nums)'''

'''nums=list(map(int,input().split()))

print(nums)'''

'''#minimum
nums=list(map(int,input().split()))
curr_min=float('inf')
for i in range(len(nums)):
  if curr_min>nums[i]:
     curr_min=nums[i]
print(curr_min)'''


'''#maximum
nums = list(map(int, input().split()))

curr_max = float('-inf')

for i in range(len(nums)):
    if curr_max < nums[i]:
        curr_max = nums[i]

print(curr_max)'''



'''num=-2
if num%2==0:
    if num>1:
        print("even postive")
    else:
        print("even negative")
else:
    if num>0:
        print("odd postive")
    else:
        print("odd negative")'''

'''num=2
if num%2==0 and num>1:
    print("even positive")
    if 100%num==0:
        print("duper number")
elif num%2==0 and num<0:
    print("even negative")
elif num%2==1 and num>1:
    print("odd positive")
elif num%2==1 and num<0:
    print("odd negative")'''

#binary search
'''def h():
 for i in range(3):
     print(i)
result=(h())
print(result)'''


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


'''nums = list(map(int, input().split()))
target = int(input())

print(search(nums, target))'''