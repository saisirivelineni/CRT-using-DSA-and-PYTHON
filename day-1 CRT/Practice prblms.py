# Day 1 Practice Problems: Python Fundamentals, Variables, Data Types & Operators


def problem_1_basics():
    # TODO: Print "Hello, Python!" to the console
    pass
def problem_1_basics():
    print("Hello, Python!")
    

def problem_2_variables():
    # TODO: Create a variable called 'user_age' and set it to 25.
    # TODO: Create a variable called 'user_name' and set it to "Alice".
    # TODO: Print a message saying "Alice is 25 years old."
    pass
def problem_2_variables():
    user_age = 25
    user_name = "Alice"
    print(user_name, "is", user_age, "years old.")
    

def problem_3_datatypes():
    # TODO: Create a variable 'price' with the value 19.99
    # TODO: Use the built-in type() function to print the data type of 'price'
    pass
def problem_3_datatypes():
    price = 19.99
    print(type(price))
    

def problem_4_type_casting():
    # TODO: You have a string variable: str_num = "50"
    # TODO: Convert it into an integer, add 10 to it, and print the result.
    str_num = "50"
    pass
def problem_4_type_casting():
    str_num = "50"
    print(int(str_num) + 10)
    


def problem_5_arithmetic():
    # TODO: Calculate the total bill for 3 coffees.
    # Each coffee is $4.50. The tax is a flat $1.50.
    # Store the result in 'total_bill' and print it.
    pass
def problem_5_arithmetic():
    coffee_price = 4.50
    num_coffees = 3
    tax = 1.50
    print((coffee_price * num_coffees) + tax)
    

def problem_6_modulo():
    # TODO: Create a variable 'number' and set it to 15.
    # TODO: Use the modulo operator (%) to find the remainder when 'number' is divided by 2.
    # Print the remainder.
    pass
def problem_6_modulo():
    number = 15
    print(number % 2)
    


def problem_7_lists():
    # TODO: Create a list named 'fruits' containing "apple", "banana", and "cherry".
    # TODO: Print the second item in the list ("banana").
    pass
def problem_7_lists():
    fruits = ["apple", "banana", "cherry"]
    print(fruits[1])
    


def problem_8_dictionaries():
    # TODO: Create a dictionary named 'student' with keys "name" and "grade".
    # Set "name" to "John" and "grade" to "A".
    # TODO: Print the student's grade.
    pass
def problem_8_dictionaries():
    student = {"name": "John", "grade": "A"}
    print(student["grade"])

def problem_9_comparison():
    # TODO: You have a saved password "secret123" and an input password "secret123".
    # TODO: Create a variable 'is_match' that uses the equality operator (==) to compare them.
    # Print 'is_match'.
    saved_pwd = "secret123"
    input_pwd = "secret123"
    pass
def problem_9_comparison():
    saved_pwd = "secret123"
    input_pwd = "secret123"
    print(saved_pwd == input_pwd)
    
def problem_10_logical():
    # TODO: To get a discount, a customer must be a member (is_member = True)
    # AND must have spent over $50 (spent = 60).
    # TODO: Create a boolean variable 'gets_discount' using logical operators and print it.
    is_member = True
    spent = 60
    pass
def problem_10_logical():
    is_member = True
    spent = 60
    print(is_member and (spent > 50))
    
def problem_11_string_formatting():
    # TODO: Use an f-string to print "My favorite language is Python." 
    # Use the variable provided below inside the f-string.
    language = "Python"
    pass
def problem_11_string_formatting():
    language = "Python"
    print(f"My favorite language is {language}.")
   
def problem_12_string_methods():
    # TODO: Convert the string 'shout' to uppercase using a string method and print it.
    shout = "hello"
    pass
def problem_12_string_methods():
    shout = "hello"
    print(shout.upper())
    

def problem_13_length():
    # TODO: Use a built-in function to print the number of characters in the word "Supercalifragilisticexpialidocious".
    word = "Supercalifragilisticexpialidocious"
    pass
def problem_13_length():
    word = "Supercalifragilisticexpialidocious"
    print(len(word))
   


def problem_14_tuples():
    # TODO: Create a tuple named 'coordinates' containing the numbers 10 and 20.
    # TODO: Try to assign the value 30 to the first element (index 0). Watch it fail! (Tuples are immutable)
    pass
def problem_14_tuples():
    coordinates = (10, 20)
    

def problem_15_sets():
    # TODO: Create a set named 'unique_numbers' with the values: 1, 1, 2, 3, 3, 4.
    # Print the set. Notice how duplicates are automatically removed!
    pass
def problem_15_sets():
    print({1, 1, 2, 3, 3, 4})
    

def problem_16_swap():
    # TODO: Swap the values of 'a' and 'b' without using a third temporary variable.
    # Print 'a' and 'b' to verify they swapped.
    a = 100
    b = 200
    pass
def problem_16_swap():
    a = 100
    b = 200
    a, b = b, a
    print(a, b)
    

def problem_17_assignment_operator():
    # TODO: Use the '+=' assignment operator to add 50 to 'score'. Print 'score'.
    score = 10
    pass
def problem_17_assignment_operator():
    score = 10
    score += 50
    print(score)
    


def problem_18_membership_operator():
    # TODO: Check if the letter "z" is in the string "alphabet" using the 'in' operator.
    # Print the boolean result.
    word = "alphabet"
    pass
def problem_18_membership_operator():
    word = "alphabet"
    print("z" in word)
    


def problem_19_identity_operator():
    # TODO: Create two variables: list1 = [1, 2] and list2 = [1, 2].
    # TODO: Use the 'is' operator to check if they are the exact same object in memory. Print the result.
    pass
def problem_19_identity_operator():
    list1 = [1, 2]
    list2 = [1, 2]
    print(list1 is list2)
    

def problem_20_precedence():
    # TODO: Calculate the result of 10 + 5 * 2. 
    # TODO: Now use parentheses to force the addition to happen first. Print both results.
    pass
def problem_20_precedence():
    print(10 + 5 * 2)
    print((10 + 5) * 2)

def problem_21_string_slicing():
    # TODO: Create a variable 'text' = "Python Programming".
    # TODO: Slice the string to extract just the word "Python" and print it.
    pass
def problem_21_string_slicing():
    text = "Python Programming"
    print(text[:6])
    

def problem_22_dict_keys():
    # TODO: You have a dictionary: car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # TODO: Print only the keys of the dictionary.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass
def problem_22_dict_keys():
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print(car.keys())
    


def problem_23_dict_values():
    # TODO: Using the same 'car' dictionary, print only the values.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass
def problem_23_dict_values():
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print(car.values())
    


def problem_24_list_append():
    # TODO: Create a list 'colors' = ["red", "green"].
    # TODO: Add "blue" to the end of the list and print the list.
    pass
def problem_24_list_append():
    colors = ["red", "green"]
    colors.append("blue")
    print(colors)
    


def problem_25_type_error():
    # TODO: Try to concatenate a string "Age: " and an integer 25 using the '+' operator.
    # TODO: Watch it fail! Fix it by converting the integer to a string first, then print it.
    pass
def problem_25_type_error():
    print("Age: " + str(25))
    

def problem_26_boolean_math():
    # TODO: In Python, True is 1 and False is 0. 
    # TODO: Print the result of True + True.
    pass
def problem_26_boolean_math():
    print(True + True)
    

def problem_27_floor_division():
    # TODO: Calculate 10 divided by 3 using standard division (/) and print it.
    # TODO: Calculate 10 divided by 3 using floor division (//) and print it. Notice the difference!
    pass
def problem_27_floor_division():
    print(10 / 3)
    print(10 // 3)
    

def problem_28_exponentiation():
    # TODO: Calculate 2 to the power of 5 using the exponentiation operator (**) and print it.
    pass
def problem_28_exponentiation():
    print(2 ** 5)
    

def problem_29_dynamic_typing():
    # TODO: Create a variable 'x' and assign it the integer 100.
    # TODO: Reassign 'x' to the string "Now I'm a string!" and print 'x'. This demonstrates dynamic typing.
    pass
def problem_29_dynamic_typing():
    x = 100
    x = "Now I'm a string!"
    print(x)


def problem_30_string_repetition():
    # TODO: Use the multiplication operator (*) to print a string of 20 dashes ("-").
    pass
def problem_30_string_repetition():
    print("-" * 20)
    