def can_make_valid_graph(nums):
    graph = {}
    pair_val = 0
    vals = set()

    # делаем словарик и если находим, что у нас больше,
    # чем 2 значения одинаковые, то возвращаем -1, -1
    for idx, val in enumerate(nums, start=1):
        graph[idx] = val
        if val in vals:
            if pair_val == 0:
                pair_val = val
            else:
                return -1, -1
        else:
            vals.add(val)
    if len(vals) + 1 != len(nums):
        return -1, -1
    if pair_val == 0:
        return -1, -1

    # получим индекс, который отсутствует в значениях
    excepted_val = 0
    for i in range(len(nums)):
        if (i + 1) not in vals:
            excepted_val = i + 1
            break

    # получим индексы элементов, которые ссылаются на одно и то же значение
    idxs_of_pair_vals = []
    for idx, val in enumerate(nums):
        if val == pair_val:
            idxs_of_pair_vals.append(idx + 1)

    # Берем висячую вершину и проходимся по всем значениям,
    # последнее должно ссылаться на висячую вершину.
    # При этом len(done_cells) == len(nums) - 1
    done_cells = set()
    next_val = graph[excepted_val]
    while next_val not in done_cells:
        done_cells.add(next_val)
        prev_val = next_val
        next_val = graph[next_val]
    if len(done_cells) == len(nums) - 1:
        return prev_val, excepted_val
    return -1, -1


