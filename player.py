class Player():
    def __init__(self, name):
        self.__name = name
        self.__health = 10
        self.__attack = 2
        '''
        self.__armor = armor
        self.__speed = speed
        '''
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health
    
    def get_attack(self):
        return self.__attack
    
    def take_damage(self, damage):
        self.__health -= damage
    
    def death_check(self):
        if self.__health <= 0:
            print ("You died! Game Over!")
            return True
        return False
