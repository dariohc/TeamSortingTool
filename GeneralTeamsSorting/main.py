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
total = 6
calendar = []
pairings = []
games = int(total) // 2
weeks = total - 1
playing = []
position = 0
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
    print_list(calendar)
    print(position)
    global position
    attempts = 0
    print(current_game, 'this is my current game')
    while attempts < weeks:
        for ka in range(0, games):
            if ((current_game[0] == calendar[position][ka][0]) or (current_game[0] == calendar[position][ka][1]) or
               (current_game[1] == calendar[position][ka][0]) or (current_game[1] == calendar[position][ka][1])):
                print('there is a match')
                position += 1
                position %= 5
                attempts += 1
                print(position, 'this is the position')
                continue
            else:
                calendar[position][ka] = search
                print("added")
                return
        print_list(calendar)
        position += 1
        position %= 5
        attempts += 1
        input('we are on the loop')


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

for i in range(0, total):
        for j in range(0, total):
            if i != j and i < j:
                pairings.append([i, j])
initialize_calendar()

print('this is my pairings list')
print_list(pairings)     
print(len(pairings))
print_list(calendar)

# now we have al matches to be played
# for weeks in range (0,weeks+1):
counter_games = 0
counter_week = 0
backup_pairings = pairings
input('please press a button')
while len(pairings) >= 1:
    for search in pairings:
        insert_team(search)  # we iterate over the whole list of pairings
    input('please press a button')

print_list(calendar)
print(len(calendar))
check_games = []
print(games, weeks)
