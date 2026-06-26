def problem_1_if():
    # TODO: Create a variable 'temperature' = 35.
    # TODO: Print "It's a hot day!" if temperature > 30
    pass
def problem_1_if():
    temperature = 35
    if temperature > 30:
        print("It's a hot day!")


def problem_2_if_else():
    # TODO: Create 'is_raining' = True.
    # TODO: If True print "Take an umbrella" else "Enjoy the sun"
    pass
def problem_2_if_else():
    is_raining = True
    if is_raining:
        print("Take an umbrella")
    else:
        print("Enjoy the sun")


def problem_3_elif():
    # TODO: Create score = 85.
    # TODO: If >=90 print A, elif >=80 print B, else print C
    pass
def problem_3_elif():
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")


def problem_4_nested_if():
    # TODO: is_weekend = True, has_money = False
    # TODO: weekend → check money → print messages
    pass
def problem_4_nested_if():
    is_weekend = True
    has_money = False

    if is_weekend:
        if has_money:
            print("Go to movies")
        else:
            print("Stay home")
    else:
        print("Go to work")


def problem_5_multiple_conditions():
    # TODO: age = 25, has_license = True
    # TODO: Print "Can drive" only if both conditions are True
    pass
def problem_5_multiple_conditions():
    age = 25
    has_license = True

    if age >= 18 and has_license:
        print("Can drive")



def problem_6_for_loop_range():
    # TODO: Print numbers from 1 to 5 using range()
    pass
def problem_6_for_loop_range():
    for i in range(1, 6):
        print(i)


def problem_7_for_loop_list():
    # TODO: fruits = ["apple","banana","cherry"]
    # TODO: Print each fruit using loop
    pass
def problem_7_for_loop_list():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)


def problem_8_for_loop_string():
    # TODO: Print each letter of "Python"
    pass
def problem_8_for_loop_string():
    for letter in "Python":
        print(letter)


def problem_9_while_loop():
    # TODO: count = 3
    # TODO: Print countdown using while loop
    pass
def problem_9_while_loop():
    count = 3
    while count > 0:
        print(count)
        count -= 1


def problem_10_break_statement():
    # TODO: Loop 1 to 10, break when i == 5
    pass
def problem_10_break_statement():
    for i in range(1, 11):
        if i == 5:
            break
        print(i)