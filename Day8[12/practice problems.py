# Day 8 Practice Problems: Advanced Sorting & Recursion
def problem_1_recursion_base_case():
    # TODO: Write a recursive function print_num(n) that prints n down to 1. Don't forget the base case!
    pass
def print_num(n):
    if n <= 0:
        return
    print(n)
    print_num(n - 1)

print_num(5)


def problem_2_recursive_sum_array():
    # TODO: Write a recursive function to sum elements in an array. Base case: empty array -> 0.
    pass
def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])

print(sum_array([1, 2, 3, 4]))
 

def problem_3_merge_two_sorted_lists():
    # TODO: Given lst1 = [1, 3] and lst2 = [2, 4], use a two-pointer approach to merge them into [1, 2, 3, 4].
    pass
def merge(lst1, lst2):
    res = []
    i = j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    res.extend(lst1[i:])
    res.extend(lst2[j:])

    return res

print(merge([1, 3], [2, 4]))
    

def problem_4_merge_sort_split():
    # TODO: Write just the 'Divide' part of Merge Sort. Return the left_half and right_half.
    pass
def split_list(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

print(split_list([1, 2, 3, 4]))
    

def problem_5_merge_sort_full():
    # TODO: Combine your logic from problem 3 and 4 to implement full Merge Sort.
    pass
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

print(merge_sort([5, 2, 4, 1, 3]))
    

def problem_6_quick_sort_partition():
    # TODO: Given arr and a pivot, create lists for elements < pivot, == pivot, and > pivot.
    pass
def simple_partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, middle, right

print(simple_partition([3, 1, 4, 2], 3))
    

def problem_7_quick_sort_full():
    # TODO: Implement full Quick Sort using list comprehensions for the partitioning step.
    pass
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([5, 1, 4, 2, 8]))


def problem_8_sort_tuples():
    # TODO: Use Python's built-in sorted() to sort a list of tuples by their SECOND element.
    # Ex: [(1, 3), (2, 1), (4, 2)] -> [(2, 1), (4, 2), (1, 3)]
    pass
def sort_by_second(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

print(sort_by_second([(1, 3), (2, 1), (4, 2)]))
 

def problem_9_sort_strings_by_length():
    # TODO: Sort ["apple", "bat", "cherry"] by length, shortest first.
    pass
def sort_by_len(words):
    return sorted(words, key=len)

print(sort_by_len(["apple", "bat", "cherry"]))


def problem_10_recursive_string_reverse():
    # TODO: Reverse a string using recursion.
    pass
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))
   

def problem_11_recursive_power():
    # TODO: Write a recursive function to calculate base^exp.
    pass
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)



def problem_12_quick_sort_descending():
    # TODO: Modify Quick Sort to sort in descending order.
    pass
def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]

    return quick_sort_desc(left) + mid + quick_sort_desc(right)


def problem_13_check_stability_concept():
    # TODO: Will the dictionary method for grouping anagrams (Day 4) maintain the original order of words?
    pass
result = {
        "listen": ["listen", "silent"],
        "eat": ["eat", "tea", "ate"]
    }

print(result)
   
def problem_14_merge_three_arrays():
    # TODO: You have 3 sorted arrays. How would you merge them using your merge() function from Problem 3?
    pass
def merge_three(l1, l2, l3):
    return merge(merge(l1, l2), l3)


def problem_15_recursive_fib_memoization():
    # TODO: Implement recursive Fibonacci, but use a dictionary to "remember" calculated values (memoization).
    pass
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
   


def problem_16_find_median_unsorted():
    # TODO: Find the median of an unsorted list of integers (hint: sort it first).
    pass
def find_median(arr):
    arr = sorted(arr)
    mid = len(arr) // 2

    if len(arr) % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    return arr[mid]

def problem_17_sort_ignoring_case():
    # TODO: Sort ["Banana", "apple", "Cherry"] ignoring case.
    pass
def sort_ignore_case(words):
    return sorted(words, key=str.lower)
    

def problem_18_sort_dictionaries_by_value():
    # TODO: Given data = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}], sort by 'age'.
    pass
def sort_dicts(data):
    return sorted(data, key=lambda x: x["age"])


def problem_19_in_place_partition():
    # TODO: Challenge: Do the Quick Sort partition step in-place by swapping elements without creating new lists.
    pass
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
   

def problem_20_in_place_quicksort_full():
    # TODO: Challenge: Implement the full Quick Sort recursively using the in-place partition.
    pass
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)