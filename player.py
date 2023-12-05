class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_hp = 200
        self.hp = 200
        self.max_mp = 5
        self.mp = 5
        self.power = 10
        self.defense = 0
        self.exp = 0
        self.level = 1
        self.item_list = []