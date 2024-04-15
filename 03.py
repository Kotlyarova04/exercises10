class NavalBattle:
    playing_field = [['~'] * 10 for i in range(10)]

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
        a = 0
        for row in NavalBattle.playing_field:
            a += row.count('~')
            if a == 100:
                print('игровое поле не заполнено')
        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.player
            print('попал')
        else:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print('мимо')



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
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)