import json



#################### NEW DEMO  ####################

def NewDemo():

    for i in range(3000):
        playerlist.append(Player(get_free_id(), i))
    
    update_json_playerlist()



####################################################

class Player:

    def __init__(self, id, elo):
        self.id = id
        self.elo = elo
    
    def __str__(self):
        return "Player :  Id : " + str(self.id) + " Elo : " + str(self.elo)
    

playerlist = [] #list of Player objects

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
    print(playerlist)



if __name__ == "__main__":
    NewDemo()
    print(playerlist)