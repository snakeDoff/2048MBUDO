from scripts.GameLogic import Game, backuping
from scripts import InterfaceElements as IE
import pygame


class GameInterface(Game):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600
        self.fps = 30
        self.win = None
        self.lose = None
        self.sizep = 0
        self.icon = pygame.image.load('images/logo.jpg')
        self.startX = 50
        self.startY = 50
        self.plineW = 10
        self.psizeQ = 125
        self.fontsize = 36
        self.possiblecuts = 0
        self.usedcuts = 0
        self.cutrez = 1000
        self.possibledob = 0
        self.useddob = 0
        self.mbutsize = (400, 75)
        self.doubrez = 1000
        self.scale = 1
        self.gamemodes = [3, 4, 8]
        self.cur = 1
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
        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()

    def makebackup(self):
        self.backup = backuping(self.pole, self.backup)
        self.scoreBack = self.score

    def drawpole(self):
        for y in range(0, self.sizep + 1):
            pygame.draw.line(self.display, self.colors['lines'],
                             (self.startX - (self.plineW / 3) * self.scale,
                              self.startY + (self.psizeQ * y) * self.scale),
                             (self.startX + (self.psizeQ * self.sizep) * self.scale + self.plineW / 2,
                              self.startY + (self.psizeQ * y) * self.scale), self.plineW)

        for x in range(0, self.sizep + 1):
            pygame.draw.line(self.display, self.colors['lines'],
                             (self.startX + (self.psizeQ * x) * self.scale, self.startY),
                             (self.startX + (self.psizeQ * x) * self.scale,
                              (self.startY + (self.psizeQ * self.sizep) * self.scale)),
                             self.plineW)
        for i in range(self.sizep):
            for j in range(self.sizep):
                if self.pole[i][j] != '.' and int(self.pole[i][j]) > 2048:
                    pygame.draw.rect(self.display, self.colors['black'],
                                     (self.startX + (self.plineW / 2 + self.psizeQ * j) * self.scale,
                                      self.startY + (self.psizeQ * i + self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale))
                    IE.print_text(self.pole[i][j], self.colors['bright'], display=self.display,
                                  x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                   ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale
                                  if (self.psizeQ / 2) -((self.fontsize / 2) * len(self.pole[i][j])) // 2 > 0 else
                                  (self.startX + (self.plineW / 2 + self.psizeQ * j)),
                                  y=self.startY + (
                                          self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                  size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
                else:
                    pygame.draw.rect(self.display, self.colors[self.pole[i][j]],
                                     (self.startX + (self.plineW / 2 + self.psizeQ * j) * self.scale,
                                      self.startY + (self.psizeQ * i + self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale))
                    if self.pole[i][j] != '.' and int(self.pole[i][j]) in range(2, 5):
                        IE.print_text(self.pole[i][j], self.colors['black'], display=self.display,
                                      x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                       ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale,
                                      y=self.startY + (
                                              self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                      size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
                    elif self.pole[i][j] != '.' and int(self.pole[i][j]) not in range(2, 5):
                        IE.print_text(self.pole[i][j], self.colors['bright'], display=self.display,
                                      x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                       ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale,
                                      y=self.startY + (
                                              self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                      size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
        IE.print_text(f'Your score: {self.score}', self.colors['black'], self.startX,
                      self.startY + (self.psizeQ * self.psize + self.plineW / 2) * self.scale, 30, self.display)

    def back(self):
        command = 'back'
        self.move(command)

    def cut(self):
        if self.possiblecuts - self.usedcuts > 0:
            self.usedcuts += 1
            self.makebackup()
            command = 'cut'
            self.move(command)
            self.possiblecuts -= 1
            self.checkclear()
            if len(self.clears) == self.psize ** 2:
                self.spawn()

    def getpoint(self):
        treep = True
        x = 0
        y = 0
        while treep:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            mpos = pygame.mouse.get_pos()
            mclick = pygame.mouse.get_pressed()
            for i in range(self.psize):
                for j in range(self.psize):
                    if self.startX + (self.plineW / 2 + self.psizeQ * j) * self.scale < mpos[0] \
                            < self.startX + (self.plineW / 2 + self.psizeQ * j + self.psizeQ - self.plineW / 2)\
                            * self.scale and \
                            self.startY + (self.psizeQ * i + self.plineW / 2) * self.scale < mpos[1] \
                            < self.startY + (self.psizeQ * i + self.plineW / 2 + self.psizeQ - self.plineW / 2)\
                            * self.scale:
                        if mclick[0] == 1 and self.pole[i][j] != '.':
                            x = i
                            y = j
                            treep = False
            self.clock.tick(self.fps)
        return x, y

    def double(self):
        i, j = self.getpoint()
        if self.possibledob - self.useddob > 0:
            self.useddob += 1
            self.makebackup()
            command = f'double-{i}-{j}'
            self.move(command)

    def BTchoose(self):
        self.BTc = 1
    def startGame(self, a):
        self.sizep = self.psize = a
        pygame.display.set_caption('2048 by MBUDO : game')
        self.usedcuts = 0
        self.BTc = 0
        self.cutrez = 1000
        self.useddob = 0
        self.score = 10 ** 6
        self.spawnpole(self.psize)
        self.spawn()
        rbut = IE.Button(30, 30, self.colors['lines'], self.colors['.'],
                         image='images/rbut1.png', imgsize=(20, 20), imgpos=(5, 5))
        cbut = IE.Button(80, 30, self.colors['lines'], self.colors['.'],
                         image='images/cut.png', imgsize=(20, 20), imgpos=(5,5))
        dbut = IE.Button(80, 30, self.colors['lines'], self.colors['.'],
                         image='images/double.png', imgsize=(20, 20), imgpos=(5,5))
        backbut = IE.Button(width=30, height=30,
                            activecolor=self.colors['lines'], inactivecolor=self.colors['.'],
                            image='images/back.png', imgsize=(20, 20), imgpos=(5, 5))
        run = True
        while run:
            self.possiblecuts = self.score // self.cutrez
            self.possibledob = self.score // self.doubrez
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
                        self.cut()
                    elif event.key == pygame.K_b:
                        self.back()
            if self.moved:
                self.spawn()
            self.display.fill(self.colors['background'])
            rbut.draw(self.startX + 90 * 2, 10, dp=self.display, action=self.back)
            cbut.draw(self.startX, 10, dp=self.display, action=self.cut,
                      text=f':{str(self.possiblecuts - self.usedcuts)}',
                      textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
            dbut.draw(self.startX + 90, 10, dp=self.display, action=self.double,
                      text=f':{str(self.possibledob - self.useddob)}',
                      textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
            backbut.draw(x=(self.width-self.startX-30), y=10, dp=self.display, action=self.BTchoose)
            if self.BTc:
                run = False
                self.startChose()
            self.drawpole()
            self.clock.tick(self.fps)
            pygame.display.update()

    def startMenu(self):
        loop = True
        self.end = 0
        pygame.display.set_caption('2048 by MBUDO : Menu')
        chmodebut = IE.Button(self.mbutsize[0], self.mbutsize[1], self.colors['lines'], self.colors['.'])
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.display.fill(self.colors['background'])
            IE.print_text('2048', self.colors['black'], 200, 5, size=75, display=self.display)
            IE.print_text('by MBUDO', self.colors['black'], 100, 85, size=75, display=self.display)
            chmodebut.draw(100, 200, text='Play', textcolor=self.colors['black'], textsize=50,
                           textpos=(50, 5), action=self.endlop)
            if self.end == 1:
                loop = False
                self.startChose()
            pygame.display.update()
            self.clock.tick(self.fps)

    def endlop(self):
        self.end = 1

    def BTmenu(self):
        self.BTm = 1
    def startChose(self):
        loop = True
        self.BTm = 0
        self.end = 0
        pygame.display.set_caption('2048 by MBUDO : Choosing mode')
        larr = IE.Button(width=100, height=50, image='images/leftarrow.png',
                         imgsize=(95, 45), imgpos=(5, 5), activecolor=self.colors['lines'],
                         inactivecolor=self.colors['.'])
        rarr = IE.Button(width=100, height=50, image='images/rightarrow.png',
                         imgsize=(100, 50), imgpos=(0, 0), activecolor=self.colors['lines'],
                         inactivecolor=self.colors['.'])
        mbut = IE.Button(width=100, height=50, activecolor=self.colors['lines'],
                         inactivecolor=self.colors['.'])
        backbut = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'],
                            image='images/back.png', imgsize=(20, 20), imgpos=(5, 5))
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.display.fill(self.colors['background'])
            IE.draw_image(f'images/{self.gamemodes[self.cur]}.png', 400, 400, 100, 50, self.display)
            larr.draw(x=100, y=450, dp=self.display, action=self.larrf)
            rarr.draw(x=400, y=450, dp=self.display, action=self.rarrf)
            mbut.draw(x=250, y=450, dp=self.display,
                      text='Start game', textcolor=self.colors['black'], textsize=15, textpos=(5, 15), action=self.endlop)
            backbut.draw(x=(self.width - 130), y=50, dp=self.display, action=self.BTmenu)
            if self.end == 1:
                loop = False
                self.setScale()
                self.startGame(self.gamemodes[self.cur])
            if self.BTm:
                loop = False
                self.startMenu()
            pygame.display.update()
            self.clock.tick(self.fps)

    def setScale(self):
        if self.gamemodes[self.cur] == 4:
            self.scale = 1
        elif self.gamemodes[self.cur] == 3:
            self.scale = 1.32
        elif self.gamemodes[self.cur] == 8:
            self.scale = 0.5
            
    def larrf(self):
        if self.cur == 0:
            self.cur = len(self.gamemodes) - 1
        else:
            self.cur -= 1

    def rarrf(self):
        if self.cur == len(self.gamemodes) - 1:
            self.cur = 0
        else:
            self.cur += 1

# a = Game()
# a.start()
a = GameInterface()
a.startMenu()