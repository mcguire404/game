
game_running = True
#Checking to see if the game is still running
while game_running == True:
  new_round = True
  player = {'name': 'Chris', 'attack':12, 'heal':16,'fireball':20, 'health':100}
  monster={'name':'Randy', 'attack':14, 'health': 100}

  
  print('----'*7)
  print('Enter player name:')
  player['name'] = input()
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
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <=0:
          player_won = True
        else:
          player['health'] = player['health'] - monster['attack']
          if player['health'] <= 0:
            monster_won = True
        
        print (monster['health'])
        print (player['health'])
    elif player_choice == str(2):
        print('Heal')
        player['health'] = player['health'] + player['heal']
        print(monster['health'])
        print(player['health'])
    elif player_choice == str(3):
        print('Fireball!!')
        monster['health'] = monster['health'] - player['fireball']

        if monster['health'] <= 0:
          player_won = True
        print(monster['health'])

    elif player_choice == str(4):
        new_round = False
        game_running = False
    else:
        print('Not a correct command!!')
    #checking to see if either health value less than or equal to 0
    if player_won == True or monster_won == True:
        new_round = False