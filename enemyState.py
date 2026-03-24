class Enemy:
    def __init__(self, HP: int,
                 strength: int = 0,
                 vulnerable: int = 0,
                 dexterity: int = 0,
                 weak: int = 0,
                 damage: int = 0,
                 block: int = 0,
                 intent_buff_self: bool = False,
                 intent_debuff_player: bool = False):
        self.HP = HP

        #(Buff / Debuff)
        self.strength = strength
        self.vulnerable = vulnerable
        self.dexterity = dexterity
        self.weak = weak

        self.damage = damage
        self.block = block

        self.intent_buff_self = intent_buff_self
        self.intent_debuff_player = intent_debuff_player

    def __repr__(self):
        return (f"<Enemy HP={self.HP}, STR={self.strength}, DEX={self.dexterity}, "
                f"VUL={self.vulnerable}, WEAK={self.weak}, "
                f"DMG={self.damage}, BLOCK={self.block}, "
                f"BUFF_SELF={self.intent_buff_self}, DEBUFF_PLAYER={self.intent_debuff_player}>")

    def end_turn(self):
        if self.vulnerable > 0:
            self.vulnerable -= 1
        if self.weak > 0:
            self.weak -= 1
        if self.block > 0:
            self.block = 0


    #set state from prompt
    @staticmethod
    def input_enemies():
        enemies = []

        try:
            enemy_count = int(input("请输入敌人数量: "))
        except ValueError:
            print("输入错误，默认敌人数量=0")
            return enemies

        for i in range(enemy_count):
            print(f"\n输入第 {i + 1} 个敌人属性（回车可用默认值0或False）：")
            try:
                HP = int(input("  HP: "))
            except ValueError:
                HP = 0

            try:
                strength = int(input("  strength: "))
            except ValueError:
                strength = 0

            try:
                vulnerable = int(input("  vulnerable: "))
            except ValueError:
                vulnerable = 0

            try:
                dexterity = int(input("  dexterity: "))
            except ValueError:
                dexterity = 0

            try:
                weak = int(input("  weak: "))
            except ValueError:
                weak = 0

            try:
                damage = int(input("  damage (敌人意图伤害): "))
            except ValueError:
                damage = 0

            try:
                block = int(input("  block: "))
            except ValueError:
                block = 0

            # 新增意图布尔输入
            try:
                intent_buff_self = input("  intent_buff_self (True/False): ").strip().lower() == "true"
            except ValueError:
                intent_buff_self = False

            try:
                intent_debuff_player = input("  intent_debuff_player (True/False): ").strip().lower() == "true"
            except ValueError:
                intent_debuff_player = False

            enemy = Enemy(
                HP=HP,
                strength=strength,
                vulnerable=vulnerable,
                dexterity=dexterity,
                weak=weak,
                damage=damage,
                block=block,
                intent_buff_self=intent_buff_self,
                intent_debuff_player=intent_debuff_player
            )

            enemies.append(enemy)

        print("\n已创建敌人列表：")
        for e in enemies:
            print(e)

        return enemies