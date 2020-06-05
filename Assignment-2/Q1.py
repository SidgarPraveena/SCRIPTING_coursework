#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:28:53 2019

@author: jyoti
"""

import random 

overseasBowler=[]
overseasBatsman=[]
overseasWicketKeeper=[]
overseasAllRounder=[]

indianBowler=[]
indianBatsman=[]
indianWicketKeeper=[]
indianAllRounder=[]

f=open("ipl_dataset.txt")

while True:
    line=f.readline().strip()
    if line == '':
        break
    player_details=line.split(":")
    if player_details[1] == "India" :
        if player_details[2] == "Bowler":
            indianBowler.append(player_details)
        elif player_details[2] == "Batsman":
            indianBatsman.append(player_details)
        elif player_details[2] == "Wicket Keeper":
            indianWicketKeeper.append(player_details)
        elif player_details[2] == "All-Rounder":
            indianAllRounder.append(player_details)
            
    else:
        if player_details[2] == "Bowler":
            overseasBowler.append(player_details)
        elif player_details[2] == "Batsman":
            overseasBatsman.append(player_details)
        elif player_details[2] == "Wicket Keeper":
            overseasWicketKeeper.append(player_details)
        elif player_details[2] == "All-Rounder":
            overseasAllRounder.append(player_details)
            
#print(len(overseasBowler))
#print(len(overseasBatsman))
#print(len(overseasWicketKeeper))
#print(len(overseasAllRounder))
#print(len(indianBowler))
#print(len(indianBatsman))
#print(len(indianWicketKeeper))
#print(len(indianAllRounder))
players_list=[overseasBowler,overseasBatsman,overseasWicketKeeper,overseasAllRounder,indianBowler,indianBatsman,indianWicketKeeper,indianAllRounder]
f1=open("config.txt")

li=f1.readline().split(":");
overseas_min=int(li[1])
overseas_max=int(li[2])

li=f1.readline().split(":");
bowlers_min=int(li[1])
bowlers_max=int(li[2])

li=f1.readline().split(":");
batsmen_min=int(li[1])
batsmen_max=int(li[2])

li=f1.readline().split(":");
wicketkeepers_min=int(li[1])
wicketkeepers_max=int(li[2])

li=f1.readline().split(":");
allrounders_min=int(li[1])
allrounders_max=int(li[2])

teams=f1.readline().split(":")[1]

#print("teams")
#print(teams)
f1.readline()
teams_list=[]
while(True):
    
    line=f1.readline().strip()
    if line == '':
        break
#    print(line)
    teams_list.append(line)
    
#print(teams_list)
#print(overseas_min,overseas_max)

for team_name in teams_list:
    print(team_name)
    file_team=open(team_name,"w")
    while True:    
        flag1=0
        while True:
              
              overseas_bowlers=random.randint(0, min(bowlers_max,len(overseasBowler)))
              #print(overseas_bowlers)
              overseas_batsmen=random.randint(0, min(batsmen_max,len(overseasBatsman)))
              #print(overseas_batsmen)
              overseas_wicketkeepers=random.randint(0, min(wicketkeepers_max,len(overseasWicketKeeper)))
              #print(overseas_wicketkeepers)
              overseas_allrounders=random.randint(0, min(allrounders_max,len(overseasAllRounder)))
             #3print(overseas_allrounders)
              overseas_count = overseas_bowlers+overseas_batsmen+overseas_wicketkeepers+overseas_allrounders
              if overseas_count >= overseas_min and overseas_count <=overseas_max:
                  flag1=1
                  break
              
        req_players=18-overseas_count
        flag2=0
        while True:
             indian_bowlers=random.randint(max(0,bowlers_min-overseas_bowlers), min(bowlers_max-overseas_bowlers,len(indianBowler)))
             #print(indian_bowlers)
             indian_batsmen=random.randint(max(0,batsmen_min-overseas_batsmen), min(batsmen_max-overseas_batsmen,len(indianBatsman)))
             #print(indian_batsmen)
             indian_wicketkeepers=random.randint(max(0,wicketkeepers_min-overseas_wicketkeepers), min(wicketkeepers_max-overseas_wicketkeepers,len(indianWicketKeeper)))
             #print(indian_wicketkeepers)
             indian_allrounders=random.randint(max(0,allrounders_min-overseas_allrounders), min(allrounders_max-overseas_allrounders,len(indianAllRounder)))
             #print(indian_allrounders)
             indian_count = indian_bowlers+indian_batsmen+indian_wicketkeepers+indian_allrounders
             if indian_count == req_players:
                 flag2=1
                 break
        if flag1==1 and flag2 ==1:
            break
    playercount=[overseas_bowlers,overseas_batsmen,overseas_wicketkeepers,overseas_allrounders,indian_bowlers,indian_batsmen,indian_wicketkeepers,indian_allrounders]
    print("playercount")
    for val in playercount:
        print(val)
    mem=1
    for j in range(0,len(playercount)):   
        #print("loop for",j," ",playercount[j])
        for i in range(1,playercount[j]+1):
            file_team.write("Player "+str(mem)+"\n")
            #f.write("Name : ",players_list[j][[0][0])
            file_team.write("Name : "+players_list[j][0][0]+"\n")
            file_team.write("Country : "+players_list[j][0][1]+"\n")
            file_team.write("Ability : "+players_list[j][0][2]+"\n")
            file_team.write("Fees : "+players_list[j][0][3]+"\n")
            mem+=1
            file_team.write("\n"+"\n")
            players_list[j].remove(players_list[j][0])
    file_team.close()
      
#print("overseas count",overseas_count)
#print("overseas bowlers",overseas_bowlers)
#print("overseas batsmen",overseas_batsmen)
#print("overseas wicket",overseas_wicketkeepers)
#print("overseas all rounder",overseas_allrounders)
#print("req count",req_players)
#print("indian bowlers",indian_bowlers)
#print("indian batsmen",indian_batsmen)
#print("indian wicket",indian_wicketkeepers)
#print("indian all rounder",indian_allrounders)
#         
    