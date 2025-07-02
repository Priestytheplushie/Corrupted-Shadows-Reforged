class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.level = 1 
        self.health = 100
        self.max_health = self.health
        self.hunger = 100
        self.xp = 0
        self.inventory = []

    def __str__(self) -> str:
        return f"Player(name={self.name}, level={self.level}, health={self.health}, max_health={self.max_health}, hunger={self.hunger}, xp={self.xp})"