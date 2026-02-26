#Q1
print(1+2+3+4+5)


#Q2
N = 1
S = 1
while N < 100:
    N = N + 2
    S = S + N
print(S)


#Q3
print("Enter an integer:")
n = int(input())
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


#Q4
print("*" * 1)
print("# " * 1)


#Q5
name = "Purnima Giri"
address = "Noida , India"
print(name)
print(address)


#Q6
x = 1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)


#Q7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print(a, b)
else:
    print(b, a)


#Q8
num = int(input("Enter 0 or 1: "))
if num == 0:
    print("You entered Zero")
elif num == 1:
    print("You entered One")
else:
    print("Invalid input")


#Q9
for n in range(2, 13):
    for i in range(2, n):
        if n % i == 0:
            print(n, "Composite")
            break
    else:
        print(n, "Prime")


#Q10
for n in range(100, 1000):
    temp = n
    s = 0
    while temp > 0:
        d = temp % 10
        s += d ** 3
        temp //= 10
    if n == s:
        print(n)


#Q11
l1 = ["A", "B", "C"]
l2 = [1, 2, 3]
for i in l1:
    for j in l2:
        print(i, j)


#Q12
person = {"Mother": "Jane Doe"}
person["Father"] = "John Doe"
print(person)


#Q13
lst = [4, 2, 9, 1, 5]
max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i
lst[max_index], lst[-1] = lst[-1], lst[max_index]
print(lst)


#Q14
a = [[1, 2], [3, 4], [5, 6]]
b = []
for i in a:
    for j in i:
        b.append(j)
print(b)


#Q15
maria = {"korean": 90, "english": 85, "math": 92, "science": 90}
avg = sum(maria.values()) / len(maria)
print(avg)


#Q16
import copy
school = {"student": {"name": "Purnima"}}
school2 = copy.deepcopy(school)
print(school is school2)


#Q17
scores = (
    ("Hyun", 88, 95, 90),
    ("Min", 92, 89, 93),
    ("Jin", 85, 90, 88),
    ("Lee", 90, 92, 91)
)
names, eng, math, sci = zip(*scores)
avg = sum(math) / len(math)
print(avg)
