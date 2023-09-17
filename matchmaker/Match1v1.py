import random as rd
import Player 

class Match1v1:

    def __init__(self, player1 : Player, player2 : Player):
        self.player1 : Player = player1
        self.player2 : Player = player2
        self.winner = None
        self.loser = None
        self.duration = abs(player1.elo - player2.elo)*10*rd.random()+3
        self.time_left = self.duration

    
    def __str__(self):
        return "Match 1v1 :  Player1 : " + str(self.player1) + " Player2 : " + str(self.player2) 
    
    def resolve_logic(self):
        if self.player1.elo> self.player2.elo:
            self.winner = self.player1
            self.loser = self.player2
        else:
            self.winner = self.player2
            self.loser = self.player1
    
    def resolve_random(self):
        ratio = self.player1.elo / (self.player1.elo + self.player2.elo)
        if rd.random() < ratio:
            self.winner = self.player1
            self.loser = self.player2
        else:
            self.winner = self.player2
            self.loser = self.player1

    def update_elo(self):       #valeures à changer
        self.winner.elo += 1
        self.loser.elo -= 1 

        

