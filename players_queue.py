class PlayersQueue:
    def __init__(self, max_count):
        self.max_count = max_count
        self.queue = []
        self.turn_way = 1
        self.n = -1 #Add +1 at start
        
    def append(self, player):
        if len(self.queue) < self.max_count:
            self.queue.append(player)
            return True
    
    def __repr__(self):
        l = [str(one) for one in self.queue]
        l[self.n] = '▶️ ' + l[self.n]
        return '\n'.join(l)
    
    def turn(self, t):
        if t == 1 or t == -1:
            self.turn_way = t
    
    def remove(self, player):
        player.game.cards.used_cards.extend(player.cards)
        self.queue.remove(player)
    
    def next(self):
        self.clear()
        if self.turn_way == 1:
            self.n += 1
            if len(self.queue) <= self.n:
                self.n = 0
        elif self.turn_way == -1:
            self.n -= 1
            if self.n < 0:
                self.n = len(self.queue) - 1
    
    def clear(self):
        self.now.is_get_card = False
    
    @property
    def now(self):
        return self.queue[self.n]
    
            
        