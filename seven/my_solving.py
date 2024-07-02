import copy
def seven_exe(bad_santa):
    one = []
    two = []
    answer = [-1, -1]
    """
    В первом цикле мы ищем пропущенный индекс и два повторяющихся индекса
    "two" – список, который будет хранить пропущенный индекс;
    "one" – список, который хранит индексы повторяющегося числа(индекса).
    """
    bad = set(bad_santa)
    ch = sum(bad_santa) - sum(bad)
    for number in range(1, len(bad_santa) + 1):
        if number not in bad:
            two.append(number)
        elif number == ch:
            duplicate = []
            for c, l in enumerate(bad_santa):
                if l == number:
                    duplicate.append(c)
            if len(duplicate) == 2:
                one.append(duplicate[0])
                one.append(duplicate[1])
    """
    С помощью следующего цикла мы поочередно меняем элемента с индексами из списка "one" на 
    единственный элемент "two".  
    """
    for i in one:
        for z in two:
            back = [bad_santa[i]]
            bad_santa[i] = int(z)
            cycle_count_one = 0
            second_copy = copy.deepcopy(bad_santa)
            secret = bad_santa[0]
            """
            В следующем цикле мы маркируем весь уже измененный список обращая элементы порядка
            в отрицательное число, следуя при этом 
            от число -> (к) индексу списка (который по условию начинается с 1) -> (к) числу.
            """

            while len(bad_santa) > cycle_count_one:
                second_copy[secret - 1] *= -1
                secret = bad_santa[secret - 1]
                cycle_count_one += 1
            second_cycle_count = 0

            """
            Переберем новый (маркированный) список, 
            если все числа меньше 0 – наш список – цикл.
            Дополнительно (необязательно) сравним суммы маркированного списка и НЕ маркированного:
            их модули должны быть равны.
            Возвращаем индекс элемента и его новое значение.
            """

            for marker in second_copy:
                if marker < 0:
                    second_cycle_count += 1
            if second_cycle_count == len(bad_santa) or sum(second_copy) == -sum(bad_santa):
                answer = [i + 1, z]
                break
            else:
                bad_santa[i] = back[0]
                continue

    """
    Если у нас не получилось все числа списка изменить на отрицательные – решение невозможно.
    Вернем "-1 -1" согласно условию задачи.
    """
    return answer


def input_():
    len_bad_santa = int(input())
    bad_santa = list(map(int, input().split()))
    print(seven_exe(bad_santa))


# input_()

