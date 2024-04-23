import random


class NavalBattle:
    playing_field = None

    def __init__(self, player):
        self.player = player

    @staticmethod
    def show():
        for row in NavalBattle.playing_field:
            for ship in row:
                if ship != 1 and ship != 0:
                    print(f'{ship}', end=" ")
                else:
                    print('~', end=' ')
            print()

    def shot(self, x, y):
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return
        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.player
            print('попал')
        elif NavalBattle.playing_field[y - 1][x - 1] == self.player or NavalBattle.playing_field[y - 1][x - 1] == 'o':
            print('ошибка')
        else:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print('мимо')

    @classmethod
    def new_game(cls):
        NavalBattle.playing_field = [['~'] * 10 for _ in range(10)]
        ships = {'однопалуб': 4, 'двухпалуб': 3, 'трехпалуб': 2, 'четырехпалуб': 1}
        ship_length = {'однопалуб': 1, 'двухпалуб': 2, 'трехпалуб': 3, 'четырехпалуб': 4}
        directions = [(0, 1), (1, 0)]

        for ship_type, count in ships.items():
            for i in range(count):
                placed = False
                while not placed:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.choice(directions)

                    if cls.can_place_ship(x, y, direction, ship_length[ship_type]):
                        for i in range(ship_length[ship_type]):
                            cls.playing_field[y + i * direction[1]][x + i * direction[0]] = 1
                        placed = True

    @staticmethod
    def can_place_ship(x, y, direction, length):
        for i in range(length):
            new_x = x + i * direction[0]
            new_y = y + i * direction[1]
            if not 0 <= new_x < 10 or not 0 <= new_y < 10 or NavalBattle.playing_field[new_y][new_x] != '~':
                return False
        return True


player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
NavalBattle.show()
NavalBattle.playing_field
player1.shot(6, 2)
player1.shot(8, 8)
player1.shot(6, 7)
player1.shot(6, 7)
player1.shot(7, 7)
player1.shot(8, 7)
player1.shot(5, 7)
player1.shot(4, 7)
player1.shot(4, 8)
player1.shot(6, 8)
player1.shot(6, 9)
player1.shot(6, 8)
player1.shot(6, 10)
player1.shot(6, 1)
NavalBattle.show()
