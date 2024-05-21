n = int(input())
a_ = list(map(int, input().split()))
j = a_[0]
b = [j]
ex = 1
ask = [-1, -1]
while len(b) < n:
    print(len(b),n)
    print(j)
    j = a_[j-1]
    print(j)
    print(b)
    if len(b) < n and j not in b:
        b.append(j)
    elif len(b) < n and j in b:
        print(b,"k")
        if ex:
            print(ex)
            for w in range(1, n+1):
                print(w)
                if w not in a_:
                    b.append(w)
                    ask = [a_.index(j) + 1, w]
                    a_[a_.index(j)]=w
                    j = a_[w - 1]
                    ex = 0
                    print(w,ask,a_,j,ex)
                elif a_.count(w) > 1 and w != j:
                    ask = [-1, -1]
                    break
                else:
                    continue
        else:
            ask = [-1, -1]
            break
    else:
        break

print(ask)

# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 1 1
