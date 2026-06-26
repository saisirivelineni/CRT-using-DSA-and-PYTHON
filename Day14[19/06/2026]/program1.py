n = int(input())

temp = n
sum_of_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if sum_of_cubes == n:
    print("armstrong")
else:
    print("not armstrong")