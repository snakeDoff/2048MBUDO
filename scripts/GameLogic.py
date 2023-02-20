import random
import copy


def backuping(l1, l2):
    l2.clear()
    for i in range(len(l1)):
        temp = []
        for j in range(len(l1[0])):
            temp.append(copy.copy(l1[i][j]))
        l2.append(temp)
    return l2


class Game:
    def __init__(self):
        self.pole = list()
        self.framenum = 0
        self.score = 0
        self.psize = len(self.pole)
        self.clears = []
        self.backup = list()
        self.scoreBack = 0
        self.started = False
        self.moved = False

    def spawnpole(self, size):
        self.pole = []
        self.psize = size
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append('.')
            self.pole.append(temp)

    def spawn(self):
        self.checkclear()
        if len(self.clears) != 0:
            point = random.choice(self.clears)
            self.pole[point[0]][point[1]] = str(random.choice([2, 4]))

    def draw(self):
        print(f"frame number: {self.framenum}")
        print(f"Your score: {self.score}")
        self.framenum += 1
        for i in self.pole:
            for j in i:
                print(j, end=' ')
            print()

    def start(self):
        print('Input N to spawn field with size NxN')
        self.spawnpole(int(input()))
        self.started = True
        while self.started:

            self.draw()
            while True:
                command = input()
                if command.lower() in ['up', 'down', 'left', 'right', 'back']:
                    break
                else:
                    print('Please type a correct command')
            self.move(command)
            self.checklose()

    def checkclear(self):
        self.clears = []
        for i in range(len(self.pole)):
            for j in range(len(self.pole[0])):
                if self.pole[i][j] == '.':
                    self.clears.append([i, j])

    def checkwin(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                if self.pole[i][j] == '2048':
                    return True

    def checklose(self):
        self.checkclear()
        if len(self.clears) == 0:
            for i in range(1, self.psize - 1):
                for j in range(1, self.psize - 1):
                    if self.pole[i][j] == '.' or \
                            self.pole[i][j + 1] == self.pole[i][j] or \
                            self.pole[i][j] == self.pole[i][j - 1] or \
                            self.pole[i][j] == self.pole[i + 1][j] or \
                            self.pole[i][j] == self.pole[i - 1][j]:
                        return False
            if self.pole[0][0] == self.pole[0][1] or self.pole[0][0] == self.pole[1][0] or \
                    self.pole[-1][0] == self.pole[-2][0] or self.pole[-1][0] == self.pole[-1][1] or \
                    self.pole[0][-1] == self.pole[0][-2] or self.pole[0][-1] == self.pole[1][-1] or \
                    self.pole[-1][-1] == self.pole[-1][-2] or self.pole[-1][-1] == self.pole[-2][-1]:
                return False
        return False if len(self.clears) != 0 else True

    def swipedown(self, k):
        for i1 in range(self.psize - 1, 0, -1):
            for i in range(i1, 0, -1):
                if self.pole[i][k] == '.' and self.pole[i - 1][k] != '.':
                    self.pole[i][k] = self.pole[i - 1][k]
                    self.pole[i - 1][k] = '.'
                    self.moved = True

    def swipeup(self, k):
        for i1 in range(self.psize - 1):
            for i in range(i1, self.psize - 1):
                if self.pole[i][k] == '.' and self.pole[i + 1][k] != '.':
                    self.pole[i][k] = self.pole[i + 1][k]
                    self.pole[i + 1][k] = '.'
                    self.moved = True

    def swiperight(self, k):
        for j1 in range(self.psize - 1, 0, -1):
            for j in range(j1, 0, -1):
                if self.pole[k][j] == '.' and self.pole[k][j - 1] != '.':
                    self.pole[k][j] = self.pole[k][j - 1]
                    self.pole[k][j - 1] = '.'
                    self.moved = True

    def swipeleft(self, k):
        for j1 in range(self.psize - 1):
            for j in range(j1, self.psize - 1):
                if self.pole[k][j] == '.' and self.pole[k][j + 1] != '.':
                    self.pole[k][j] = self.pole[k][j + 1]
                    self.pole[k][j + 1] = '.'
                    self.moved = True

    def move(self, command):
        if command.lower() == 'down':
            for j in range(self.psize):
                self.swipedown(j)
                for i in range(self.psize - 1, 0, -1):
                    self.swipedown(j)
                    if self.pole[i][j] == self.pole[i - 1][j] and self.pole[i][j] != '.':
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)
                        self.pole[i - 1][j] = '.'
                        self.score += int(self.pole[i][j])
                        self.swipedown(j)
                        self.moved = True

        elif command.lower() == 'up':
            for j in range(self.psize):
                self.swipeup(j)
                for i in range(self.psize - 1):
                    self.swipeup(j)
                    if self.pole[i][j] == self.pole[i + 1][j] and self.pole[i][j] != '.':
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)
                        self.pole[i + 1][j] = '.'
                        self.score += int(self.pole[i][j])
                        self.swipeup(j)
                        self.moved = True
        elif command.lower() == 'right':
            for i in range(self.psize):
                self.swiperight(i)
                for j in range(self.psize - 1, 0, -1):
                    self.swiperight(i)
                    if self.pole[i][j] == self.pole[i][j - 1] and self.pole[i][j] != '.':
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)
                        self.pole[i][j - 1] = '.'
                        self.score += int(self.pole[i][j])
                        self.moved = True
                        self.swiperight(i)

        elif command.lower() == 'left':
            for i in range(self.psize):
                self.swipeleft(i)
                for j in range(self.psize - 1):
                    self.swipeleft(i)
                    if self.pole[i][j] == self.pole[i][j + 1] and self.pole[i][j] != '.':
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)
                        self.pole[i][j + 1] = '.'
                        self.score += int(self.pole[i][j])
                        self.swipeleft(i)
                        self.moved = True

        elif command.lower() == 'back':
            self.pole = backuping(self.backup, self.pole)
            self.score = self.scoreBack

        elif command.lower() == 'cut':
            for i in range(self.psize):
                for j in range(self.psize):
                    if self.pole[i][j] != '.':
                        if self.pole[i][j] == '2':
                            self.pole[i][j] = '.'
                        else:
                            self.pole[i][j] = str(int(self.pole[i][j]) // 2)
        elif 'double' in command.lower():
            i = int(command.split('-')[1])
            j = int(command.split('-')[2])
            self.pole[i][j] = str(int(self.pole[i][j]) * 2)
