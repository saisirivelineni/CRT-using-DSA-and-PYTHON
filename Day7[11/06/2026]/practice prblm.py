# Day 7 Practice Problems: Space Complexity & Sorting Algorithms
def problem_1_find_max():
    # TODO: Find the maximum element in [3, 1, 8, 2] without using max().
    pass
def find_max(arr):
    if not arr:
        return None

    maximum = arr[0]

    for n in arr:
        if n > maximum:
            maximum = n

    return maximum

print(find_max([3, 1, 8, 2]))
   

def problem_2_find_min():
    # TODO: Find the minimum element in [3, 1, 8, 2] without using min().
    pass
def find_min(arr):
    if not arr:
        return None

    minimum = arr[0]

    for n in arr:
        if n < minimum:
            minimum = n

    return minimum

print(find_min([3, 1, 8, 2]))
   

def problem_3_find_second_max():
    # TODO: Find the second largest distinct element in an array.
    pass
def second_max(arr):
    first = second = float('-inf')

    for n in arr:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    return second

print(second_max([3, 1, 8, 2]))


def problem_4_find_second_min():
    # TODO: Find the second smallest distinct element in an array.
    pass
def second_min(arr):
    first = second = float('inf')

    for n in arr:
        if n < first:
            second = first
            first = n
        elif n < second and n != first:
            second = n

    return second

print(second_min([3, 1, 8, 2]))
   

def problem_5_print_even_indices():
    # TODO: Print elements located at even indices (0, 2, 4...).
    pass
def even_indices(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])

even_indices([10, 20, 30, 40, 50])

def problem_6_print_odd_indices():
    # TODO: Print elements located at odd indices (1, 3, 5...).
    pass
def odd_indices(arr):
    for i in range(1, len(arr), 2):
        print(arr[i])

odd_indices([10, 20, 30, 40, 50])
   

def problem_7_find_even_index_max():
    # TODO: Find the maximum value among elements at EVEN indices.
    pass
def even_index_max(arr):
    if not arr:
        return None

    maximum = arr[0]

    for i in range(0, len(arr), 2):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum

print(even_index_max([3, 1, 8, 2]))
 

def problem_8_find_odd_index_max():
    # TODO: Find the maximum value among elements at ODD indices.
    pass
def odd_index_max(arr):
    if len(arr) < 2:
        return None

    maximum = arr[1]

    for i in range(1, len(arr), 2):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum

print(odd_index_max([3, 1, 8, 2]))


def problem_9_print_square_indices():
    # TODO: Print elements at indices that are perfect squares (0, 1, 4, 9...).
    pass
def square_indices(arr):
    i = 0
    while i * i < len(arr):
        print(arr[i * i])
        i += 1

square_indices([10, 20, 30, 40, 50])


def problem_10_print_cube_indices():
    # TODO: Print elements at indices that are perfect cubes (0, 1, 8, 27...).
    pass
def cube_indices(arr):
    i = 0
    while i * i * i < len(arr):
        print(arr[i * i * i])
        i += 1

cube_indices([10, 20, 30, 40, 50])
   

def problem_11_check_sorted():
    # TODO: Write a function to check if an array is sorted in ascending order.
    pass
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))
print(is_sorted([3, 1, 2]))


def problem_12_bubble_sort_one_pass():
    # TODO: Perform just ONE pass of bubble sort. What does the array look like?
    pass
def bubble_one_pass(arr):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_one_pass([4, 3, 2, 1]))
  

def problem_13_bubble_sort_full():
    # TODO: Implement the full Bubble Sort algorithm.
    pass
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

print(bubble_sort([5, 1, 4, 2, 8]))


def problem_14_selection_sort_find_min_idx():
    # TODO: Find the INDEX of the minimum element in the sub-array arr[start:].
    pass
def find_min_idx(arr, start):
    min_idx = start

    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    return min_idx

print(find_min_idx([4, 2, 7, 1], 0))
  

def problem_15_selection_sort_full():
    # TODO: Implement the full Selection Sort algorithm.
    pass
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort([64, 25, 12, 22, 11]))
    

def problem_16_insertion_sort_shift():
    # TODO: Given a sorted array and a new key, shift elements right to make room for the key.
    pass
def shift_for_key(arr, key):
    arr.append(0)  # make space

    j = len(arr) - 2

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    return arr

print(shift_for_key([1, 3, 5, 7], 4))
    

def problem_17_insertion_sort_full():
    # TODO: Implement the full Insertion Sort algorithm.
    pass
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

print(insertion_sort([12, 11, 13, 5, 6]))

def problem_18_sort_descending():
    # TODO: Modify Bubble Sort to sort in DESCENDING order.
    pass
def bubble_sort_desc(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort_desc([3, 1, 5, 2]))
   

def problem_19_find_3_max():
    # TODO: Find the 3 largest elements in an array. (Hint: Sorting is easiest).
    pass
def top_3(arr):
    if len(arr) < 3:
        return None

    arr.sort(reverse=True)
    return arr[:3]

print(top_3([10, 4, 3, 50, 23, 90]))
  

def problem_20_in_place_swap():
    # TODO: Swap elements at index `i` and `j` in an array in-place.
    pass
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

print(swap([1, 2, 3, 4], 1, 3))