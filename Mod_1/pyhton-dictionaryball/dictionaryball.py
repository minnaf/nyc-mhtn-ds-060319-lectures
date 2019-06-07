game_dictionary = {'home': {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players': {'Alan Anderson': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 22,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 1
                                        },
                                        'Reggie Evans': {
                                            'number': 30,
                                            'shoe': 14,
                                            'points': 12,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 12,
                                            'blocks': 12,
                                            'slam_dunks': 7
                                        },
                                        'Brook Lopez': {
                                            'number': 11,
                                            'shoe': 17,
                                            'points': 17,
                                            'rebounds': 19,
                                            'assists': 10,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 15
                                        },
                                        'Mason Plumlee': {
                                            'number': 1,
                                            'shoe': 19,
                                            'points': 26,
                                            'rebounds': 12,
                                            'assists': 6,
                                            'steals': 3,
                                            'blocks': 8,
                                            'slam_dunks': 5
                                        },
                                        'Jason Terry': {
                                            'number': 31,
                                            'shoe': 15,
                                            'points': 19,
                                            'rebounds': 2,
                                            'assists': 2,
                                            'steals': 4,
                                            'blocks': 11,
                                            'slam_dunks': 1
                                        }
                                        }},
                    'away': {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players': {'Jeff Adrien': {
                                            'number': 4,
                                            'shoe': 18,
                                            'points': 10,
                                            'rebounds': 1,
                                            'assists': 1,
                                            'steals': 2,
                                            'blocks': 7,
                                            'slam_dunks': 2
                                        },
                                        'Bismak Biyombo': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 12,
                                            'rebounds': 4,
                                            'assists': 7,
                                            'steals': 7,
                                            'blocks': 15,
                                            'slam_dunks': 10
                                        },
                                        'DeSagna Diop': {
                                            'number': 2,
                                            'shoe': 14,
                                            'points': 24,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 4,
                                            'blocks': 5,
                                            'slam_dunks': 5
                                        },
                                        'Ben Gordon': {
                                            'number': 8,
                                            'shoe': 15,
                                            'points': 33,
                                            'rebounds': 3,
                                            'assists': 2,
                                            'steals': 1,
                                            'blocks': 1,
                                            'slam_dunks': 0
                                        },
                                        'Brendan Haywood': {
                                            'number': 33,
                                            'shoe': 15,
                                            'points': 6,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 22,
                                            'blocks': 5,
                                            'slam_dunks': 12
                                        }}}}



def game_dict():
    return game_dictionary


def num_points_scored(name):
    for location, team_stats in game_dict().items():
        for stats, data in team_stats.items(): 
                for item in data:
                    if item == name:
                        return game_dict()[location][stats][item]['points']
                                
def shoe_size(name):
    for location, team_stats in game_dict().items():
        for stats, data in team_stats.items(): 
                for item in data:
                    if item == name:
                        return game_dict()[location][stats][item]['shoe']      
    
def team_colors(team_name):
    for location, team_stats in game_dict().items():
        for stats, data in team_stats.items(): 
            #print(data)
            if data == team_name:
                return (game_dict()[location]['colors'])
        
def team_names():
    for location, team_stats in game_dict().items():
         return (game_dict()[location]['team_name'])

def player_numbers(team_name):
    jersey_numbers = []
    for location, team_stats in game_dict().items():
        if game_dict()[location]['team_name'] == team_name:
            for player, player_stats in game_dict()[location]['players'].items():
                jersey_numbers.append(player_stats['number'])       
    return jersey_numbers


def player_stats(name):
    for location, team_stats in game_dict().items():
        for stats, data in team_stats.items(): 
                for item in data:
                    if item == name:
                        return game_dict()[location][stats][item]  

def big_shoe_rebounds():
    player_shoe_size = []
    for location, team_stats in game_dict().items():
            for players, player_stats in game_dict()[location]['players'].items():
                player_shoe_size.append(player_stats['shoe'])
                
    max_shoe = max(player_shoe_size)

    for location, team_stats in game_dict().items():
            for players, player_stats in game_dict()[location]['players'].items():
                if player_stats['shoe'] == max_shoe:
                    return "{} has the biggest shoe size and {} rebounds".format(players, player_stats['rebounds'])
    
#Bonus Problems 
    
def most_points_scored():
    player_max_points = []
    for location, team_stats in game_dict().items():
            for players, player_stats in game_dict()[location]['players'].items():
                player_max_points.append(player_stats['points'])
                
    max_point = max(player_max_points)
    
    for location, team_stats in game_dict().items():
            for players, player_stats in game_dict()[location]['players'].items():
                if player_stats['points'] == max_point:
                    return "{} has the max points with {} points".format(players, player_stats['points'])

                
                
def winning_team():
    team_1 = []
    team_2 = []
    
    for location, team_stats in game_dict().items():
        if location == 'home':
            for player, player_stats in game_dict()[location]['players'].items():
                team_1.append(player_stats['points']) 
               
    for location, team_stats in game_dict().items():
        if location == 'away':
            for player, player_stats in game_dict()[location]['players'].items():
                team_2.append(player_stats['points'])              
                
    team_1 = sum(team_1)  
    team_2 = sum(team_2)
    
    if team_1 > team_2:
        return "team_1 won with {} points".format(team_1)
    
    elif team_1 == team_2:
        return "the two teams tied with {} points".format(team_1)
    
    else:
        return "team_2 won with {} points".format(team_2)
    
    
def player_with_longest_name():
    list_of_names = []
    for location, team_stats in game_dict().items():
            for player, player_stats in game_dict()[location]['players'].items():
                list_of_names.append(player)
                
    return max(list_of_names, key=len)
        
                
                    
                    