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
 
# for k in range(0,weeks+1):
# calendar.append(k)


def print_list(aux_list):
    print('...printing list...')
    if len(aux_list) == 0:
        print('this list is empty')
    for k in range(0, len(aux_list)):
        print(aux_list[k])
    print('.....')


def check_team(aux_list):
    # returns True if there is a game
    if (aux_list[0] in playing) or (aux_list[1] in playing):
        return True
    else:
        return False


def add_playing(aux_list):
    if aux_list[0] not in playing:
        playing.append(aux_list[0])
    if aux_list[1] not in playing:
        playing.append(aux_list[1])                   
    
# create all pairings


for i in range(0, total):
    for j in range(0, total):
        if i != j and i < j:
            pairings.append([i, j])
print('this is my pairings list')
print_list(pairings)     
print(len(pairings))

# now we have al matches to be played
# for weeks in range (0,weeks+1):
counter_games = 0
counter_week = 0
backup_pairings = pairings
while len(pairings) >= 1:
    for search in pairings:
        if check_team(search):
            continue
        else:
            calendar.append(search)
            add_playing(search)
            print ("added")
            counter_games += 1
            if counter_games%(total/2) == 0:
                playing = []
                counter_games = 0
                counter_week += 1
    # print(calendar)
    for element in calendar:
        if element in pairings:
            pairings.remove(element)
    print(len(pairings))
    # print(pairings)
    counter_week += 1
    print(counter_week)

print_list(calendar)
print(len(calendar))
check_games = []
print(games, weeks)
