import math
n=float(input())
result=1
while n>2: n= math.ceil(n / 2); result+=1
print(result)