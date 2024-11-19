# 初始化一副纸牌，花色和点数
# 三个人打炸金花，规则是:
#     豹子：三张一样的点数，牌面最大的是三张A，最小的是三张2
#     顺子：三张同样花色且数字连着，QKA也是三张连着的（牌面最大），但是 KA2不是
#     同花：三张同样花色
#     同花顺：三张同样花色，数字相连（同一花色的顺子）
#     对子：一个对+一个单牌，对子中“对2”最小，“对A”最大
#     其他 不符合上述的，叫高牌（High Cards）
#     牌型大小顺序为：豹子>同花顺>同花>顺子>对子>高牌
# 1. 随机给三个玩家发牌
# 2. 比出这三手牌大小

import random

# 定义一副不包含大小王的纸牌
suits = ['黑桃', '红心', '梅花', '方块']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# deck = [{'花色': suit, '点数': rank} for suit in suits for rank in ranks]

# 定义牌型大小顺序
rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}


# 定义牌型
def get_hand_rank(hand):
    values = [rank_order[card[1]] for card in hand]
    values.sort(reverse=True)
    value = values[0]  # 主值
    count = {v: values.count(v) for v in values}

    # 豹子
    if count[value] == 3:
        return (6, value)
    # 同花顺
    elif len(set([card[0] for card in hand])) == 1 and max(count.values()) == 2 and all(
            abs(rank_order[hand[i][1]] - rank_order[hand[i + 1][1]] == 1) for i in range(2)):
        return (5, value)
    # 同花
    elif len(set([card[0] for card in hand])) == 1:
        return (4, value)
    # 顺子
    elif max(count.values()) == 2 and all(
            abs(rank_order[hand[i][1]] - rank_order[hand[i + 1][1]] == 1) for i in range(2)):
        return (3, value)
    # 对子
    elif 2 in count.values():
        return (2, value)
    # 高牌
    else:
        return (1, value)


# 初始化牌堆
deck = [f'{suit}{rank}' for suit in suits for rank in ranks]
random.shuffle(deck)

# 发牌
player1 = [deck.pop(), deck.pop(), deck.pop()]
player2 = [deck.pop(), deck.pop(), deck.pop()]
player3 = [deck.pop(), deck.pop(), deck.pop()]

# 获取牌型和大小
hand_ranks = [(get_hand_rank(player), player) for player in [player1, player2, player3]]

# 比较牌型大小
winner = max(hand_ranks, key=lambda x: x[0])

# 输出结果
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
print(f"Player 3: {player3}")
print(f"Winner is Player {hand_ranks.index(winner) + 1} with {winner[1]}")
























# # 洗牌
# deck = random.sample(deck, len(deck))
#
# #发牌
# def deal_cards():
#     players = [[] for _ in range(3)]  # 初始化玩家手牌列表
#     # 每个玩家轮流起三张牌
#     for i in range(3):  # 每轮每个玩家起一张牌
#         for j in range(3):  # 三个玩家轮流
#             players[j].append(deck[i * 3 + j])    #(deck.pop(0))
#     for i, hand in enumerate(players):
#         print(f'玩家{i + 1}的牌：{hand}')
#     return players
# deal_cards()


# # # 定义炸金花的牌型规则
# def classify_hand(hand):
#     # 将牌按点数排序
#     sorted_hand = sorted(hand, key=lambda x: ranks.index(x['点数']))    # sorted函数，对列表进行排序后返回一个新的列表，包含排序后的元素。
#     # 豹子
#     if sorted_hand[0]['点数'] == sorted_hand[1]['点数'] == sorted_hand[2]['点数']:
#         return '豹子', ranks.index(sorted_hand[0]['点数'])
#     # 同花顺
#     if sorted_hand[0]['花色'] == sorted_hand[1]['花色'] == sorted_hand[2]['花色']:
#         if ranks.index(sorted_hand[0]['点数']) + 2 == ranks.index(sorted_hand[1]['点数']) + 1 == ranks.index(sorted_hand[2]['点数']):
#             return '同花顺', ranks.index(sorted_hand[2]['点数'])
#     # 同花
#     if sorted_hand[0]['花色'] == sorted_hand[1]['花色'] == sorted_hand[2]['花色']:
#         return '同花', ranks.index(sorted_hand[2]['点数'])
#     # 顺子
#     if ranks.index(sorted_hand[0]['点数']) + 2 == ranks.index(sorted_hand[1]['点数']) + 1 ==  ranks.index(sorted_hand[2]['点数']):
#         return '顺子', ranks.index(sorted_hand[2]['点数'])
#     # 对子
#     if sorted_hand[0]['点数'] == sorted_hand[1]['点数'] or sorted_hand[1]['点数'] == sorted_hand[2]['点数']:
#         return '对子', ranks.index(sorted_hand[1]['点数'])
#     # 其他情况为高牌
#     return '高牌', ranks.index(sorted_hand[2]['点数'])
#
# # 定义牌型大小顺序
# hand_rank = {'豹子': 6, '同花顺': 5, '同花': 4, '顺子': 3, '对子': 2, '高牌': 1}
#
# # 发三张牌给三个玩家
# # def deal_cards():
# #     random.shuffle(deck)
# #     player1 = deck[:3]
# #     player2 = deck[3:6]
# #     player3 = deck[6:9]
# #     return player1, player2, player3
# def deal_cards():
#     random.shuffle(deck)
#     return [deck[i:i+3] for i in range(0, 9, 3)]
#
# # 比较牌的大小
# def compare_hands(player1, player2, player3):
#     hands = [player1, player2, player3]
#     hand_types = [classify_hand(hand) for hand in hands]
#     hand_types.sort(key=lambda x: (hand_rank[x[0]], x[1]), reverse=True)
#     return hand_types
#
# # 发牌并比较
# player1, player2, player3 = deal_cards()
# result = compare_hands(player1, player2, player3)
#
# # 打印每个玩家的手牌和比较后手牌排序结果
# print(f'玩家1的手牌: {player1}')
# print(f'玩家2的手牌: {player2}')
# print(f'玩家3的手牌: {player3}')
# print(f'比较结果: {result}')
#
# # 确定赢家并打印
# max_hand = max(result, key=lambda x: (hand_rank[x[0]], x[1]))
# max_player = result.index(max_hand) + 1  # 因为玩家编号从1开始，结果从零开始
# print(f'赢家为: 玩家{max_player}')


