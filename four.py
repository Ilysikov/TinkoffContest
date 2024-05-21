one_str = list(map(int, input().split()))
two_str = list(map(int, input().split()))
my_str = []
my_sum = 0
tes=0
my_len = len(str(max(two_str)))
if my_len == 1 and min(two_str) != 9:
    my_str = sorted(two_str)
    for k, i in enumerate(my_str):
        if i != 9 and one_str[1] > 0:
            my_str[k] = 9
            one_str[1] -= 1
    my_sum = sum(my_str) - sum(two_str)
elif my_len > 1:
    my_str = sorted(two_str, reverse=True)
    for c in range(my_len):
        if one_str[1]:
            t = sorted([])
            for x, b in enumerate(my_str):
                z = str(b)
                if len(z) >= my_len - c:
                    if z[-my_len + c] != '9':
                        t.append([int(z[-my_len + c]), x])
            t.sort()
            for s in t:
                if one_str[1]:
                    my_sum += (9 - s[0]) * (10 ** (my_len - c - 1))
                    print(my_str[s[1]])
                    print(my_str[s[1]] +(9 - s[0]) * (10 ** (my_len - c - 1)))
                    print(one_str[1])
                    one_str[1] -= 1

print(my_sum)  # if my_str else 0)
# print(my_str)
# print(sum(two_str))
# print(sum(my_str))
# print(sum(my_str)-sum(two_str))
# print(sorted(my_str))
# print(sorted(two_str))
# print(len(my_str))
# print(len(''.join([str(i) for  i in my_str])))
# print(len(''.join([str(i) for  i in two_str])))