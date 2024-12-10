import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'is_frozen = True')
    def test_walk(self):
        """
            Тест функции walk
        :return: None
        """
        self.test_Runner = runner.Runner("test_Runner")
        for i in range(10):
            self.test_Runner.walk()
        self.assertEqual(self.test_Runner.distance, 50, "Тест функции walk не пройден")

    @unittest.skipIf(is_frozen, 'is_frozen = True')
    def test_run(self):
        """
            Тест функции run
        :return: None
        """
        self.test_Runner = runner.Runner("test_Runner")
        for i in range(10):
            self.test_Runner.run()
        self.assertEqual(self.test_Runner.distance, 100, "Тест функции run не пройден")

    @unittest.skipIf(is_frozen, 'is_frozen = True')
    def test_challenge(self):
        self.test_Runner_1 = runner.Runner("test_Runner_1")
        self.test_Runner_2 = runner.Runner("test_Runner_2")
        for i in range(10):
            self.test_Runner_1.run()
            self.test_Runner_2.walk()
        self.assertNotEqual(self.test_Runner_1.distance, self.test_Runner_2.distance, "Тест test_challenge не пройден")


if __name__ == "__main__":
    unittest.main()
