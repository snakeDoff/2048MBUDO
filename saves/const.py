import pygame

RESOLUTIONS ={
            "1:1": ['600x600', '700x700', '800x800', '900x900', '1000x1000', '1200x1200', '1600x1600'],
            "4:3": ['800x600', '1024x768', '1400x1050'],
            "16:9": ['1280x720', '1600x900', '1920x1080', '2560x1440', '3840x2160'],
            "16:10": ['1440x900', '1680x1050', '2560x1600', '3840x2400']
        }

BINDEDBUTTONS = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d
        }

COLORS = {
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


KEYS = {
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