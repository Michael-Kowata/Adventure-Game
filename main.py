from player import Player
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
    print ("\nIn front of you stands a guard to the town which you were exhiled.")
    print (f"Guard: Hello {protag.get_name()}, I cannot allow you back into town after your crimes. If you can redeem yourself the council will consider your crimes forgiven.\n")

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
            print ("You stole and ate the mayor's prized cookie collection of course! Now please leave!\n")
        elif Choice == '2':
            print ("Hey what do you think you are doing! (You lost 2 health!)\n")
            protag.take_damage(2)
            if protag.death_check():
                sys.exit()
            print (f"Current Health: {protag.get_health()}")
        elif Choice == '3':
            print ("There's a growing monster popoluation that is terrorizing the local farmers. Reduce their population and I shall let you back in.\n")
        else:
            print ("You left the gate.\n")
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
            break
        elif Choice == '2':
            print ("You decided to check out the east path.\n")
            break
        elif Choice == '3':
            print ("You went back to the gate.\n")
            gate(protag)
        elif Choice == '4':
            print ("You chose to walk the western path.\n")
            break
        elif Choice == '5':
            print ("You read the sign.\n")
            print ("North path -> Moonshine Valley")
            print ("East path -> Grave of the Dragonflies")
            print ("South path -> Cookie Dough Kingdom")
            print ("West path -> Lake of Lost Souls\n")
        else:
            print ("Invalid option.\n")
            

if __name__ == "__main__":
    main()
