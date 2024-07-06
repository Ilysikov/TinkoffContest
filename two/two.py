import math
n = int(input())
result = 0
while n > 1: n = math.ceil(n / 2); result += 1
print(result)
