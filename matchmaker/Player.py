import random
import Timeline


class Player:

    def __init__(self, id, elo):
        self.id = id
        self.elo = elo
        self.look_for_match = [] #List of time intervals where the player is looking for a match

    
    def __str__(self):
        return "Player :  Id : " + str(self.id) + " Elo : " + str(self.elo)
    
    def add_to_timeline(self, timeline : Timeline.Timeline):
        timeline.player_pool.append(self)

        self.look_for_match=[timeline.time ,timeline.end_time] #player always looking for a match
    
    

