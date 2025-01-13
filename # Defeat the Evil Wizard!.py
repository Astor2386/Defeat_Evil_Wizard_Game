# Defeat the Evil Wizard!
# Import random for range feature to be utilized.
import random

# Initialize main class with public attributes
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

# Shared attack function function
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
           
# Shared display of stats function
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Shared self heal function
    def heal(self):
        heal_amount = random.randint(15, 30)
        if self.health + heal_amount < self.max_health:
            self.health += heal_amount
        else:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount}. Health now: {self.health}")
# Shared damage indicator function  
    def take_damage(self, damage):
        self.health -= damage
        return damage
# Creating new Characters
# Warrior
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def Power_Bash(self, opponent): # Unique ability
        damage = random.randint(30, 40)
        opponent.health -= damage
        print(f"{self.name} uses Power_Bash on {opponent.name} for {damage} damage!")

# Mage
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def Mage_Bolt(self, opponent): # Unique ability
        damage = random.randint(40, 50)
        opponent.health -= damage
        print(f"{self.name} casts Mage Bolt on {opponent.name} for {damage} damage!")

# Archer
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.evade_next = False  # New attribute to track if the next attack should be evaded

    def Quick_Shot(self, opponent): # Unique ability 
        damage = random.randint(self.attack_power, self.attack_power * 2)
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def Evade(self): # Unique ability
        self.evade_next = True
        print(f"{self.name} uses Evade! Will avoid the next attack.")
        
    def take_damage(self, damage):
        if self.evade_next:
            self.evade_next = False  # Reset evade for next turn
            print(f"{self.name} Evades the attack!")
            return 0
        else:
            return super().take_damage(damage)
        
# Paladin
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=18)
        self.shield_active = False  

    def Holy_Strike(self, opponent): # Unique ability
        damage = random.randint(self.attack_power, self.attack_power + 10)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    def Divine_Shield(self): # Unique ability
        self.shield_active = True
        print(f"{self.name} activates Divine Shield! Next attack will be blocked.")

    def take_damage(self, damage):
        if self.shield_active:
            self.shield_active = False  # Deactivate shield after use
            print(f"{self.name}'s Divine Shield blocks the attack!")
            return 0
        else:
            return super().take_damage(damage)
# Unique Character class!!
# Vampire
class Vampire(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)  # Moderate health and attack
        self.instant_kill_chance = .10  # 10% chance for instant kill

    def weak_bite(self, opponent): # Unique ability
        # Weak attack with a chance for instant kill
        damage = random.randint(5, 10)  # Weak damage
        if random.random() < self.instant_kill_chance:
            opponent.health = 0
            print(f"{self.name} uses Weak Bite on {opponent.name}, but it results in an INSTANT KILL!")
        else:
            opponent.health -= damage
            print(f"{self.name} uses Weak Bite on {opponent.name} for {damage} damage!")

    def blood_drain(self, opponent): # Unique ability
        # Drain health from opponent to heal self
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        heal_amount = damage // 2  # Heal half of the damage dealt
        opponent.health -= damage
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} uses Blood Drain on {opponent.name} for {damage} damage, healing for {heal_amount}!")

# Minion for EvilWizard
class Minion:
    def __init__(self, name):
        self.name = name
        self.health = 30  # Minion's health
        self.attack_power = 4  # Minion's attack power

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

# EvilWizard
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.minion = None  # Initially, no minion
        self.summon_chance = 0.20  # 20% chance to summon a minion

    def regenerate(self):
        if self.health + 5 < self.max_health:
            self.health += 5
        else:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        # This only announces the attack, does not apply damage
        print(f"{self.name} attacks {opponent.name}!")  

    def summon_minion(self):
        if random.random() < self.summon_chance and self.minion is None:
            self.minion = Minion(f"{self.name}'s Minion")
            print(f"{self.name} summons {self.minion.name}!")
            
# Fucntion creation to apply to character classes
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    print("5. Vampire")  # New option

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return Vampire(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats (no turn cost)") # Viewing stats will not cost a turn

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if type(player) == Warrior:
                player.Power_Bash(wizard)
            elif type(player) == Mage:
                player.Mage_Bolt(wizard)
            elif type(player) == Archer:
                action = input("Choose ability: 1. Quick Shot, 2. Evade: ")
                if action == '1':
                    player.Quick_Shot(wizard)
                elif action == '2':
                    player.Evade()
            elif type(player) == Paladin:
                action = input("Choose ability: 1. Holy Strike, 2. Divine Shield: ")
                if action == '1':
                    player.Holy_Strike(wizard)
                elif action == '2':
                    player.Divine_Shield()
            elif type(player) == Vampire:
                action = input("Choose ability: 1. Weak Bite, 2. Blood Drain: ")
                if action == '1':
                    player.weak_bite(wizard)
                elif action == '2':
                    player.blood_drain(wizard)
            else:
                print("No special abilities for this character.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue # no turn cost, loops back to choices
        else:
            print("Invalid choice. Try again.")
            continue # Any Invalid choice returns the turn to the player

        if wizard.health > 0:
            wizard.regenerate()
            
            # Calculate damage before applying
            wizard_damage = random.randint(wizard.attack_power - 5, wizard.attack_power + 5)
            
            # Announce the Wizard's attack
            wizard.attack(player)  # Announce the attack
            
             # Then apply and report damage
            actual_damage = player.take_damage(wizard_damage)
            if actual_damage > 0:
                print(f"{player.name} takes {actual_damage} damage!")
            else:
                # Keeping the Archer distinguishable for his evade ability vs block
                if type(player) == Archer:
                    print(f"{player.name} assumes normal stance!")
                else:
                    print(f"{wizard.name}'s attack was blocked!")

            # Summon minion based on chance
            if random.random() < wizard.summon_chance and wizard.minion is None:
                wizard.minion = Minion(f"{wizard.name}'s Minion")
                print(f"{wizard.name} summons {wizard.minion.name}!")
                # Minion attacks once on the turn it's summoned
                minion_damage = random.randint(wizard.minion.attack_power - 2, wizard.minion.attack_power + 2)
                minion_actual_damage = player.take_damage(minion_damage)
                print(f"{player.name} takes {minion_actual_damage} damage from {wizard.minion.name}!")

            # If minion already exists, it attacks normally
            elif wizard.minion:
                minion_damage = random.randint(wizard.minion.attack_power - 2, wizard.minion.attack_power + 2)
                minion_actual_damage = player.take_damage(minion_damage)
                print(f"{player.name} takes {minion_actual_damage} damage from {wizard.minion.name}!")

        # Check if the player has been defeated after the wizard's turn
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break  

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()