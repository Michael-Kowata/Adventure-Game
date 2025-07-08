class Monster():
    def __init__(self, name):
        self.__name = name
        self.__health = 10
        self.__attack = 3

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
            return True
        return False
'''
class Spirit():
    def __init__(self):
        super().__Monster__()
'''

