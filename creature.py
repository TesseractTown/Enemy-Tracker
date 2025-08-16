class Enemy:
    def __init__(self, name, ac, health=10, color=(0,0,0)):
        self.name = name
        self.curr_health = health
        self.max_health = health
        self.ac = ac
        self.color = color # RGB tuple (r, g, b)

    enemy_dict = {}

    def create_enemy(name, hp, ac):
        enemy = Enemy(name, hp, ac)
        #enemy_dict[name] = self.name 

    def heal(self, amount):
        pass

    def damage(self, amount):
        pass