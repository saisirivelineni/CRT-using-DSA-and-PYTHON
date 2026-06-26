'''def fibonacci(a, b):
    if a > 21:
        return

    print(a, end=" ")
    fibonacci(b, a + b)

fibonacci(0, 1)'''

'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))'''

'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))'''

'''def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
print(fib(8))'''

'''Dynamic Programming (DP) Notes
1. Dynamic Programming Fundamentals
Dynamic Programming is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

Key Properties:
1.Overlapping Subproblems: Subproblems are evaluated many times. DP avoids recomputing them by storing their results.
2. Optimal Substructure: The optimal solution to a problem can be constructed from optimal solutions of its subproblems.
Approaches:
1.DP problems are typically solved using one of two approaches:

2.Top-Down (Memoization): Recursive formulation + caching.
3.Bottom-Up (Tabulation): Iterative formulation using tables.'''

'''def fib(n):
    if n<=1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]'''

'''def fib(n):
    if n <= 1:
        return n

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b'''

def fib(n):
    if n <= 1:
        return n

    prev2 = 0   
    prev1 = 1   

    for i in range(2, n + 1):
        i = prev1 + prev2
        prev2 = prev1
        prev1 = i
    return prev1
print(fib(12))