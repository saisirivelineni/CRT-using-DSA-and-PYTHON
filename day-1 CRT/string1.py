def check_ascii_even_odd(s):
    for ch in s:
        ascii_value = ord(ch)

        if ascii_value % 2 == 0:
            print(f"Character: {ch}, ASCII: {ascii_value}, Even")
        else:
            print(f"Character: {ch}, ASCII: {ascii_value}, Odd")

check_ascii_even_odd("hello")