import pygame


def print_text(message, color, x, y, size=50, display=pygame.display.set_mode(), font='fonts/Kefa.ttf'):
    font_size = pygame.font.Font(font, size)
    text = font_size.render(message, True, color)
    display.blit(text, (x, y))


def draw_image(image, width, height, x, y, dp=pygame.display.set_mode()):
    img = pygame.image.load(image)
    img = pygame.transform.scale(img, (width, height))
    dp.blit(img, (x, y))


def textScale(elem):
    if len(elem) in range(5, 7):
        return 0.85
    elif len(elem) in range(7, 8):
        return 0.8
    elif len(elem) in range(2, 5):
        return 0.9
    elif len(elem) in range(8, 10):
        return 0.7
    else:
        return 1


class Button:
    def __init__(self, width, height, activecolor=None, inactivecolor=None, image=None, imgpos=None, imgsize=None):
        self.width = width
        self.height = height
        self.active = activecolor
        self.incative = inactivecolor
        self.image = image
        self.imgpos = imgpos
        self.imgsize = imgsize
        if image is not None and imgpos is not None and imgsize is not None:
            self.pic = pygame.image.load(self.image)
            self.pic = pygame.transform.scale(self.pic, tuple(self.imgsize))

    def draw(self, x, y, dp=pygame.display.set_mode(), action=None, text=None, textcolor=None, textpos=None, textsize=None):
        mpos = pygame.mouse.get_pos()
        mclick = pygame.mouse.get_pressed()
        if (x < mpos[0] < x + self.width) and (y < mpos[1] < y + self.height):
            if self.active is not None:
                pygame.draw.rect(dp, self.active, (x, y, self.width, self.height))
            if mclick[0] == 1:
                if action is not None:
                    action()
                    pygame.time.delay(300)
        else:
            if self.active is not None:
                pygame.draw.rect(dp, self.incative, (x, y, self.width, self.height))
        if self.image is not None and self.imgpos is not None and len(self.imgpos) != 0:
            dp.blit(self.pic, (self.imgpos[0] + x, self.imgpos[1] + y))
        if text is not None and textpos is not None:
            print_text(str(text), textcolor, textpos[0] + x, textpos[1] + y, textsize, display=dp)



