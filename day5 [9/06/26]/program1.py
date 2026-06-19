'''nums=[1, 2, 3, 4, 5]
print('nums')'''

'''for loop
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)'''

'''while loop
nums = [1, 2, 3, 4, 5]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1'''


'''nums=[1, 2, 3, 4, 5]
print(nums[4])#
print(nums[-3])
print(nums[4])#2
print(nums[::-1])#variable_name[start:end:step]
print(nums[4:1:-1])
print(nums[::3])'''

'''nums=[1, 2, 3, 4, 5]
print(nums[1:10:-1])#'''


'''even numbers
nums=[1,2,3,4,5]

for i in range(1,101):
    if i%2==0:
       print(i)'''


'''odd numbers
nums=[1,2,3,4,5]

for i in range(1,101):
    if i%2==1:
       print(i)'''

'''nums=[1,2,3,4,5]
x=0
for i in range(1,101):
    x+=1
    print(x)'''

'''nums=[1,2,3,4,5]

for i in range(1,101,2):
    print(2)'''


'''nums=[1,2,3,4,5]
for i in range(0,101,2):
    print(i)'''

'''print(5)'''
nums=[1,2,3]

'''nums.append(4)
print(nums)'''

'''nums.clear()
print(nums)'''

'''nums=[1,2,3]
nums.append(4)
x=nums.copy()
print(nums)
nums.clear()
print(nums,x)'''

nums=[1,1,2,3]
nums.append(4)
x=nums.copy()
print(nums)
nums.clear()
print(x.count(1))