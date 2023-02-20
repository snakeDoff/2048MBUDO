import pygame


def print_text(message, color, x, y, display, size=50, font='fonts/Kefa.ttf'):
    font_size = pygame.font.Font(font, size)
    text = font_size.render(message, True, color)
    display.blit(text, (x, y))


def draw_image(image, width, height, x, y, dp):
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


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key


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

    def draw(self, x, y, dp, action=None, text=None, textcolor=None, textpos=None, textsize=None, actionkey=None,
             textfont='fonts/Kefa.ttf'):
        mpos = pygame.mouse.get_pos()
        mclick = pygame.mouse.get_pressed()
        if (x < mpos[0] < x + self.width) and (y < mpos[1] < y + self.height):
            if self.active is not None:
                pygame.draw.rect(dp, self.active, (x, y, self.width, self.height))
            if mclick[0] == 1:
                if action is not None:
                    if actionkey is not None:
                        action(actionkey)
                    else:
                        action()
                    pygame.time.wait(501)
        else:
            if self.active is not None:
                pygame.draw.rect(dp, self.incative, (x, y, self.width, self.height))
        if self.image is not None and self.imgpos is not None and len(self.imgpos) != 0:
            dp.blit(self.pic, (self.imgpos[0] + x, self.imgpos[1] + y))
        if text is not None and textpos is not None and textcolor is not None and textsize is not None:
            print_text(str(text), textcolor, textpos[0] + x, textpos[1] + y, dp, textsize, font=textfont)


keys = {
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    "0": pygame.K_0,
    "q": pygame.K_q,
    "w": pygame.K_w,
    "e": pygame.K_e,
    "r": pygame.K_r,
    "t": pygame.K_t,
    "y": pygame.K_y,
    "u": pygame.K_u,
    "i": pygame.K_i,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "[": pygame.K_LEFTBRACKET,
    "]": pygame.K_RIGHTBRACKET,
    "|": pygame.K_BACKSLASH,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    ";": pygame.K_SEMICOLON,
    "'": pygame.K_QUOTE,
    "z": pygame.K_z,
    "x": pygame.K_x,
    "c": pygame.K_c,
    "v": pygame.K_v,
    "b": pygame.K_b,
    "n": pygame.K_n,
    "m": pygame.K_m,
    ",": pygame.K_COMMA,
    ".": pygame.K_PERIOD,
    "/": pygame.K_SLASH,
    "left": pygame.K_LEFT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
}
