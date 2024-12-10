import unittest
import rt_with_exceptions as runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
            Тест функции walk
        :return: None
        """
        try:
            self.test_Runner = runner.Runner("test_Walker", -5)
            for i in range(10):
                self.test_Runner.walk()
            self.assertEqual(self.test_Runner.distance, 50, "Тест функции walk не пройден")
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
            Тест функции run
        :return: None
        """
        try:
            self.test_Runner = runner.Runner(777, 5)
            for i in range(10):
                self.test_Runner.run()
            self.assertEqual(self.test_Runner.distance, 100, "Тест функции run не пройден")
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.test_Runner_1 = runner.Runner("test_Runner_1")
        self.test_Runner_2 = runner.Runner("test_Runner_2")
        for i in range(10):
            self.test_Runner_1.run()
            self.test_Runner_2.walk()
        self.assertNotEqual(self.test_Runner_1.distance, self.test_Runner_2.distance, "Тест test_challenge не пройден")


logging.basicConfig(filename='runner_tests.log', level=logging.INFO, filemode='w', encoding='utf-8',
                        format='%(asctime)s - %(levelname)s:%(message)s')
