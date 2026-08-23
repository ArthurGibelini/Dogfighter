# C
import pygame

C_GREY = (69,69,69)
C_ORANGE = (255,156,0)
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_INDIGO = (63,72,204)
C_GREEN = (0,128,0)
C_CYAN = (0,128,128)
C_GOLD = (255,201,14)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Lvl1Bg0' : 0,
    'Lvl1Bg1' : 1,
    'Lvl1Bg2' : 2,
    'Lvl1Bg3' : 3,
    'Lvl1Bg4' : 4,
    'Lvl1Bg5' : 5,
    'Lvl2Bg0': 0,
    'Lvl2Bg1': 1,
    'Lvl2Bg2': 2,
    'Player1' : 3,
    'Player1Shot' : 4,
    'Player2' : 3,
    'Player2Shot': 4,
    'Enemy1' : 3,
    'Enemy1Shot': 4,
    'Enemy2' : 2,
    'Enemy2Shot': 3,
}

ENTITY_HEALTH = {
    'Lvl1Bg0' : 9999,
    'Lvl1Bg1' : 9999,
    'Lvl1Bg2' : 9999,
    'Lvl1Bg3' : 9999,
    'Lvl1Bg4' : 9999,
    'Lvl1Bg5' : 9999,
    'Lvl2Bg0': 9999,
    'Lvl2Bg1': 9999,
    'Lvl2Bg2': 9999,
    'Player1' : 100,
    'Player1Shot': 1,
    'Player2' : 100,
    'Player2Shot': 1,
    'Enemy1' : 25,
    'Enemy1Shot': 1,
    'Enemy2' : 50,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 80,
    'Enemy2': 70,
}

ENTITY_DAMAGE = {
    'Lvl1Bg0' : 0,
    'Lvl1Bg1' : 0,
    'Lvl1Bg2': 0,
    'Lvl1Bg3': 0,
    'Lvl1Bg4': 0,
    'Lvl1Bg5': 0,
    'Lvl2Bg0': 0,
    'Lvl2Bg1': 0,
    'Lvl2Bg2': 0,
    'Player1' : 10,
    'Player1Shot' : 25,
    'Player2' : 10,
    'Player2Shot': 25,
    'Enemy1': 10,
    'Enemy1Shot': 15,
    'Enemy2': 10,
    'Enemy2Shot': 25,
}

ENTITY_SCORE = {
    'Lvl1Bg0' : 0,
    'Lvl1Bg1' : 0,
    'Lvl1Bg2': 0,
    'Lvl1Bg3': 0,
    'Lvl1Bg4': 0,
    'Lvl1Bg5': 0,
    'Lvl2Bg0': 0,
    'Lvl2Bg1': 0,
    'Lvl2Bg2': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 125,
    'Enemy1Shot': 0,
    'Enemy2': 90,
    'Enemy2Shot': 0,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - VERSUS',
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
SPAWN_TIME = 750

# T

TIMEOUT_STEP = 100 # 100ms
TIMEOUT_LEVEL = 20000 # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = { 'Title': (WIN_WIDTH / 2, 50),
              'EnterName': (WIN_WIDTH / 2, 80),
              'Label': (WIN_WIDTH / 2, 90),
              'Name': (WIN_WIDTH / 2, 110),
              0: (WIN_WIDTH / 2, 110),
              1: (WIN_WIDTH / 2, 130),
              2: (WIN_WIDTH / 2, 150),
              3: (WIN_WIDTH / 2, 170),
              4: (WIN_WIDTH / 2, 190),
              5: (WIN_WIDTH / 2, 210),
              6: (WIN_WIDTH / 2, 230),
              7: (WIN_WIDTH / 2, 250),
              8: (WIN_WIDTH / 2, 270),
              9: (WIN_WIDTH / 2, 290),
              }