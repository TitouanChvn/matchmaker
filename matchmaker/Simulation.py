import Player
import Match1v1
import Timeline
import random as rd


def main():
    print("Creating timeline...")
    #create timeline
    timeline = Timeline.Timeline()
    #ask for end time
    time = input("Enter Timeline end time (for infinite type -1): ")
    try :
        timeline.define_end_time(int(time))
        print("Timeline end time set to "+str(time))
    except ValueError:
        print("Error, End time set to infinite")
    #create players :
    print("Creating players...")
    number_of_players = input("Enter number of players : ")
    elo_min = input("Enter minimum elo : ")
    elo_max = input("Enter maximum elo : ")
    for i in range(int(number_of_players)):
        new_player = Player.Player(i, rd.randint(int(elo_min), int(elo_max)))
        new_player.add_to_timeline(timeline)


    while(timeline.tick()):
        #print(timeline)
        #print(timeline.players_waiting)
        #print(timeline.players_playing)
        #print(timeline.ongoing_matches)
        pass
    return True


if __name__ == "__main__":
    main()