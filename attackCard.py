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

        self.name = name
        self.cost = cost
        self.damage = damage
        self.block = block
        self.draw = draw #the number of drawing cards
        self.vulnerable = vulnerable #the number of vulnerable turns
        self.loseHp = loseHp
        self.toEnemies = toEnemies #the number of enemies
        self.exhaust = exhaust  #is exhaust card or not
        self.strength = strength
        self.raiseMaxHp = raiseMaxHp
        self.lostEnemyStrength = lostEnemyStrength

    def __repr__(self):
        return f"<AttackCard id={self.card_id} name={self.name}>"


def load_attack_cards_from_excel(file_path: str) -> List[AttackCard]:
    df = pd.read_excel(file_path)
    cards = []
    for idx, row in df.iterrows():
        data = {}
        for col in df.columns:
            value = row[col]
            # start with '#' means dynamic value,init none first
            if isinstance(value, str) and value.startswith('#'):
                value = None
            data[col] = value


        def safe_int(x):
            try:
                return int(x)
            except (TypeError, ValueError):
                return 0

        card = AttackCard(
            card_id=idx,
            name=data.get('name', ''),
            cost=safe_int(data.get('cost')),
            damage=safe_int(data.get('damage')),
            block=safe_int(data.get('block')),
            draw=safe_int(data.get('draw')),
            vulnerable=safe_int(data.get('vulnerable')),
            loseHp=safe_int(data.get('loseHp')),
            toEnemies=safe_int(data.get('toEnemies')),
            exhaust=bool(data.get('exhaust', False)),
            strength=safe_int(data.get('strength')),
            raiseMaxHp=safe_int(data.get('raiseMaxHp')),
            lostEnemyStrength=safe_int(data.get('lostEnemyStrength'))
        )
        cards.append(card)
    return cards