from scripts.GameLogic import Game, backuping, checkravn
from scripts import InterfaceElements as IE
from saves.const import *
import pygame
import json


def restart():
    import sys
    print("argv was", sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")
    import os
    os.execv(sys.executable, ['python'] + sys.argv)


class GameInterface(Game):
    def __init__(self):
        super().__init__()
        self.BTc = None
        self.width = 600
        self.height = 600
        self.fps = 30
        self.sizep = 0
        self.icon = pygame.image.load('images/logo1.png')
        self.startX = 50
        self.startY = 50
        self.plineW = 10
        self.conti = 0
        self.topscore = None
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
        self.gamemodes = [3, 4, 5, 8]
        self.cur = 1
        self.fullscrined = 0
        self.topscoreback = 0
        self.colors = COLORS
        self.resolutions = RESOLUTIONS
        self.bindedButtons = BINDEDBUTTONS
        self.dss = "1:1"
        self.curds = 0
        self.curres = 0
        self.resline = self.resolutions[self.dss]
        self.loadRecords("load")
        pygame.init()
        self.settingssaves('load')
        if self.fullscrined:
            self.display = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()

    def makebackup(self):
        if not checkravn(self.pole, self.backup):
            self.backup = backuping(self.pole, self.backup)
            self.scoreBack = self.score
            self.useddobBack = self.useddob
            self.usedcutsBack = self.usedcuts

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
                    IE.print_text(self.pole[i][j], self.colors['bright'],
                                  x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                   ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale
                                  if (self.psizeQ / 2) - ((self.fontsize / 2) * len(self.pole[i][j])) // 2 > 0 else
                                  (self.startX + (self.plineW / 2 + self.psizeQ * j)),
                                  y=self.startY + (
                                          self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                  display=self.display,
                                  size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
                else:
                    pygame.draw.rect(self.display, self.colors[self.pole[i][j]],
                                     (self.startX + (self.plineW / 2 + self.psizeQ * j) * self.scale,
                                      self.startY + (self.psizeQ * i + self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale,
                                      (self.psizeQ - self.plineW / 2) * self.scale))
                    if self.pole[i][j] != '.' and int(self.pole[i][j]) in range(2, 5):
                        IE.print_text(self.pole[i][j], self.colors['black'],
                                      x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                       ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale,
                                      y=self.startY + (
                                              self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                      display=self.display,
                                      size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
                    elif self.pole[i][j] != '.' and int(self.pole[i][j]) not in range(2, 5):
                        IE.print_text(self.pole[i][j], self.colors['bright'],
                                      x=self.startX + (self.plineW / 2 + self.psizeQ * (j + 0.5) -
                                                       ((self.fontsize / 2) * len(self.pole[i][j])) // 2) * self.scale,
                                      y=self.startY + (
                                              self.psizeQ * i + self.plineW / 2 + self.fontsize) * self.scale,
                                      display=self.display,
                                      size=int(self.fontsize * self.scale * IE.textScale(self.pole[i][j])))
        IE.print_text(f'Your score: {self.score}', self.colors['black'], self.startX,
                      self.startY + (self.psizeQ * self.psize + self.plineW / 2) * self.scale, self.display, 30)

    def back(self):
        command = 'back'
        # if (self.usedcuts or self.useddob) and (self.usedcutsBack or self.useddobBack):
        #     if self.topscore[f"{self.sizep}x{self.sizep}"][1] > self.scr
        #     self.topscore[f"{self.sizep}x{self.sizep}"] = [self.topscore[f"{self.sizep}x{self.sizep}"][0], self.topscoreback]
        # elif (self.usedcuts or self.useddob) and not (self.usedcutsBack or self.useddobBack):
        #     self.topscore[f"{self.sizep}x{self.sizep}"]
        self.usedcuts = self.usedcutsBack
        self.useddob = self.useddobBack
        self.move(command)

    def settingssaves(self, key):
        if key == 'upload':
            save = {
                "fullscreen": self.fullscrined,
                "aspectratio": list(self.resolutions.keys())[self.curds],
                "resolution": self.curres,
                "up": IE.get_key(self.bindedButtons["up"], KEYS),
                "down": IE.get_key(self.bindedButtons["down"], KEYS),
                "left": IE.get_key(self.bindedButtons["left"], KEYS),
                "right": IE.get_key(self.bindedButtons["right"], KEYS)
            }
            with open(f"saves/settings.json", 'w') as F:
                json.dump(save, F, indent=4)

        if key == 'load':
            try:
                with open(f"saves/settings.json", 'rb') as F:
                    save = json.load(F)
            except FileNotFoundError or KeyError:
                self.settingssaves('upload')
                with open(f"saves/settings.json", 'rb') as F:
                    save = json.load(F)
            finally:
                self.fullscrined = save["fullscreen"]
                self.width, self.height = list(
                    map(int, self.resolutions[save["aspectratio"]][save["resolution"]].split('x')))
                self.curres = save["resolution"]
                print(self.width, self.height)
                self.curds = list(self.resolutions.keys()).index(save["aspectratio"])
                self.bindedButtons['up'] = KEYS[save["up"]]
                self.bindedButtons['down'] = KEYS[save["down"]]
                self.bindedButtons['left'] = KEYS[save["left"]]
                self.bindedButtons['right'] = KEYS[save["right"]]

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

    def Brestart(self):
        self.spawnpole(self.psize)
        self.score = 0
        self.useddob = 0
        self.usedcuts = 0
        self.conti = 0
        self.spawn()
        self.makebackup()

    def GameSave(self, key):
        if key == 'upload':
            save = {
                "pole": self.pole,
                "score": self.score,
                "usedcuts": self.usedcuts,
                "useddob": self.useddob,
                "scoreBack": self.scoreBack,
                "poleBack": self.backup,
                "continue": self.conti,
                "useddobBack": self.useddobBack,
                "usedcutsBack": self.usedcutsBack
            }
            with open(f"saves/{self.psize}.json", 'w') as F:
                json.dump(save, F, indent=4)
                F.close()
        else:
            try:
                with open(f'saves/{self.psize}.json', 'rb') as F:
                    save = json.load(F)
                    self.pole = save["pole"]
                    self.score = save["score"]
                    self.usedcuts = save["usedcuts"]
                    self.useddob = save["useddob"]
                    self.scoreBack = save["scoreBack"]
                    self.backup = save["poleBack"]
                    self.conti = save["continue"]
                    self.usedcutsBack = save["usedcutsBack"]
                    self.useddobBack = save["useddobBack"]
            except FileNotFoundError or KeyError:
                self.spawnpole(self.psize)
                self.score = 0
                self.conti = 0
                self.useddob = 0
                self.usedcuts = 0
                self.useddobBack = 0
                self.usedcutsBack = 0
                self.spawn()
                self.makebackup()

    def contGame(self):
        self.conti = 1

    def drawwin(self):
        backbut1 = IE.Button(width=300, height=50, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        restart = IE.Button(width=300, height=50, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        continu = IE.Button(width=300, height=50, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        surface1 = self.display.convert_alpha()
        surface1.fill([255, 255, 255, 0])
        pygame.draw.rect(surface1, (230, 198, 89, 200), (0, 0, self.width, self.height))
        self.display.blit(surface1, (0, 0))
        IE.print_text("You win!", x=self.width / 2 - 150, y=self.height / 2 - 100,
                      display=self.display, color=self.colors['black'], size=70)
        backbut1.draw((self.width / 2 - 150), self.height / 2, self.display, action=self.BTchoose, text='back to menu',
                      textsize=40, textpos=(5, 5), textcolor=self.colors['black'])
        restart.draw((self.width / 2 - 150), self.height / 2 + 60, self.display, action=self.Brestart, text='restart',
                     textsize=40, textpos=(65, 5), textcolor=self.colors['black'])
        continu.draw((self.width / 2 - 150), self.height / 2 + 120, self.display, action=self.contGame, text='continue',
                     textsize=40, textpos=(55, 5), textcolor=self.colors['black'])

    def drawlose(self):
        backbut1 = IE.Button(width=300, height=50, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        restart = IE.Button(width=300, height=50, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        surface1 = self.display.convert_alpha()
        surface1.fill([255, 255, 255, 0])
        pygame.draw.rect(surface1, (228, 130, 71,  200), (0, 0, self.width, self.height))
        self.display.blit(surface1, (0, 0))
        IE.print_text("You lose.", x=self.width / 2 - 150, y=self.height / 2 - 100,
                      display=self.display, color=self.colors['black'], size=70)
        backbut1.draw((self.width / 2 - 150), self.height / 2, self.display, action=self.BTchoose, text='back to menu',
                      textsize=40, textpos=(5, 5), textcolor=self.colors['black'])
        restart.draw((self.width / 2 - 150), self.height / 2 + 60, self.display, action=self.Brestart, text='restart',
                     textsize=40, textpos=(65, 5), textcolor=self.colors['black'])
        
    def checkTop(self):
        toprate = self.topscore[f"{self.sizep}x{self.sizep}"]
        if not (self.usedcuts or self.useddob):
            if self.score > toprate[0]:
                nr = [self.score, toprate[1]]
                self.topscore[f"{self.sizep}x{self.sizep}"] =  nr
                self.loadRecords("upload")
        else:
            if self.score > toprate[1]:
                nr = [toprate[0], self.score]
                self.topscore[f"{self.sizep}x{self.sizep}"] =  nr
                self.loadRecords("upload")
       

    def startGame(self, a):
        self.sizep = self.psize = a
        pygame.display.set_caption('2048 by MBUDO : game')
        self.BTc = 0
        self.startX = (self.width - 500) // 2
        self.startY = (self.height - 500) // 2
        self.GameSave("load")
        rbut = IE.Button(30, 30, self.colors['lines'], self.colors['.'],
                         image='images/rbut1.png', imgsize=(20, 20), imgpos=(5, 5))
        cbut = IE.Button(80, 30, self.colors['lines'], self.colors['.'],
                         image='images/cut.png', imgsize=(20, 20), imgpos=(5, 5))
        dbut = IE.Button(80, 30, self.colors['lines'], self.colors['.'],
                         image='images/double.png', imgsize=(20, 20), imgpos=(5, 5))
        backbut = IE.Button(width=30, height=30,
                            activecolor=self.colors['lines'], inactivecolor=self.colors['.'],
                            image='images/back.png', imgsize=(20, 20), imgpos=(5, 5))
        resbut = IE.Button(width=69, height=30,
                           activecolor=self.colors['lines'], inactivecolor=self.colors['.'])

        run = True
        while run:
            self.possiblecuts = self.score // self.cutrez
            self.possibledob = self.score // self.doubrez
            win = self.checkwin()
            lose = self.checklose()
            self.moved = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN and (not win or self.conti) and not lose:
                    if event.key == self.bindedButtons['up']:
                        command = 'up'
                        self.move(command)
                    elif event.key == self.bindedButtons['down']:
                        command = 'down'
                        self.move(command)
                    elif event.key == self.bindedButtons['left']:
                        command = 'left'
                        self.move(command)
                    elif event.key == self.bindedButtons['right']:
                        command = 'right'
                        self.move(command)
                    elif event.key == pygame.K_c:
                        self.cut()
                    elif event.key == pygame.K_b:
                        self.back()
            self.makebackup()
            self.GameSave("upload")
            if self.moved:
                self.spawn()
                self.checkTop()
            self.display.fill(self.colors['background'])
            self.drawpole()
            if (win and not self.conti) or lose:
                rbut.draw(self.startX + 90 * 2, self.startY - 40, dp=self.display)
                cbut.draw(self.startX, self.startY - 40, dp=self.display,
                          text=f':{str(self.possiblecuts - self.usedcuts)}',
                          textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
                dbut.draw(self.startX + 90, self.startY - 40, dp=self.display,
                          text=f':{str(self.possibledob - self.useddob)}',
                          textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
                backbut.draw(x=(self.width - self.startX - 30), y=self.startY - 40, dp=self.display)
                resbut.draw(x=(self.startX + 220), y=self.startY - 40, dp=self.display,
                            text='reset', textsize=20, textpos=(5, 3), textcolor=self.colors['black'])
                if win and not lose:
                    self.drawwin()
                else:
                    self.drawlose()
            else:
                rbut.draw(self.startX + 90 * 2, self.startY-40, dp=self.display, action=self.back)
                cbut.draw(self.startX, self.startY-40, dp=self.display, action=self.cut,
                          text=f':{str(self.possiblecuts - self.usedcuts)}',
                          textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
                dbut.draw(self.startX + 90, self.startY-40, dp=self.display, action=self.double,
                          text=f':{str(self.possibledob - self.useddob)}',
                          textpos=(25, 3), textsize=20, textcolor=self.colors['black'])
                backbut.draw(x=(self.width - self.startX - 30), y=self.startY-40, dp=self.display, action=self.BTchoose)
                resbut.draw(x=(self.startX + 220), y=self.startY-40, dp=self.display, action=self.Brestart,
                            text='reset', textsize=20, textpos=(5, 3), textcolor=self.colors['black'])

            if self.BTc:
                run = False
                self.startChose()
            self.clock.tick(self.fps)
            pygame.display.update()

    def close(self):
        pygame.quit()
        quit(0)

    def startMenu(self):
        loop = True
        self.end = 0
        self.startX = (self.width - 400) / 2
        self.startY = (self.height - 600) / 2
        pygame.display.set_caption('2048 by MBUDO : Menu')
        chmodebut = IE.Button(self.mbutsize[0], self.mbutsize[1], self.colors['lines'], self.colors['.'])
        quitbut = IE.Button(self.mbutsize[0], self.mbutsize[1], self.colors['lines'], self.colors['.'])
        settingsbut = IE.Button(self.mbutsize[0], self.mbutsize[1], self.colors['lines'], self.colors['.'])
        topscoresbut = IE.Button(self.mbutsize[0], self.mbutsize[1], self.colors['lines'], self.colors['.'])
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.display.fill(self.colors['background'])
            IE.print_text('2048', self.colors['black'], self.startX + 100, self.startY + 5,
                          size=75, display=self.display)
            IE.print_text('by MBUDO', self.colors['black'], self.startX, self.startY + 85,
                          size=75, display=self.display)
            chmodebut.draw(self.startX, self.startY + 200, text='Play', textcolor=self.colors['black'], textsize=50,
                           textpos=(75, 5), action=self.endlop, actionkey=1, dp=self.display)
            quitbut.draw(self.startX, self.startY + 470, text='Quit', textcolor=self.colors['black'], textsize=50,
                         textpos=(75, 5), action=self.close, dp=self.display)
            topscoresbut.draw(self.startX, self.startY + 380, dp=self.display,
                              text='Top scores',  textcolor=self.colors['black'], textsize=50, textpos=(42, 5),
                              action=self.endlop, actionkey=3)
            settingsbut.draw(self.startX, self.startY + 290, text='Settings', textcolor=self.colors['black'], textsize=50,
                             textpos=(75, 5), action=self.endlop, actionkey=2, dp=self.display)
            if self.end == 1:
                loop = False
                self.startChose()
            if self.end == 2:
                loop = False
                self.startSettings()
            if self.end == 3:
                loop = False
                self.startRecords()
            pygame.display.update()
            self.clock.tick(self.fps)

    def endlop(self, key):
        if key == 1:
            self.end = 1
        elif key == 2:
            self.end = 2
        elif key == 3:
            self.end = 3

    def BTmenu(self):
        self.BTm = 1

    def startChose(self):
        loop = True
        self.BTm = 0
        self.end = 0
        self.startX = (self.width - 400) / 2
        self.startY = (self.height - 600) / 2
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
            IE.draw_image(f'images/spaces/{self.gamemodes[self.cur]}.png', 400, 400, self.startX, self.startY + 50, self.display)
            larr.draw(x=self.startX, y=self.startY+450, dp=self.display, action=self.larrf)
            rarr.draw(x=self.startX + 300, y=self.startY+450, dp=self.display, action=self.rarrf)
            mbut.draw(x=self.startX + 150, y=self.startY+450, dp=self.display,
                      text='Start game', textcolor=self.colors['black'], textsize=15, textpos=(5, 15),
                      action=self.endlop, actionkey=1)
            backbut.draw(x=self.startX + 370, y=self.startY + 50, dp=self.display, action=self.BTmenu)
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
        elif self.gamemodes[self.cur] == 5:
            self.scale = 0.8
            
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

    def isfullscrined(self):
        if self.fullscrined:
            return '✓'
        else:
            return '✖'

    def setfullscreen(self):
        if not self.fullscrined:
            self.fullscrined = 1
        else:
            self.fullscrined = 0

    def drawSettingsText(self):
        IE.print_text('Full-screen :', x=self.startX, y=self.startY + 50, color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Aspect ratio :', x=self.startX, y=self.startY + 100,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Resolution :', x=self.startX, y=self.startY + 150,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Buttons :', x=self.startX, y=self.startY + 200,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Move UP :', x=self.startX + 50, y=self.startY + 250,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Move DOWN :', x=self.startX + 50, y=self.startY + 300,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Move LEFT :', x=self.startX + 50, y=self.startY + 350,  color=self.colors['black'],display=self.display,
                      size=25)
        IE.print_text('Move RIGHT :', x=self.startX + 50, y=self.startY + 400, display=self.display, color=self.colors['black'],
                      size=25)
        IE.print_text(list(self.resolutions.keys())[self.curds], x=self.startX + 500 - 175, y=self.startY + 100,
                      color=self.colors['black'], display=self.display, size=25)
        IE.print_text(self.resline[self.curres],
                      x=(self.startX + 500 - 220 if len(self.resline[self.curres]) < 8
                         else self.startX + 500 - 240), y=self.startY + 150,
                      color=self.colors['black'], display=self.display, size=25)

    def startSettings(self):
        self.changing = False
        loop = True
        self.startX = (self.width - 400) / 2
        self.startY = (self.height - 500) / 2
        self.BTm = 0
        pygame.display.set_caption('2048 by MBUDO : Settings')
        backbut = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'],
                            image='images/back.png', imgsize=(20, 20), imgpos=(5, 5))
        fscreenbut = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        confsetbut = IE.Button(width=110, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        nextres = IE.Button(width=60, height=40, image="images/rightarrow.png", imgpos=(0, 0), imgsize=(60, 40))
        prevres = IE.Button(width=60, height=40, image="images/leftarrow.png", imgpos=(0, 0), imgsize=(60, 40))
        nextss = IE.Button(width=60, height=40, image="images/rightarrow.png", imgpos=(0, 0), imgsize=(60, 40))
        prevss = IE.Button(width=60, height=40, image="images/leftarrow.png", imgpos=(0, 0), imgsize=(60, 40))
        bindupb = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        binddownb = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        bindleftb = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])
        bindrightb = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'])

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.resline = self.resolutions[list(self.resolutions.keys())[self.curds]]
            self.display.fill(self.colors['background'])
            backbut.draw(x=self.startX + 370, y=self.startY, dp=self.display, action=self.BTmenu)
            fscreenbut.draw(x=self.startX + 250, y=self.startY + 50, dp=self.display, text=str(self.isfullscrined()),
                            textcolor=self.colors['black'], textpos=(4, 2), textsize=25, textfont='fonts/symbols.ttc',
                            action=self.setfullscreen)
            confsetbut.draw(x=self.startX + 260, y=self.startY + 450, dp=self.display,
                            text='confirm', textcolor=self.colors['black'], textsize=25, textpos=(2, 2),
                            action=self.confirmB)
            nextres.draw(x=self.startX + 400, y=self.startY + 150, dp=self.display, action=self.moveres, actionkey='next')
            prevres.draw(x=self.startX + 200, y=self.startY + 150, dp=self.display, action=self.moveres, actionkey='prev')
            nextss.draw(x=self.startX + 400, y=self.startY + 100, dp=self.display, action=self.movess, actionkey='next')
            prevss.draw(x=self.startX + 250, y=self.startY + 100, dp=self.display, action=self.movess, actionkey='prev')
            bindupb.draw(x=self.startX + 250, y=self.startY + 250, dp=self.display,
                         text=f'{IE.get_key(self.bindedButtons["up"], KEYS)}',
                         textcolor=self.colors['black'],
                         textsize=25, textpos=(7, 1), action=self.bindbuttons, actionkey='up')
            binddownb.draw(x=self.startX + 250, y=self.startY + 300, dp=self.display,
                           text=f'{IE.get_key(self.bindedButtons["down"], KEYS)}',
                           textcolor=self.colors['black'],
                           textsize=25, textpos=(7, 1), action=self.bindbuttons, actionkey='down')
            bindrightb.draw(x=self.startX + 250, y=self.startY + 400, dp=self.display,
                            text=f'{IE.get_key(self.bindedButtons["right"], KEYS)}',
                            textcolor=self.colors['black'],
                            textsize=25, textpos=(7, 1), action=self.bindbuttons, actionkey='right')
            bindleftb.draw(x=self.startX + 250, y=self.startY + 350, dp=self.display,
                           text=f'{IE.get_key(self.bindedButtons["left"], KEYS)}',
                           textcolor=self.colors['black'],
                           textsize=25, textpos=(7, 1), action=self.bindbuttons, actionkey='left')
            if len(IE.get_key(self.bindedButtons["up"], KEYS)) > 1:
                bindupb.width = 90
            else:
                bindupb.width = 30
            if len(IE.get_key(self.bindedButtons["down"], KEYS)) > 1:
                binddownb.width = 90
            else:
                binddownb.width = 30
            if len(IE.get_key(self.bindedButtons["left"], KEYS)) > 1:
                bindleftb.width = 90
            else:
                bindleftb.width = 30
            if len(IE.get_key(self.bindedButtons["right"], KEYS)) > 1:
                bindrightb.width = 90
            else:
                bindrightb.width = 30
            self.drawSettingsText()
            if self.BTm:
                loop = False
                self.startMenu()
            pygame.display.update()
            self.clock.tick(self.fps)

    def moveres(self, key):
        if key == 'prev':
            if self.curres == 0:
                self.curres = len(self.resolutions[list(self.resolutions.keys())[self.curds]]) - 1
            else:
                self.curres -= 1
        else:
            if self.curres == len(self.resolutions[list(self.resolutions.keys())[self.curds]]) - 1:
                self.curres = 0
            else:
                self.curres += 1

    def movess(self, key):
        if key == 'prev':
            if self.curds == 0:
                self.curds = len(self.resolutions.keys()) - 1
            else:
                self.curds -= 1
        else:
            if self.curds == len(self.resolutions.keys()) - 1:
                self.curds = 0
            else:
                self.curds += 1
        self.curres = 0

    def confirmB(self):
        setres = self.resolutions[list(self.resolutions.keys())[self.curds]][self.curres].split('x')
        self.width1 = int(setres[0])
        self.height1 = int(setres[1])
        self.settingssaves('upload')
        restart()

    def bindbuttons(self, key):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key in KEYS.values():
                        if event.key in self.bindedButtons.values():
                            self.bindedButtons[IE.get_key(event.key, self.bindedButtons)] = self.bindedButtons[key]
                            self.bindedButtons[key] = event.key
                        else:
                            self.bindedButtons[key] = event.key
                        loop = False

    def drawTopScores(self):
        w = self.width - self.startX * 2
        h = self.height - self.startY * 2 - 150
        surface = pygame.Surface((w, h))
        surface.fill(self.colors['background'])
        hs = 45
        IE.print_text('mode', self.colors['black'], 0, 5, surface, 30)
        IE.print_text('casual', self.colors['black'], 100, 5, surface, 30)
        IE.print_text('gigachad mode', self.colors['black'], 300, 5, surface, 30)
        step = (h - hs * len(self.topscore.keys())) / (len(self.topscore.keys()) + 2)
        for index, key in enumerate(list(self.topscore.keys())):
            ts = pygame.Surface((w, hs))
            ts.fill(self.colors["background"])
            IE.print_text(str(key), self.colors["black"], 5, 5, ts, 30)
            wt = len(str(self.topscore[key][0])) * 45 
            ee = pygame.Surface((wt, 30))
            ee.fill(self.colors["background"])
            IE.print_text(str(self.topscore[key][0]), self.colors['black'], 0, 0, ee, 30)
            if wt > 300:
                ee = pygame.transform.scale(ee, (300, 30))
            ts.blit(ee,(100, 5))
            wt = len(str(self.topscore[key][1])) * 20
            ee = pygame.Surface((wt, 30))
            ee.fill(self.colors["background"])
            IE.print_text(str(self.topscore[key][1]), self.colors['black'], 0, 0, ee, 30)
            if wt > 300:
                ee = pygame.transform.scale(ee, (300, 30))
            ts.blit(ee,(300, 5))

            surface.blit(ts, (0, (hs + step) * (index + 1)))

        return surface
        
    def startRecords(self):
        loop = True
        self.BTm = 0
        self.startX = (self.width - 550) / 2
        self.startY = (self.height - 550) / 2
        backbut = IE.Button(width=30, height=30, activecolor=self.colors['lines'], inactivecolor=self.colors['.'],
                            image='images/back.png', imgsize=(20, 20), imgpos=(5, 5))
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)
            self.display.fill(self.colors['background'])
            backbut.draw(x=(self.width - self.startX - 50), y=(self.startY + 50), dp=self.display, action=self.BTmenu)
            IE.print_text("Top scores", x=self.startX + 40, y=self.startY + 20, color=self.colors['black'],
                          display=self.display, size=70)

            if self.BTm:
                loop = False
                self.startMenu()
            self.display.blit(self.drawTopScores(), (self.startX,  self.startY + 100))
            pygame.display.update()
            self.clock.tick(self.fps)

    def loadRecords(self, key):
        if key == "load":
            try:
                with open("saves/topscores.json", 'r') as F:
                    self.topscore = json.load(F)
            except FileNotFoundError:
                with open("saves/topscores.json", "w") as F:
                    defoul = {
                        "3x3": [0, 0],
                        "4x4": [0, 0],
                        "5x5": [0, 0],
                        "8x8": [0, 0]
                    }
                    json.dump(defoul, F, indent=4)
        else:
            with open("saves/topscores.json", "w") as F:
                json.dump(self.topscore, F, indent=4)



if __name__ == "__main__":
    a = GameInterface()
    a.startMenu()