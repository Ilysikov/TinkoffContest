n = int(input())
a_index = list(map(int, input().split()))


def recursion(bad_=[], ask=[-1, -1], ex=1,
       rec=n, ind=a_index[0]):
    rec -= 1
    erot=[i for i in range(1, n + 1) if i not in a_index]
    sk=[ind, a_index[ind - 1]]
    w=[i for i in range(1, n + 1) if i not in a_index][0]
    if a_index[ind - 1] in bad_ and rec <= 0:
        if erot:
            a_index[ind - 1] = w
            ask = sk
            rec = n - 1
            bad_ = []
            ex -= 1
            print(ask)
            print(bad_,2)
            return recursion(bad_, ask, ex, rec, ind=a_index[ind - 1])
        else:
            return ask,1
    elif a_index[ind - 1] in bad_ and ex > 0:
        if erot:
            a_index[ind - 1] = w
            ask = sk
            rec = n
            bad_ = []
            ex -= 1
            print(ask)
            print(bad_)
            return recursion(bad_, ask, ex, rec, ind=a_index[ind - 1])
    elif a_index[ind - 1] in bad_ and ex <= 0:
        ask = [-1, -1]
        return ask,2
    bad_.append(a_index[ind - 1])
    print(a_index)
    print(a_index[ind-1])
    print(bad_,3)
    return recursion(bad_, ask, ex, rec, ind=a_index[ind - 1])



print(recursion())

# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 1 1
