import random
import platform
import os

my_os = platform.system()

class Enemie:
    def __init__(self, input_value):
        self.value = input_value
    
    def __repr__(self):
        return "\nThis enemie has the value of: {}".format(self.value)

class EnemiesTower:
    def __init__(self, input_enemies = []):
        self.enemies = input_enemies

    def __repr__(self):
         return "\nThis is a tower fullfilled of {} enemie/s".format(len(self.enemies))

    def generate_tower(self, total_enemies):
        for enemie in range(0, total_enemies):
            new_enemie = Enemie( random.randint(0,30) )
            self.enemies.append( new_enemie )
    
    def delete_an_enemie(self, enemie):
        deleted_enemie = self.enemies.pop( self.enemies.index(enemie) )
        return "\nThe enemie {} was deleted. Good one!".format(deleted_enemie)

class MainCharacter:
    def __init__(self, input_name = "Unknown Player", input_value = 10):
        self.name = input_name
        self.value = input_value
    
    def __repr__(self):
        return "\nThis is your main character named {} and its goal is to destroy the whole tower of enemies. Its initial value is {}".format(self.name, self.value)

    def destroy_an_enemie(self, enemies_tower, enemie):
        if enemie in enemies_tower.enemies:
            if ( self.value > enemie ):
                self.value += enemie
                return enemies_tower.delete_an_enemie(enemie)
            else:
                return False

# Reading some input from the user
main_character_name = input("\nGive the main character a cool name: ")
main_character_initial_value = 5

total_enemies_integers = [5,1,2,3,10,15,20,35,50]
    
# Creating an instance of EnemiesTower and generating at least 10 enemies
new_enemies_tower = EnemiesTower(total_enemies_integers)

# Creating an instance of my new MainCharacter
new_main_character = MainCharacter(main_character_name, int(main_character_initial_value))

print(new_main_character)
print(new_enemies_tower)

def clear_the_terminal( os_type ):
    if os_type == "Windows":
        os.system("cls")
    elif os_type == "Linux":
        os.system("clear")

def render_characters( main_character, enemies_tower ):
    print("\nCharacter value | Enemies")
    index = 0

    for enemie in enemies_tower.enemies:
        if index < (len(enemies_tower.enemies) - 1):
            print("  {}".format(enemie))
            index += 1
        else:
            print("{} {}".format(main_character.value, enemie))

def start_game( main_character, enemies_tower ):
    print("\nLet's start the game!")
    render_characters( main_character, enemies_tower )
    choose_an_enemie = input("\nSelect an enemie to fight with: ")

    while ( len(enemies_tower.enemies) > 1 ):
        clear_the_terminal( my_os )
        was_enemie_destroyed = main_character.destroy_an_enemie(enemies_tower, int(choose_an_enemie))
        if ( was_enemie_destroyed ):
            print(was_enemie_destroyed)
            render_characters( main_character, enemies_tower )
            choose_an_enemie = input("\nSelect an enemie to fight with: ")
        else:
            print("Oh no! You have selected a more powered enemie than you, your character has been destroyed! No worries, you can try again by running this python program when you're ready.")
            return

    print("\nCongrats! Your character {} has destroyed all of its enemies. You're a real fighter!".format(main_character.name))
    
start_game( new_main_character, new_enemies_tower )