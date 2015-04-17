class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.current_health = self.health

    def known_as(self):
        return "{} the {}" .format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if (get_health(self) > 0 ):
            return True
        else:
            return False

    def can_cast(self):
        if (get_mana(self) > 0):
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if (damage_points > current_health):
            self.current_health = 0
        else:
            self.current_health -= damage_points

    def take_healing(self, healing_points):
        if self.current_health is 0:
            return False
        elif ((self.current_health + healing_points) > get_health(self)):
            self.current_health = get_health(self)
        else:
            return True

    def take_mana(self,mana_points):
        pass


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def equip(weapon):
        pass


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def learn(spell):
        pass

class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def is_alive(self):
        if (get_health(self) > 0 ):
            return True
        else:
            return False

