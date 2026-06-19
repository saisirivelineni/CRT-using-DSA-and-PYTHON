'''#palindrome or not

n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

'''n = "121"
n = "1234"
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

'''# Anagram program
s1 ='abc'
s2 = 'ACB'
s1=s1.lower()
s2=s2.lower()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")'''

'''#time complexity
n=int(input())

for i in range(n):
   for j in range(n):
    print(i)
#O(1)
#O(n)
#O(1)'''


'''#factors number
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)'''


'''#prime
n = int(input())
c = 0
for i in range(2,int(n**0.5)+1):
    if n % i==0:
        c +=1
        print("not a prime")
        break
if c==0:
    print("prime")'''

#linear search
target=9900
seen=False
list2=list(range(1,100000))
for i in list2:
    if i ==target:
        seen=True
        break
