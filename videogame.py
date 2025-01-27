  
import random

#Global Variables
hp = 100
enemy_hp = 100
stealth = 0
strength = 0
power = 0
healing_potion = 3
game_state = 'name'

#Functions
def name():
    global game_state
    input("Please choose your character's name ")
    game_state = 'choose_class'
    choose_class()

def choose_class():
    global power, stealth, strength
    print("Please choose your character's class")
    print("1. Mage")
    print("2. Rogue")
    print("3. Fighter")
    group = input("Enter the number of your choice ").strip()
    if group == "1":
        power += 20
        start()
    elif group == "2":
        stealth += 20
        start()
    elif group == "3":
        strength += 20
        start()
    else:
        print("Try again!")
        choose_class()

def return_to_state():
    global game_state
    if game_state == "village":
        village()
    elif game_state == "blacksmith":
        blacksmith()
    elif game_state == "herbalist":
        herbalist()
    elif game_state == "forest":
        forest()
    elif game_state == "footprints":
        footprints()
    elif game_state == "river":
        river()
    elif game_state == "victory":
        victory()
    else:
        print("Error: Unknown state!")
        start()

def win_lose():
    global hp, enemy_hp
    if hp >0 and enemy_hp == 0:
        print("You win!")
        reset()
        return_to_state()
    elif hp==0 and enemy_hp>0:
        print("You lose! Game over!")
        name()
    elif hp==0 and enemy_hp==0:
        print("You win, but at the cost of your own life! Game over!")
        name()
    else:
        attack()

def attack():
    global hp, enemy_hp
    print("Your hp: " + str(hp))
    print("Enemy hp: " + str(enemy_hp))
    print("Choose your move!")
    print("1. Attack")
    print("2. Heal")
    print("3. Run away!")
    choice = input("Enter the number of your choice ").strip()
    if choice == "1":
        fight()
    elif choice == "2":
        heal()
    elif choice == "3":
        run_away()
    else:
        print("Try again!")
        attack()

def fight():
    global hp, enemy_hp, power, strength, stealth
    random_number = random.randint(1, 9)
    if random_number in [1, 3, 5]:
        print("The enemy does 40 damage!")
        hp = max(0, hp - 40)
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()
    elif random_number in [2, 4, 6] and stealth==20:
        print("The enemy attack misses!")
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()
    elif random_number in [7, 8, 9]:
        print("You do 40 damage!")
        enemy_hp = max(0, enemy_hp - 40)
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()
    elif random_number in [2, 4, 6] and strength==20:
        print("You do 70 damage!")
        enemy_hp = max(0, enemy_hp - 70)
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()
    elif random_number in [2, 4, 6] and power==20:
        print("You do 70 damage!")
        enemy_hp = max(0, enemy_hp - 70)
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()
    else:
        print("Attack misses!")
        print("Your hp: " + str(hp))
        print("Enemy hp: " + str(enemy_hp))
        win_lose()

def heal():
    global hp, enemy_hp, healing_potion
    random_number = random.randint(1, 9)
    if random_number == "1" or "3" or "5" and healing_potion >=3:
        print("You use one healing potion!")
        healing_potion -=1
        print("You have " + str(healing_potion) + " potions remaining")
        hp = min(100, hp + 50)
        print("Your hp: " + str(hp))
        win_lose()
    elif random_number == "2" or "4" or "6" and healing_potion >=3:
        print("Your healing potion was only partly effective!")
        healing_potion -=1
        print("You have " + str(healing_potion) + " potions remaining")
        hp = min(100, hp + 25)
        print("Your hp" + str(hp))
        win_lose()
    elif random_number == "7" or "8" or "9" and healing_potion >=3:
        print("Your wounds are too great! Healing potion fails!")
        print("Your hp" + str(hp))
        win_lose()
    else:
        print("You have no healing potions remaining!")
        print("Your hp" + str(hp))
        win_lose()

def run_away():
    global game_state
    random_number = random.randint(1, 9)
    if random_number in [1, 4, 7, 9]:
        print("Success!")
        return_to_state()
    else:
        print("Escape failed!")
        win_lose()

def reset():
    global enemy_hp
    enemy_hp = 100

def start():
    global game_state
    game_state = 'village'
    print("You arrive at Grimhollow, a village plagued")
    print ("by a strange curse. The crops have withered,")
    print ("and villagers avoid your gaze.")
    print("Elder Myra, the frail village elder,")
    print("approaches you with desperation in her eyes.")
    print("1. Agree to help the village.")
    print("2. Refuse and leave.")

    choice = input("What do you do? ").strip()

    if choice == "1":
        village()
    elif choice == "2":
        print("A scream echoes through the village.")
        print("You realise your mistake as a cursed villager races towards you!")
        reset()
        attack()
    else:
        print("Invalid choice. Try again.")
        start()


def village():
    global game_state
    game_state = 'village'
    print("Elder Myra tells you about the Oathstone,")
    print ("a relic stolen from the village's altar.") 
    print ("She suspects Aldric, a hermit herbalist.")
    print("You have two leads:")
    print("1. Visit the blacksmith Roland.")
    print("2. Confront Aldric directly.")
    
    choice = input("Where do you go? ").strip()
    if choice == "1":
        blacksmith()
    elif choice == "2":
        herbalist()
    else:
        print("Invalid choice. Try again.")
        village()

def blacksmith():
    global game_state
    game_state = 'blacksmith'
    print("You find Roland, the blacksmith, hammering")
    print("away at a dull sword. He looks up, wary")
    print("of your approach.")
    print("1. Ask about the Oathstone.")
    print("2. Demand answers forcefully.")
    
    choice = input("What do you do? ").strip()
    if choice == "1":
        print("Roland admits he doesn't trust Aldric,")
        print("but hints at a secret cave in the forest.")
        forest()
    elif choice == "2":
        print("Roland grows hostile and attacks!")
        reset()
        attack()
    else:
        print("Invalid choice. Try again.")
        blacksmith()

def herbalist():
    global game_state
    game_state = 'herbalist'
    print("You arrive at Aldric's hut, surrounded by")
    print("strange herbs and bottles. He looks startled to see you.")
    print("1. Accuse him of stealing the Oathstone.")
    print("2. Ask him for help with the curse.")
    
    choice = input("What do you do? ").strip()
    if choice == "1":
        print("Aldric grows hostile and attacks!.")
        reset()
        attack()
    elif choice == "2":
        print("Aldric tells you he has seen strange lights in the forest")
        forest()
    else:
        print("Invalid choice. Try again.")
        herbalist()

def forest():
    global game_state
    game_state = 'forest'
    print("You enter the dark forest. The air feels heavy,")
    print("and shadows dance between the trees.")
    print("1. Follow a set of footprints.")
    print("2. Head toward the sound of rushing water.")
    
    choice = input("What do you do? ").strip()
    if choice == "1":
        footprints()
    elif choice == "2":
        river()
    else:
        print("Invalid choice. Try again.")
        forest()

def footprints():
    global game_state
    game_state = 'footprints'
    print("You follow the footprints to a hidden cave")
    print("and discover Roland inside, holding the")
    print("stolen Oathstone!")
    print("1. Fight Roland to retrieve the Oathstone.")
    print("2. Try to reason with Roland.")
    
    choice = input("What do you do? ").strip()
    if choice == "1":
       reset()
       attack()
    elif choice == "2":
        print("Roland confesses that he stole the Oathstone") 
        print("out of desperation. You convince him to return")
        print("it and redeem himself.")
        victory()
    else:
        print("Invalid choice. Try again.")
        footprints()

def river():
    global game_state
    game_state = 'river'
    print("You follow the sound of water but are") 
    print("ambushed by cursed villagers.")
    reset()
    attack()
    forest()

def victory():
    global game_state
    game_state = 'victory'
    print("With the Oathstone returned to its altar,")
    print("the curse is lifted. The villagers are free!")
    print("Congratulations!")
    name()

#Game
print('Welcome to The Shattered Oath!')

print("A small, isolated village called Grimhollow,")
print("nestled at the edge of an ancient forest.")
print("Recently, strange happenings, like crops")
print("wilting overnight and eerie howls at dusk,")
print("have unsettled the villagers.")

name()
