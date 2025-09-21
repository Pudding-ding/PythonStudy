import os
import random

class Go:
    def __init__(self, size=15):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.human = '●'
        self.ai = 'X'
        self.last_ai_move = None  # 记录电脑最后一次的落子坐标

    # 清理终端屏幕---清空pycharm的运行台没成功，搜索结果可以强制清屏，但逻辑不顺就没继续了
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # 输出当前棋盘状态
    def draw_board(self):
        self.clear_screen()  #先清屏
        print("   " + " ".join([chr(ord('a') + i) for i in range(self.size)]))  #顶部用字母表示列标
        for i, row in enumerate(self.board):   #左侧部用数字表示行标
            print(f"{i+1:2d} " + " ".join(row))
        if self.last_ai_move:
            col, row = self.last_ai_move
            print(f"\n电脑刚刚在 {chr(col + ord('a'))}{row + 1} 落子")

    # 判断是否为有效输入
    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.board[y][x] == '.'
    def get_input(self):
        while True:
            move = input("请落子(如 h8): ").strip().lower()
            if len(move) < 2 or not move[0].isalpha() or not move[1:].isdigit():
                print("输入格式错误，请重新输入，例如 h8")
                continue
            # 将输入字符转化为合法坐标
            x = ord(move[0]) - ord('a')
            y = int(move[1:]) - 1
            if self.is_valid_move(x, y):
                return x, y
            else:
                print("该位置不合法或已被占用，请重新输入新位置")

    # 在棋盘上指定位置放置相对玩家的棋子
    def place_move(self, x, y, symbol):
        self.board[y][x] = symbol

    # 检查是否出现五子连珠--修改了函数嵌套部分
    def check_win(self, x, y, symbol):
        # 一共四个方向，对每个方向进行正负两侧的排查，记录相同棋子的数量
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for d in [1, -1]:
                i = 1
                while True:
                    nx, ny = x + dx * i * d, y + dy * i * d
                    if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == symbol:
                        count += 1
                        i += 1
                    else:
                        break
            if count >= 5:  #连成五个了
                return True
        return False

    # 找寻电脑落子位置
    def find_pattern(self, symbol, length):
        # 遍历每一个棋盘的格子，判断是否能落子
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] != '.':
                    continue
                # 对能落子的每个格子尝试往四个方向去走
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    count = 1
                    for d in [1, -1]:
                        i = 1
                        while True:
                            nx = x + dx * i * d
                            ny = y + dy * i * d
                            # 判断是否为连续的某方棋子
                            if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == symbol:
                                count += 1
                                i += 1
                            else:
                                break
                    # 判断是否为目标连子数量--合适的落子点
                    if count >= length:
                        return (x, y)
        return None

    # 定义电脑落子的七个优先级
    def ai_move(self):
        # 1.电脑连五--电脑胜利
        win = self.find_pattern(self.ai, 5)
        if win:
            return win
        # 2.阻止玩家连五--阻止玩家胜利
        block_win = self.find_pattern(self.human, 5)
        if block_win:
            return block_win
        # 3.电脑成四
        four = self.find_pattern(self.ai, 4)
        if four:
            return four
        # 4.阻止玩家成四
        block_four = self.find_pattern(self.human, 4)
        if block_four:
            return block_four
        # 5.自己成三
        three = self.find_pattern(self.ai, 3)
        if three:
            return three
        # 6.自己成二
        two = self.find_pattern(self.ai, 2)
        if two:
            return two
        # 7.随机落子
        empty_cells = [(x, y) for y in range(self.size) for x in range(self.size) if self.board[y][x] == '.']
        return random.choice(empty_cells) if empty_cells else None

    # 游戏过程
    def play(self):
        self.draw_board()
        while True:
            x, y = self.get_input()
            self.place_move(x, y, self.human)
            self.draw_board()
            if self.check_win(x, y, self.human):
                print("你赢啦！")
                break
            ai_x, ai_y = self.ai_move()
            self.place_move(ai_x, ai_y, self.ai)
            self.last_ai_move = (ai_x, ai_y)
            self.draw_board()
            if self.check_win(ai_x, ai_y, self.ai):
                print("电脑获胜！")
                break

if __name__ == "__main__":
    game = Go()
    game.play()
