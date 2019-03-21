from cards import get_cards
import random

class CardsController:
    def __init__(self):
        self.cards = get_cards()
        self.used_cards = []
        self.now = self.cards.pop(0)
        self.previous = None
    
    def reload_cards(self):
        card_list = self.used_cards.copy()
        self.used_cards.clear()
        card_list.extend(self.cards)
        random.shuffle(card_list)
        self.cards = card_list
    
    def get_some_cards(self, count):
        if len(self.cards) < count:
            self.reload_cards()
        if len(self.cards) > count:
            some_cards = self.cards[:count]
            self.cards = self.cards[count:]
            return some_cards
    
    def get_start_cards(self):
        return self.get_some_cards(7)
    
    def draw_two(self):
        return self.get_some_cards(2)
        
    def draw_four(self):
        return self.get_some_cards(4)
        
    def draw_six(self):
        return self.get_some_cards(6)
            
    def get_card(self):
        if not self.cards:
            self.reload_cards()
        if self.cards:
            return self.cards.pop(0)
        
    def drop(self, card):
        prev = self.now
        self.used_cards.append(self.previous)
        self.previous = prev
        self.now = card
        
        