class Character:
    """A simple RPG character class with health, attack, and defense attributes
    and methods to attack and take damage.
    """

    def __init__(self, health: int, attack: int, defense: int):
        if health < 0 or attack < 0 or defense < 0:
            raise ValueError("Health, attack, and defense cannot be negative.")
        if health == 0 or attack == 0:
            raise ValueError("Health and attack must be greater than zero.")

        self._health = health
        self._attack = attack
        self._defense = defense

    @property
    def health(self) -> int:
        """Returns the current health of the character."""
        return self._health

    @property
    def attack(self) -> int:
        """Returns the current attack of the character."""
        return self._attack

    @property
    def defense(self) -> int:
        """Returns the current defense of the character."""
        return self._defense

    def attack_enemy(self, enemy: "Character"):
        """Attacks another character based on enemy's defense and own attack"""
        enemy.take_damage(self._attack)

    def take_damage(self, damage: int):
        """Reduces health based on incoming damage and defense"""
        if damage <= 0:
            raise ValueError("Damage must be greater than zero.")
        final_damage = max(0, damage - self._defense)
        self._health -= final_damage
