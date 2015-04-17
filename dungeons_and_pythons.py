class Enemy:
    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.current_health = self.health

    def is_alive(self):
        if self.current_health == 0:
            return False

        return True

    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        if self.mana == 0:
            return False

        return True

    def take_damage(self, damage_points):
        if not self.is_alive:
            return False

        if damage_points > self.current_health:
            self.current_health = 0
        else:
            self.current_health -= damage_points

    def take_healing(self, healing_points):
        if self.current_health == 0:
            return "Can't, yout Hero is dead."

        elif self.current_health + healing_points <= self.health:
            self.current_health += healing_points
            return True

        return False

    def attack(self):
        pass


class dungeon:
    def __init__(self, file_name):
        self.file_name = file_name

    def print_map(self):
        f = open(self.file_name, "r")
        file_content = f.read()
        file_content.join("\n")
        return file_content


