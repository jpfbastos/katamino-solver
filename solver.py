import numpy as np
from PIL import Image, ImageDraw
import pieces


def get_free(array):
    coordinates = []
    for row in range(array.shape[0]):
        for col in range(array.shape[1]):
            if array[row][col] == 0:
                coordinates.append((row, col))
    return coordinates


def get_occupied(array):
    coordinates = []
    for row in range(array.shape[0]):
        for col in range(array.shape[1]):
            if array[row][col] != 0:
                coordinates.append((row, col))
    return coordinates


def is_empty_contiguous(board):
    free_coords = get_free(board)

    if not free_coords:
        return True

    visited = []
    stack = [free_coords[0]]

    while stack:
        current = stack.pop()
        x = current[0]
        y = current[1]
        if current not in visited:
            visited.append(current)
            potential_neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            neighbours = [x for x in potential_neighbours if x in free_coords]
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)

    return len(visited) == len(free_coords)


def is_valid(board, piece, top_left):
    row = get_occupied(piece)[0][0]
    col = get_occupied(piece)[0][1]
    occupied_coords = np.array(get_occupied(board))
    if occupied_coords.size == 0:
        occupied_coords = occupied_coords.reshape(0, 2)
    piece_coords = np.array(get_occupied(piece)) - np.array([row, col]) + np.array(top_left)

    for coord in piece_coords:
        if np.any(np.all(occupied_coords == coord, axis=1)) or coord[0] >= board.shape[0] or coord[0] < 0 \
                or coord[1] >= board.shape[1] or coord[1] < 0:
            return False
    provisional_board = np.array(board)
    provisional_board[-row + top_left[0]:-row + top_left[0] + piece.shape[0],
                      -col + top_left[1]:-col + top_left[1] + piece.shape[1]] += piece
    return is_empty_contiguous(provisional_board)


def solve(board, remaining):
    all_positions = {key: pieces.ALL_POSITIONS[key] for key, value in remaining.items() if value == 1}
    free = get_free(board)
    while len(free) > 0:
        for colour, positions in all_positions.items():
            for position in positions:
                top_left = free[0]
                if is_valid(board, position, free[0]):
                    row = get_occupied(position)[0][0]
                    col = get_occupied(position)[0][1]
                    board[-row + top_left[0]:-row + top_left[0] + position.shape[0],
                          -col + top_left[1]:-col + top_left[1] + position.shape[1]] += position
                    remaining.update({colour: 0})
                    if solve(board, remaining):
                        return True
                    board[-row + top_left[0]:-row + top_left[0] + position.shape[0],
                          -col + top_left[1]:-col + top_left[1] + position.shape[1]] -= position
                    remaining.update({colour: 1})
        return False
    return True


def make_square(top_left):
    top_corner_x = 102
    top_corner_y = 99
    return [(top_corner_x + top_left[0], top_corner_y + top_left[1]),
            (top_corner_x + 100 + top_left[0], top_corner_y + top_left[1]),
            (top_corner_x + 100 + top_left[0], top_corner_y + 100 + top_left[1]),
            (top_corner_x + top_left[0], top_corner_y + 100 + top_left[1])]

def pretty_print(board):
    PATH = 'static/images/board_solved.png'

    colours = {1: (219, 58, 38), 2: (209, 147, 77), 3: (251, 239, 109), 4: (159, 200, 77), 5: (83, 171, 98),
               6: (84, 189, 211), 7: (67, 155, 193), 8: (27, 55, 119), 9: (70, 51, 158), 10: (193, 110, 152),
               11: (99, 63, 52), 12: (94, 92, 89)}

    img_board = Image.open('static/images/board.png').convert('RGBA')
    separator = Image.open('static/images/separator.png').convert('RGBA')
    rows = board.shape[0]
    cols = board.shape[1]
    img_board.paste(separator, (410 + 100*(max(3, cols)-3), 53), separator)
    img_board1 = ImageDraw.Draw(img_board)
    for i in range(rows):
        for j in range(cols):
            img_board1.polygon(make_square((100*j, 100*i)), fill=colours.get(board[i][j]))

    img_board.save(PATH)

    return PATH


