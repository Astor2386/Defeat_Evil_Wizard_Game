"Defeat the Evil Wizard!"
Python based-
Classic RPG where you choose a character class to battle against the Evil Wizard and his minion. 
Each class has unique abilities and strategies to employ in battle

Overview and Game break down-
To start, you must choose between one of five character classes 
Warrior,
Mage,
Archer,
Paladin,
(Special class Vampire) to fight in a turn-based style battle with the Evil Wizard. 
The game introduces elements like minion summoning by the Wizard and character-specific abilities.
Your goal is to reduce the Wizard's health to zero before he reduces yours through an array of different strategies. 
The longer the match goes on, the more difficult it will become.

Classes
Character: Base class with shared attributes and methods for all characters.
Attributes: name, health, attack_power, max_health.
Methods: attack, display_stats, heal, take_damage.
Warrior: Strong physical attacker.
Mage: High damage magic user.
Archer: Speed and evasion specialist.
Paladin: Defensive with healing and shield abilities.
Vampire: Uses life-draining to survive combat.
EvilWizard(non-playable): The main antagonist with regeneration and minion summoning abilities.
Minion(non-playable): summoned attacker for EvilWizard
--------------------------------------------------------------------------------------------------
How to Play-
Copy the repository and download
Ensure you have Python installed on your machine.
Find the directory with the script in your terminal.

Gameplay Instructions-
Choose Your Class: Select from Warrior, Mage, Archer, Paladin, or Vampire.
Battle Mechanics:
Attack: Basic attack move.(Not all basic attack power is the same)
Use Special Ability: Class-specific actions like Power Bash for Warrior or Mage Bolt for Mage.
Heal: Restore some health.
View Stats: Check your character's status (no turn cost). - This was implemented because there should be no charge of a turn just to see where your health is at.
Turn Phases:
Your turn: Choose an action from the menu.
Wizard's turn: The Wizard might attack, regenerate health, or summon a minion. (20% chance of minion summon per turn)
Winning Condition: Defeat the Wizard by reducing his health to zero.
Losing Condition: Your character's health reaches zero.

Special notes-
- Vampire class is a unique class, with a possibility of a INSTANT KILL! Using weak bite special ability
It also has the unique health drain ability to attack, and recover health
- No turn cost for checking stats
- Battle does get harder when minion is summoned, it's made to balance the power dynamics
- minion cannot be attacked directly or killed!

Strategy-
Use the special abilities in conjunction with the attack! Heal when neccesary and check your health using view stats at any time
without a cost to your turn!
Understand the battle gets harder as time goes on and a minion may be summoned.
As minion is summoned, recognize you will take more damage per turn.

Requirements-
Python 3.x

-End ReadMe



