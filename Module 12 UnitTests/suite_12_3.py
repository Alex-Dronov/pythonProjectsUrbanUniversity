import unittest
import tests_12_1
import tests_12_2

raceTS = unittest.TestSuite()
raceTS.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
raceTS.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

_runner = unittest.TextTestRunner(verbosity=2)
_runner.run(raceTS)