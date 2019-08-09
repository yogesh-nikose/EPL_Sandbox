from models_2019 import *
from EPL_table_scrape_2019 import *
from player_stats_scrape_2019 import *
from sqlalchemy import create_engine

def inst_teams():
    teams = final_teams_list(url1)
    teams_list = []
    for item in teams:
        team = Team(position = item['position'], strength = item['strength'], name = item['team']['name'], logo = item['team']['crestUrl'], GP = item['playedGames'], W = item['won'], D = item['draw'], L = item['lost'], points = item['points'], GF = item['goalsFor'], GA = item['goalsAgainst'], GD = item['goalDifference'], player_points = 0, players = [])
        teams_list.append(team)
    return teams_list

def inst_players_and_teams():
    players = final_players_list(player_positions_teams)
    teams = inst_teams()
    players_final = []
    teams_final = []
    # pdb.set_trace()
    for team in teams:
        for item in players:
            if team.name == item['team_name']:
                player = Player(team = team, name = item['name'], position = item['position'], cost = item['cost'], total_points = item['total_points'], roi = item['roi'], pts_per_90m = item['pts_per_90m'], bonus = item['bonus'], red_cards = item['red_cards'], minutes = item['minutes'], status = item['status'], transfers_out = item['transfers_out'], transfers_in = item['transfers_in'])
                team.players.append(player)
                team.player_points += item['total_points']
                players_final.append(player)
                if team not in teams_final:
                    teams_final.append(team)
    return (teams_final, players_final)

team_results = inst_players_and_teams()[0]
player_results = inst_players_and_teams()[1]
