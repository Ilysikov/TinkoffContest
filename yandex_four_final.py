import random


def gen():
    x=random.randrange(1,99)
    y=random.randrange(1,99)
    print(sorted([x,y]))
    return f"{x} {y}" if sorted([x,y]) not in mel and x!=y else gen()
import copy

tela = [100,98]#list(map(int, input().split()))
mel = []
for z in range(tela[1]):
    meta = list(map(int,gen().split()))
    print(meta)
    mel.append(sorted(meta))
gero = [i for i in range(1, tela[0] + 1)]
dic = {}
answer = []
print(sorted(mel))
print(sorted([i[0] for i in mel]+[h[1] for h in mel]))
def remove(dic, q, x):
    one = 0
    for j in gero:
        if (sorted([j,x]) not in mel and sorted([q,j]) not in mel) and (j!=q and j!=x):
            one=j
            break
    two = 0
    for w in gero:
        if w!=one:
            if (sorted([w,x]) not in mel and sorted([q,w]) not in mel) and (w!=x and q!=w):
                two=w
            break
    answer.append([x, one])
    mel.append([x, one])
    memory = dic[x]
    dic[x] = dic[one]
    dic[one] = memory
    answer.append([q, two])
    mel.append([q, two])
    memory = dic[q]
    dic[q] = dic[two]
    dic[two] = memory
    answer.append([q,one])
    mel.append([q,one])
    memory = dic[q]
    dic[q] = dic[one]
    dic[one] = memory
    answer.append([x,two])
    mel.append([x,two])
    memory = dic[x]
    dic[x] = dic[two]
    dic[two] = memory


for d in gero:
    dic[d] = str(d)
dic_cop=copy.deepcopy(dic)
for m in mel:
    dic[m[0]] = str(m[1])
    dic[m[1]] = str(m[0])

while dic_cop!=dic:
    for x in dic:
        if dic[x] != str(x):
            q = int(dic[x])
            if (dic[q] == str(x) and dic[x] == str(q)) and sorted([x,q]) not in mel:
                dic[q]=str(q)
                dic[x]=str(x)
                answer.append(sorted([x,q]))
            elif dic[q] == str(x) and sorted([x,q]) in mel:
                remove(dic, q, x)
            elif dic[q] != str(x):
                for v in dic:
                    if dic[v] == str(x):
                        q = v
                        remove(dic, q, x)
                        break
print(dic)
for an in answer:
    if an:
        print(an[0],an[1])

