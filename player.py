from character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack_power = 15)
        self.level = 1
        self.xp = 0

    def attack(self, target):
        print(f"{self._name} attacks {target._name} for {self._attack_power} damage!")
        target.take_damage(self._attack_power)
    
    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self._name} gained {amount} xp. Total XP: {self.xp}")
        if self.xp >= self.level * 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self._health += 20
        self._attack_power += 5
        print(f"{self._name} leveled up! Now level {self.level} with HP {self._health} and attack {self._attack_power}")