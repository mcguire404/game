from random import randint
game_running = True
#Checking to see if the game is still running
while game_running == True:
  new_round = True
  player = {'name': 'Chris', 'attack_min':13, 'attack_max':30,  'heal':16,'fireball':20, 'health':100}
  monster={'name':'Randy', 'attack_min':10, 'attack_max':20, 'health': 100}

  
  print('----'*7)
  print('Enter player name:')
  player['name'] = input()
  print('----'*7)


  print(player['name'] + ' has ' + str(player['health']) + ' hp')
  print(monster['name'] + ' has ' + str(monster['health']) + ' hp')
  #Checking to see if it is a new round
  while new_round == True:
  
    player_won = False
    monster_won = False


    print('Please select one of the following options.')
    print('1) Attack')
    print('2) Heal')
    print('3) Fireball')
    print('4) Exit Game')

    player_choice = input()

    #Combat system Code

    if player_choice == str(1):
        print('Attack!!')
        player_attack = randint(player['attack_min'], player['attack_max'])
        monster['health'] = monster['health'] - player_attack
        if monster['health'] <=0:
          player_won = True
        else:
          monster_attack = randint(monster['attack_min'], monster['attack_max'])
          player['health'] = player['health'] - monster_attack
          if player['health'] <= 0:
            monster_won = True
        
    elif player_choice == str(2):
        print('Heal')
        player['health'] = player['health'] + player['heal']
        player['health'] = player['health'] - monster_attack
        if player['health'] <= 0:
            monster_won = True
        
    elif player_choice == str(3):
        print('Fireball!!')
        monster['health'] = monster['health'] - player['fireball']

        if monster['health'] <= 0:
          player_won = True

    elif player_choice == str(4):
        new_round = False
        game_running = False
    else:
        print('Not a correct command!!')
    #checking to see if either health value less than or equal to 0

#Checking to see if the player or monster Won!!
    if player_won == False and monster_won == False:
      print(player['name'] + ' has ' + str(player['health']) + ' left')
      print(monster['name'] + ' has ' + str(monster['health']) + ' left')
    elif player_won:
      print(player['name'] + ' has Won!!!')
      new_round = False
    elif monster_won:
      print(player['name'] + ' has Lost...')

    