# one_s,two_s,three_s = list(map(int, input().split())),list(map(int, input().split())),int(input())

a = input()
b = input()
c = input()
one_s = list(map(int, a.split()))
two_s = list(map(int, b.split()))
three_s = int(c)
result = 0
if two_s[three_s - 1]-two_s[0] <= one_s[1] or two_s[-1]-two_s[three_s - 1] <= one_s[1]:
    result = two_s[-1] - two_s[0]
elif two_s[0] + one_s[1] < two_s[three_s - 1] < two_s[-1] - one_s[1]:
    result = (two_s[three_s - 1] - two_s[0]) * 2 + (two_s[-1] - two_s[three_s - 1])
    if two_s[three_s - 1]-two_s[0] <= (two_s[-1]-two_s[0]) // 2:
        result = (two_s[three_s - 1] - two_s[0]) * 2 + (two_s[-1] - two_s[three_s - 1])
    elif two_s[three_s - 1]-two_s[0] > (two_s[-1]-two_s[0]) // 2:
        result =(two_s[three_s - 1] - two_s[0]) + (two_s[-1] - two_s[three_s - 1]) * 2
print(result)
