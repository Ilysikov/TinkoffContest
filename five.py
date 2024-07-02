l, r = map(int, input().split())
ask = set()
for i in range(len(str(r))):
    for h in range(1, 10):
        ask.add(h * int('1' * (i + 1)))
result = len([d for d in ask if d >= l and d <= r])
print(result)
