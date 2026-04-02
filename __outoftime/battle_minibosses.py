import random


# def battle(player, boss):
#     while player.health > 0 or boss.health > 0:
#         print(f"The Boss health is {boss.health}\n")
#         print(f"Your health is {player.health} and your defense is {player.defense}")
#         boss_options = []
#         for value in boss.damage.values():
#             boss_options.append(value) 
#         boss_choice = int(random.choice(boss_options))
#         if player.defense > 1:
#             player.defense -= boss_choice
#         else:
#             player.defense = 0
#             player.take_damage(boss_choice)
#         print(f"The Boss has done {boss_choice} damage to you\n")
#         print(f"Your new health is {player.health} and defense is {player.defense}\n")
#         print("You can:")
#         for attack in player.inventory:
#             if attack.damage != 0:
#                 print(f"Use your {attack.name} to {attack.damage} damage")
#             if attack.defense != 0:
#                 print(f"Or use {attack.name} to increase defense {attack.defense}")
#         player_choice = (input("What would you like to do: ")).lower()
#         for attack in player.inventory:
#             if player_choice == attack.name:
#                 boss.boss_take_damage(attack.damage) 
#         print(f"Boss health is {boss.health}\n")
#     else:
#         print("Invalid Input, Please enter a valid input")

#     if player.health == 0:
#         print("You have died")
#     else:
#         print("The enemy has died")


def battle(player, boss):
    print(f"The {boss.name}s' health is {boss.health}\n")
    print(f"Your health is {player.health} and your defense is {player.defense}\n")
    while player.health > 0 or boss.health > 0:
        print("You can attack using:")
        for attack in player.inventory:
            if attack.damage != 0:
                print(f"Use your {attack.name.capitalize()} to {attack.damage} damage")
        print("You can defend using:")
        for attack in player.inventory:
            if attack.defense != 0:
                print(f"Or use {attack.name.capitalize()} to increase defense {attack.defense}")
        print("You can heal using:")
        for attack in player.inventory:
            if attack.health != 0:
                print(f"Or use {attack.name} to increase health by {attack.health}")
        player_choice = (input("What would you like to do: ")).lower()
        valid_attack = False
        for attack in player.inventory:
            if player_choice == attack.name and attack.uses > 0:
                boss.boss_take_damage(attack.damage)
                player.add_defense(attack.defense)
                player.heal_health(attack.health)
                attack.uses -= 1
                valid_attack = True
                if attack.uses == 0:
                    player.inventory.remove(attack)
        if valid_attack == False:
            print("Invalid input, Please enter a listed attack and only use the name of the attack")
        boss_options = []
        for value in boss.damage.values():
            boss_options.append(value) 
        boss_choice = int(random.choice(boss_options))
        if player.defense > 1:
            damage_done = boss_choice - player.defense
            print(f"Your defense for this round is {player.defense}\n")
            if damage_done > 1:
                player.take_damage(damage_done)
                player.defense = 5
                print(f"The Boss has done {damage_done} damage to you.\n")
            if damage_done < 1:
                print("You blocked the attack")
                player.defense = 5
        if player.health:
            print(f"Your new health is {player.health} and defense is {player.defense}\n")
        if boss.health > 1:
            print(f"The {boss.name}s' health is {boss.health}\n")
        if player.health < 0:
            print("You have died")
            return
        if boss.health < 0:
            print("The enemy has died")
            return











            


