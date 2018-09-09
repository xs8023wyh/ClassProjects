import sys


class compete:
    def __init__(self, size=3):
        self.pos_size = size ** 2
        self.arr = ['' for _ in range(size ** 2)]
        self.HUMAN_TURN = None
        self.HUMAN_MARK, self.AI_MARK = None, None
        self.HUMAN_WIN = False
        self.AI_WIN = False

    def plot_block(self):
        for i, str in enumerate(self.arr):
            if (i + 1) % 3 != 0:
                sys.stderr.write(self.arr[i])
                sys.stderr.write(' | ')
            else:
                sys.stderr.write(self.arr[i])
                sys.stderr.write('\n')
                sys.stderr.write('______')
                sys.stderr.write('\n')

    def check_first(self):
        sys.stderr.write('Would u like first(1) or second(2):')
        if int(input()) == 1:
            self.HUMAN_TURN = True
            self.HUMAN_MARK, self.AI_MARK = 'X', 'O'
        else:
            self.HUMAN_TURN = False
            self.HUMAN_MARK, self.AI_MARK = 'O', 'X'

    def is_not_win(self):
        win_cases = [[0, 1, 2], [0, 3, 6], [0, 4, 8],
                     [3, 4, 5], [1, 4, 7], [2, 4, 6],
                     [6, 7, 8], [2, 5, 8]]

        for win_case in win_cases:
            win_pool = set()
            for index in win_case:
                win_pool.add(self.arr[index])
            if len(win_pool) == 1 and '' not in win_pool:
                if self.HUMAN_MARK in win_pool:
                    self.HUMAN_WIN = True
                    return False
                else:
                    self.AI_WIN = True
                    return False

        return True

    def mark(self):
        if self.HUMAN_TURN:
            sys.stderr.write('please input position:')
            pos = input()

            if int(pos) > self.pos_size or int(pos) < 0:
                sys.stderr.write('too large number for input!\n')
            elif self.arr[int(pos) - 1] != '':
                sys.stderr.write('this place has been marked!\n')
            else:
                self.arr[int(pos) - 1] = self.HUMAN_MARK
                self.HUMAN_TURN = False
                self.plot_block()

        else:
            sys.stderr.write('----AI turn--------')
            sys.stderr.write('\n')
            for i, _ in enumerate(self.arr):
                if self.arr[i] == '':
                    self.arr[i] = self.AI_MARK
                    self.HUMAN_TURN = True
                    self.plot_block()
                    break
            self.HUMAN_TURN = True

    def play(self):
        while self.is_not_win():
            self.mark()
        if self.HUMAN_WIN:
            sys.stderr.write('human win')
        else:
            sys.stderr.write('AI win')


if __name__ == '__main__':
    test = compete()
    test.check_first()
    test.play()
