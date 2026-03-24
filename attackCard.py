from typing import List
import pandas as pd

class AttackCard:
    def __init__(self, card_id: int, name: str, cost: int,
                 damage: int = None,
                 block: int = None,
                 draw: int = None,
                 vulnerable: int = None,
                 loseHp: int = None,
                 isAOE: bool = False,
                 exhaust: int = False,
                 strength: int = None,
                 raiseMaxHp: int = None,
                 lostEnemyStrength: int = None,
                 hitCount: int = None,
                 isRandomHit: bool = False):

        self.card_id = card_id

        self.name = name
        self.cost = cost
        self.damage = damage
        self.block = block
        self.draw = draw
        self.vulnerable = vulnerable
        self.loseHp = loseHp

        # 新字段
        self.isAOE = isAOE
        self.exhaust = exhaust
        self.strength = strength
        self.raiseMaxHp = raiseMaxHp
        self.lostEnemyStrength = lostEnemyStrength
        self.hitCount = hitCount
        self.isRandomHit = isRandomHit

    def __repr__(self):
        return f"<AttackCard id={self.card_id} name={self.name}>"

def load_attack_cards_from_excel(file_path: str) -> List[AttackCard]:
    df = pd.read_excel(file_path)
    cards = []

    for idx, row in df.iterrows():
        data = {}

        for col in df.columns:
            value = row[col]

            if isinstance(value, str) and value.startswith('#'):
                value = None
            data[col] = value

        def safe_int(x):
            try:
                return int(x)
            except (TypeError, ValueError):
                return 0

        def safe_bool(x):
            if isinstance(x, bool):
                return x
            if isinstance(x, str):
                return x.lower() == 'true'
            return bool(x)

        card = AttackCard(
            card_id=idx,
            name=data.get('name', ''),
            cost=safe_int(data.get('cost')),
            damage=safe_int(data.get('damage')),
            block=safe_int(data.get('block')),
            draw=safe_int(data.get('draw')),
            vulnerable=safe_int(data.get('vulnerable')),
            loseHp=safe_int(data.get('loseHp')),

            # 新字段
            isAOE=safe_bool(data.get('isAOE')),
            exhaust=safe_int(data.get('exhaust')),
            strength=safe_int(data.get('strength')),
            raiseMaxHp=safe_int(data.get('raiseMaxHp')),
            lostEnemyStrength=safe_int(data.get('lostEnemyStrength')),
            hitCount=safe_int(data.get('hitCount')),
            isRandomHit=safe_bool(data.get('isRandomHit'))
        )

        cards.append(card)

    return cards