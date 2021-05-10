from OSRSBytes import Hiscores
import pandas as pd
import os
import json

def load_player(player_name):
    try:
        return Hiscores(player_name).stats
    except :
        print("    {} - player not found".format(player_name))
        return {}


def store_file(data):
    data_out = json.dumps(data)
    file = open('database.json', 'w')
    file.write(data_out)
    file.close()


playerlist = os.listdir('../runelite/outputs/players/')
playerlist = map(lambda l: l.split('.json')[0], playerlist)
# playerlist = ['bambinoh', 'daleksupr']
players = []

savefail = 25
counter = 0

for p in playerlist:
    counter += 1
    stats = load_player(p)
    players.append(stats)

    if ((counter % savefail) == 0):
        print("Now stored {} entries".format(counter))
        store_file(players)

store_file(players)

