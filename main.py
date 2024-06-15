import solver
import numpy as np
from flask import Flask, request, render_template
app = Flask(__name__)

PIECES = ['red', 'orange', 'yellow', 'green', 'dark_green', 'cyan',
          'blue', 'dark_blue', 'purple', 'pink', 'brown', 'grey']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        red = request.form.get('red')
        orange = request.form.get('orange')
        yellow = request.form.get('yellow')
        green = request.form.get('green')
        dark_green = request.form.get('dark_green')
        cyan = request.form.get('cyan')
        blue = request.form.get('blue')
        dark_blue = request.form.get('dark_blue')
        purple = request.form.get('purple')
        pink = request.form.get('pink')
        brown = request.form.get('brown')
        grey = request.form.get('grey')

        results = [red, orange, yellow, green, dark_green, cyan, blue, dark_blue, purple, pink, brown, grey]

        for i in range(len(results)):
            if results[i] is None:
                results[i] = 0
            else:
                results[i] = 1

        remaining = dict(zip(PIECES, results))
        num_pieces = 0
        for i in remaining.values():
            num_pieces += i
        board = np.zeros((5, num_pieces))
        if solver.solve(board, remaining):
            path = solver.pretty_print(board)
        else:
            path = 'static/images/no_sol.png'
            print('No solution found')
        return render_template('index.html', img_board=path)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    '''
    pieces = ['red', 'orange', 'yellow', 'green', 'dark_green', 'cyan',
              'blue', 'dark_blue', 'purple', 'pink', 'brown', 'grey']
    remaining = {piece: 0 for piece in pieces}
    remaining.update({'red': 0, 'orange': 1, 'yellow': 1, 'green': 1, 'dark_green': 1, 'cyan': 1,
                      'blue': 0, 'dark_blue': 0, 'purple': 1, 'pink': 1, 'brown': 1, 'grey': 1})
    num_pieces = 0
    for i in remaining.values():
        num_pieces += i
    board = np.zeros((5, num_pieces))
    if solver.solve(board, remaining):
        print(board)
    else:
        print('No solution found')
    '''