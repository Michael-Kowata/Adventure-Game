from player import Player
from monster import Monster
import sys

def main():
    print("Welcome to the adventure game!")
    print("When prompted choose an option to continue the story.")
    name = input("But first what is the protagonist's name? \n")
    protag = Player(name)
    print("-------------------------------------------------------")
    gate(protag)
    intersection(protag)

def gate(protag):
    print ("\nIn front of you stands a gate to dangerous dungeon.")
    print (f"Dungeon Guard: Hello {protag.get_name()}, as punishment for your crimes you were sentenced to scout and map out the area. If you can redeem yourself the council will consider your crimes forgiven.\n")

    while (True):
        print ("-------------------------------------------------------")
        print ("Options:")
        print ("1: What did I do exactly?")
        print ("2: Screw you! (Attack the guard)")
        print ("3: What must I do to redeem myself?")
        print ("Press any key to leave") 
        print ("-------------------------------------------------------")
        Choice = input("\nOption: ")
        
        if Choice == '1':
            print ("You stole and ate the mayor's prized cookie collection of course! Now off you go!\n")
        elif Choice == '2':
            print ("Hey what do you think you are doing! (You lost 2 health!)\n")
            protag.take_damage(2)
            if protag.death_check():
                sys.exit()
            print (f"Current Health: {protag.get_health()}")
        elif Choice == '3':
            print ("There's a growing monster popoluation in this dungeon that is terrorizing the local farmers. Reduce their population and we will pardon your transgression; that is if you manage to even come out alive. Ha ha!\n")
        else:
            print ("You left the gate and walked into the dungeon.\n")
            break  

def intersection(protag):
    print ("You come across an intersection leading 3 different ways, which pathway will you take?")
    
    while (True):
        print ("-------------------------------------------------------")
        print ("Options:")
        print ("1: North path")
        print ("2: East path")
        print ("3: South path (back to the gate)")
        print ("4: West path") 
        print ("5: Read the sign")
        print ("-------------------------------------------------------")
        Choice = input("\nOption: ")
    
        if Choice == '1':
            print ("You continue through north path.\n")
            north(protag)
            break
        elif Choice == '2':
            print ("You decided to check out the east path.\n")
            east(protag)
            break
        elif Choice == '3':
            print ("You went back to the gate.\n")
            gate(protag)
        elif Choice == '4':
            print ("You chose to walk the western path.\n")
            break
        elif Choice == '5':
            print ("You read the sign. It's worn out so it's hard to decipher what it is saying.\n")
            print ("North path -> De  h Val  y")
            print ("East path -> Gr v  of H ro s")
            print ("South path -> S im  Ki gd m")
            print ("West path -> S litu e\n")
        else:
            print ("Invalid option.\n")

def north(protag):
    print ("Walking across the northern path. You see a shiny glowing rock. What do you do?")
    
    while (True):
        print ("-------------------------------------------------------")
        print ("Options:")
        print ("1: Pick it up")
        print ("2: Kick it")
        print ("-------------------------------------------------------")
        Choice = input("\nOption: ")
    
        if Choice == '1':
            print ("You picked up the rock. A wild spirit attacks!.\n")
            monster = Monster("spirit")
            break
        elif Choice == '2':
            print ("You kicked the rock. A wild spirit appears from the rock! ")
            monster = Monster("spirit")
            #Encounter function 
            break
        else:
            print ("Invalid option.\n")

def east(protag):
    print ("Walking across the eastern path. You hear a bunch of slime roaming around. What do you do?")
    
    while (True):
        print ("-------------------------------------------------------")
        print ("Options:")
        print ("1: Charge at them!")
        print ("2: Try and sneak by")
        print ("-------------------------------------------------------")
        Choice = input("\nOption: ")
    
        if Choice == '1':
            print ("You charge at the slimes. In the process you accidently slip and bump into one of them.\n")
            monster = Monster("slime")
            break
        elif Choice == '2':
            print ("You try sneaking past the slimes, but they heard your footsteps! ")
            monster = Monster("slime")
            #Encounter function 
            break
        else:
            print ("Invalid option.\n")

if __name__ == "__main__":
    main()
