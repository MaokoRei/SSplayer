import pandas as pd
from typing import List, Optional


class AttackCard:
    def __init__(self, card_id: int, name: str, cost: int,
                 damage: Optional[int] = None, block: Optional[int] = None, draw: Optional[int] = None,
                 vulnerable: Optional[int] = None, loseHp: Optional[int] = None, toEnemies: Optional[int] = None,
                 exhaust: Optional[bool] = False, strength: Optional[int] = None,
                 raiseMaxHp: Optional[int] = None, lostEnemyStrength: Optional[int] = None):
        # 唯一标识
        self.card_id = card_id

        # 静态属性
        self.name = name
        self.cost = cost
        self.damage = damage
        self.block = block
        self.draw = draw
        self.vulnerable = vulnerable
        self.loseHp = loseHp
        self.toEnemies = toEnemies
        self.exhaust = exhaust
        self.strength = strength
        self.raiseMaxHp = raiseMaxHp
        self.lostEnemyStrength = lostEnemyStrength

    def __repr__(self):
        return f"<AttackCard id={self.card_id} name={self.name}>"


def load_attack_cards_from_excel(file_path: str) -> List[AttackCard]:
    df = pd.read_excel(file_path)
    cards = []
    for idx, row in df.iterrows():
        # 对于以 # 开头的列，直接设置为 None（表示公式列，未填数值）
        data = {col: (None if col.startswith('#') else row[col]) for col in df.columns}

        card = AttackCard(
            card_id=idx,
            name=data.get('name', ''),
            cost=int(data.get('cost', 0)),
            damage=data.get('damage'),
            block=data.get('block'),
            draw=data.get('draw'),
            vulnerable=data.get('vulnerable'),
            loseHp=data.get('loseHp'),
            toEnemies=data.get('toEnemies'),
            exhaust=bool(data.get('exhaust', False)),
            strength=data.get('strength'),
            raiseMaxHp=data.get('raiseMaxHp'),
            lostEnemyStrength=data.get('lostEnemyStrength')
        )
        cards.append(card)
    return cards