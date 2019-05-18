from random import randint

game_running = True

def monster_atk():
    return randint(monster['attack_min'], monster['attack_max'])
def player_atk():
    return randint(player['attack_min'], player['attack_max'])
while game_running == True:
    new_round = True
    player = {'name': 'Cloud', 'attack_min': 10, 'attack_max' :15,'magic': 25, 'magic_cost':7, 'heal': 50, 'health': 100, 'mp':30}
    monster = {'name': 'Imp', 'attack_min': 14, 'attack_max': 20, 'health': 160}


    while new_round == True:

        player_won = False
        monster_won = False

        print('---' * 7)
        print('Select an action')
        print('1) Attack')
        print('2) Magic')
        print('3) Heal')
        print('4) Exit')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player_atk()
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster_atk()
                if player['health'] <= 0:
                    monster_won = True
        elif player_choice == '2':
            if player['mp'] >= 7:
                player['mp'] = player['mp'] - player['magic_cost']
                monster['health'] = monster['health'] - player['magic']
                if monster['health'] <= 0:
                    player_won == True
                else:
                    player['health'] = player['health'] - monster_atk()
                    if player['health'] <= 0:
                        monster_won = True
            else:
                print("Not Enough MP")
        elif player_choice == '3':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - monster_atk()
            if player['health'] <= 0:
                monster_won == True
        elif player_choice == '4':
            game_running = False
            new_round = False
        else:
            print("Invalid Input")

        if player_won == False and monster_won == False:
            print('---' * 7)
            print(monster['name'] + " HP = " + str(monster['health']))
            print('---' * 7)
            print(player['name'] + " HP = " + str(player['health']))
            print("\t  MP = " + str(player['mp']))
        if monster_won == True:
            new_round = False
            print("Game Over")
        elif player_won == True:
            new_round = False
            print("You Win")
