from datetime import datetime, timedelta

class Player:
    def __init__(self, player_id, name, game):
        self.id = player_id
        self.name = name
        self.game = game
        self.time = None
        self.cards = []
        self.is_get_card = False
        self.start_cards()
        self.update()
    
    def update(self):
        self.time = datetime.now()
        
    def in_time(self, **kwargs):
        return datetime.now() > (self.time + timedelta(**kwargs))
        
    def if_has(self, type=None, content=None):
        for card in self.cards:
            if card.type == type or card.content == content:
                return True
    
    def __repr__(self):
        return '<a href=\"tg://user?id={}\">{}</a>({}🎴)'.format(self.id, self.name, len(self.cards))
        
    def check_card(self, card_id):
        if self == self.game.players.now:
            for card in self.cards:
                if card.light == card_id:
                    return card
                
    def start_cards(self):
        cards = self.game.cards.get_start_cards()
        if cards:
            self.cards = cards
        
    def get_card(self):
        self.is_get_card = True
        self.cards.append(self.game.cards.get_card())
        
    def del_card(self, card):
        self.cards.remove(card)
            
    def draw_two(self):
        self.cards.extend(self.game.cards.draw_two())
        
    def draw_four(self):
        self.cards.extend(self.game.cards.draw_four())
        
    def draw_six(self):
        self.cards.extend(self.game.cards.draw_six())
            
    def get_cards(self):
        now_card = self.game.cards.now
        return [card.get_file(now_card) for card in self.cards]