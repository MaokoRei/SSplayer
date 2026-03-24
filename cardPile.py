from typing import List

class Deck:
    def __init__(self, cards: List = None):
        """
        cards: List[AttackCard]，初始化时传入完整卡牌对象
        """
        self.cards = cards if cards else []
        # 创建 card_id -> AttackCard 的映射
        self.card_map = {card.card_id: card for card in self.cards}

        # 牌堆
        self.draw_pile = [card.card_id for card in self.cards]
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []
        self.turn_played_pile = []

        # strike 计数
        self.strikeCount = 0
        self.turnStrikeCount = 0

    # ------------------------
    # 根据 card_id 获取卡牌对象
    # ------------------------
    def get_card_by_id(self, card_id):
        return self.card_map.get(card_id)

    # ------------------------
    # 出牌
    # ------------------------
    def play_card(self, card_id, exhaust=False):

        card = self.get_card_by_id(card_id)
        if not card:
            print(f"card_id {card_id} 不存在")
            return
        if card_id == 22:
            self.reset_from_input()
            # 特殊逻辑 28：消耗牌增加伤害,该逻辑与实际有差异，实际会添加卡牌结算后的伤害，此处简化处理
        if card_id == 28:
            selected_id = self.select_card_to_exhaust()
            if selected_id is not None:
                exhaust_card = self.get_card_by_id(selected_id)
                if exhaust_card and exhaust_card.damage:
                    # 把消耗牌伤害加到当前卡牌
                    card.damage = (card.damage or 0) + exhaust_card.damage
                    print(f"28号卡牌伤害更新为: {card.damage}")

        if card_id == 29:
            print(f"29号卡牌效果：消耗手牌 {self.hand}")
            self.exhaust_pile.extend(self.hand)
            self.hand = []

        if card_id in self.hand:
            self.hand.remove(card_id)
            if exhaust:
                self.exhaust_pile.append(card_id)
            else:
                self.discard_pile.append(card_id)
                self.turn_played_pile.append(card_id)

    # ------------------------
    # 消耗牌交互
    # ------------------------
    def select_card_to_exhaust(self):
        if not self.hand:
            print("手牌为空，无法消耗卡牌。")
            return None

        print(f"当前手牌: {self.hand}")

        while True:
            try:
                card_id = input("请输入要消耗的卡牌 id: ").strip()
                if card_id == "":
                    print("取消选择")
                    return None
                card_id = int(card_id)
                if card_id in self.hand:
                    self.hand.remove(card_id)
                    self.exhaust_pile.append(card_id)
                    print(f"已消耗卡牌 {card_id}")
                    return card_id
                else:
                    print("输入的 card_id 不在手牌中，请重新输入。")
            except ValueError:
                print("输入无效，请输入整数 card_id。")

    # ------------------------
    # strike 统计
    # ------------------------
    def update_turn_strike_count(self):
        target_ids = {0, 8, 9, 12, 14, 18}
        self.turnStrikeCount = sum(
            card_id in target_ids
            for card_id in self.turn_played_pile
        )

    def update_strike_count(self):
        target_ids = {0, 8, 9, 12, 14, 18}
        self.strikeCount = sum(
            card_id in target_ids
            for pile in [self.draw_pile, self.hand, self.discard_pile]
            for card_id in pile
        )

    # ------------------------
    # 单独消耗牌函数
    # ------------------------
    def exhaust_card(self, card_id):
        if card_id in self.hand:
            self.hand.remove(card_id)
            self.exhaust_pile.append(card_id)
        self.update_strike_count()

    # ------------------------
    # 回合操作
    # ------------------------
    def end_turn(self):
        self.discard_pile.extend(self.hand)
        self.hand = []
        self.turn_played_pile = []

    def start_turn(self):
        print("\n=== 回合开始：请输入牌堆状态 ===")
        self.reset_from_input()

    # ------------------------
    # 控制台重置牌堆
    # ------------------------
    def reset_from_input(self):
        print("输入格式：用空格分隔 card_id，直接回车表示空")

        def read_list(prompt):
            line = input(prompt).strip()
            if line == "":
                return []
            try:
                return list(map(int, line.split()))
            except ValueError:
                print("输入错误，默认空列表")
                return []

        self.draw_pile = read_list("draw_pile: ")
        self.hand = read_list("hand: ")
        self.discard_pile = read_list("discard_pile: ")
        self.update_strike_count()
        print("当前牌堆状态：", self)

    # ------------------------
    # 打印牌堆状态
    # ------------------------
    def __repr__(self):
        return (f"<Deck hand={self.hand}, "
                f"draw={len(self.draw_pile)}, "
                f"discard={len(self.discard_pile)}, "
                f"exhaust={len(self.exhaust_pile)}>")
