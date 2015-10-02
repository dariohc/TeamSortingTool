'''
Created on 8 Sep 2015
modified
@author: Dario Hermida
Taken a 'total' of teams, it is created a 'calendar' with all the matches to be played
during a whole 1 round league. Matches are evenly distributed to have all teams playing
the same amount of early and late games.
'''

import random

# variables
total = 14  # it works fine for even numbers. For odd numbers just use one more team to rest.
calendar = []  # it will contain the final calendar with [team A, team B] display.
pairings = []  # initial list containing all matches to be played
games = int(total) // 2  # games to be played during a week
weeks = total - 1  # Enough weeks to play all matches
playing = []
position = 0
games_week = 0  # used for presentation of the calendar
games_day = 0  # used for presentation
total_games_inserted = 0
teams_names = []  # used for storing the real name of the teams
early_limit = games // 2  # maximum allowed games to be played at early schedule
early_limit_weeks = total // 2  # maximum allowed weeks to be played at early schedule
late_limit = games - early_limit
late_limit_weeks = total - late_limit
early_total = total  # total teams playing at early schedule
late_total = total
max_early = 0  # maximum games played by a team at early schedule, looping purposes
max_late = 0
adjusting_parameter = 0  # used to improve random nature of searching best solution
max_iterations = 1000  # used to limit the search of the best calendar
counter_games = 0
counter_week = 0


def print_list(aux_list):
    '''
    :param aux_list:
    :return:
    '''
    print('...printing list...')
    if len(aux_list) == 0:
        print('this list is empty')
    for k in range(0, len(aux_list)):
        print(aux_list[k])
    print('.....')


def insert_team(current_game):
    # returns True if there is a game
    # print_list(calendar)
    global calendar, games_week, games_day, total_games_inserted
    game_match = False
    game_inserted = False
    games_day = 0
    games_week_attempts = 0
    # print(current_game, 'this is my current game')
    while games_week_attempts < weeks or (game_inserted == False):
        while games_day < games:
            # print('this is my current game', current_game)
            # print('this is my comparison game', calendar[games_week][games_day])
            if ((current_game[0] == calendar[games_week][games_day][0]) or
                (current_game[0] == calendar[games_week][games_day][1]) or
                (current_game[1] == calendar[games_week][games_day][0]) or
                    (current_game[1] == calendar[games_week][games_day][1])) and (game_match == False):
                # print('there is a match')
                game_match = True
                # print(games_week, games_day, 'this is the current position')
            if (game_match == False) and (games_day == games - 1) and (game_inserted == False):
                calendar[games_week].remove([total+1, total+1])
                calendar[games_week].append(search)
                game_inserted = True
                games_week += 1
                games_week %= weeks
                # print("added")
                total_games_inserted += 1
            games_day += 1
            # print('currently checking', games_week, games_day)
        # print_list(calendar)
        game_match = False
        # input('we are on the loop')
        # print('we are on the week', games_week)
        if game_inserted == False:
            games_week += 1
            games_week %= weeks
        games_week_attempts += 1
        games_day = 0


def add_playing(aux_list):
    if aux_list[0] not in playing:
        playing.append(aux_list[0])
    if aux_list[1] not in playing:
        playing.append(aux_list[1])                   
    
# create all pairings


def initialize_calendar():

    global calendar
    for i in range(0, weeks):
            filling = [total+1, total+1]
            calendar.append(filling)
    for i in range(0, weeks):
        for j in range(0, games):
            filling = [total+1, total+1]
            calendar[i].append(filling)
    for i in range(0, weeks):
            calendar[i].remove(total+1)
            calendar[i].remove(total+1)


def verify_calendar():
    current_verify = []
    global calendar, weeks, games
    # print('Im doing verification')
    for weeks_verif in range(0, weeks):
        for games_verif in range(0, games):
            current_verify.append(calendar[weeks_verif][games_verif][0])
            current_verify.append(calendar[weeks_verif][games_verif][1])
        # print('verifying this list', current_verify)
        current_verify.sort()
        for k in range(0, total):
            # print(current_verify.count(k), 'the count for', k)
            if current_verify.count(k) > 1 or (current_verify.count(total + 1) > 1):
                return 'there is a problem with the calendar'
        current_verify = []


def compile_team_names():
    global teams_names
    for k in range(0, total):
        print('set the name for team', k+1)
        team_name = input('name:')
        teams_names.append(team_name)


def apply_team_names():
    global calendar, teams_names, games, weeks
    for current_week in range(0, weeks):
        for current_game in range(0, games):
            calendar[current_week][current_game][0] = teams_names[calendar[current_week][current_game][0]]
            calendar[current_week][current_game][1] = teams_names[calendar[current_week][current_game][1]]
    # print_list(calendar)


def present_full_calendar():
    global calendar, weeks, games
    # counter_week = 0
    # counter_games = 0
    for current_week in range(0, weeks):
        print('Games for the week', current_week)
        for current_game in range(0, games):
            print(current_game, '-', calendar[current_week][current_game])


def present_players():
    global calendar, games, weeks, early_limit, early_limit_weeks, late_limit_weeks, max_early, max_late
    early_list = []
    late_list = []
    early_total = 0
    late_total = 0
    max_early = 0
    max_late = 0
    for current_week in range(0, weeks):
        for current_game in range(0, early_limit):
            early_list.append(calendar[current_week][current_game][0])
            early_list.append(calendar[current_week][current_game][1])
    # print('this is early_list', early_list)
    for team in range(0, total):
        if early_list.count(team) > early_limit_weeks:
            print(team, 'this team is playing too Early', 'total of', early_list.count(team), 'times')
            early_total += 1
            if early_list.count(team) > max_early:
                max_early = early_list.count(team)
    # this will be for the late players
    for current_week in range(0, weeks):
        for current_game in range(early_limit, games):
            late_list.append(calendar[current_week][current_game][0])
            late_list.append(calendar[current_week][current_game][1])
    # print('this is my late_list', late_list)
    for team in range(0, total):
        if late_list.count(team) > late_limit_weeks:
            print(team, 'this team is playing too Late', 'total of', late_list.count(team), 'times')
            late_total += 1
            if late_list.count(team) > max_late:
                max_late = late_list.count(team)
    # print('--this is early total method', early_total)
    # print('--this is late total', late_total)
    return max_early, max_late


def shuffle_calendar():
    global calendar, weeks
    for current_week in range(0, weeks):
        random.shuffle(calendar[current_week])


def compensate_calendar():
    global max_early, max_late, early_limit_weeks, late_limit_weeks, adjusting_parameter, max_iterations
    current_iterations = 0
    while ((max_early > (early_limit_weeks + adjusting_parameter)) or \
            (max_late > (late_limit_weeks + adjusting_parameter))) and current_iterations < max_iterations:
        shuffle_calendar()
        # print_list(calendar)
        max_early, max_late = present_players()
        print('checking max_early and max_late', max_early, max_late)
        current_iterations += 1


def perfect_calendar():
    global max_early, max_late, early_limit_weeks, late_limit_weeks, adjusting_parameter, max_iterations
    current_iterations = 0
    while ((max_early != 0) or (max_late != 0)) and current_iterations < max_iterations:
        shuffle_calendar()
        # print_list(calendar)
        max_early, max_late = present_players()
        print('checking max_early and max_late', max_early, max_late)
        current_iterations += 1


for i in range(0, total):
        for j in range(0, total):
            if i != j and i < j:
                pairings.append([i, j])
initialize_calendar()
while len(pairings) > total_games_inserted:
    for search in pairings:
        insert_team(search)  # we iterate over the whole list of pairings
early_total, late_total = present_players()
# compensate_calendar()
perfect_calendar()
print('*****')
print('*****This should be your calendar')
print_list(calendar)
print(len(calendar))
verify_calendar()
present_players()
print('calendar done')
compile_team_names()
apply_team_names()
present_full_calendar()
