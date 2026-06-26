'''nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print([seen[complement], i])  
        break

    seen[num] = i'''

#Two sums
'''nums = [2, 7, 11, 15]
T = 9

hash_table = {}

for i in range(len(nums)):
    c = T - nums[i]

    if c in hash_table:
        print([i, hash_table[c]])
        break
    else:
        hash_table[nums[i]] = i'''

'''#contains Duplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}

        for num in nums:
            if num in hash_table:
                return True
            hash_table[num] = 1

        return False'''

'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True'''
#count of each character
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True

          