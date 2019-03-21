import random
import copy

class Card:
    def __init__(self, type, content, light, dark, quantity, ability=None, possibility=None):
        self.type = type
        self.content = content
        self.light = light
        self.is_usual = not(ability or possibility)
        self.dark = dark
        self.ability = ability
        self.possibility = possibility
        self.quantity = quantity
    
    def checker(self, card):
        return self.type == card.type or self.content == card.content
    
    def usual_checker(self, card):
        if self.checker(card):
            return {'id': self.light, 'card': True}
        else:
            return {'id': self.dark, 'card': False}
    
    def get_file(self, card):
        # if self.possibility:
        #     return self.possibility(self, card)
        # else:
            return self.usual_checker(card)
            
    def __repr__(self):
        return '{}_{}'.format(self.type, self.content)

# def show_black_cards(this, card):
#     return this.light
    
# def show_draw(this, card):
#     if card.content == 'four' and card.type == this.type:
#         return this.light
#     else:
#         return this.usual_checker(card)
        
        

ALL_CARDS = [
# Card('draw', 'four', 'CAADAgADiQMAAk9wUEg1fzyY8FgCZgI', 'CAADAgADtAMAAk9wUEiEDCzN-ZufxAI', 4, show=show_black_cards),
# Card('choose', 'color', 'CAADAgADmwMAAk9wUEgGjFv_XetVPAI', 'CAADAgADyQMAAk9wUEj7TDyDL4ZMhgI', 4, show=show_black_cards),
# Card('y', 'reverse', 'CAADAgAD3AIAAseySUhy5e5w5AYaqwI', 'CAADAgADnwMAAk9wUEg3oD-QCtyv_gI', 2),
# Card('r', 'reverse', 'CAADAgAD5wIAAseySUjSFQmCV0Q5VQI', 'CAADAgADsAMAAk9wUEgbnhIc2DCM_AI', 2),
# Card('b', 'reverse', 'CAADAgADmgMAAk9wUEixAkTWMiRZQgI', 'CAADAgADyAMAAk9wUEgDZTylBEJZ2wI', 2),
# Card('g', 'reverse', 'CAADAgADngMAAk9wUEg2sF3mAr6D4AI', 'CAADAgADzQMAAk9wUEjWTC1ZGH4WqAI', 2),
# Card('y', 'draw', 'CAADAgADigMAAk9wUEhhq91otjZ-qwI', 'CAADAgAD8wIAAseySUgmv5CDF4flhgI', 2),
# Card('r', 'draw', 'CAADAgADkQMAAk9wUEjbNUD6Fn1GIQI', 'CAADAgADvgMAAk9wUEgmR-3ymzxtxAI', 2),
# Card('b', 'draw', 'CAADAgAD5QIAAseySUhcruhIu1G-ngI', 'CAADAgADrwMAAk9wUEh_7u4zSVkaSQI', 2),
# Card('g', 'draw', 'CAADAgADfgMAAk9wUEgsghsS-Zc_iwI', 'CAADAgADpwMAAk9wUEjrXEV7gihhCgI', 2),
# Card('y', 'skip', 'CAADAgAD4gIAAseySUi2odgfcaIRFwI', 'CAADAgADqAMAAk9wUEhWIwWt1YTOQgI', 2),
# Card('r', 'skip', 'CAADAgAD3wIAAseySUitxTgGuFZo4gI', 'CAADAgADpAMAAk9wUEjVZAKzIajF3wI', 2),
# Card('b', 'skip', 'CAADAgADjQMAAk9wUEhioLRerJ23FwI', 'CAADAgADugMAAk9wUEgB60poi4fRfwI', 2),
# Card('g', 'skip', 'CAADAgADiwMAAk9wUEjbnFgLYpuG7wI', 'CAADAgADtwMAAk9wUEjHvt7slZazUwI', 2),
Card('g', '1', 'CAADAgADewMAAk9wUEi4DJO-L2tZNAI', 'CAADAgADoAMAAk9wUEj5guEu1Lbk_QI', 2),
Card('y', '8', 'CAADAgADfAMAAk9wUEjJ15Lr-10XRgI', 'CAADAgADoQMAAk9wUEg7E0IMmfHOBAI', 2),
Card('b', '6', 'CAADAgADfQMAAk9wUEhxgz0hGpmoJgI', 'CAADAgADogMAAk9wUEhmKkXJg_Fv9gI', 2),
Card('y', '5', 'CAADAgAD3QIAAseySUjQ4T4byCeH-QI', 'CAADAgAD7gIAAseySUj6a9-7sg5LHwI', 2),
Card('r', '5', 'CAADAgAD3gIAAseySUjdkhZ6ikBotAI', 'CAADAgADowMAAk9wUEivJSp08kP4XQI', 2),
Card('b', '4', 'CAADAgAD4AIAAseySUhAe-WUua50hQI', 'CAADAgADpQMAAk9wUEgma85xe3g_DwI', 2),
Card('y', '0', 'CAADAgAD4QIAAseySUgg7DTlbUZ7JgI', 'CAADAgADpgMAAk9wUEgLNo1CAj1-qAI', 1),
Card('b', '8', 'CAADAgADfwMAAk9wUEhqalELuqlqGwI', 'CAADAgADqQMAAk9wUEgG5jqe1VGoQAI', 2),
Card('y', '9', 'CAADAgADgAMAAk9wUEjJLhdHH4gfTwI', 'CAADAgADqgMAAk9wUEhSETm0HGOu1QI', 2),
Card('r', '6', 'CAADAgADgQMAAk9wUEhR8swdwflaQwI', 'CAADAgAD7wIAAseySUjDrhiSw8IxfgI', 2),
Card('r', '2', 'CAADAgADggMAAk9wUEgoaiUIRbe3IQI', 'CAADAgAD8AIAAseySUjJti9Flw6D8QI', 2),
Card('y', '4', 'CAADAgADgwMAAk9wUEiZluO_3K4VDQI', 'CAADAgADqwMAAk9wUEi8e4aX6OIF5wI', 2),
Card('g', '2', 'CAADAgADhAMAAk9wUEiSka25-wAB4mYC', 'CAADAgAD8QIAAseySUg2tYP02DsTmAI', 2),
Card('y', '6', 'CAADAgAD4wIAAseySUihNLTWE-v_dQI', 'CAADAgADrAMAAk9wUEh6sR2aCrBAeAI', 2),
Card('g', '7', 'CAADAgADhQMAAk9wUEhJaq5oUqeDgQI', 'CAADAgADrQMAAk9wUEg53kujX5rP2AI', 2),
Card('y', '3', 'CAADAgAD5AIAAseySUgFrbgN67cbXwI', 'CAADAgADrgMAAk9wUEgXZ_aapTQPiAI', 2),
Card('b', '0', 'CAADAgAD5gIAAseySUhpOyN2IdIeBAI', 'CAADAgAD8gIAAseySUiS8q6SPfkSdwI', 1),
Card('r', '0', 'CAADAgADhgMAAk9wUEjescGFZdFv7QI', 'CAADAgADsQMAAk9wUEgWY_IdvljiYwI', 1),
Card('b', '2', 'CAADAgADhwMAAk9wUEjUxdZoY4EaKAI', 'CAADAgADsgMAAk9wUEhX_1ki4Kc3ggI', 2),
Card('y', '2', 'CAADAgADiAMAAk9wUEjPFzRjZNbL-wI', 'CAADAgADswMAAk9wUEjYTDVsrHcKNAI', 2),
Card('r', '3', 'CAADAgAD6AIAAseySUit_A1wxY7fQgI', 'CAADAgADtQMAAk9wUEjDhKZTwO06cAI', 2),
Card('g', '8', 'CAADAgAD6QIAAseySUi_JI3nWGyrOwI', 'CAADAgADtgMAAk9wUEij5aWiQSRvsQI', 2),
Card('b', '9', 'CAADAgADjAMAAk9wUEgrDuMzknc7gQI', 'CAADAgADuAMAAk9wUEgAAZBQy2Lzr1UC', 2),
Card('y', '7', 'CAADAgAD6gIAAseySUhrT7VCx9Up0wI', 'CAADAgADuQMAAk9wUEhZe8nHdNVftwI', 2),
Card('b', '3', 'CAADAgADjgMAAk9wUEhUtoQgz4tIIQI', 'CAADAgADuwMAAk9wUEhlQ10DpjmDDAI', 2),
Card('r', '9', 'CAADAgADjwMAAk9wUEiFG0ayDANWvwI', 'CAADAgADvAMAAk9wUEhb4cnEL_GGfQI', 2),
Card('g', '3', 'CAADAgADkAMAAk9wUEhGiA1COUKTWQI', 'CAADAgADvQMAAk9wUEjmRGnHhfEQkQI', 2),
Card('r', '1', 'CAADAgADkgMAAk9wUEhk4v36yl_VWQI', 'CAADAgAD9AIAAseySUhsJoBNviG6fQI', 2),
Card('r', '8', 'CAADAgADkwMAAk9wUEjodD4zjAh7FgI', 'CAADAgADvwMAAk9wUEhvZPDJwpvLFAI', 2),
Card('b', '5', 'CAADAgADlAMAAk9wUEikiYYpAYCrmQI', 'CAADAgADwAMAAk9wUEh_ttsP70SyUAI', 2),
Card('g', '0', 'CAADAgAD6wIAAseySUjZ0JmK93kJTQI', 'CAADAgADwQMAAk9wUEgAATFHPdMw5QMC', 1),
Card('g', '9', 'CAADAgADlQMAAk9wUEg8X2LEMEOjJQI', 'CAADAgADwgMAAk9wUEhz68cfrzdOnAI', 2),
Card('g', '4', 'CAADAgADlgMAAk9wUEjLPr0btKoBdAI', 'CAADAgADwwMAAk9wUEiq7Z8QOwty_AI', 2),
Card('g', '6', 'CAADAgADlwMAAk9wUEhBZ0E4WkpZIwI', 'CAADAgADxAMAAk9wUEjBbpPfZpIE3gI', 2),
Card('g', '5', 'CAADAgAD7AIAAseySUiZ94yjPRKKPwI', 'CAADAgADxQMAAk9wUEiOMCwiPYDioQI', 2),
Card('r', '7', 'CAADAgADmAMAAk9wUEiFp5poipC8hgI', 'CAADAgADxgMAAk9wUEiYlQeP8jOplQI', 2),
Card('b', '7', 'CAADAgADmQMAAk9wUEhMIYl9DLwSNgI', 'CAADAgADxwMAAk9wUEgS0TUi3RRojwI', 2),
Card('r', '4', 'CAADAgADnAMAAk9wUEiPhQKi3V5BVAI', 'CAADAgADygMAAk9wUEhF_V8hXwMuagI', 2),
Card('y', '1', 'CAADAgADnQMAAk9wUEin6Vo81VdUSAI', 'CAADAgADywMAAk9wUEiqZCKbaLaHjAI', 2),
Card('b', '1', 'CAADAgAD7QIAAseySUiFeYcg24aSxgI', 'CAADAgADzAMAAk9wUEin3-xSuHYRHwI', 2)
]

def get_cards():
    CARDS = []
    for card in ALL_CARDS:
        for i in range(card.quantity):
            CARDS.append(copy.deepcopy(card))
    random.shuffle(CARDS)
    return CARDS

if __name__ == '__main__':
    print(len(get_cards()))
