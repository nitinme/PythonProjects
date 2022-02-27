#Imports
import random as r
import sys as s
#Attacks List
attacks = ['Punch', 'Kick', 'Bomb', 'Blast']
#Game Tutorial
print('In this game you will fight against a bot and see who can survive the longest in four moves!')
print('------------------------')
print('Here are the attack options:')
print(attacks)
print('------------------------')
#Name Creation
name = input('What is your Username?')
bossname = input("What is the Boss' name?")

#Creating health bars
bosshealth = 400
userhealth = 400

#User's first attack
attack1 = input('What is your first move?')
if attack1 == 'Blast' or 'blast':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 50
    print(name, 'Played', attack1)
    print(bossname, 'health is now: ', bosshealth)
    print(name, 'health is now', userhealth)
    
elif attack1 == 'punch' or 'Punch':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 10
    print(name, 'Played', attack1)
    print(bossname, 'Health is now: ', bosshealth)
    print(name, 'health is now: ', userhealth)
elif attack1 == 'Kick' or 'kick':
    bosshealth = bosshealth - 75
    userhealth = userhealth - 5
    print(name, 'Played: ', attack1)
    print(name, 'health is now: ', userhealth)
    print(bossname, 'health is now: ', bosshealth)
elif attack1 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(name, 'Played: ', attack1)
    print(name, 'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
#AI's First attack
botattack1 = r.choice(attacks)
if botattack1 == 'Blast' or 'blast':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 100
    print(bossname, 'Played', botattack1)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif botattack1 == 'punch' or 'Punch':
    bosshealth = bosshealth - 10
    userhealth = userhealth - 50
    print(bossname, 'Played: ', botattack1)
    print(bossname,'Health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif botattack1 == 'Kick' or 'kick':
    bosshealth = bosshealth - 5
    userhealth = userhealth - 75
    print(bossname, 'Played: ', botattack1)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
elif botattack1 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(bossname, 'Played: ', botattack1)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
#User's second attack
attack2 = input('What is your next attack?')
if attack2 == 'Blast' or 'blast':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 50
    print(name, 'Played', attack2)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif attack2 == 'punch' or 'Punch':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 10
    print(name, 'Played', attack2)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif attack2 == 'Kick' or 'kick':
    bosshealth = bosshealth - 75
    userhealth = userhealth - 5
    print(name, 'Played: ', attack2)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
elif attack2 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(name, 'Played: ', attack2)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
#AI Attack 2
botattack2 = r.choice(attacks)
if botattack2 == 'Blast' or 'blast':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 100
    print(bossname, 'Played', botattack2)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif botattack2 == 'punch' or 'Punch':
    bosshealth = bosshealth - 10
    userhealth = userhealth - 50
    print(bossname, 'Played: ', botattack2)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif botattack2 == 'Kick' or 'kick':
    bosshealth = bosshealth - 5
    userhealth = userhealth - 75
    print(bossname, 'Played: ', botattack2)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
elif botattack2 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(bossname, 'Played: ', botattack2)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
#User 3rd Attack
attack3 = input('What is your next attack?')
if attack3 == 'Blast' or 'blast':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 50
    print(name, 'Played', attack3)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif attack3 == 'punch' or 'Punch':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 10
    print(name, 'Played', attack3)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif attack3 == 'Kick' or 'kick':
    bosshealth = bosshealth - 75
    userhealth = userhealth - 5
    print(name, 'Played: ', attack3)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
elif attack3 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(name, 'Played: ', attack3)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
#AI 3rd Attack
botattack3= r.choice(attacks)
if botattack3 == 'Blast' or 'blast':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 100
    print(bossname, 'Played', botattack3)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif botattack3 == 'punch' or 'Punch':
    bosshealth = bosshealth - 10
    userhealth = userhealth - 50
    print(bossname, 'Played: ', botattack3)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif botattack3 == 'Kick' or 'kick':
    bosshealth = bosshealth - 5
    userhealth = userhealth - 75
    print(bossname, 'Played: ', botattack3)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
elif botattack3 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(bossname, 'Played: ', botattack3)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
#User final attack
attack4 = input('What is your final attack?')
if attack4 == 'Blast' or 'blast':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 50
    print(name, 'Played', attack4)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif attack4 == 'punch' or 'Punch':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 10
    print(name, 'Played', attack4)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif attack4 == 'Kick' or 'kick':
    bosshealth = bosshealth - 75
    userhealth = userhealth - 5
    print(name, 'Played: ', attack4)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
elif attack4 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(name, 'Played: ', attack4)
    print(name,'health is now: ', userhealth)
    print(bosshealth,'health is now: ', bosshealth)
#AI Final Attack
botattack4 = r.choice(attacks)
if botattack4 == 'Blast' or 'blast':
    bosshealth = bosshealth - 50
    userhealth = userhealth - 100
    print(bossname, 'Played', botattack4)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now', userhealth)
elif botattack4 == 'punch' or 'Punch':
    bosshealth = bosshealth - 10
    userhealth = userhealth - 50
    print(bossname, 'Played: ', botattack4)
    print(bossname,'health is now: ', bosshealth)
    print(name,'health is now: ', userhealth)
elif botattack4 == 'Kick' or 'kick':
    bosshealth = bosshealth - 5
    userhealth = userhealth - 75
    print(bossname, 'Played: ', botattack4)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
elif botattack4 == 'Bomb' or 'bomb':
    bosshealth = bosshealth - 100
    userhealth = userhealth - 90
    print(bossname, 'Played: ', botattack4)
    print(name,'health is now: ', userhealth)
    print(bossname,'health is now: ', bosshealth)
#Final resulting
else:
    print('Error. Try again!')

if bosshealth > userhealth:
    print('You lost. Try again!')
    winorloss = 'Lost'
elif bosshealth == userhealth:
    print('You tied... Wow, thats rare!')
    winorloss = 'Tie'
elif bosshealth < userhealth:
    print('You win! Congratulations!')
    winorloss = 'win'
