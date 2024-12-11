import unittest
from unittest import skipIf


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner= Runner('Vasya')
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk_broken(self):
        runner = Runner('Vasya')
        for i in range(0, 10):
            runner.walk()
        self.assertEqual(runner.distance, 150)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Vasya')
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_chellange(self):
        runner1 = Runner('Vasya')
        runner2 = Runner('Andrey')
        for i in range(0, 10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner('Usein', 10)
        self.runner2 = Runner('Andrey', 9)
        self.runner3 = Runner('Nik', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key,val in cls.all_results.items():
            print( "".join(f'{i}:{val[i]}, ' for i in val))

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        t1 = Tournament(90, self.runner1,self.runner3)
        self.all_results[0] = t1.start()
        last_key = list(self.all_results)[-1]
        self.assertTrue( self.all_results[last_key], 'Nik' )

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        t1 = Tournament(90, self.runner2, self.runner3)
        self.all_results[1] = t1.start()
        last_key = list(self.all_results)[-1]
        self.assertTrue( self.all_results[last_key], 'Nik' )

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        t1 = Tournament(90, self.runner1, self.runner2,self.runner3)
        self.all_results[2] = t1.start()
        last_key = list(self.all_results)[-1]
        self.assertTrue( self.all_results[last_key], 'Nik' )

if __name__ == '__main__':
    unittest.main()