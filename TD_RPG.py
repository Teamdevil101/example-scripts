#!/usr/bin/python3.8
# The text base (UNIX) / graphical (WIN32) rogue-like RPG

# This is a small project that I made back in school. This was supposed to be a graphical and non graphical 
# RPG (Graphical for windows and non graphical for linux). Now, you may notice the amount of ELSE IFs.
# I hate looking at this. I was just bored and botched this crap together.
# Also, contains little to no comments. I need to comment my code a little more often.


from random import randrange
import sys

monsterDamageLvlRng = 0
monsterHealthLvlRng = 0

healingPotions = 2
magicPotions = 1

strengthLvl = 1
magicLvl = 1
healthLvl = 1

requiredStrengthAmount = 2
requiredMagicAmount = 2
requiredHealthAmount = 2

currentStrengthAmount = 0
currentMagicAmount = 0
currentHealthAmount = 0

playerCurrentHealth = 10
playerMaxHealth = 10

playerCurrentMana = 2
playerMaxMana = 2

enemiesKilled = 0
heardSomething = False
foundChest = False
foundBody = False

skipTextInput = False
usrinput = ""

def RestartGame():
    global currentStrengthAmount
    global requiredStrengthAmount
    global currentMagicAmount
    global requiredMagicAmount
    global currentHealthAmount
    global requiredHealthAmount
    global strengthLvl
    global magicLvl
    global healthLvl
    global playerCurrentHealth
    global playerMaxHealth
    global playerCurrentMana
    global playerMaxMana
    global healingPotions
    global magicPotions
    global heardSomething
    global foundChest
    global foundBody
    global enemiesKilled
    
    healingPotions = 2
    magicPotions = 1
    
    strengthLvl = 1
    magicLvl = 1
    healthLvl = 1
    
    requiredStrengthAmount = 4
    requiredMagicAmount = 2
    requiredHealthAmount = 4
    
    currentStrengthAmount = 0
    currentMagicAmount = 0
    currentHealthAmount = 0
    
    playerCurrentHealth = 10
    playerMaxHealth = 10

    playerCurrentMana = 2
    playerMaxMana = 2
    
    heardSomething = False
    foundChest = False
    foundBody = False
    
    enemiesKilled = 0
    
    randomGameEvent()


# START OF LINUX VERSION

def passiveGameFunction():
    
    global heardSomething
    global foundChest
    global foundBody
    global currentStrengthAmount
    global requiredStrengthAmount
    global currentMagicAmount
    global requiredMagicAmount
    global currentHealthAmount
    global requiredHealthAmount
    global strengthLvl
    global magicLvl
    global healthLvl
    global playerCurrentHealth
    global playerMaxHealth
    global playerCurrentMana
    global playerMaxMana
    global healingPotions
    global magicPotions
    global enemiesKilled
    global usrinput
    global skipTextInput
    
    if(playerCurrentHealth <= 0):
        print("You are dead.")
        print("Your final levels:")
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        print("You have killed " + str(enemiesKilled) + " enemies.")
        
        if(skipTextInput):
            print("Got user input as:", usrinput)
        else:
            usrinput = input("Do you wish to play again? (Y/N) ?>")
        
            if("n" in usrinput.lower()):
                sys.exit("Game Over")
            else:
                RestartGame()

    if(currentStrengthAmount >= requiredStrengthAmount):
        print('You leveled up strength! Damage UP.')
        strengthLvl += 1
        requiredStrengthAmount *= 2
        currentStrengthAmount = 0
    elif(currentMagicAmount >= requiredMagicAmount):
        print('You leveled up magic! Magic UP.')
        magicLvl += 1
        playerMaxMana += 1
        requiredMagicAmount *= 2
        currentMagicAmount = 0
    elif(currentHealthAmount >= requiredHealthAmount):
        print('You leveled up health! Health UP.')
        healthLvl += 1
        playerCurrentHealth += 2
        playerMaxHealth += 4
        requiredHealthAmount *= 2
        currentHealthAmount = 0

    print("\n< You have " + str(playerCurrentHealth) + "/" + str(playerMaxHealth) + " HP and " + str(playerCurrentMana) + "/" + str(playerMaxMana) + " Magic >")
    print("< You are carrying " + str(healingPotions) + " Health potion(s) and " + str(magicPotions) + " Magic potion(s) >")
    print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
    
    if(skipTextInput):
        print("Got user input as:", usrinput)
        skipTextInput = False
    else:
        usrinput = input(">> ")
    
    if(usrinput.lower() == "forward" or usrinput.lower() == "go forward" or usrinput.lower() == "north" or usrinput.lower() == "up"):
        print('You moved north.')
        
    elif(usrinput.lower() == "backward" or usrinput.lower() == "back" or usrinput.lower() == "south" or usrinput.lower() == "down"):
        print('You moved south.')
        
    elif(usrinput.lower() == "right" or usrinput.lower() == "go right" or usrinput.lower() == "east"):
        print('You moved east.')
        
    elif(usrinput.lower() == "left" or usrinput.lower() == "go left" or usrinput.lower() == "west"):
        print('You moved south.')
        
    elif(usrinput.lower() == "jump" or usrinput.lower() == "hop"):
        print('You jumped in place.')
        
    elif(usrinput.lower() == "help"):
        print('Here are a list of available actions:')
        print('\n forward, backward, right, left, jump, die, move, run, check, search/open chest, search skeleton, search body, heal, drink mana, run toward sound, fight, wait, quit')
        passiveGameFunction()
        
    elif(usrinput.lower() == "die" or usrinput.lower() == "kill self" or usrinput.lower() == "kill me" or usrinput.lower() == "suicide"):
        print('You ended your life. Pathetic.')
        playerCurrentHealth = 0
        passiveGameFunction()
        
    elif("move" in usrinput.lower().split() or "go" in usrinput.lower().split()):
        print('You moved somewhere.')
        
    elif(usrinput.lower() == "run"):
        print('You ran.')
        
    elif(usrinput.lower() == "open" or usrinput.lower() == "check" or usrinput.lower() == "search"):
        if(foundChest == True or foundBody == True):
            print('You checked it out...')
            randomChestEvent()
        else:
            print('There is nothing to do.')
            passiveGameFunction()
        
    elif(usrinput.lower() == "search chest" or usrinput.lower() == "grab chest" or usrinput.lower() == "pick up chest" or usrinput.lower() == "open chest"):
        if(foundChest == True):
            print('You opened the chest...')
            randomChestEvent()
        else:
            print('There is no chest to open.')
            passiveGameFunction()
            
    elif(usrinput.lower() == "search body" or usrinput.lower() == "search skeleton" or usrinput.lower() == "pick up skeleton" or usrinput.lower() == "pick up body"):
        if(foundBody == True):
            print('You took a look at the body...')
            randomChestEvent()
        else:
            print('There is no body to check.')
            passiveGameFunction()
        
    elif(usrinput.lower() == "drink health potion" or usrinput.lower() == "drink health" or usrinput.lower() == "drink healing" or usrinput.lower() == "drink healing potion" or usrinput.lower() == "heal"):
        if(healingPotions <= 0):
            print('You dont have any healing potions.')
            passiveGameFunction()
        else:
            print('You used a healing potion')
            healingPotions -= 1
            playerCurrentHealth = playerMaxHealth
            passiveGameFunction()
            
    elif(usrinput.lower() == "drink mana potion" or usrinput.lower() == "drink mana" or usrinput.lower() == "drink magic" or usrinput.lower() == "drink magic potion" or usrinput.lower() == "heal"):
        if(magicPotions <= 0):
            print('You dont have any mana potions.')
            passiveGameFunction()
        else:
            print('You used a mana potion')
            magicPotions -= 1
            playerCurrentMana = playerMaxMana
            passiveGameFunction()

    elif(usrinput.lower() == "fight" or usrinput.lower() == "fight monster" or usrinput.lower() == "attack" or usrinput.lower() == "attack monster" or usrinput.lower() == "run towards sound" or usrinput.lower() == "kill monster"):
        if(heardSomething == True):
            print('You charged toward the sound. It was a monster')
            randomMonsterSpawingEvent()
        else:
            print('There is nothing to attack, fight nor kill.')
            passiveGameFunction()
            
    elif(usrinput.lower() == "stand" or usrinput.lower() == "stay" or usrinput.lower() == "wait"):
        if(heardSomething == True):
            print('You waited but a monster got to you.')
            if(playerCurrentHealth < playerMaxHealth):
                playerCurrentHealth += 1
            heardSomething = False
            randomMonsterSpawingEvent()
        else:
            if(playerCurrentHealth < playerMaxHealth):
                playerCurrentHealth += 1
            print('You waited.')
            
    elif(usrinput.lower() == "exit" or usrinput.lower() == "quit" or usrinput.lower() == "stop"):
        print('Do you want to stop playing?')
        usrwat = input("?> ")
        if(usrwat.lower() == "yes" or usrwat.lower() == "y"):
            print('Thank you for trying my script. :)')
            sys.exit("Game Ended")
        else:
            passiveGameFunction()
            
    elif(len(usrinput) <= 0):
        print('Type something, so I can do something.')
        passiveGameFunction()
    else:
        print('I dont understand "' + str(usrinput) + '". Try something else.')
        passiveGameFunction()
    
    randomGameEvent()
        
def randomGameEvent():
    global heardSomething
    global foundChest
    global foundBody
    
    heardSomething = False
    foundChest = False
    foundBody = False
    
    randomNr = randrange(0, 5)
    print("\n\n----------------------------------------------------------------")
    print("\n[<PASSIVE PHASE>]")
    print('You are in a very dark and foggy room. You feel like everytime you move, you will always be in a different place, no matter where you go.')
    if(randomNr == 0):
        passiveGameFunction()
        
    elif(randomNr == 1):
        print('You hear something getting closer to you. You can still get away from it.')
        heardSomething = True
        passiveGameFunction()
        
    elif(randomNr == 2):
        print("You notice a skeleton on the ground. Someone died here.")
        foundBody = True
        passiveGameFunction()
        
    elif(randomNr == 3):
        print("You found a chest. Maybe you can open it?")
        foundChest = True
        passiveGameFunction()
        
    elif(randomNr == 4):
        print("You were jumped by a monster without warning!")
        randomMonsterSpawingEvent()
        
    elif(randomNr == 5):
        passiveGameFunction()
        
    
def randomChestEvent():
    global healingPotions
    global magicPotions
    global foundBody
    global foundChest
    
    if(foundBody == True):
        foundBody = False
        randomNr = randrange(0, 10)
        if(randomNr == 1):
            print("The skeleton has a mana potion on him. You took it.")
            magicPotions += 1
            passiveGameFunction()
            
        elif(randomNr == 2):
            print("The skeleton has a healing potion on him. You took it.")
            healingPotions += 1
            passiveGameFunction()
            
        elif(randomNr == 5):
            print("The skeleton came back to life!")
            randomMonsterSpawingEvent()
        
        else:
            print("There was nothing on the skeleton.")
            passiveGameFunction()
            
    elif(foundChest == True):
        foundChest = False
        randomNr = randrange(1, 5)
        if(randomNr == 1):
            print("The chest has a mana potion. You took it.")
            magicPotions += 1
            passiveGameFunction()
            
        elif(randomNr == 2):
            print("The chest has a healing potion. You took it.")
            healingPotions += 1
            passiveGameFunction()
            
        elif(randomNr == 5):
            print("A skeleton came out of the chest!")
            randomMonsterSpawingEvent()
        
        else:
            print("There was nothing in the chest.")
            passiveGameFunction()
        
def randomMonsterSpawingEvent():
    global monsterDamageLvlRng
    global monsterHealthLvlRng
    global strengthLvl
    global magicLvl
    global healthLvl
    
    monsterDamageLvlRng = randrange(1, 2 * healthLvl)
    monsterHealthLvlRng = monsterDamageLvlRng * randrange(1, 10)
    randomMonsterEvent()
        
def randomMonsterEvent():
    print("\n\n----------------------------------------------------------------")
    print("\n[<BATTLE PHASE>]")
    
    global currentStrengthAmount
    global requiredStrengthAmount
    global currentMagicAmount
    global requiredMagicAmount
    global currentHealthAmount
    global requiredHealthAmount
    global strengthLvl
    global magicLvl
    global healthLvl
    global playerCurrentHealth
    global playerMaxHealth
    global playerCurrentMana
    global playerMaxMana
    global healingPotions
    global magicPotions
    global monsterDamageLvlRng
    global monsterHealthLvlRng
    global enemiesKilled
    global usrinput
    global skipTextInput
    
    if(playerCurrentHealth <= 0):
        print("You are dead.")
        print("Your final levels:")
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        print("You have killed " + str(enemiesKilled) + " enemies.")
        
        usrinput = input("Do you wish to play again? (Y) ?> ")
        
        if("n" in usrinput.lower()):
            sys.exit("Game Over")
        else:
            RestartGame()

    if(currentStrengthAmount >= requiredStrengthAmount):
        print('You leveled up strength! Damage UP.')
        strengthLvl += 1
        requiredStrengthAmount *= 1.25
        currentStrengthAmount = 0
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        
    elif(currentMagicAmount >= requiredMagicAmount):
        print('You leveled up magic! Magic UP.')
        magicLvl += 1
        playerMaxMana += 1
        requiredMagicAmount *= 1.25
        currentMagicAmount = 0
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        
    elif(currentHealthAmount >= requiredHealthAmount):
        print('You leveled up health! Health UP.')
        healthLvl += 1
        playerCurrentHealth += 2
        playerMaxHealth += 4
        requiredHealthAmount *= 1.25
        currentHealthAmount = 0
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
    
    print("< You have " + str(playerCurrentHealth) + "/" + str(playerMaxHealth) + " HP and " + str(playerCurrentMana) + "/" + str(playerMaxMana) + " Magic >")
    print("< You are carrying " + str(healingPotions) + " Health potion(s) and " + str(magicPotions) + " Magic potion(s) > \n")

    print('<(A Monster)> [Health:'+ str(monsterHealthLvlRng) +' | Level:'+ str(monsterDamageLvlRng) +']')
    
    if(skipTextInput):
        print("Got user input as:", usrinput)
        skipTextInput = False
    else:
        usrinput = input(">> ")
    
    if(usrinput.lower() == "attack" or usrinput.lower() == "kill" or usrinput.lower() == "fight" or usrinput.lower() == "hit" or usrinput.lower() == "punch"):
        print('You attack the monster.')
        monsterHealthLvlRng -= strengthLvl
        print('You dealt: -'+ str(strengthLvl) + ' Dmg')
        currentStrengthAmount += 1
        
    elif(usrinput.lower() == "help"):
        print('Here are a list of available actions:')
        print('\n attack, hit, cast, wait, use magic, magic, heal, drink mana, run, cast spell, punch, die')
        randomMonsterEvent()
        
    elif(usrinput.lower() == "die" or usrinput.lower() == "kill self" or usrinput.lower() == "kill me" or usrinput.lower() == "suicide"):
        print('You ended your life. Pathetic.')
        playerCurrentHealth = 0
        randomMonsterEvent()
        
    elif(usrinput.lower() == "exit" or usrinput.lower() == "quit" or usrinput.lower() == "stop"):
        print('Do you want to stop playing?')
        usrwat = input("?> ")
        if(usrwat.lower() == "yes" or usrwat.lower() == "y"):
            print('Thank you for trying my script. :)')
            sys.exit("Game Ended")
        else:
            randomMonsterEvent()
        
    elif(usrinput.lower() == "wait" or usrinput.lower() == "stand still" or usrinput.lower() == "do nothing"):
        print('You stood idle.')
        if(playerCurrentHealth < playerMaxHealth):
            playerCurrentHealth += 1
        if(playerCurrentMana < playerMaxMana):
            playerCurrentMana += 1
        
    elif(usrinput.lower() == "use magic" or usrinput.lower() == "cast spell" or usrinput.lower() == "spell" or usrinput.lower() == "magic" or usrinput.lower() == "cast"):
        if(playerCurrentMana <= 0):
            print('You tried casted a spell but you forgot that you dont have any mana left.')
            print('You dealt: 0 Dmg')
        else:
            print('You casted a spell')
            playerCurrentMana -= 1
            currentMagicAmount += 1
            damage = randrange(2, 10) * magicLvl
            print('You dealt: -'+ str(damage) + ' Dmg')
            monsterHealthLvlRng -= damage
    
    elif(usrinput.lower() == "drink health potion" or usrinput.lower() == "drink health" or usrinput.lower() == "drink healing" or usrinput.lower() == "drink healing potion" or usrinput.lower() == "heal"):
        if(healingPotions <= 0):
            print('You dont have any healing potions.')
            randomMonsterEvent()
        else:
            print('You used a healing potion')
            healingPotions -= 1
            playerCurrentHealth = playerMaxHealth
            
    elif(usrinput.lower() == "drink mana potion" or usrinput.lower() == "drink mana" or usrinput.lower() == "drink magic" or usrinput.lower() == "drink magic potion" or usrinput.lower() == "heal"):
        if(magicPotions <= 0):
            print('You dont have any mana potions.')
            randomMonsterEvent()
        else:
            print('You used a mana potion')
            magicPotions -= 1
            playerCurrentMana = playerMaxMana
        
    elif(usrinput.lower() == "run" or usrinput.lower() == "run away"):
        tryingToEscape = randrange(0, 2)
        
        if(tryingToEscape == 1):
            print('You ran away.')
            randomGameEvent()
        else:
            print('You tried to ran away but you fell.')
    
    elif(len(usrinput) <= 0):
        print('You cant just leave me hanging here. Come on!')
        randomMonsterEvent()
    else:
        print('I dont understand "' + str(usrinput) + '". Try attacking? Maybe running away?')
        randomMonsterEvent()
    
    if(monsterHealthLvlRng <= 0):
        print("You killed the monster.")
        enemiesKilled += 1
        
        randomNr = randrange(1, 7)
        if(randomNr == 4):
            print("The monster dropped a mana potion. You took it.")
            magicPotions += 1
            
        elif(randomNr == 5):
            print("The monster dropped a healing potion. You took it.")
            healingPotions += 1
            
        elif(randomNr == 6):
            print("OH WOW! The monster dropped a experience rune. It fuzed with you.")
            currentStrengthAmount = 999999999
            currentMagicAmount = 999999999
            currentHealthAmount = 999999999
            
        else:
            print("Sadly, the monster had nothing on him.")
            
        randomGameEvent()
    
    randomMonsterAIEvent()
        
def randomMonsterAIEvent():
    global monsterDamageLvlRng
    global monsterHealthLvlRng
    global playerCurrentHealth
    global currentHealthAmount
    
    randomnr = randrange(0, 5)
    
    if(randomnr == 1):
        print('The Monster is standing still.')
        monsterHealthLvlRng += 1
    else:
        print('The Monster attacks!')
        playerCurrentHealth -= monsterDamageLvlRng
        print('The Monster dealt: -'+ str(monsterDamageLvlRng) + ' Dmg')
        currentHealthAmount += monsterDamageLvlRng / 2
    
    randomMonsterEvent()
    
        
# END OF LINUX VERSION

# START OF WINDOWS VERSION

def GetPlayerData():
    
    # Display the players info through labels
    print("< You have " + str(playerCurrentHealth) + "/" + str(playerMaxHealth) + " HP and " + str(playerCurrentMana) + "/" + str(playerMaxMana) + " Magic >")
    print("< You are carrying " + str(healingPotions) + " Health potion(s) and " + str(magicPotions) + " Magic potion(s) > \n")

def GetMonsterData():
    
    # Display the enemy info through labels
    print('<(A Monster)> [Health:'+ str(monsterHealthLvlRng) +' | Level:'+ str(monsterDamageLvlRng) +']')


def WINDOWSrandomMonsterEvent():
    print("\n\n----------------------------------------------------------------")
    print("\n[<BATTLE PHASE>]")
    
    global currentStrengthAmount
    global requiredStrengthAmount
    global currentMagicAmount
    global requiredMagicAmount
    global currentHealthAmount
    global requiredHealthAmount
    global strengthLvl
    global magicLvl
    global healthLvl
    global playerCurrentHealth
    global playerMaxHealth
    global playerCurrentMana
    global playerMaxMana
    global healingPotions
    global magicPotions
    global monsterDamageLvlRng
    global monsterHealthLvlRng
    global enemiesKilled
    global usrinput
    global skipTextInput
    
    if(playerCurrentHealth <= 0):
        # You are fucking dead. Show that to the user by text!
        print("You are dead.")
        print("Your final levels:")
        print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        print("You have killed " + str(enemiesKilled) + " enemies.")

    if(currentStrengthAmount >= requiredStrengthAmount):
        print('You leveled up strength! Damage UP.')
        strengthLvl += 1
        requiredStrengthAmount *= 1.25
        currentStrengthAmount = 0
        # Display that you leveled up.
        #print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        
    elif(currentMagicAmount >= requiredMagicAmount):
        print('You leveled up magic! Magic UP.')
        magicLvl += 1
        playerMaxMana += 1
        requiredMagicAmount *= 1.25
        currentMagicAmount = 0
        # Display that you leveled up.
        #print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
        
    elif(currentHealthAmount >= requiredHealthAmount):
        print('You leveled up health! Health UP.')
        healthLvl += 1
        playerCurrentHealth += 2
        playerMaxHealth += 4
        requiredHealthAmount *= 1.25
        currentHealthAmount = 0
        # Display that you leveled up.
        #print("\n[Strength Level:" + str(strengthLvl) + " | Magic Level:" + str(magicLvl) + " | Health Level:" + str(healthLvl) + "]")
    
    if(usrinput.lower() == "attack" or usrinput.lower() == "kill" or usrinput.lower() == "fight" or usrinput.lower() == "hit" or usrinput.lower() == "punch"):
        print('You attack the monster.')
        monsterHealthLvlRng -= strengthLvl
        print('You dealt: -'+ str(strengthLvl) + ' Dmg')
        currentStrengthAmount += 1
        
    elif(usrinput.lower() == "help"):
        print('Here are a list of available actions:')
        print('\attack, hit, cast, wait, use magic, magic, heal, drink mana, run, cast spell, punch, die')
        randomMonsterEvent()
        
    elif(usrinput.lower() == "die" or usrinput.lower() == "kill self" or usrinput.lower() == "kill me" or usrinput.lower() == "suicide"):
        print('You ended your life. Pathetic.')
        playerCurrentHealth = 0
        randomMonsterEvent()
        
    elif(usrinput.lower() == "exit" or usrinput.lower() == "quit" or usrinput.lower() == "stop"):
        print('Do you want to stop playing?')
        usrwat = input("?> ")
        if(usrwat.lower() == "yes" or usrwat.lower() == "y"):
            print('Thank you for trying my script. :)')
            sys.exit("Game Ended")
        else:
            randomMonsterEvent()
        
    elif(usrinput.lower() == "wait" or usrinput.lower() == "stand still" or usrinput.lower() == "do nothing"):
        print('You stood idle.')
        if(playerCurrentHealth < playerMaxHealth):
            playerCurrentHealth += 1
        if(playerCurrentMana < playerMaxMana):
            playerCurrentMana += 1
        
    elif(usrinput.lower() == "use magic" or usrinput.lower() == "cast spell" or usrinput.lower() == "spell" or usrinput.lower() == "magic" or usrinput.lower() == "cast"):
        if(playerCurrentMana <= 0):
            print('You tried casted a spell but you forgot that you dont have any mana left.')
            print('You dealt: 0 Dmg')
        else:
            print('You casted a spell')
            playerCurrentMana -= 1
            currentMagicAmount += 1
            damage = randrange(2, 10) * magicLvl
            print('You dealt: -'+ str(damage) + ' Dmg')
            monsterHealthLvlRng -= damage
    
    elif(usrinput.lower() == "drink health potion" or usrinput.lower() == "drink health" or usrinput.lower() == "drink healing" or usrinput.lower() == "drink healing potion" or usrinput.lower() == "heal"):
        if(healingPotions <= 0):
            print('You dont have any healing potions.')
            randomMonsterEvent()
        else:
            print('You used a healing potion')
            healingPotions -= 1
            playerCurrentHealth = playerMaxHealth
            
    elif(usrinput.lower() == "drink mana potion" or usrinput.lower() == "drink mana" or usrinput.lower() == "drink magic" or usrinput.lower() == "drink magic potion" or usrinput.lower() == "heal"):
        if(magicPotions <= 0):
            print('You dont have any mana potions.')
            randomMonsterEvent()
        else:
            print('You used a mana potion')
            magicPotions -= 1
            playerCurrentMana = playerMaxMana
        
    elif(usrinput.lower() == "run" or usrinput.lower() == "run away"):
        tryingToEscape = randrange(0, 2)
        
        if(tryingToEscape == 1):
            print('You ran away.')
            randomGameEvent()
        else:
            print('You tried to ran away but you fell.')
    
    elif(len(usrinput) <= 0):
        print('You cant just leave me hanging here. Come on!')
        randomMonsterEvent()
    else:
        print('I dont understand "' + str(usrinput) + '". Try attacking? Maybe running away?')
        randomMonsterEvent()
    
    if(monsterHealthLvlRng <= 0):
        print("You killed the monster.")
        
        randomNr = randrange(1, 6)
        if(randomNr == 4):
            print("The monster dropped a mana potion. You took it.")
            magicPotions += 1
            
        elif(randomNr == 5):
            print("The monster dropped a healing potion. You took it.")
            healingPotions += 1
            
        elif(randomNr == 6):
            print("OH WOW! The monster dropped a experience rune. It fuzed with you.")
            currentStrengthAmount = 999999999
            currentMagicAmount = 999999999
            currentHealthAmount = 999999999
            
        else:
            print("Sadly, the monster had nothing on him.")
            
        randomGameEvent()
    
    randomMonsterAIEvent()

def setUsrInput(string):
    global usrinput
    global skipTextInput
    
    skipTextInput = True
    usrinput = string
    randomGameEvent()

#if(sys.platform == 'win32' or sys.platform == "cygwin"):
if(sys.platform != 'win32'):
    
    print('Im on windows')
    import tkinter as tk
    import tkinter.ttk as ttk

    mainWindow = tk.Tk()
    mainWindow.title('The windows rogue-like RPG (V0.0.1)')
    mainWindow.geometry('700x600')
    mainWindow.resizable(False, False)

    healthBar = ttk.Progressbar(mainWindow, orient = "horizontal", length = 100, maximum = playerMaxHealth, mode = 'determinate')
    healthBar.pack(pady = 1)
    healthBar['value'] = playerCurrentHealth
    magicBar = ttk.Progressbar(mainWindow, orient = "horizontal", length = 100, maximum = playerMaxMana, mode = 'determinate')
    magicBar.pack(pady = 1)
    magicBar['value'] = playerCurrentMana
    
    randomGameEvent()
    
    button3 = tk.Button(mainWindow, text="Click Me", command=lambda: setUsrInput("run"))
    button3.place(relx=.5, rely=.5, anchor="c")
    
    mainWindow.update_idletasks() 
    mainWindow.mainloop()
    
else:
    print('[The UNIX rogue-like RPG] (Version 0.0.1)')
    print('To play, just type in a word that I understand and you will try to survive for as long as you can.')
    randomGameEvent()