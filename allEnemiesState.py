class AllEnemy:
    def __init__(self,
                 min_enemy_HP: int = 0,
                 max_enemy_HP: int = 0,
                 total_HP: int = 0,
                 min_enemy_block: int = 0,
                 max_damage: int = 0,
                 total_damage: int = 0,
                 enemy_count: int = 0,
                 buff_self_count: int = 0,
                 debuff_player_count: int = 0):

        self.min_enemy_HP = min_enemy_HP
        self.max_enemy_HP = max_enemy_HP
        self.total_HP = total_HP

        self.min_enemy_block = min_enemy_block

        self.max_damage = max_damage
        self.total_damage = total_damage

        self.enemy_count = enemy_count

        self.buff_self_count = buff_self_count
        self.debuff_player_count = debuff_player_count

    def __repr__(self):
        return (f"<AllEnemy count={self.enemy_count}, "
                f"HP(min={self.min_enemy_HP}, max={self.max_enemy_HP}, total={self.total_HP}), min_block={self.min_enemy_block} "
                f"DMG(max={self.max_damage}, total={self.total_damage}), "
                f"BUFF_SELF={self.buff_self_count}, DEBUFF_PLAYER={self.debuff_player_count}>")

    @staticmethod
    def from_enemies(enemies):
        if not enemies:
            return AllEnemy()

        min_hp = min(e.HP for e in enemies)
        max_hp = max(e.HP for e in enemies)
        total_hp = sum(e.HP for e in enemies)

        min_block = min(e.block for e in enemies)

        max_damage = max(e.damage for e in enemies)
        total_damage = sum(e.damage for e in enemies)

        buff_self_count = sum(1 for e in enemies if e.intent_buff_self)
        debuff_player_count = sum(1 for e in enemies if e.intent_debuff_player)

        return AllEnemy(
            min_enemy_HP=min_hp,
            max_enemy_HP=max_hp,
            total_HP=total_hp,
            min_enemy_block=min_block,
            max_damage=max_damage,
            total_damage=total_damage,
            enemy_count=len(enemies),
            buff_self_count=buff_self_count,
            debuff_player_count=debuff_player_count
        )