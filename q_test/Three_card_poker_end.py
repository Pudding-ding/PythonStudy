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
# 2. 比出这三手牌大小并说明赢家是谁

import random

# 定义牌面的花色和点数
suits = ['♥', '♠', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# 初始化一副扑克牌
def create_deck():
    return [f'{rank}{suit}' for suit in suits for rank in ranks]

# 给三个玩家发牌
# def deal_cards(deck):
#     random.shuffle(deck)  # 洗牌
#     hands = [[], [], []]  # 三个玩家的牌
#     for i in range(9):  # 9张牌，三名玩家
#         hands[i % 3].append(deck[i])  # 按顺序将牌分配给玩家
#     return hands
def deal_cards(deck):
    random.shuffle(deck)  # 洗牌
    return [deck[i:i + 3] for i in range(0, 9, 3)]  # 发给三名玩家

#定义游戏规则

# 对手牌进行解析
def parse_card(card):
    rank = card[:-1]
    suit = card[-1]
    return rank, suit

# 判断牌型大小
def hand_value(hand):
    ranks = [parse_card(card)[0] for card in hand]   #获取手牌的点数
    suits = [parse_card(card)[1] for card in hand]
    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}  #统计每个点数出现的次数
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}
    # 豹子
    if len(rank_counts) == 1:
        return ('豹子', sorted(ranks, key=rank_order, reverse=True))
    # 同花顺
    if len(suit_counts) == 1:
        sorted_ranks = sorted([ranks.index(r) for r in ranks])
        if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] + 3)):
            return ('同花顺', sorted(ranks, key=rank_order, reverse=True))
    # 同花
    if len(suit_counts) == 1:
        return ('同花', sorted(ranks, key=rank_order, reverse=True))
    # 顺子
    if len(suit_counts) == 1:
        sorted_ranks = sorted([ranks.index(r) for r in ranks])
        if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] + 3)):
            return ('顺子', sorted(ranks, key=rank_order, reverse=True))
    # 对子
    if len(rank_counts) == 2:
        pair_rank = max(rank_counts, key=rank_counts.get)
        single_rank = min(rank_counts, key=rank_counts.get)
        return ('对子', pair_rank, single_rank)
    # 高牌
    return ('高牌', sorted(ranks, key=rank_order, reverse=True))

# 对手牌进行排序
def rank_order(rank):
    order = {ranks[i]: i for i in range(len(ranks))}
    return order[rank]

# 比较手牌的大小
def compare_hands(hands):
    hand_values = [hand_value(hand) for hand in hands]

    hand_order = {
        "豹子": 6,
        "同花顺": 5,
        "同花": 4,
        "顺子": 3,
        "对子": 2,
        "高牌": 1,
    }
#     # 比较两个手牌的大小
#     def compare_two_hands(hand1, hand2):
#         type1, *value1 = hand1
#         type2, *value2 = hand2
#         if hand_order[type1] > hand_order[type2]:
#             return 1
#         elif hand_order[type1] < hand_order[type2]:
#             return -1
#         else:
#             return compare_values(value1, value2)    # 如果牌型相同，按具体牌值比较
#     # 比较具体的牌值
#     def compare_values(value1, value2):
#         return (value1 > value2) - (value1 < value2)
#     # 逐个比较
#     def hand_sort_key(hand):
#         hand_type, *hand_detail = hand_value(hand)
#         hand_rank = hand_order[hand_type]
#         return (hand_rank, hand_detail)
#     # 排序
#     sorted_hands = sorted(hands, key=hand_sort_key, reverse=True)
#     return sorted_hands     # 返回排序后的手牌

    # 通过手牌的类型和详细信息排序
    def hand_sort_key(hand_with_index):
        hand, player_index = hand_with_index
        hand_type, *hand_detail = hand_value(hand)
        hand_rank = hand_order[hand_type]
        return (hand_rank, hand_detail)
    # 给每个玩家的手牌添加玩家编号
    hands_with_index = [(hand, i) for i, hand in enumerate(hands)]
    # 根据牌型大小排序玩家的手牌
    sorted_hands = sorted(hands_with_index, key=hand_sort_key, reverse=True)
    return sorted_hands

# 开始游戏--游戏流程
def play_game():
    deck = create_deck()
    hands = deal_cards(deck)
    # 比较三个人的手牌
    sorted_hands = compare_hands(hands)
    # 输出每个玩家的手牌
    for i, hand in enumerate(hands, start=1):
        hand_type, *value = hand_value(hand)
        print(f'玩家{i}的牌: {hand}')
    # 对玩家手牌进行排序
    print('\n对手牌排序：')
    for i, (hand, player_index) in enumerate(sorted_hands, start=1):
        hand_type, *value = hand_value(hand)
        print(f'玩家{player_index + 1}:{hand_type} - {hand}')
    # 确定赢家编号
    winner_index = sorted_hands[0][1] + 1
    print(f'赢家是:玩家{winner_index}-{sorted_hands[0][0]}')

# 执行游戏
play_game()
