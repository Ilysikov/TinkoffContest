n = int(input())
a,b,c = map(int,input().split())
n_my = n - 1
my_list = [a, b, c]
res = [i for i in my_list if i <= n_my]
for l in res:
    for o in [g + l for g in my_list if g + l <= n_my]:
        res.append(o)
print(len(set(res)) + 1)
