import random

a = random.randrange(101)
b = random.randrange(101)
c = random.randrange(101)
d = random.randrange(101)


def one(a, b, c, d):
    return a if d <= b else c * (d - b) + a

a,b,c,d=map(int, input().split())
print(a,b,c,d)
result = a if d <= b else c * (d - b) + a
print(result)


print(one(a, b, c, d))
print(a, b, c, d)
