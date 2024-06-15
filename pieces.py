import numpy as np

RED = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
])

RED_LIST = [RED]

ORANGE = np.array([
    [2, 0],
    [2, 0],
    [2, 0],
    [2, 2],
])

ORANGE_LIST = [ORANGE, np.rot90(ORANGE), np.rot90(ORANGE, 2), np.rot90(ORANGE, 3),
               np.fliplr(ORANGE), np.fliplr(np.rot90(ORANGE)), np.fliplr(np.rot90(ORANGE, 2)),
               np.fliplr(np.rot90(ORANGE, 3))]

YELLOW = np.array([
    [3, 3, 3],
    [3, 0, 3]
])

YELLOW_LIST = [YELLOW, np.rot90(YELLOW), np.rot90(YELLOW, 2), np.rot90(YELLOW, 3)]

GREEN = np.array([
    [4, 0, 0],
    [4, 4, 0],
    [0, 4, 4]
])

GREEN_LIST = [GREEN, np.rot90(GREEN), np.rot90(GREEN, 2), np.rot90(GREEN, 3),
              np.fliplr(GREEN), np.fliplr(np.rot90(GREEN)), np.fliplr(np.rot90(GREEN, 2)),
              np.fliplr(np.rot90(GREEN, 3))]

DARK_GREEN = np.array([
    [5, 5, 5],
    [0, 5, 0],
    [0, 5, 0]
])

DARK_GREEN_LIST = [DARK_GREEN, np.rot90(DARK_GREEN), np.rot90(DARK_GREEN, 2), np.rot90(DARK_GREEN, 3)]

CYAN = np.array([
    [6, 6, 0],
    [0, 6, 0],
    [0, 6, 6]
])

CYAN_LIST = [CYAN, np.rot90(CYAN), np.fliplr(CYAN), np.fliplr(np.rot90(CYAN))]

BLUE = np.array([
    [7, 0, 0],
    [7, 0, 0],
    [7, 7, 7]
])

BLUE_LIST = [BLUE, np.rot90(BLUE), np.rot90(BLUE, 2), np.rot90(BLUE, 3)]

DARK_BLUE = np.array([
    [8, 8, 8, 8, 8]
])

DARK_BLUE_LIST = [DARK_BLUE, np.rot90(DARK_BLUE)]

PURPLE = np.array([
    [9, 9, 9, 0],
    [0, 0, 9, 9]
])

PURPLE_LIST = [PURPLE, np.rot90(PURPLE), np.rot90(PURPLE, 2), np.rot90(PURPLE, 3),
               np.fliplr(PURPLE), np.fliplr(np.rot90(PURPLE)), np.fliplr(np.rot90(PURPLE, 2)),
               np.fliplr(np.rot90(PURPLE, 3))]

PINK = np.array([
    [10, 10, 10],
    [0, 10, 10]
])

PINK_LIST = [PINK, np.rot90(PINK), np.rot90(PINK, 2), np.rot90(PINK, 3),
             np.fliplr(PINK), np.fliplr(np.rot90(PINK)), np.fliplr(np.rot90(PINK, 2)),
             np.fliplr(np.rot90(PINK, 3))]

BROWN = np.array([
    [11, 11, 11, 11],
    [0, 11, 0, 0]
])

BROWN_LIST = [BROWN, np.rot90(BROWN), np.rot90(BROWN, 2), np.rot90(BROWN, 3),
              np.fliplr(BROWN), np.fliplr(np.rot90(BROWN)), np.fliplr(np.rot90(BROWN, 2)),
              np.fliplr(np.rot90(BROWN, 3))]

GREY = np.array([
    [12, 12, 0],
    [0, 12, 12],
    [0, 12, 0]
])

GREY_LIST = [GREY, np.rot90(GREY), np.rot90(GREY, 2), np.rot90(GREY, 3),
             np.fliplr(GREY), np.fliplr(np.rot90(GREY)), np.fliplr(np.rot90(GREY, 2)),
             np.fliplr(np.rot90(GREY, 3))]

ALL_POSITIONS = {'red': RED_LIST, 'orange': ORANGE_LIST, 'yellow': YELLOW_LIST, 'green': GREEN_LIST,
                 'dark_green': DARK_GREEN_LIST, 'cyan': CYAN_LIST, 'blue': BLUE_LIST, 'dark_blue': DARK_BLUE_LIST,
                 'purple': PURPLE_LIST, 'pink': PINK_LIST, 'brown': BROWN_LIST, 'grey': GREY_LIST}
