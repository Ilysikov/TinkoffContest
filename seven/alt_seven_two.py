def is_valid_graph(graph):
    first_key = 1
    current_key = 1
    for _ in range(len(graph)):
        next_key = graph[current_key]
        del graph[current_key]
        current_key = next_key
        if next_key == first_key:
            break
    return len(graph) == 0


def can_make_valid_graph_two(nums):
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
        return [-1, -1]
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

    # Общая проверка
    graph[idxs_of_pair_vals[0]] = excepted_val
    if is_valid_graph(graph.copy()):
        return [[idxs_of_pair_vals[0], excepted_val]]
    graph[idxs_of_pair_vals[0]] = pair_val

    graph[idxs_of_pair_vals[1]] = excepted_val
    if is_valid_graph(graph.copy()):
        return idxs_of_pair_vals[1], excepted_val

    return -1, -1
