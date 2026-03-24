import attackCard
import enemyState
import playerState
import allEnemiesState
import cardPile

class TurnState:
    def __init__(self,
                 lost_HP_count: int = 0,
                 left_cost: int = 3
                 ):
        self.lost_HP_count = lost_HP_count
        self.left_cost = left_cost

def compute_card_effect(card, player, enemy, deck, turnState):
    result = {
        "cost": card.cost or 0,
        "damage": card.damage or 0,
        "block": card.block or 0,
        "draw": card.draw or 0,
        "vulnerable": card.vulnerable or 0,
        "loseHp": card.loseHp or 0,
        "exhaust": card.exhaust or 0,
        "strength": card.strength or 0,
        "raiseMaxHp": card.raiseMaxHp or 0,
        "lostEnemyStrength": card.lostEnemyStrength or 0,
        "hitCount": card.hitCount or 1
    }

    if card.card_id == 3:  # bodySlam
        result["damage"] = player.block

    if card.card_id == 14:  # perfectedStrike
        result["damage"] = deck.strikeCount * 2 + 6

    if card.card_id == 15:  # bully
        result["damage"] = enemy.vulnerable * 2 + 4

    if card.card_id == 7:  # moltenFirst
        result["vulnerable"] = enemy.vulnerable * 2

    if card.card_id == 16:  # spite
        result["draw"] = 1 if turnState.lost_HP_count > 0 else 0

    if card.card_id == 17:  # whirlwind
        result["cost"] = turnState.left_cost
        result["hitCount"] = turnState.left_cost

    if card.card_id == 18:  # ashenStrike
        result["damage"] = len(deck.exhaust_pile) * 3 + 6

    if card.card_id == 19:  # dismantle
        result["hitCount"] = 2 if enemy.vulnerable > 0 else 1

    if card.card_id == 20:  # grapple
        result["damage"] = 7

    if card.card_id == 24:  # stomp
        result["cost"] = 3 - len(deck.turn_played_pile) if len(deck.turn_played_pile) <= 3 else 0

    if card.card_id == 26:  # conflagration
        result["damage"] = len(deck.turn_played_pile) * 2 + 8

    if card.card_id == 29:  # fiendFire
        result["damage"] = 7 * (len(deck.hand) - 1)
        result["exhaust"] = len(deck.hand)

    if card.card_id == 30:  # tearAsunder
        result["damage"] = 5 * turnState.lost_HP_count

    if result["damage"] > 0:
        result["damage"] += player.strength

    if player.weak > 0:
        result["damage"] = int(result["damage"] * 0.75)

    if enemy.vulnerable > 0:
        result["damage"] = int(result["damage"] * 1.5)

    total_damage = result["damage"] * result["hitCount"]
    result["total_damage"] = total_damage

    if card.card_id == 27:  # feed  # 结算damage之后再处理
        if result["damage"] > (enemy.HP + enemy.block):
            result["raiseMaxHp"] = 3
        else:
            result["raiseMaxHp"] = 0

    if result["block"] > 0:
        result["block"] += player.dexterity

    return result