""""
拧魔方大挑战！
1.构建魔方模型，随机出一个魔方，三维向量代表每一个色块的位置和颜色
2.U,D,F,B,L,R六种魔方顺时针转动函数的编写--小写代表逆时针转动
3.魔方打乱与还原步骤展示
"""""
import random
# 初始化魔方
def initialize_cube():
    """
    一共6个面，每个面都是3*3个色块，色块颜色用0-5表示，这样就是一个数组
    :return:
    """
    return [[[face for _ in range(3)] for _ in range(3)] for face in range(6)]

# 用数字输出打印魔方当前状态
def print_cube(cube):
    face_names = ['U', 'D', 'F', 'B', 'L', 'R']
    for i, face in enumerate(cube):
        print(f"面 {face_names[i]} ({i}):")
        for row in face:
            print("  ", row)
        print()

# 将3x3面顺时针旋转90°--leetcode48题
def rotate_face_clockwise(face):
    return [list(row) for row in zip(*face[::-1])]

# 顺时针旋转函数定义,分别为六个面分别顺时针旋转90°--旋转一个面实际上是其四个相邻面（3*3矩阵）的首行（row(0)）要依次循环交换
# U面--0
def rotate_U(cube):
    """
    顺时针旋转U面（面0）90°，并更新相邻面的顶行
    相邻顺序：L->F->R->B->L
    """
    # 旋转U面本身（0）
    cube[0] = rotate_face_clockwise(cube[0])
    # 暂存原始的四条边顶行数据
    temp = [cube[4][0][:],  # L顶行
            cube[2][0][:],  # F顶行
            cube[5][0][:],  # R顶行
            cube[3][0][:]]  # B顶行（需反转）
    # 更新四条边（注意B要反转顺序）
    cube[2][0] = temp[0]          # L->F
    cube[5][0] = temp[1]          # F->R
    cube[3][0] = temp[2][::-1]    # R->B（反转）
    cube[4][0] = temp[3][::-1]    # B->L（反转）
# D面--1
def rotate_D(cube):
    cube[1] = rotate_face_clockwise(cube[1])

    temp = [cube[2][2][:],
            cube[5][2][:],
            cube[3][2][:],
            cube[4][2][:]]
    cube[5][2] = temp[0]
    cube[3][2] = temp[1]
    cube[4][2] = temp[2]
    cube[2][2] = temp[3]
# F面--2
def rotate_F(cube):
    cube[2] = rotate_face_clockwise(cube[2])

    temp = [cube[0][2][:],                        # U底行
            [cube[4][2-i][2] for i in range(3)],  # L右列（从上至下）
            cube[1][0][:],                        # D顶行
            [cube[5][i][0] for i in range(3)]]    # R左列（从上至下）
    cube[0][2] = temp[1]
    for i in range(3):
        cube[4][i][2] = temp[2][2 - i]
        cube[1][0][i] = temp[3][i]
        cube[5][i][0] = temp[0][i]
# B面--3
def rotate_B(cube):
    cube[3] = rotate_face_clockwise(cube[3])

    temp = [cube[0][0][:],                          # U顶行
            [cube[5][i][2] for i in range(3)],      # R右列（从下至上）
            cube[1][2][:],                          # D底行
            [cube[4][2 - i][0] for i in range(3)]]  # L左列（从下至上）
    cube[0][0] = temp[3]
    for i in range(3):
        cube[5][i][2] = temp[0][i]
        cube[1][2][i] = temp[1][i]
        cube[4][i][0] = temp[2][2 - i]
# L面--4
def rotate_L(cube):
    cube[4] = rotate_face_clockwise(cube[4])

    temp = [[cube[0][i][0] for i in range(3)],
            [cube[3][2 - i][2] for i in range(3)],
            [cube[1][i][0] for i in range(3)],
            [cube[2][i][0] for i in range(3)]]
    for i in range(3):
        cube[0][i][0] = temp[3][i]
        cube[3][2 - i][2] = temp[0][i]
        cube[1][i][0] = temp[1][i]
        cube[2][i][0] = temp[2][i]
# R面--5
def rotate_R(cube):
    cube[5] = rotate_face_clockwise(cube[5])

    temp = [[cube[0][i][2] for i in range(3)],
            [cube[2][i][2] for i in range(3)],
            [cube[1][i][2] for i in range(3)],
            [cube[3][2 - i][0] for i in range(3)]]
    for i in range(3):
        cube[0][i][2] = temp[3][i]
        cube[2][i][2] = temp[0][i]
        cube[1][i][2] = temp[1][i]
        cube[3][2 - i][0] = temp[2][i]

# 逆操作--逆时针旋转，最简单且不易出错的就是执行顺时针旋转三次
def rotate_u(cube):
    for _ in range(3):
        rotate_U(cube)

def rotate_d(cube):
    for _ in range(3):
        rotate_D(cube)

def rotate_f(cube):
    for _ in range(3):
        rotate_F(cube)

def rotate_b(cube):
    for _ in range(3):
        rotate_B(cube)

def rotate_l(cube):
    for _ in range(3):
        rotate_L(cube)

def rotate_r(cube):
    for _ in range(3):
        rotate_R(cube)

# 利用字典将字母（命令字符）映射到相应的函数--根据命令字符串依次旋转魔方
def execute_commands(cube, command_str):
    commands = command_str.strip().split()
    command_map = {
        'U': rotate_U,
        'D': rotate_D,
        'F': rotate_F,
        'B': rotate_B,
        'L': rotate_L,
        'R': rotate_R,
        'u': rotate_u,
        'd': rotate_d,
        'f': rotate_f,
        'b': rotate_b,
        'l': rotate_l,
        'r': rotate_r
    }
    for cmd in commands:
        if cmd in command_map:
            command_map[cmd](cube)
            if history is not None:
                history.append(cmd)
        else:
            print(f"无效命令: {cmd}")

# 随机打乱魔方--自主决定拧多少次
def scramble_cube(cube, num_moves=20, history=None):
    moves = ['U', 'D', 'F', 'B', 'L', 'R']
    directions = ['', 'i']  # '' 表示顺时针，'i' 表示逆时针（小写）
    # 构建命令：顺时针为大写，逆时针为对应小写
    all_moves = moves + [m.lower() for m in moves]
    commands = []
    for _ in range(num_moves):
        cmd = random.choice(all_moves)
        commands.append(cmd)
    # 执行打乱
    execute_commands(cube, ' '.join(commands))
    print(f"\n已经随机打乱 {num_moves} 步！")
    print(f"执行命令：{' '.join(commands)}\n")

# 逆操作还原魔方
def reverse_commands(cube, history):
    inverse = {
        'U': 'u',
        'D': 'd',
        'F': 'f',
        'B': 'b',
        'L': 'l',
        'R': 'r',
        'u': 'U',
        'd': 'D',
        'f': 'F',
        'b': 'B',
        'l': 'L',
        'r': 'R'
    }
    reversed_cmds = [inverse[cmd] for cmd in reversed(history)]
    print(f"\n复原中!：{' '.join(reversed_cmds)}")
    execute_commands(cube, ' '.join(reversed_cmds))

# 检查是否复原成功--每一面3*3颜色是否一致
def is_solved(cube):
    for face in cube:
        color = face[0][0]
        for row in face:
            for val in row:
                if val != color:
                    return False
    return True

if __name__ == "__main__":
    # 初始化魔方
    cube = initialize_cube()
    print("初始魔方：")
    print_cube(cube)
    history = []      # 记录历史旋转

    # 随机打乱魔方
    try:
        num = int(input("请输入要打乱的步数："))
    except ValueError:
        num = 20
        print("无效，使用默认20步")
    scramble_cube(cube, num, history)
    print("打乱后的魔方：")
    print_cube(cube)

    # 还原魔方
    reverse_commands(cube, history)
    print("还原后魔方：")
    print_cube(cube)

    # 检查是否复原
    if is_solved(cube):
        print("复原啦！")
    else:
        print("再试试吧！")

