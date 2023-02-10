import random
import copy
import pygame


def backuping(l1, l2):
    l2.clear()
    for i in range(len(l1)):
        temp = []
        for j in range(len(l1[0])):
            temp.append(copy.copy(l1[i][j]))
        l2.append(temp)
    return l2


def print_text(message, color, x, y, size=50, display=pygame.display.set_mode(), font='Kefa.ttf'):
    font_size = pygame.font.Font(font, size)
    text = font_size.render(message, True, color)
    display.blit(text, (x, y))


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
                    else:
                        return True
            if self.pole[0][0] == self.pole[0][1] or self.pole[0][0] == self.pole[1][0] or \
                    self.pole[-1][0] == self.pole[-2][0] or self.pole[-1][0] == self.pole[-1][1] or \
                    self.pole[0][-1] == self.pole[0][-2] or self.pole[0][-1] == self.pole[1][-1] or \
                    self.pole[-1][-1] == self.pole[-1][-2] or self.pole[-1][-1] == self.pole[-2][-1]:
                return False
            else:
                return True

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


class GameInterface(Game):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600
        self.fps = 30
        self.win = None
        self.lose = None
        self.sizep = 0
        self.icon = pygame.image.load('images/logo1.png')
        self.startX = 50
        self.startY = 50
        self.plineW = 10
        self.psizeQ = 125
        self.fontsize = 36
        self.colors = {
            'background': (248, 248, 232),
            'lines': (183, 173, 161),
            '.': (213, 205, 197),
            '2': (236, 227, 218),
            '4': (234, 223, 201),
            '8': (232, 179, 129),
            '16': (231, 153, 107),
            '32': (230, 130, 102),
            '64': (228, 130, 71),
            '128': (233, 208, 126),
            '256': (230, 205, 113),
            '512': (231, 201, 101),
            '1024': (230, 198, 89),
            '2048': (230, 195, 79),
            'black': (61, 58, 51),
            'bright': (250, 250, 250)
        }

    def makebackup(self):
        self.backup = backuping(self.pole, self.backup)
        self.scoreBack = self.score

    def drawpole(self, display):
        for y in range(0, self.sizep + 1):
            pygame.draw.line(display, self.colors['lines'],
                             (self.startX - self.plineW / 3, self.startY + self.psizeQ * y),
                             (self.psizeQ * self.sizep + self.startX + self.plineW / 2,
                              self.startY + self.psizeQ * y), self.plineW)

        for x in range(0, self.sizep + 1):
            pygame.draw.line(display, self.colors['lines'],
                             (self.startX + self.psizeQ * x, self.startY),
                             (self.startX + self.psizeQ * x, self.psizeQ * self.sizep + self.startY), self.plineW)
        for i in range(self.sizep):
            for j in range(self.sizep):
                if self.pole[i][j] != '.' and int(self.pole[i][j]) > 2048:
                    pygame.draw.rect(display, self.colors['black'],
                                     (self.startX + self.plineW / 2 + self.psizeQ * j,
                                      self.startY + self.psizeQ * i + self.plineW / 2,
                                      self.psizeQ - self.plineW / 2, self.psizeQ - self.plineW / 2))
                    print_text(self.pole[i][j], self.colors['bright'],
                               self.startX + self.plineW / 2 + self.psizeQ * (j + 0.5) -
                               self.fontsize * 0.35 * len(self.pole[i][j]) // 2,
                               self.startY + self.psizeQ * i + self.plineW / 2 + self.fontsize * 0.35,
                               int((self.fontsize * 0.35) // 1), display)
                else:
                    pygame.draw.rect(display, self.colors[self.pole[i][j]],
                                     (self.startX + self.plineW / 2 + self.psizeQ * j,
                                      self.startY + self.psizeQ * i + self.plineW / 2,
                                      self.psizeQ - self.plineW / 2, self.psizeQ - self.plineW / 2))
                    if self.pole[i][j] != '.' and int(self.pole[i][j]) in range(2, 5):
                        print_text(self.pole[i][j], self.colors['black'],
                                   self.startX + self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                   self.fontsize * len(self.pole[i][j]) // 2,
                                   self.startY + self.psizeQ * i + self.plineW / 2 + self.fontsize,
                                   self.fontsize, display)
                    elif self.pole[i][j] != '.' and int(self.pole[i][j]) not in range(2, 5):
                        print_text(self.pole[i][j], self.colors['bright'],
                                   self.startX + self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                   self.fontsize * len(self.pole[i][j]) // 2,
                                   self.startY + self.psizeQ * i + self.plineW / 2 + self.fontsize,
                                   self.fontsize, display)
        print_text(f'Your score: {self.score}', self.colors['black'], 10, 10, 30, display)

    def startGame(self):
        self.sizep = self.psize = 4
        cutrez = 1000
        usedcuts = 0
        self.spawnpole(self.psize)
        self.spawn()
        pygame.init()
        display = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption('2048 by MBUDO : game')
        pygame.display.set_icon(self.icon)
        clock = pygame.time.Clock()
        run = True
        while run:
            possiblecuts = self.score // cutrez
            self.moved = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        command = 'up'
                        self.makebackup()
                        self.move(command)
                    elif event.key == pygame.K_s:
                        command = 'down'
                        self.makebackup()
                        self.move(command)
                    elif event.key == pygame.K_a:
                        command = 'left'
                        self.makebackup()
                        self.move(command)
                    elif event.key == pygame.K_d:
                        command = 'right'
                        self.makebackup()
                        self.move(command)
                    elif event.key == pygame.K_c:
                        if possiblecuts - usedcuts> 0:
                            usedcuts += 1
                            self.makebackup()
                            command = 'cut'
                            self.move(command)
                            possiblecuts -= 1
                    elif event.key == pygame.K_b:
                        command = 'back'
                        self.move(command)
            if self.moved:
                self.spawn()
            display.fill(self.colors['background'])
            self.drawpole(display)
            clock.tick(self.fps)
            pygame.display.update()


# a = Game()
# a.start()
a = GameInterface()
a.startGame()