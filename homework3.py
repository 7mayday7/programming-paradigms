class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # одномерный массив для доски 3x3
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if 1 <= position <= 9 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            print("\nНедопустимый ход. Попробуйте снова.\n")
            return False

    def check_winner(self):
        # Проверка строк, столбцов и диагоналей
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def check_board_full(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.print_board()

            try:
                position = int(input(f"Ход игрока {self.current_player}. Введите номер клетки (1-9): "))
            except ValueError:
                print("\nНекорректный ввод. Попробуйте снова.\n")
                continue

            if self.make_move(position):
                if self.check_winner():
                    self.print_board()
                    print(f"\nИгрок {self.current_player} победил!")
                    break
                elif self.check_board_full():
                    self.print_board()
                    print("\nНичья!")
                    break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
