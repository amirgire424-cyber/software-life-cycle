🔹 CHIT 01

1. Triangle side

import math
base = 2.3
height = 6.7
side = math.sqrt(base*base + height*height)
print(side)


2. Even & Odd lists

L=[2,19,24,56,77,59,90,62,46]
even=[]
odd=[]
for i in L:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even, odd)

🔹 CHIT 02

1. Mean, Median, Mode

import statistics
L=[84,95,76,54,96,88,91,92,95,75,91,97,80]
print(statistics.mean(L))
print(statistics.median(L))
print(statistics.mode(L))


2. Random numbers

import random
L=[]
for i in range(10):
    L.append(random.randint(1,20))
print(L)

🔹 CHIT 03

1. Hypotenuse

import math
b=float(input())
p=float(input())
print(math.sqrt(b*b+p*p))


2. Perfect squares

for i in range(1,101):
    if int(i**0.5)**2==i and sum(map(int,str(i)))<10:
        print(i)

🔹 CHIT 04

1. Bitwise

a=int(input())
b=int(input())
print(a&b)
print(a|b)
print(a^b)
print(a<<1)
print(a>>1)


2. Remove duplicates

L=[1,2,2,3,4,4]
print(list(set(L)))

🔹 CHIT 05

1. Valid date

import datetime
d=input()
try:
    datetime.datetime.strptime(d,"%d-%m-%Y")
    print("Valid")
except:
    print("Invalid")


2. Concatenate dictionary

d1={1:10}
d2={2:20}
d3={}
d3.update(d1)
d3.update(d2)
print(d3)

🔹 CHIT 06

1. Quadratic roots

import math
a,b,c=map(float,input().split())
d=b*b-4*a*c
print((-b+math.sqrt(d))/(2*a))
print((-b-math.sqrt(d))/(2*a))


2. Key exists

d={1:10,2:20}
k=int(input())
print(k in d)

🔹 CHIT 07

1. Decimal conversion

n=int(input())
print(bin(n))
print(oct(n))
print(hex(n))


2. Merge dictionary

d1={1:10}
d2={2:20}
print({**d1,**d2})

🔹 CHIT 08

1. Sum of digits

n=input()
print(sum(map(int,n)))


2. Count vowels

def count_vowels(s):
    return sum(1 for i in s if i in "aeiouAEIOU")
print(count_vowels("hello"))

🔹 CHIT 09

1. Leap year

y=int(input())
if y%400==0 or (y%4==0 and y%100!=0):
    print("Leap")
else:
    print("Not Leap")


2. Factorial

def fact(n):
    return 1 if n==0 else n*fact(n-1)
print(fact(5))

🔹 CHIT 10

1. Delete index divisible by 3

s=input()
print("".join(s[i] for i in range(len(s)) if i%3!=0))


2. Update set

s1={1,2,3}
s2={2,4}
s1=s1-s2
print(s1)

🔹 CHIT 11

1. Reverse number

n=int(input())
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)


2. Concatenate dict

d1={1:1}
d2={2:2}
d1.update(d2)
print(d1)

🔹 CHIT 12

1. Sort words

s=input().split()
s.sort()
print(s)


2. Square & cube

def calc(n):
    return n*n, n*n*n
print(calc(3))

🔹 CHIT 13

1. Circle

r=float(input())
if r>0:
    print(3.14*r*r,2*3.14*r)


2. Even or odd

def check(n):
    return "Even" if n%2==0 else "Odd"
print(check(7))

🔹 CHIT 14

1. Divisible

n=int(input())
print(n%3==0 and n%15==0)


2. Word count file

f=open("a.txt")
count=len(f.read().split())
f.close()
f2=open("b.txt","w")
f2.write(str(count))
f2.close()

🔹 CHIT 15

1. Square ending with 5

for i in range(1,100):
    if i%10==5:
        print(i*i)


2. Copy file

open("b.txt","w").write(open("a.txt").read())

🔹 CHIT 16

1. Sum of digits

n=input()
print(sum(map(int,n)))


2. Patient file

f=open("data.txt","a")
f.write("Patient Record\n")
f.close()

🔹 CHIT 17

1. Reverse

n=int(input())
print(int(str(n)[::-1]))


2. Sum recursion

def s(n):
    return 0 if n==0 else n%10+s(n//10)
print(s(123))

🔹 CHIT 18

1. Armstrong

n=int(input())
print(n==sum(int(i)**3 for i in str(n)))


2. Power

a,b=map(int,input().split())
print(a**b)

🔹 CHIT 19

1. Greatest

L=list(map(int,input().split()))
print(max(L))


2. Capitalize

s=input()
print(s.capitalize())

🔹 CHIT 20

1. Pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


2. Last element

L=[1,2,3]
print(L[-1])

🔹 CHIT 21

1. Prime

n=int(input())
i=2
while i<n:
    if n%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")


2. Swap

def swap(a,b):
    return b,a
print(swap(2,3))

🔹 CHIT 22

1. Remove space

s=input()
for i in s:
    if i==" ":
        continue
    print(i,end="")


2. Table

n=5
i=1
while i<=10:
    print(n*i)
    i+=1

🔹 CHIT 23

1. Desks

a,b,c=20,21,22
print((a+1)//2+(b+1)//2+(c+1)//2)


2. Area

def area(b=5,h=4):
    return 0.5*b*h
print(area())

🔹 CHIT 24

1. Clock angle

h,m,s=map(int,input().split())
print(h*30+m*0.5+s*(0.5/60))


2. Celsius

c=float(input())
print(c*9/5+32)

🔹 CHIT 25

1. Fourth vertex

print(7,6)


2. Largest

a,b,c=map(int,input().split())
print(max(a,b,c))

🔹 CHIT 26

1. Lost card

n=5
L=[1,2,3,5]
print(n*(n+1)//2-sum(L))


2. Sum natural

n=int(input())
print(n*(n+1)//2)

🔹 CHIT 27

1. Bowling

pins=["I"]*10
pins[2:5]=["."]*3
print("".join(pins))


2. Divisible

for i in range(1,50):
    if i%5==0:
        print(i)

🔹 CHIT 28

1. Timestamp

t1=1*3600+2*60+3
t2=2*3600+3*60+4
print(t2-t1)


2. Number sign

n=int(input())
print("Positive" if n>0 else "Negative" if n<0 else "Zero")

🔹 CHIT 29

1. Greatest

L=list(map(int,input().split()))
g=L[0]
for i in L:
    if i>g:
        g=i
print(g)


2. ASCII

print(ord(input()))

🔹 CHIT 30

1. Sum every 5th

i=0
s=0
while i<=500:
    s+=i
    i+=5
print(s)


2. LCM

import math
a,b=map(int,input().split())
print(a*b//math.gcd(a,b))

🔹 CHIT 31

1. Password

for i in range(3):
    if input()=="python":
        print("welcome")
        break


2. Sum recursion

def s(n):
    return 0 if n==0 else n+s(n-1)
print(s(5))

🔹 CHIT 32

1. Count digits

n=input()
print(len(n))


2. Matrix add

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print([[A[i][j]+B[i][j] for j in range(2)] for i in range(2)])

🔹 CHIT 33

1. Fibonacci

a,b=0,1
for i in range(5):
    print(a)
    a,b=b,a+b


2. Index

L=[10,20,30]
for i in range(len(L)):
    print(i,L[i])

🔹 CHIT 34

1. Palindrome

n=input()
print(n==n[::-1])


2. Substring

s="python"
print(s[1:4])

🔹 CHIT 35

1. Alphabet pattern

import string
k=0
for i in range(1,6):
    for j in range(i):
        print(string.ascii_uppercase[k],end=" ")
        k+=1
    print()


2. Count item

L=[1,2,2,3]
print(L.count(2))

🔹 CHIT 36

1. Primes

L=[2,3,7,8,10,13]
print([i for i in L if i>1 and all(i%j!=0 for j in range(2,i))])


2. Change case

def change(s):
    return s.swapcase()
print(change("Hello"))

🔹 CHIT 37

1. Grade

L=[78,90,34,56,89]
for i,m in enumerate(L):
    if m>=90: g="A"
    elif m>=80: g="B"
    elif m>65: g="C"
    elif m>=40: g="D"
    else: g="F"
    print(i+1,m,g)


2. Factorial

def f(n):
    return 1 if n==0 else n*f(n-1)
print(f(5))

🔹 CHIT 38

1. Duplicate

def dup(L):
    return len(L)!=len(set(L))
print(dup([1,2,2]))


2. Power of 2

print(list(map(lambda x:2**x,range(5))))

🔹 CHIT 39

1. Count letter

def count(w,l):
    return w.count(l)
print(count("hello","l"))


2. GCD

import math
a,b=map(int,input().split())
print(math.gcd(a,b))

🔹 CHIT 40

1. Remove letter

def remove(w,l):
    return w.replace(l,"")
print(remove("hello","l"))


2. Sum natural

n=int(input())
print(sum(range(1,n+1)))

🔹 CHIT 41

1. Reverse words

def rev(a,b):
    return a[::-1]==b
print(rev("abc","cba"))


2. Remove space

s=input()
print(s.replace(" ",""))

🔹 CHIT 42

1. Squares dict

d={i:i*i for i in range(1,6)}
print(d)


2. Reverse loop

for i in range(10,0,-1):
    print(i)

🔹 CHIT 43

1. Pos/Neg

L=[1,-2,-3,4]
d={"pos":0,"neg":0}
for i in L:
    if i>0:
        d["pos"]+=1
    else:
        d["neg"]+=1
print(d)


2. Series

n=5
for i in range(1,n+1):
    print(i*i)