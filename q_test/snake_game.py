import curses    #用于控制台图形界面
import random
from collections import deque

class SnakeGame:
    def __init__(self, width=60, height=30):
        self.width = width
        self.height = height
        self.snake = deque([(width // 2, height // 2)])  #储存蛇的每个身体坐标--头在左边
        # 初始方向为向下，向上（0，-1），向右（1，0），向左（-1，0）
        # 这个是（dx, dy）而不是（x, y）
        # python控制台当中 Y 轴正向为下
        self.direction = (0, 1)
        self.food = self._generate_food()
        self.score = 0
        self.game_over = False

    def _generate_food(self):
        while True:
            # 在游戏未结束前，在游戏区域内随机选择一个不在蛇身体上的位置
            food = (random.randint(1, self.width - 2), random.randint(1, self.height - 2))
            if food not in self.snake:
                return food

    def _move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # 撞墙或撞自己则游戏结束
        # 新头部的横坐标--宽度， 新头部的纵坐标--高度， 新头--自己
        if (new_head[0] in (0, self.width - 1) or
            new_head[1] in (0, self.height - 1) or
            new_head in self.snake):
            self.game_over = True
            return

        # 如果吃到了食物（新头部位置和食物位置重合），得分+1，不移除尾巴（蛇变长）
        # 否则正常移动，头部加一个新位置，尾巴删掉
        self.snake.appendleft(new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def _render(self, stdscr):
        stdscr.clear()
        # 画边界
        for x in range(self.width):
            stdscr.addch(0, x, '#')
            stdscr.addch(self.height - 1, x, '#')
        for y in range(self.height):
            stdscr.addch(y, 0, '#')
            stdscr.addch(y, self.width - 1, '#')

        # 画蛇
        for x, y in self.snake:
            stdscr.addch(y, x, 'O')
        # 画食物
        stdscr.addch(self.food[1], self.food[0], '*')
        # 显示分数
        stdscr.addstr(self.height, 0, f"Score: {self.score}")
        stdscr.refresh()

    # 用户交互--输入方向控制蛇
    def _get_input(self, stdscr):
        key = stdscr.getch()
        # 防止反向立即掉头
        if key == curses.KEY_UP and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == curses.KEY_DOWN and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == curses.KEY_LEFT and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == curses.KEY_RIGHT and self.direction != (-1, 0):
            self.direction = (1, 0)

    def run(self, stdscr):
        curses.curs_set(0)  # 隐藏光标
        stdscr.nodelay(True)  # 设置是（False）否(Ture)阻塞等待输入
        stdscr.timeout(300)  # 控制刷新速度（ms）

        while not self.game_over:
            self._render(stdscr)
            self._get_input(stdscr)
            self._move()

        # curses常用的函数
        stdscr.nodelay(False)
        stdscr.addstr(self.height // 2, self.width // 2 - 5, "GAME OVER")  # 打印字符串
        stdscr.addstr(self.height // 2 + 1, self.width // 2 - 7, f"Score: {self.score}")
        stdscr.getch()  # 获取按键（非阻塞时可能返回 -1）

if __name__ == "__main__":
    curses.wrapper(SnakeGame().run)