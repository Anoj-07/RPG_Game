from character import Character
import random


class Enemy(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def attack(self, target):
        damage = random.randint(5, self._attack_power)
        print(f"{self._name} attacks {target._name} for {damage} damage!")
        target.take_damage(damage)


def generate_random_ememy():
    ememies = [Enemy("Badarnii", 60, 10), Enemy("dear", 80, 12), Enemy("paru", 90, 15)]
    return random.choice(ememies)
