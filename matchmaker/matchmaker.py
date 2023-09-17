import json
import random as rd
import time
import threading


#################### NEW DEMO  ####################

def NewDemo():

    for i in range(3000):
        playerlist.append(Player(get_free_id(), i))
    
    update_json_playerlist()

    start_timer()


def change_random():
    load_json_playerlist()
    while True:
        time.sleep(5)
        #change elo of player 0
        #print(playerlist)
        playerlist[0].elo = rd.randint(0, 1000)
        update_json_playerlist()
        

####################################################

class Player:

    def __init__(self, id, elo):
        self.id = id
        self.elo = elo
    
    def __str__(self):
        return "Player :  Id : " + str(self.id) + " Elo : " + str(self.elo)


playerlist = [] #list of Player objects


class TimeFrame : 
    def __init__(self):
        self.time = 0
        self.players_waiting = []
        self.players_playing = []

    def __str__(self):
        return "Time : " + str(self.time) + "\nPlayers waiting : " + str(self.players_waiting) + "\nPlayers playing : " + str(self.players_playing)



def get_free_id():
    return len(playerlist)

def update_json_playerlist():
    with open('players.json', 'w') as outfile:
        json.dump([ob.__dict__ for ob in playerlist], outfile)
    
def load_json_playerlist():
    global playerlist
    with open('players.json') as json_file:
        data = json.load(json_file)
        for p in data:
            playerlist.append(Player(p['id'], p['elo']))
    print("Loaded json playerlist")
    #print(playerlist)

def start_timer():
    pass
    



if __name__ == "__main__":
    #NewDemo()
    #print(playerlist)
    pass