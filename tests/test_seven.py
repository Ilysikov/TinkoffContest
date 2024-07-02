from seven.my_solving import seven_exe
from seven.alt_seven_one import can_make_valid_graph
from seven.alt_seven_two import can_make_valid_graph_two
from seven.sat import Create_seven_graph
from unittest import TestCase, main
import json


class seven_test(TestCase):
    """
    проверка "my_sloving" c помощью рандомно сгенерированных тестов
    """
    def test_seven_exe(self):
        test_graf = []
        while not test_graf:
            create = Create_seven_graph()
            test_graf = create.create_graph(n=10**2)
        for i in test_graf:
            with self.subTest(i=i):
                self.assertIsNot(seven_exe(list(i[0])), list(i[0]))
                self.assertEqual(seven_exe(list(i[0])), list(i[1]))

    def test_sat_check_3(self):
        """
        в этом тесте проверяются функции, от которых зависит генерация тестовых случаев
        """
        my_list = []
        create = Create_seven_graph()
        while len(my_list) < 10:
            graf = []
            while not graf:
                graf = create.untested_graph(n=10 ** 2)
            my_list.append(graf)
        for i in my_list:
            with self.subTest(i=i):
                self.assertEqual(create.check_three(i), create.check_one(i))

    def test_sat_check_1(self):
        """
        в этом тесте проверяются функции, от которых зависит генерация тестовых случаев
        """
        my_list = []
        create = Create_seven_graph()
        while len(my_list) < 10:
            graf = []
            while not graf:
                graf = create.untested_graph(n=10 ** 2)
            my_list.append(graf)
        for i in my_list:
            with self.subTest(i=i):
                self.assertEqual(create.check_one(i), create.check_three(i))

    def test_graph_two(self):
        """
        в этом тесте сравниваются решения взятые из интернета"
        """
        test_graf = []
        while not test_graf:
            create = Create_seven_graph()
            test_graf = create.create_graph(n=10 ** 2)
        for i in test_graf:
            with self.subTest(i=i):
                self.assertIsNot(i[1][:-1:], can_make_valid_graph_two(i[0]))

    def test_battle(self):
        """
        в этом тесте сравниваются результат решения взятое из интернета и 'my_sloving.py'"
        """
        test_graf = []
        while not test_graf:
            create = Create_seven_graph()
            test_graf = create.create_graph(n=10 ** 2)
        for i in test_graf:
            with self.subTest(i=i):
                self.assertEqual(sum(can_make_valid_graph(i[0])), sum(seven_exe(i[0])))


    def test_with_text_(self):
        """
        проверка на тесты загруженные из json-файла
        """
        with open("//seven/text_massive.json") as fn:
            mydic = json.load(fn)
            lenlong = len(mydic)
        for d in range(lenlong):
            i=mydic[str(d)]
            with self.subTest(i=i):
                self.assertEqual(seven_exe(list(i[0])), list(i[1]))


if __name__ == '__main__':
    main()
