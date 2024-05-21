a=input()
b=input()
c=input()
one_s=list(map(int, a.split()))
two_s=list(map(int, b.split()))
three_s=int(c)
result=0
if three_s <= two_s[0] + one_s[1] or three_s >= two_s[-1] - one_s[1]:
    result = two_s[-1] - two_s[0]
elif three_s > two_s[0] + one_s[1] or three_s < two_s[-1] - one_s[1]:
    result = three_s * 2 + (two_s[-1] - three_s) if three_s <= two_s[-1] / 2 \
        else three_s + (two_s[-1] - three_s) * 2
print(result)