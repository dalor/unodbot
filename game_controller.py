from game import Game
from player import Player

class GameController:
    def __init__(self):
        self.games = {}
        self.players = {}
    
    def get_game(self, game_id):
        return self.games.get(game_id)
    
    def new_game(self, game_id):
        if not self.get_game(game_id):
            game = Game(game_id)
            self.games[game_id] = game
            return game
    
    def del_game(self, game_id):
        game = self.games.pop(game_id, None)
        if game:
            game.stop()
            for player in game.players.queue:
                self.del_player(player.id)
            return game
    
    def get_player(self, player_id, anyway=False):
        player = self.players.get(player_id)
        if anyway:
            return player
        else:
            if player and player.game.play:
                return player
        
    def new_player(self, game, player_id, name):
        if not self.get_player(player_id, True):
            player = Player(player_id, name, game)
            can_add = game.add_player(player)
            if can_add:
                self.players[player_id] = player
                return player
            
    def del_player(self, player_id):
        player = self.players.pop(player_id, None)
        if player:
            player.game.players.remove(player)
            return player
            
if __name__ == '__main__':
    c = GameController()
    game = c.new_game(1)
    c.new_player(game, 1, 2)
    c.new_player(game, 2, 3)
    game.start()
    print(game)