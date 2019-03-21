def draw_two(player):
    queue = player.game.players
    queue.next()
    player = queue.now
    if player.if_has(content='draw'):
        player.game.ability = draw_four
    else:
        player.game.players.next()

def draw_four(player):
    pass

def skip(player):
    pass

def choose_colour(player):
    pass

def reverse(player):
    pass

def bluff(player):
    pass