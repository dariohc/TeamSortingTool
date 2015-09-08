'''
Created on 8 Sep 2015

@author: Dario Hermida
'''
#it works only for 2**k (4,8,16,32, teams due to the sorting algorithm.
#script to generate matches between teams
#it is required to have all matches evenly distributed


#variables
total = 8
calendar = []
pairings = []
games = total / 2
weeks = total - 1
playing = []
 
#for k in range(0,weeks+1):
#    calendar.append(k)

def print_list(calendar):
    print ('......')
    for k in range(0,len(calendar)):
        print (calendar[k])
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
#now we have al matches to be played
#for weeks in range (0,weeks+1):
counter_games = 0
counter_week = 0

while len(pairings) >= total/2:
#while counter_week >= 3 :   
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
    print (calendar)  
    for element in calendar:
        if element in pairings: pairings.remove(element)
    print (len(pairings)) 
    print (pairings)
    counter_week += 1

for i in range(0,weeks):
    for j in range(0,games):
        print (calendar[j+i*games])
    print ('>>>>')