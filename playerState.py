class Player:
    def __init__(self, maxHP: int,
                 HP: int = None,
                 block: int = 0,
                 strength: int = 0,
                 vulnerable: int = 0,
                 dexterity: int = 0,
                 weak: int = 0):
        self.maxHP = maxHP
        self.HP = HP if HP is not None else maxHP
        self.block = block

        # （Buff / Debuff）
        self.strength = strength  # 力量：增加攻击
        self.vulnerable = vulnerable  # 易伤：受到更多伤害（回合数）
        self.dexterity = dexterity  # 敏捷：增加格挡
        self.weak = weak  # 虚弱：减少伤害（回合数）

    def __repr__(self):
        return (f"<Player HP={self.HP}/{self.maxHP},Block = {self.block} "
                f"STR={self.strength}, DEX={self.dexterity}, "
                f"VUL={self.vulnerable}, WEAK={self.weak}>")

    # debuff reduce
    def end_turn(self):
        if self.vulnerable > 0:
            self.vulnerable -= 1
        if self.weak > 0:
            self.weak -= 1


    #set state from prompt
    def input_player_state(player):
        print("=== 输入玩家状态（直接回车表示不修改）===")

        def read_int(prompt, current):
            val = input(f"{prompt} (当前: {current})：")
            if val.strip() == "":
                return current
            try:
                return int(val)
            except ValueError:
                print("输入无效，保持原值")
                return current

        player.maxHP = read_int("maxHP", player.maxHP)
        player.HP = read_int("HP", player.HP)
        player.block = read_int("block", player.block)
        player.strength = read_int("strength", player.strength)
        player.vulnerable = read_int("vulnerable", player.vulnerable)
        player.dexterity = read_int("dexterity", player.dexterity)
        player.weak = read_int("weak", player.weak)

        print("更新完成：", player)