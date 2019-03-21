from players_queue import PlayersQueue
from cards_controller import CardsController

class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.play = False
        self.cards = CardsController()
        self.players = PlayersQueue(10)
        self.colour = None
        self.ability = None
        self.message_id = None
                
    def __repr__(self):
        return str(self.players)
        #return 'Card: {} Turn: {}\nAll: \n{}'.format(self.cards.now, '⬆️' if self.players.turn_way == -1 else '⬇️', self.players)
    
    def add_player(self, player):
        return self.players.append(player)
    
    def start(self):
        self.players.next()
        self.play = True
        
    def stop(self):
        self.play = False
    
    def clear(self):
        self.colour = None
        self.ability = None
        
    def next(self):
        self.players.next()
    
    def is_end(self):
        return len(self.players.queue) <= 1
    
    def put_card(self, card):
        now = self.cards.now
        if now.is_usual:
            if now.checker(card):
                self.players.now.del_card(card)
                self.cards.drop(card)
                self.next()
                return True
    

                
