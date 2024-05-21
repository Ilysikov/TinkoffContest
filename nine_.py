n_strigs = list(map(int, input().split()))
p_list = n_strigs[:]
el = 0
shots = []
hundreds = []
tens = []
for i in sorted(n_strigs, reverse=True):
    if i >= 100:
        el += 1
        shots.append(p_list.index(i))
        p_list[p_list.index(i)] = i * 0
    elif i < 100 and el > 0:
        shots.append(p_list.index(i))
        p_list[p_list.index(i)] = i * 0
        el -= 1
    else:
        break

shots.sort()
new_shots = []
for g in shots:
    new_shots.append(n_strigs[g])
    if n_strigs[g] >= 100:
        hundreds.append(n_strigs[g])
    elif n_strigs[g] < 100:
        tens.append(n_strigs[g])

minus = 0

for m in new_shots:
    if m < 100 and m in tens:
        tens.remove(m)
    elif m < 100 and m not in tens:
        continue
    elif m in hundreds and sum(hundreds[hundreds.index(m) + 1:]) <= sum(tens):
        if tens:
            minus += max(tens)
            tens.remove(max(tens))
        hundreds.remove(m)
    elif m in hundreds and sum(hundreds[hundreds.index(m) + 1:]) > sum(tens):
        minus += max(hundreds)
        hundreds.remove(m)
        hundreds.remove(max(hundreds) if hundreds else None)
    else:
        continue

result = sum(n_strigs) - minus
print(result)
