import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен!")
                break
            print(f"Здоровье игрока: {self.player.health}")
            print(f"Здоровье компьютера: {self.computer.health}")

if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()
