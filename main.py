def main():
    print("Welcome to the adventure game!")
    print("Use the WASD keys to choose where to go and the I key to check your stats\n")
    gate()

def gate():
    print ("In front of you stands a guard to the town which you were exhiled.")
    print ("Guard: Hello there, I cannot allow you back into town after your crimes. If you can redeem yourself the council will consider your crimes forgiven.\n")

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
        elif Choice == '3':
            print ("There's a growing monster popoluation that is terrorizing the nearby farmers. Reduce the population and I shall let you back in.\n")
        else:
            print ("You left the gate.\n")
            break  


if __name__ == "__main__":
    main()
