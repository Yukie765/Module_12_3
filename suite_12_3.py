import unittest
import Module_12_2

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)
