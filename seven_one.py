n = int(input())
a = list(map(int, input().split()))


def bad_santa(n, a):
    two = [-1]
    one = [-1]
    ask = (-1, -1)
    for w in range(1, n + 1):
        if len(one) > 2 or len(two) > 2:
            return ask
        else:
            if w not in a:
                two.append(w)
            elif a.count(w) == 2:
                if a.index(w) == w - 1:
                    one.append(a.index(w) + 1)
                elif a.index(w) != w - 1:
                    one.append(a[a.index(w) + 1:].index(w) + 1)
            elif a.count(w) > 2:
                return ask
            elif a.count(w) == 1:
                continue
    if len(one) == 2 and len(two) == 2:
        a[one[-1] - 1] = two[-1]
        print(a)
        b = [a[0]]
        h = 0
        while n >= h:
            if b[0] != a[b[-1] - 1] and len(b) < n:
                b.append(a[b[-1] - 1])
            h += 1
            print(b)
        if sum(b) == sum(a):
            ask = (one[-1], two[-1])
            return ask
    return ask


print(bad_santa(n, a))
