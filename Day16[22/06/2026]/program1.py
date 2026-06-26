'''#minheap
import heapq
nums=[7,1,4,3]
heapq.heapify(nums)
print(nums)'''


'''import heapq
nums=[8,1,2,3,6,7]

min_heaq=[]
for i in nums:
    heapq.heappush(min_heaq,i)
print(min_heaq)'''


'''import heapq
nums=[8,1,2,3,6,7]

#deletion
min_heaq=[]
for i in nums:
    heapq.heappush(min_heaq,i)
for i in min_heaq:
    heapq.heappop(min_heaq)
    print(min_heaq)'''

'''import heapq

nums = [5,7,8,9,10]

min_heap = []
for i in nums:
    heapq.heappush(min_heap, i)

for i in nums:
    print(min_heap[0],min_heap)
    heapq.heappop(min_heap)'''
    

'''#maxheap
import heapq

nums = [10,8,20,7,6,15]
nums = [-num for num in nums]
heapq.heapify(nums)
print(nums)

nums = [-num for num in nums]  
print(nums)'''

'''import heapq

nums = [10,8,20,7,6,15]
max_heap=[]
nums = [-num for num in nums]
for i in nums:
 heapq.heappush(max_heap,i)

print(max_heap)'''


'''import heapq

nums = [10,8,20,7,6,15]
max_heap=[]
nums = [-num for num in nums]
for i in nums:
    heapq.heappush(max_heap,i)
for i in nums:
    print(max_heap)
    heapq.heappop(max_heap)'''

min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
    if len(min_heap)>k:
        heapq.heappop(min_heap)
return min_heap[0]
