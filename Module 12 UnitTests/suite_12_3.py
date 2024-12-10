import unittest
import tests_12_3 as tst

raceTS = unittest.TestSuite()
raceTS.addTests(unittest.TestLoader().loadTestsFromTestCase(tst.RunnerTest))
raceTS.addTests(unittest.TestLoader().loadTestsFromTestCase(tst.TournamentTest))

_runner = unittest.TextTestRunner(verbosity=2)
_runner.run(raceTS)