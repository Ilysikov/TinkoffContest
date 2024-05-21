# # one_str = list(map(int, input().split()))
# # two_str = list(map(int, input().split()))
# # my_str = []
# # if sum(two_str) <= one_str[0] * 9:
# #     my_str = sorted(two_str)
# #     for i in range(one_str[1]):
# #         my_str[i] = 9
# # elif sum(two_str) > one_str[0] * 9:
# #     my_str = sorted(two_str, reverse=True)
# #     my_len=len(str(my_str[0]))
# #     for c in range(my_len):
# #         if one_str[1]:
# #             t = sorted([])
# #             for x, b in enumerate(my_str):
# #                 if len(str(b)) >= my_len - c:
# #                     t.append([int(str(b)[-my_len + c]), x])
# #             for s in t:
# #                 if str(my_str[s[1]])[-my_len + c] != '9':
# #                     my_str[s[1]] += (9-int(str(my_str[s[1]])[-my_len + c]))*(10**(my_len-c-1))
# #                     one_str[1] -= 1
# # print(sum(my_str) - sum(two_str) if my_str else 0)
# import random
# from typing import List, Any
#
# h: list[Any]=[]
# i:int=0
# while 1000 > len(h):
#     i=0
#
#     i=i + random.randrange(10) ** random.randrange(10)
#     print(i)
#     h.append(i)
# print(' '.join([str(i) for i in h]))
import random


#
# print(' '.join([str(i) for i in h]))
n=[]
i=1
while len(n)<1000: n.append(1+2*i); i+=1; n.append(2+2*i)
e=[]
print(len(n))
print(' '.join([str(i) for i in n]))

f=1000
while len(e)<1000: h=n[random.randrange(f)];e.append(h);n.remove(h); f-=1
print(' '.join([str(i) for i in n]))