class miniboss:
    def __init__(self, name, description, attack, health,):
        self.name = name
        self.description = description
        self.damage = attack
        self.health = health

    def boss_take_damage(self, damage):
        self.health -= damage
