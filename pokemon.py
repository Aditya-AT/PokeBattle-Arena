import random


class Pokemon:
    def __init__(self, name='Unknown', types=None):
        self._name = name
        self._types = types if types is not None else ['normal']  # Default type if none provided
        self._hp = None
        self._attack = None
        self._defense = None
        self._sp_attack = None
        self._sp_defense = None
        self._speed = None

    @property
    def name(self):
        return self._name

    @property
    def types(self):
        return self._types

    @property
    def hp(self):
        if self._hp is None:
            self._hp = random.randint(20, 35)  # Assign a random HP if not already set
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value  # Allows updating the HP value

    @property
    def attack(self):
        if self._attack is None:
            self._attack = random.randint(3, 11)
        return self._attack

    @property
    def defense(self):
        if self._defense is None:
            self._defense = random.randint(3, 11)
        return self._defense

    @property
    def sp_attack(self):
        if self._sp_attack is None:
            self._sp_attack = random.randint(3, 11)
        return self._sp_attack

    @property
    def sp_defense(self):
        if self._sp_defense is None:
            self._sp_defense = random.randint(3, 11)
        return self._sp_defense

    @property
    def speed(self):
        if self._speed is None:
            self._speed = random.randint(3, 11)
        return self._speed

    def __str__(self):
        types_str = '/'.join(self.types)
        return (f"Name: {self.name}, Types: {types_str}, HP: {self.hp}, "
                f"Atk: {self.attack}, Def: {self.defense}, SpA: {self.sp_attack}, "
                f"SpD: {self.sp_defense}, Spe: {self.speed}")
