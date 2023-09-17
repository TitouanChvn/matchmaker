import Player
import Match1v1


class Timeline:

    def __init__(self):
        self.time = 0
        self.end_time = -1 # -1 means infinite
        self.player_pool = []
        self.players_waiting = []
        self.players_playing = []
        self.ongoing_matches = []
    
    def __str__(self):
        return "Time is : "+str(self.time)
    
    def details(self):
        return "Time is : "+str(self.time)+"\nPlayers waiting : "+len(self.players_waiting)+"\nPlayers playing : "+len(self.players_playing)+"\nOngoing matches : "+len(self.ongoing_matches)

    def define_end_time(self, end_time):
        self.end_time = end_time

    def tick(self):
        self.time += 1
        #self.update_players()
        #self.update_matches()
        if self.end_time != -1 and self.time >= self.end_time:
            print("time = "+str(self.time)+" End of Timeline")
            return False
        return True
