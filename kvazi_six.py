one_string = int(input())
two_string = list(map(int, input().split()))
list_i = []
list_j = []
i = -1
j = -1
for c, u in enumerate(two_string, start=1):
    if c % 2 != u % 2:
        if u % 2 == 0:
            list_i.append(c)
        elif u % 2 != 0:
            list_j.append(c)
if len(list_j) == 1 and len(list_i) == 1:
    i = list_i[0]
    j = list_j[0]
elif len(list_j) == 0 and 0 == len(list_i):
    if one_string >= 3:
        i, j = 1, 3
print(i, j)
#
# print(no)
# print(ch)
# print(list_i)
# print(list_j)
