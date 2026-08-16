# C
import pygame

C_GREY = (69,69,69)
C_ORANGE = (255,156,0)
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_INDIGO = (63,72,204)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Lvl1Bg0' : 0,
    'Lvl1Bg1' : 1,
    'Lvl1Bg2' : 2,
    'Lvl1Bg3' : 3,
    'Lvl1Bg4' : 4,
    'Lvl1Bg5' : 5,
    'Player1' : 4,
    'Player2' : 4,
    'Enemy1' : 2,
    'Enemy2' : 3,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_SPACE}

# S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324