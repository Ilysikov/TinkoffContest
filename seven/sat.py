"""
Класс – автоматически создающий тестовые примеры для автоматического тестирования "seven_exe"
"""

import random
import copy
from seven.alt_seven_one import can_make_valid_graph
import json

class Create_seven_graph():
    def __init__(self):
        self.test_graph = []
        self.good_graph = []

    def check_one(self, graph):
        first_copy = copy.deepcopy(graph)
        cycle_count_one = 0
        second_copy = copy.deepcopy(first_copy)
        secret = second_copy[0]
        """
        В следующем цикле мы маркируем весь уже измененный список обращая элементы порядка
        в отрицательное число, следуя при этом 
        от число -> (к) индексу списка (который по условию начинается с 1) -> (к) числу.
        """
        while len(graph) > cycle_count_one:
            second_copy[first_copy.index(secret)] *= -1
            secret = first_copy[secret - 1]
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
        if second_cycle_count == len(graph) or sum(second_copy) == -sum(first_copy):
            return True
        else:
            return False

    def check_two(self, graph_two):
        return can_make_valid_graph(graph_two)

    def check_three(self, graph):
        """
        :param graph: список-цикл
        :return: True – если список действительно цикл
        создадим словарик индексы-ключи, элементы списка-значения
        """
        dict_graph = {}
        for index, value in enumerate(graph, start=1):
            dict_graph[index] = value
        """
        с помощью цикла переберем все элементы словаря от ключа к значению 
        от значения к ключу (пример: 1:3 -> 3:5 -> 5:2 и т.д.)
        каждое новое значение добавляем в множество "verification_set"
        """
        verification_set = set()
        next_value = dict_graph[1]
        prev_value = -1
        cycle_count = 0
        while cycle_count < len(graph):
            verification_set.add(next_value)
            prev_value = next_value
            next_value = dict_graph[next_value]
            cycle_count += 1
        """
        Если graph – это цикл, то на итерации равной длине списке 
        мы окажемся в начальной точке
        т.е. в dict_graph[1].
        """
        if len(verification_set) == len(graph):
            return dict_graph[prev_value] == dict_graph[1]
        else:
            return False

    def untested_graph(self, n):
        """
        :param n: длина списка, который необходимо вернуть
        :return: список, который возможно явлеся циклом
        """
        sch = [int(i) for i in range(1, n + 1)]
        graph = []
        tem = 0
        """
        "sch" – список чисел, которые должны быть в цикле
        с помощью random поставим элементы в случайном порядке, 
        но так, чтобы выполнялись условия Тайного Санты
        """
        while 3 < len(sch):
            y = random.randrange(n - tem)
            x = sch[y]
            if x not in graph and len(graph) != x:
                graph.append(x)
                sch.pop(y)
                tem += 1
        if len(sch) == 3:
            graph.append(sch[0])
            graph.append(sch[1])
            graph.append(sch[2])
        return graph if len(graph) == tem+3 else self.untested_graph(n)

    def create_graph(self, n=2000):
        """
        создание списка цикличных графов определенной длины n
        :param n:
        :return:
        """
        while len(self.test_graph) < 2:
            """создаем потенциально цикличный граф"""
            graph = self.untested_graph(n)
            """ проверяем его в двух разных алгоритмах проверки цикличности"""
            if  self.check_three(graph):
                """ 
                если граф цикличен заменим в его глубокой копии одно число на дубликат другого числа так, чтобы 
                цикл нарушился, но при этом его возможно было исправить одним действием обратной замены
                """
                graph_two = copy.deepcopy(graph)
                self.good_graph.append(graph)
                two = 0
                one_t = 0
                one = 0
                while graph_two[one] == graph[one_t]:
                    two = random.randrange(1, n + 1)
                    one_t = random.randrange(n)
                    one = graph_two.index(two)
                graph_two[one] = graph[one_t]
                v = self.check_two(graph_two)
                if v == (one + 1, two) or v == (one_t + 1, two):
                    if graph not in self.test_graph:
                        a = copy.deepcopy(graph_two)
                        """ 
                        добавляем в тест граф с висячей вершиной и правильный индекс
                        и значение для обратной замены
                        """
                        self.test_graph.append((a, v))
            else:
                continue

        return self.test_graph

    def __str__(self):
        return str(self.test_graph)

    def txt(self):
        """
        перезапись словаря с новыми тестами в json файл
        """
        with open("text_massive.json", "r+") as fn:
            mydic = json.load(fn)
            lenlong = len(mydic) if mydic else 0
        for c,i in enumerate(self.test_graph,start=lenlong):
            mydic[c]=i
        with open("text_massive.json", "w") as fn:
            json.dump(mydic,fn)


if __name__ == "__main__":
    run = Create_seven_graph()
    run.create_graph(100000)
    run.txt()