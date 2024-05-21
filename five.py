# l, r = map(int, input().split())
# ask = []
# for i in range(l, r + 1):
#     if i == int(str(i)[0]) * int('1' * len(str(i))):
#         ask.append(i)
# print(len(ask))
l, r = map(int, input().split())
ask = set()
for i in range(len(str(r))):
    for h in range(1, 10):
        ask.add(h * int('1' * (i + 1)))
result = len([d for d in ask if d >= l and d <= r])
print(result)
