import random

class GobangAI:
    def __init__(self, size=15):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.human = '●'
        self.ai = '○'
        self.turn = self.human
        self.moves = 0

    def draw_board(self):
        print("   " + ' '.join([chr(i + ord('a')) for i in range(self.size)]))
        for i, row in enumerate(self.board):
            print(f"{i+1:2} " + ' '.join(row))

    def input_move(self):
        while True:
            move = input(f"你的回合 ({self.human})，请输入坐标 (如 h8)：").strip().lower()
            if len(move) < 2 or not move[0].isalpha() or not move[1:].isdigit():
                print("输入格式错误！")
                continue
            x = ord(move[0]) - ord('a')
            y = int(move[1:]) - 1
            if 0 <= x < self.size and 0 <= y < self.size and self.board[y][x] == '.':
                return x, y
            else:
                print("坐标非法或已被占用！")

    def place_move(self, x, y, player):
        self.board[y][x] = player
        self.moves += 1

    def check_win(self, x, y, player):
        return self.count_max_continuous(x, y, player) >= 5

    def count_max_continuous(self, x, y, player):
        """
        检查当前位置最大连续棋子数（四个方向）
        """
        max_count = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            cnt = 1
            for d in [1, -1]:
                nx, ny = x + d * dx, y + d * dy
                while 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == player:
                    cnt += 1
                    nx += d * dx
                    ny += d * dy
            max_count = max(max_count, cnt)
        return max_count

    def find_critical_move(self, target_player, count_required=5):
        """
        尝试找到使某一方连 count_required 个的落子
        """
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] != '.':
                    continue
                self.board[y][x] = target_player
                if self.count_max_continuous(x, y, target_player) >= count_required:
                    self.board[y][x] = '.'
                    return x, y
                self.board[y][x] = '.'
        return None

    def ai_move(self):
        # 1. AI 自己能赢
        win_move = self.find_critical_move(self.ai, 5)
        if win_move:
            print(f"电脑落子（获胜）在：{chr(win_move[0] + ord('a'))}{win_move[1] + 1}")
            return win_move

        # 2. 阻止玩家连五
        block_win = self.find_critical_move(self.human, 5)
        if block_win:
            print(f"电脑落子（阻止你连五）在：{chr(block_win[0] + ord('a'))}{block_win[1] + 1}")
            return block_win

        # 3. 阻止玩家连四（更早干预）
        block_four = self.find_critical_move(self.human, 4)
        if block_four:
            print(f"电脑落子（阻止你连四）在：{chr(block_four[0] + ord('a'))}{block_four[1] + 1}")
            return block_four

        # 4. 随机落子
        empty = [(x, y) for y in range(self.size) for x in range(self.size) if self.board[y][x] == '.']
        move = random.choice(empty)
        print(f"电脑随机落子在：{chr(move[0] + ord('a'))}{move[1] + 1}")
        return move

    def play(self):
        while True:
            self.draw_board()
            if self.turn == self.human:
                x, y = self.input_move()
            else:
                x, y = self.ai_move()

            self.place_move(x, y, self.turn)

            if self.check_win(x, y, self.turn):
                self.draw_board()
                print("🎉 你赢啦！" if self.turn == self.human else "😈 电脑获胜！")
                break

            if self.moves == self.size * self.size:
                print("棋盘已满，平局！")
                break

            self.turn = self.ai if self.turn == self.human else self.human

if __name__ == "__main__":
    game = GobangAI()
    game.play()
