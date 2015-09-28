'''
Created on 8 Sep 2015
modified
@author: Dario Hermida
'''
# it works only for 2**k (4,8,16,32, teams due to the sorting algorithm.
# script to generate matches between teams
# it is required to have all matches evenly distributed

import random

# variables
total = 8
calendar = []
pairings = []
games = int(total) // 2
weeks = total - 1
playing = []
position = 0
games_week = 0
games_day = 0
total_games_inserted = 0
teams_names = []
early_limit = games // 2
early_limit_weeks = weeks // 2
late_limit = games - early_limit
late_limit_weeks = weeks - late_limit
early_total = total
late_total = total
max_early = 0
max_late = 0

# for k in range(0,weeks+1):
# calendar.append(k)


def print_list(aux_list):
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
    for current_week in range(0, weeks):
        for current_game in range(0, early_limit):
            early_list.append(calendar[current_week][current_game][0])
            early_list.append(calendar[current_week][current_game][1])
    for team in range(0, total):
        if early_list.count(team) > early_limit_weeks + 1:
            print(team, 'this team is playing too Early', 'total of', early_list.count(team), 'times')
            early_total += 1
            if early_list.count(team) > max_early:
                max_early = early_list.count(team)

    # this will be for the late players
    for current_week in range(0, weeks):
        for current_game in range(early_limit, games):
            late_list.append(calendar[current_week][current_game][0])
            late_list.append(calendar[current_week][current_game][1])
    for team in range(0, total):
        if late_list.count(team) > early_limit_weeks + 1:
            print(team, 'this team is playing too Late', 'total of', late_list.count(team), 'times')
            late_total += 1
            if late_list.count(team) > max_late:
                max_late = late_list.count(team)
    print('--this is early total method', early_total)
    print('--this is late total', late_total)
    return early_total, late_total


def shuffle_calendar():
    global calendar, weeks
    for current_week in range(0, weeks):
        random.shuffle(calendar[current_week])


for i in range(0, total):
        for j in range(0, total):
            if i != j and i < j:
                pairings.append([i, j])
initialize_calendar()
counter_games = 0
counter_week = 0
while len(pairings) > total_games_inserted:
    for search in pairings:
        # verify_calendar()
        insert_team(search)  # we iterate over the whole list of pairings
    # input('please press a button')
# print('this is just when created:')
early_total, late_total = present_players()
# shuffle_calendar()
# print('this is after the shuffle')
# print_list(calendar)
print('this is my early_total', early_total)
print('this is my early limit_weeks', early_limit_weeks)
adjusting_parameter = 2
while (abs(early_total - late_total) > 2) or ((early_total < early_limit_weeks + adjusting_parameter) and
      (early_total > early_limit_weeks - adjusting_parameter)) or \
      ((late_total < late_limit_weeks + adjusting_parameter) and
      (late_total > early_limit_weeks - adjusting_parameter)) or (max_early > (early_limit_weeks + 2)) or\
      (max_late > (late_limit_weeks + 2)):
    shuffle_calendar()
    print_list(calendar)
    # input('lets continue')
    early_total, late_total = present_players()
    print('checking early_total and late_total', early_total, late_total)
    print('this is condition', abs(early_total - late_total))
print_list(calendar)
print(len(calendar))
verify_calendar()
present_players()
# here should be the place to verify
print('calendar done')
# compile_team_names()
# apply_team_names()
# present_full_calendar()
# present_early_players()