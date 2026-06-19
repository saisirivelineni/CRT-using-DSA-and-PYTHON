
'''#sum of all numbers
nums=input()
s=0

for i in nums:
    if i.isdigit():
        s+=int(i)

print(s)'''


'''product of all numbers
nums = input()
p = 1

for i in nums:
    if i.isdigit():
        p *= int(i)

print(p)'''

'''#count of target  among all numbers
nums = input()
t=int(input())
c=0
for i in nums:
    if i.isdigit() and int(i)==t:
       c+=1

print(c)'''

'''#sum of square of all numbers
nums = [1, 2, 3, 4, 5, 6, 7]

s = 0
for num in nums:
    s += num * num

print(s)'''


'''#printing square of all numbers
nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    print(num * num)'''

'''#print all unique pair combinations in the 
nums = input().split(",")

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])'''

'''nums=input().split(",")
for i in range(1,6):
    print(nums[0],nums[i])'''

'''nums=input().split(",")
l=len(nums)
for j in range(1):
    for i in range(j+1,l):
     print(nums[j],nums[i])'''


'''nums=[1,2,3,4]
l=len(nums)#4
for i in range(l):
    for j in range(i+1,l):
        print(nums[i],nums[j])'''

'''nums = [1, 2, 3, 4, 5, 6]
l = len(nums)

for i in range(l - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        print(nums[i], nums[j])
'''


'''nums = [1, 2, 3, 4, 5, 6]

for i in range(len(nums)-1, -1, -1):
    print(nums[i])'''

'''nums=input().split()
L=len(nums)
for i in range(L):
    for j in range(i+1,L):
        print(nums[i],nums[j])'''


'''nums=input().split()
L=len(nums)
#nums.reverse()
#nums=nums[::-1]
print(nums)'''

'''nums=input().split()
L=len(nums)
list2=[]
for i in range(1,L+1):
    print(nums[L-i])
#print(nums)'''

'''#reversing list
nums=input().split()
L=len(nums)
list2=[]
for i in range(1,L+1):
    list2.append(nums[L-i])
print(list2)'''

'''nums=input().split()#reverse pairs
L=len(nums)
list2=[]
for i in range(1,L+1):
    list2.append(nums[L-i])
nums=list2
for i in range(L):
    for j in range(i+1,L):
       print(nums[i],nums[j])'''

'''nums=input().split()#reverse pairs
L=len(nums)
c=0
for i in range(L):
    for j in range(i+1,L):
        c+=1
        print(c,i,j,nums[L-i-1])'''

'''#for loop
c=0
for i in range(100,0,-2):
    c+=1
    print(i,"hello")'''

'''#nested loop
c=0
for i in range(5):
 for j in range(100):
    c+=1
    print(c,j,i,)'''

'''c=0
for i in range(17,28):
 for j in range(29,37):
    c+=1
    print(c,j,i,)'''


for i in range(109,117):
     for j in range(8,19):
         print(i,j)

