one_string = int(input())
two_string = list(map(int, input().split()))
ask = []
for c, x in enumerate(two_string, start=1):
    if len(ask) < 2:
        if c % 2 != 0 and x % 2 == 0:
            for l, y in enumerate(two_string[c:], start=1):
                if y % 2 != 0 and (l + c) % 2 == 0:
                    two_string[c - 1] = y
                    two_string[l + c - 1] = x
                    ask.append([c, l + c])
                    break
                else:
                    continue
        elif c % 2 == 0 and x % 2 != 0:
            for l, y in enumerate(two_string[c:], start=1):
                if y % 2 == 0 and (l + c) % 2 != 0:
                    two_string[c - 1] = y
                    two_string[l + c - 1] = x
                    ask.append([c, l + c])
                    break
                else:
                    continue
    else:
        break

if 0 < len(ask) < 2:
    i = ask[0][0]
    j = ask[0][1]
else:
    i = -1
    j = -1
print(i, j)
# print((ask[0][0],ask[0][1]) if ask[0] and len(ask) < 2 else (-1, -1)) #'-1 -1'
# print(' '.join(str(i) for i in ask[0])if len(ask) < 2 else '-1 -1')
print(ask)
print(two_string)
