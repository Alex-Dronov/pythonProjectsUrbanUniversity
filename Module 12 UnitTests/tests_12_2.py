from pprint import pprint
import runner_and_tournament as rat
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self._Usain = rat.Runner('Усэйн', 10)
        self._Andrey = rat.Runner('Андрей', 9)
        self._Nick = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    def test_Usain_Nick(self):
        _race = rat.Tournament(90, self._Usain, self._Nick)
        _results = _race.start()

        for _key, _runner in _results.items():
            _results.update({_key : _runner.name})

        #print(_results)
        self.assertTrue(_results[len(_results)] == 'Ник', 'test_Usain_Nick was failed')
        TournamentTest.all_results.append(_results)

    def test_Andrey_Nick(self):
        _race = rat.Tournament(90, self._Andrey, self._Nick)
        _results = _race.start()

        for _key, _runner in _results.items():
            _results.update({_key : _runner.name})

        #print(_results)
        self.assertTrue(_results[len(_results)] == 'Ник', 'test_Andrey_Nick was failed')
        TournamentTest.all_results.append(_results)

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