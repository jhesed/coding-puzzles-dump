import math

DEFAULT_DAMAGE = 40
DAMAGE_SUBTRACTOR_PER_ENEMY = 0.20


class Enemy:
    def __init__(self, x, y, health=300):
        self.x = x
        self.y = y
        self.health = health

    def damage(self, amount):
        self.health -= math.floor(self.health - amount)

    def isdead(self):
        return self.health == 0


class Archer:
    def __init__(self, arrows, field, damage=40):
        self.x = 0  # starts at the leftmost square
        self.kills = 0
        self.arrows = arrows
        self.field = field
        self.damage = damage

    def moveleft(self):
        if self.x == 0:
            return
        self.x -= 1

    def moveright(self):
        if self.field.numCols == self.x:
            return
        self.x += 1

    def shoot(self):
        enemies = self.field.getEnemiesAtColumn(column=self.x)
        current_damage = DEFAULT_DAMAGE
        for enemy in enemies:
            enemy.damage(amount=current_damage)
            current_damage = current_damage - (
                current_damage * DAMAGE_SUBTRACTOR_PER_ENEMY
            )

    def outOfArrows(self):
        return self.arrows == 0


class Field:
    def __init__(self, rows=11, cols=10):
        self.grid = []
        self.numRows = rows
        self.numCols = cols
        for x in range(self.numCols):
            column = []
            for j in range(self.numRows):
                column.append(None)
            self.grid.append(column)

    @staticmethod
    def loadFromFileContents(contents):
        # create a field from file contents, usage should be:
        # const field = Field.loadFromFileContents("10 x 11 / (5, 2), (5, 3), (2, 4)")
        # BONUS
        pass

    def placeEnemy(self, x, y):
        self.grid[x][y] = Enemy(x, y)

    def vacateTile(self, x, y):
        # opposite of placeEnemy(), just marks a tile as null
        pass

    def getEnemiesAtColumn(self, column):
        # gets all "alive" enemies in the given column number
        pass

    def damageEnemiesAtColumn(self, column, initialDamage):
        # damage all enemies given the column number
        pass
