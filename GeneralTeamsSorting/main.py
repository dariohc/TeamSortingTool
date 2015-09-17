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
total = 14
calendar = []
pairings = []
games = int(total) // 2
weeks = total - 1
playing = []
 
# for k in range(0,weeks+1):
# calendar.append(k)


def print_list(calendar):
    print ('......')
    for k in range(0, len(calendar)):
        print(calendar[k])
    print('.....')

def check_team(aux_list):
    if (aux_list[0] in playing) or (aux_list[1] in playing):
        return True
    else:
        return False #returns  #returns True if 1 team playing
def add_playing(aux_list):
    if aux_list[0] not in playing:
        playing.append(aux_list[0])
    if aux_list[1] not in playing:
        playing.append(aux_list[1])                   
    
#create all pairings
for i in range(0, total):
    for j in range (0,total):
        if i!=j and i<j :
            pairings.append([i,j])
print_list(pairings)     
print (len(pairings))

print_list(calendar)
random.shuffle(pairings)
print_list(pairings) 
#now we have al matches to be played
#for weeks in range (0,weeks+1):
counter_games = 0
counter_week = 0
backup_pairings = pairings
while len(pairings) >= 1:   
    if (counter_week % total) == 0:
        print('restart')
        pairings = backup_pairings
        random.shuffle(pairings)
        playing = []
        counter_games = 0
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
    #print (calendar)  
    for element in calendar:
        if element in pairings: pairings.remove(element)
    print (len(pairings)) 
    #print (pairings)
    counter_week += 1
    print(counter_week)
    

print_list(calendar)
print(len(calendar))

check_games = []
print (games, weeks)
for i in range(0,weeks):
    print ('>>>>',i+1)
    for j in range(0,games):
        print (calendar[j+i*games])
        check_games.append(calendar[j+i*games][0])
        check_games.append(calendar[j+i*games][1])

total_loop = 0
games_counter = 0
for i in range(1,total):
        for k in check_games:
            if check_games[k] == i :
                games_counter+=1    
            total_loop +=1    
            if games_counter > 1 and total_loop < 7: print (i, 'team is NOK')
            if total_loop == 7 : 
                total_loop = 0
                games_counter = 0