import unittest
import runner
import runner_and_tournament as rat


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
            Тест функции walk
        :return: None
        """
        self.test_Runner = runner.Runner("test_Runner")
        for i in range(10):
            self.test_Runner.walk()
        self.assertEqual(self.test_Runner.distance, 50, "Тест функции walk не пройден")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
            Тест функции run
        :return: None
        """
        self.test_Runner = runner.Runner("test_Runner")
        for i in range(10):
            self.test_Runner.run()
        self.assertEqual(self.test_Runner.distance, 100, "Тест функции run не пройден")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.test_Runner_1 = runner.Runner("test_Runner_1")
        self.test_Runner_2 = runner.Runner("test_Runner_2")
        for i in range(10):
            self.test_Runner_1.run()
            self.test_Runner_2.walk()
        self.assertNotEqual(self.test_Runner_1.distance, self.test_Runner_2.distance, "Тест test_challenge не пройден")

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self._Usain = rat.Runner('Усэйн', 10)
        self._Andrey = rat.Runner('Андрей', 9)
        self._Nick = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        #pprint(cls.all_results)
        pass

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Usain_Nick(self):
        _race = rat.Tournament(90, self._Usain, self._Nick)
        _results = _race.start()

        for _key, _runner in _results.items():
            _results.update({_key : _runner.name})

        #print(_results)
        self.assertTrue(_results[len(_results)] == 'Ник', 'test_Usain_Nick was failed')
        TournamentTest.all_results.append(_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Andrey_Nick(self):
        _race = rat.Tournament(90, self._Andrey, self._Nick)
        _results = _race.start()

        for _key, _runner in _results.items():
            _results.update({_key : _runner.name})

        #print(_results)
        self.assertTrue(_results[len(_results)] == 'Ник', 'test_Andrey_Nick was failed')
        TournamentTest.all_results.append(_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Usain_Andrey_Nick(self):
        _race = rat.Tournament(90, self._Usain, self._Andrey, self._Nick)
        _results = _race.start()

        for _key, _runner in _results.items():
            _results.update({_key: _runner.name})

        #print(_results)
        self.assertTrue(_results[len(_results)] == 'Ник', 'test_Usain_Andrey_Nick was failed')
        TournamentTest.all_results.append(_results)

if __name__ == "__main__":
    unittest.main()