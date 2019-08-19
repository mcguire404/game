player = {'name': 'Chris', 'attack':12, 'heal':16,'fireball':20, 'health':100}
monster={'name':'Randy', 'attack':14, 'health': 100}

game_running = True

while game_running == True:

  print('Please select one of the following options.')
  print('1) Attack')
  print('2) Heal')
  print('3) Fireball')

  player_choice = input()

  #Combat system Code

  if player_choice == str(1):
    print('Attack!!')
    monster['health'] = monster['health'] - player['attack']
    player['health'] = player['health'] - monster['attack']
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
    print(monster['health'])
  else:
    print('Not a correct command!!')
  #checking to see if either health value less than or equal to 0
  if player['health'] <=0 or monster['health'] <=0:
    game_running = False