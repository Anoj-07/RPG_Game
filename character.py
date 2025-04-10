from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack_power):
        self._name= name
        self._health = health
        self._attack_power = attack_power

    def is_alive(self):
        return self._health > 0
    
    def take_damage(self, damage):
        self._health -= damage
        print(f"{self._name} took {damage}.Health now: {self._health}")

    def get_status(self):
        return f"{self._name} | HP : {self._health}"
    
    @abstractmethod
    def attack(self, target):
        pass
