'''def BubbleSort(nums):
    if nums[0]>nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    return nums
nums = [5, 4, 3, 1, 2]
print(BubbleSort(nums))'''

'''#for loop bubble sort
def BubbleSort(nums):
    L=len(nums)

    for i in range(L):
        for j in range(L - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

nums = [5, 4, 3, 1, 2]
print(BubbleSort(nums))'''



'''def BubbleSort(nums):
    L=len(nums)
    c=0
    for j in range(L):
        swapped=False
        for i in range(L - 1 - j):
            c+=1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped=True
            print(c,j,i,nums)
        if not swapped:
            break

    return nums

nums = [2,4,1,9] 
print(BubbleSort(nums))'''

'''#selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))'''


'''#insertion sort
def insertion_sort(arr):
   
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    return arr'''

'''#for loop
for i in range(1, 11):
    print(i)'''

'''#while loop 
i = 1

while i <= 10:
    print(i)
    i += 1'''

'''#for loop reverse order
for i in range(10, 0, -1):
    print(i)'''

'''#while loop reverse order
i = 20

while i >= 10:
    print(i-10)
    i -= 1'''




'''#recursion reverse order
def print_numbers(n):
    if n == 0:   # base case
        return
    print(n)
    print_numbers(n - 1)

print_numbers(10)'''

'''#recursion
def print_numbers(n):
    if n == 11:   # base case
        return
    print(n)
    print_numbers(n + 1)

print_numbers(1)'''


'''i=11
while i>10:
   print(10)
   print(8)
   break'''
'''#recursion through print
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(10)'''

'''def Hello():
    for i in range(5):
        print(i)
      
        if i == 2:
            return
Hello()'''


'''def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)'''

#sum of first n natural numbers
def sum_n(10):
    if n<=0:
        return 0
    return n + sum_n(10-1)