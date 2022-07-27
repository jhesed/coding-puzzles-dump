import unittest

from src.merida import Archer, Field


class TestMerida(unittest.TestCase):
    def test_ObjectOrientedProgramming_moveleft(self):
        archer = Archer(40, Field())
        archer.x = 5
        archer.moveleft()
        archer.moveleft()

        self.assertEqual(archer.x, 3)

    def test_ObjectOrientedProgramming_moveleft_edge(self):
        archer = Archer(40, Field())
        archer.x = 0
        archer.moveleft()
        archer.moveleft()

        self.assertEqual(archer.x, 0)

    def test_ObjectOrientedProgramming_moveright(self):
        archer = Archer(40, Field())
        archer.x = 5
        archer.moveright()
        archer.moveright()

        self.assertEqual(archer.x, 7)

    def test_ObjectOrientedProgramming_moveright_edge(self):
        archer = Archer(40, Field())
        archer.x = 9
        archer.moveright()
        archer.moveright()

        self.assertEqual(archer.x, 9)

    def test_ObjectOrientedProgramming_shoot(self):
        archer = Archer(40, Field())
        archer.shoot()

        self.assertEqual(archer.arrows, 39)
        self.assertEqual(archer.outOfArrows(), False)

    def test_ObjectOrientedProgramming_shoot_none(self):
        archer = Archer(0, Field())
        archer.shoot()

        self.assertEqual(archer.outOfArrows(), True)

    def test_Algorithms_shoot(self):
        field = Field()
        archer = Archer(40, field)

        for i in range(9):
            archer.moveright()

        self.assertEqual(archer.x, 9)

        field.placeEnemy(9, 2)
        field.placeEnemy(9, 5)
        field.placeEnemy(3, 4)
        field.placeEnemy(9, 6)
        field.placeEnemy(1, 8)

        archer.shoot()
        enemies = field.getEnemiesAtColumn(9)

        self.assertEqual(enemies[0].health, 260)
        self.assertEqual(enemies[1].health, 268)
        self.assertEqual(enemies[2].health, 275)
        self.assertEqual(archer.kills, 0)

    def test_Algorithms_shoot_col(self):
        field = Field()
        archer = Archer(10, field)

        for i in range(9):
            archer.moveright()

        self.assertEqual(archer.x, 9)

        field.placeEnemy(9, 2)
        field.placeEnemy(9, 5)
        field.placeEnemy(3, 4)
        field.placeEnemy(9, 6)
        field.placeEnemy(1, 8)

        for i in range(10):
            archer.shoot()

        enemies = field.getEnemiesAtColumn(9)

        self.assertEqual(len(enemies), 1)
        self.assertEqual(enemies[0].health, 36)
        self.assertEqual(archer.kills, 2)

    def test_DataStructures_getEnemiesAtColumn(self):
        field = Field()
        field.placeEnemy(1, 5)
        field.placeEnemy(9, 2)
        field.placeEnemy(9, 5)

        self.assertEqual(len(field.getEnemiesAtColumn(9)), 2)
        self.assertTrue(field.getEnemiesAtColumn(9))
