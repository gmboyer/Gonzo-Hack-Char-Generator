###############################################################################
#         Random Gonzo Character Generator for Black Hack + Rad Hack          #
#                with random character traits from Maze Rats                  #
#                                                                             #
#                 Black Hack by David Black, available free:                  #
#               https://the-black-hack.jehaisleprintemps.net/                 #
#                                                                             #
#                Rad Hack by Kark Stjernberg, available free:                 #
#            http://rad-hack.jehaisleprintemps.net/english/index.html         #
#                                                                             #
#                  Maze Rats by Ben Milton, available free:                   #
#              http://questingblog.com/maze-rats-now-available/               #
#                                                                             #
#                  Male and Female random names borrowed from:                #
#         http://www.random-generator.com/index.php?title=Victorian_Names     #
#                           and "weird" names from:                           #
#                   http://www.fantasynamegenerators.com/                     #
#                                                                             #
###############################################################################
# About:
#     This generator creates a random character for Black Hack and Rad Hack
#     using the flavorful character traits from Maze Rats and names borrowed
#     from free online fantasy name generators.
#
#     Names, traits, class, abilities, wealth, equipment, and spells will all
#     be randomly generated according to the character guidelines given in their
#     respectives sources. For instance, Black-Hack classes (warrior, thief,
#     cleric, conjurer) will have their ability scores generated via 3d6,
#     while Rad-Hack humans will use 4d6 and drop lowest, mutants a d20, robots
#     a 27 point-buy, and psionics a mix of 3d6 for physical stats and 4d6 drop
#     lowest for mental stats. Equipment is purchased according to random
#     starting wealth, generally beginning with a weapon and armor and using
#     leftover money to purchase other things.
#
#     This generator was created to provide my players with fun 'anything goes'
#     characters for a deadly adventure in the dungeon of Kihago ("Beneath the
#     Ruins" by Alex Fotinakes published in the "Wizards Mutants Lazer Pistols"
#     OSR fan-zine). Rest in peace, Photoserpent the Cleric, killed by a laser
#     blast followed shortly by an eruption of a billion parasitic worms
#     from your egg-infested corpse. I dedicate this generator to your memory.
#
#
# How to use:
#     Place RandomGonzoHack.py, RandomGonzoNames.py, and RandomGonzoDesc.py in
#     a single directory, then run RandomGonzoHack.py
#
#
# Any future work would be aimed at:
#     Adding an option to include randomly-generated Maze Rats spells
#     Formatting output to look pretty
#     Overall condensing and cleanup of code
#
###############################################################################

import random
<<<<<<< HEAD
from RandomGonzoDesc import *
from RandomGonzoNames import *
from RandomMazeRatLists import *
=======
from RandomGonzoNames import *
from RandomGonzoDesc import *
>>>>>>> origin/master

class_list = [  "Human",    "Mutant",   "Robot",    "Psionic",
                "Warrior",  "Thief",    "Cleric",   "Conjurer"]

rand_class = random.choice(class_list)

# for testing purposes:
# rand_class = random.choice(["Human",    "Mutant",   "Robot",    "Psionic"])
rand_class = "Maze Rat"

# function for rolling an N-sided die
def rolldN(N):
    return random.randint(1,N)

# function for rolling 4d6 and dropping the lowest
def roll_4d6_drop_lowest():
    fourd6 = [rolldN(6), rolldN(6), rolldN(6), rolldN(6)]
    return sum(fourd6)-min(fourd6)

# function for rolling 3d6
def roll_3d6():
    return rolldN(6) + rolldN(6) + rolldN(6)

# function for rolling a d20, excluding 1 and 20
# used for rolling Mutant stats
def mutroll():
    return random.randint(2,19)

# function that returns the quality of die
# for RAD-Hack equipment
def quality():
    result = rolldN(8)
    if 1 <= result <= 3: return " (d4 usage die)"
    if 4 <= result <= 5: return " (d6 usage die)"
    if 6 <= result <= 7: return " (d8 usage die)"
    if result == 8: return " (d10 usage die)"

# randomly chooses M/F/Wierd names based on lists
# that are imported from another .py file
rand_male_name = random.choice(male_names)
rand_female_name = random.choice(female_names)
rand_weird_name = random.choice(weird_names)

# rolling for character sex on a percentile die
# and then assigning names based on chosen sex
char_sex_roll = rolldN(100)
if char_sex_roll <= 47:
    char_sex = "Male"
    char_name = random.choice(
        [rand_male_name, rand_weird_name]
        )
    if rand_class == "Robot":
        char_sex = random.choice(["Android", "None"])
elif 48 <= char_sex_roll <= 95:
    char_sex = "Female"
    char_name = random.choice(
        [rand_female_name, rand_weird_name]
        )
    if rand_class == "Robot":
        char_sex = random.choice(["Gynoid", "None"])
else:
    char_sex = "It's complicated"
    char_name = random.choice(
        [rand_male_name, rand_female_name, rand_weird_name]
        )
    if rand_class == "Robot":
        char_sex = random.choice(["Hermaphroid","None"])

# assigning character details based on lists
# that are imported from another .py file
physical_description = random.choice(physical_description_list)
physical_detail = random.choice(physical_detail_list)
background = random.choice(background_list)
clothing = random.choice(clothing_list)
personality = random.choice(personality_list)
mannerism = random.choice(mannerism_list)

# function for a random maze rat spell
def rand_maze_rat_spell():

    rand_mr_spell_combo = random.choice([
        [physical_effect, physical_form],
        [physical_effect, ethereal_form],
        [ethereal_effect, physical_form],
        [ethereal_effect, ethereal_form],
        [physical_element, physical_form],
        [physical_element, ethereal_form],
        [ethereal_element, physical_form],
        [ethereal_element, ethereal_form],
        [physical_effect, physical_element],
        [physical_effect, ethereal_element],
        [ethereal_effect, physical_element],
        [ethereal_effect, ethereal_element],
        ])

    word1 = random.choice(rand_mr_spell_combo[0])
    word2 = random.choice(rand_mr_spell_combo[1])

    return str(word1 + " " + word2)

    #return str(random.choice(mr_physical_effect) + " " + random.choice(mr_physical_element))



# function for a random point buy system for Robot characters
def rand_robotbuy():
    # number of points used to improve stats. Robots start with 27.
    available_points = 27

    # ability scores
    STR = [8, "STR"]
    DEX = [8, "DEX"]
    CON = [8, "CON"]
    INT = [8, "INT"]
    WIS = [8, "WIS"]
    CHA = [8, "CHA"]

    stat_list = [STR, DEX, CON, INT, WIS, CHA] #baseline stats

    # random point buy using randomly selected stats
    # increasing a stat above 13 costs 2 points, above 14 costs 3, and so on
    while available_points > 0:
        current_stat = random.choice(stat_list) #choose a random stat_list
        if 8 <= current_stat[0] < 13 and available_points >= 1:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 1
        elif current_stat[0] == 13 and available_points >= 2:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 2
        elif current_stat[0] == 14 and available_points >= 3:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 3
        elif current_stat[0] == 15 and available_points >= 4:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 4
        elif current_stat[0] == 16 and available_points >= 5:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 5
        elif current_stat[0] == 17 and available_points >= 6:
            current_stat[0] = current_stat[0] + 1
            available_points = available_points - 6
        else:
            pass # loop again if too few points to improve the stat

    # returns a list of 6 numbers; the first item in each tuple of stat_list
    return [x[0] for x in stat_list]

def check_if_can_buy(cash, cost):
    if cash >= cost:
        return True #can buy it
    else:
        return False #can't buy it

# determines if an item can be purchased from a list
# returns two elements: [0] is the item, [1] is the remaining cash
# returns "no buy" if not enough cash for any armor
def buy_item_from_list(cash, item_list):
    cash = cash #is this needed?
    #skip if do not have enough cash to buy ANY armor:
    if cash >= min([x[1] for x in item_list]):
        has_item = False
        while has_item == False:
            rand_item = random.choice(item_list)
            if check_if_can_buy(cash, rand_item[1]) == True:
                cash = cash - rand_item[1]
                has_item = True
                return [rand_item[0], cash]
            else:
                pass
    else:
        return "no buy"


# returns a list. [0] returns leftover money
# and [1] returns purchased equipment list
def buy_equip(start_cash, char_class):
    cash = start_cash
    purchased_equipment = []

    # items within equipment categories
    warrior_armor_list = [
        ["Gambeson (AP 2)", 50],
        ["Leather Armor (AP 4)", 100],
        ["Chain Mail (AP 6)", 350],
        ["Plate and Mail (AP 8)", 600],
        ]
    thief_armor_list = [
        ["Gambeson (AP 2)", 50],
        ["Leather Armor (AP 4)", 100],
        ]
    cleric_armor_list = [
        ["Gambeson (AP 2)", 50],
        ["Leather Armor (AP 4)", 100],
        ["Chain Mail (AP 6)", 350],
        ]
    optional_tool_list = [
        ["Work tools", 2],
        ["Iron Spikes", 1],
        ["Handheld Mirror", 5],
        ["50 ft Rope", 1],
        ["10 ft pole", 1],
        ["Assorted Common Herbs (d8 usage die)", 10],
        ]
    food_and_drink = [
        ["Preserved rations (d8 usage die)", 15],
        ["Fresh Rations (d4 usage die)", 5],
        ["Bottle of Wine", 1],
        ["Wineskin (d6 usage die)", 1],
        ]
    storage_list = [
        ["Backpack", 5],
        ["Small Sack", 1],
        ["Large Sack", 2],
        ]
    light_list = [
        ["Lantern", 10],
        ["Torches (x6, each torch has a d6 usage die)", 1],
        ["Flint and Steel", 3],
        ["Flask of oil (d6 usage die)", 2],
        ]
    holy_list = [
        ["Holy Symbol (+2 to WIS when banishing)", 25],
        ["Holy Water (d4 usage die)", 25],
        ]
    thief_tool_list = [
        ["Thieves Tools", 25],
        ]
    thief_shield_list = [
        ["Small Shield (AP 2)", 50],
        ]
    shield_list = [
        ["Small Shield (AP 2)", 50],
        ["Large Shield (AP 4)", 100],
        ]

    rad_weapon_list = [
        [random.choice(["Knife (light melee)", "Shiv (light melee)", \
            "Iron Pipe (light melee)"]) + quality(), 15],
        [random.choice(["Junk-Sword (1H, medium melee)", \
            "Baseball Bat (medium melee)", \
            "Machete (medium melee)"]) + quality(), 25],
        [random.choice(["Junk-Sword (2H, heavy melee)", \
            "Fire Axe (heavy melee)", \
            "Sledgehammer (heavy melee)"]) + quality(), 100],
        [random.choice(["Slingshot (light ranged)", \
            "Bow and Arrow (light ranged)", \
            "Crossbow (light ranged)"]) + quality(), 25],
        [random.choice(["Rifle (medium ranged)", "Handgun (medium ranged)", \
            "SMG (medium ranged)"]) + quality(), 50],
        [random.choice(["Machine Gun (heavy ranged)", \
            "Sniper Rifle (heavy ranged)", \
            "Shotgun (heavy ranged)"]) + quality(), 150],
        ]

    rad_psionic_weapon_list = [
        [random.choice(["Knife (light melee)", "Shiv (light melee)", \
            "Iron Pipe (light melee)"]) + quality(), 15],
        [random.choice(["Slingshot (light ranged)", \
            "Bow and Arrow (light ranged)", \
            "Crossbow (light ranged)"]) + quality(), 25],
        ]

    rad_armor_list = [
        ["Light Armor (AP 2)" + quality(), 50],
        ["Medium Armor (AP 4)" + quality(), 100],
        ["Heavy Armor (AP 6)" + quality(), 350],
        ]

    rad_psionic_armor_list = [
        ["Light Armor (AP 2)" + quality(), 50],
        ]

    scraproll = rolldN(4)
    rad_other_list = [
        ["Can of Gasoline (d6 usage die)", 25],
        ["Glowing Water (d6 usage die)", 10],
        ["Rusty Spikes", 1],
        ["Flashlight", 15],
        ["Batteries (d8 usage die)", 10],
        ["{0} Scrap for repairs".format(scraproll), 10 * scraproll]
        ]

    # buy necessities according to class
    if (char_class == "Warrior"):
        result = buy_item_from_list(cash, warrior_armor_list)#buy armor
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, shield_list)#buy a shield
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    if (char_class == "Thief"):
        result = buy_item_from_list(cash, thief_armor_list)#buy armor
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, thief_tool_list)#buy thief tools
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, thief_shield_list)#buy shield
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    if (char_class == "Cleric"):
        result = buy_item_from_list(cash, holy_list)#buy holy item
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, cleric_armor_list)#buy armor
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, shield_list)#buy a shield
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    if (char_class == "Human"):
        result = buy_item_from_list(cash, rad_weapon_list) #buy a weapon
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, rad_armor_list) #buy armor
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, rad_other_list) #buy a RAD item
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, shield_list) #buy a shield
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    if (char_class == "Mut_all_ranged"):
        result = buy_item_from_list(cash, rad_weapon_list) #buy a weapon
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
    if (char_class == "Mut_all_melee"):
        result = buy_item_from_list(cash, rad_weapon_list) #buy a weapon
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
    if (char_class == "Mut_all_melee") or (char_class == "Mut_all_ranged"):
        result = buy_item_from_list(cash,  rad_other_list) #buy a RAD item
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    if (char_class == "Psionic"):
        result = buy_item_from_list(cash, rad_psionic_weapon_list) #buy a weapon
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, rad_psionic_armor_list) #buy armor
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]
        result = buy_item_from_list(cash, rad_other_list) #buy a RAD item
        if result != "no buy":
            purchased_equipment.append(result[0])
            cash = result[1]

    # buy storage (any class)
    result = buy_item_from_list(cash, storage_list)
    if result != "no buy":
        purchased_equipment.append(result[0])
        cash = result[1]
    # buy food and drink (any class)
    result = buy_item_from_list(cash, food_and_drink)
    if result != "no buy":
        purchased_equipment.append(result[0])
        cash = result[1]
    # buy light source (any class)
    result = buy_item_from_list(cash, light_list)
    if result != "no buy":
        purchased_equipment.append(result[0])
        cash = result[1]
    # buy tool (any class)
    result = buy_item_from_list(cash, optional_tool_list)
    if result != "no buy":
        purchased_equipment.append(result[0])
        cash = result[1]

    return [cash, purchased_equipment]

def Buy_Spells(char_class):
    divine_spell_list_lvl1 = [
        "Lvl 1: Cure Light Wounds : Heal 1d8 HP to a Nearby target.",
        "Lvl 1: Detect Evil : Everything Nearby that is evil glows " \
            "for 5 mins.",
        "Lvl 1: Light : Create dim light from a Nearby spot or object " \
            "for 1hr.",
        "Lvl 1: Protection from Evil : Advantage on all harmful tests " \
            "from an Evil source for 1hr.",
        "Lvl 1: Purify Food and Drink : Removes all diseases from all " \
            "Nearby food and drink.",
        ]
    divine_spell_list_lvl2 = [
        "Lvl 2: Bless : Nearby allies gain +1 to stats when making " \
            "attacks and saves for 1hr.",
        "Lvl 2: Find Traps : Notice all nearby traps for 10mins.",
        "Lvl 2: Hold Person : Paralyse 1d4 Nearby targets. Test WIS " \
            "each turn to see if the effect lasts.",
        "Lvl 2: Silence : Magical silence covering everything Nearby to " \
            "a target for 1hr.",
        "Lvl 2: Speak with Animals : Can understand and talk with " \
            "animals - 1hr.",
        ]
    arcane_spell_list_lvl1 = [
        "Lvl 1: Charm : A Nearby target obeys commands. Test WIS each " \
            "turn to see if the effect lasts.",
        "Lvl 1: Detect Magic : Everything Nearby that is magic glows " \
            "for 5 mins.",
        "Lvl 1: Light : Create dim light from a Nearby spot or object " \
            "for 1 hr.",
        "Lvl 1: Magic Missile : A Nearby, Far-Away or Distant target " \
            "takes 1d4 damage/level.",
        "Lvl 1: Shield : Gain 2 AP/ level.","Lvl 1: Sleep : Puts 4d6 HD " \
            "'worth' of beings to sleep - 8hrs.",
        ]
    arcane_spell_list_lvl2 = [
        "Lvl 2: Darkness : Creates darkness covering a Nearby area that " \
            "blocks all types of vision for 1 hr.",
        "Lvl 2: Invisibility : A nearby creature is made invisible until " \
            "it attacks or dispelled.",
        "Lvl 2: Knock : A Nearby door or lock is opened.",
        "Lvl 2: Levitate : The caster floats up to 6 feet from the " \
            "ground - 10mins/level.",
        "Lvl 2: Web : Traps a Nearby area, stopping movement. Test " \
            "WIS/hr to see if the effect lasts.",
        ]

    char_spells = []

    if char_class == "Cleric":
        n_spells = rolldN(4)
        spell = random.choice(divine_spell_list_lvl1)
        divine_spell_list_lvl1.pop(divine_spell_list_lvl1.index(spell))
        char_spells.append(spell)
        switch_to_second_level_spells = rolldN(10)
        for n in range(0, n_spells - 1):
            if (switch_to_second_level_spells == 10):
                spell = random.choice(divine_spell_list_lvl2)
                divine_spell_list_lvl2.pop(divine_spell_list_lvl2.index(spell))
                char_spells.append(spell)
            else:
                spell = random.choice(divine_spell_list_lvl1)
                divine_spell_list_lvl1.pop(divine_spell_list_lvl1.index(spell))
                char_spells.append(spell)
                switch_to_second_level_spells = rolldN(10)

    if char_class == "Conjurer":
        n_spells = rolldN(4) + 2
        spell = random.choice(arcane_spell_list_lvl1)
        arcane_spell_list_lvl1.pop(arcane_spell_list_lvl1.index(spell))
        char_spells.append(spell)
        switch_to_second_level_spells = rolldN(10)
        for n in range(0, n_spells - 1):
            if (switch_to_second_level_spells == 10):
                spell = random.choice(arcane_spell_list_lvl2)
                arcane_spell_list_lvl2.pop(arcane_spell_list_lvl2.index(spell))
                char_spells.append(spell)
            else:
                spell = random.choice(arcane_spell_list_lvl1)
                arcane_spell_list_lvl1.pop(arcane_spell_list_lvl1.index(spell))
                char_spells.append(spell)
                switch_to_second_level_spells = rolldN(10)

    return char_spells



#### HUMANS ####
# Generate stats for humans
if rand_class == "Human":

    # human professions and starting equipment
    human_prof_list = [
        ["Water Merchant",
            "Water Container (d10)\n\tMap to the location " \
            "of a source of clean water"],
        ["Caravan Guard",
            "Light Armor\n\tList of nearby settlements"],
        ["Raider",
            "%s doses of combat-related Drug of choice" % str(rolldN(4))],
        ["Mechanic",
            "Big Wrench (Medium Melee)"],
        ["Survivalist",
            "Water Canteen (d6)\n\tHunting Knife (Light Melee)"],
        ["Shaman",
            "Medical Herbs (d6)\n\tPipe for smoking"],
        ["Sniper",
            "One half of a pair of Binoculars"],
        ["Cage Fighter",
            "Brass Knuckles (Light Melee)"],
        ["Hunter",
            "A small but vicious Hyena (%s HP)" % str(rolldN(4)+2)],
        ["Farmer",
            "Waste Pig named 'Betty'"],
        ["Scavenger",
            "%s Scrap" % str(rolldN(6))],
        ["Drug Dealer",
            "%s Drugs of choice\n\tA debt " \
            "to someone unpleasant" % str(rolldN(4))],
        ["Smuggler",
            "%s extra Slugs and a debt to " \
            "someone powerful" % str((rolldN(6)+rolldN(6))*10)],
        ["Entertainer",
            "Make-up set (d6)\n\tMusical Instrument"],
        ["Archivist",
            "Stack of old books\n\tA pair of glasses"],
        ["Surgeon",
            "Scalpel (Light Melee)"],
        ["Butcher",
            "Meat Cleaver (Medium Melee)"],
        ["Driver",
            "Keys to a vehicle you lost during a bet"],
        ["RAD-Cultist",
            "Glowing Water (d6)\n\tHoly Symbol"],
        ["Common Thief",
            "%s extra slugs" % str(rolldN(6)+rolldN(6))],
        ]

    # choose random profession
    rand_human_prof = random.choice(human_prof_list)

    print "\n"
    print char_name.upper(),"THE",rand_human_prof[0].upper()
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", rand_human_prof[0]
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # choose random weapon proficiency
    rand_human_weap_prof = random.choice(["Up to Heavy Melee and Medium " \
        "Ranged Weapons","Up to Medium Melee and Heavy Ranged Weapons"])

    # print their stats and abilities
    print "HP:", rolldN(8) + 4
    print "HP per level/Resting: d8"
    print "Weapons & Armor:", rand_human_weap_prof, "and any armor and shield"
    print "Attack Damage: 1d8 if armed, 1d6 if unarmed or improvising"
    print "Equipment:\n\t", rand_human_prof[1]
    stat = roll_4d6_drop_lowest()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = roll_3d6()
        else:
            stat = roll_4d6_drop_lowest()
        stat_list.append(stat)
        num = num + 1

    print "\n"

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"

    print "Special Features:"
    print "\tElitist: Humans always have advantage on CHA tests " \
        "against mutants in places dominated by humans."
    print "\tControl Robot: A human can spend an action to attempt " \
        "to Control a Nearby Robot by testing their CHA and adding the " \
        "targets HD to the roll."
    print "\tLeveling up: Roll to see if attributes increase. " \
        "Roll twice for STR and DEX. If a human has the opportunity " \
        "to change her profession, as established in the fiction of " \
        "the game, she may do so the next time she levels up."

    start_cash = start_cash = (roll_3d6() + rolldN(6)) * 10
    purchased = buy_equip(start_cash, "Human")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "\n"
    print "Ammo:", leftover_money, "slugs"
    print "Equipment:\t"
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

    print "\n\n"

#### MUTANTS ####
# Generate stats for mutants
if rand_class == "Mutant":
    # mutant mutations and effects
    mutant_mutations_list = [
        ["Chameleon", "Blend into environment to gain" \
            "advantage on stealth test."],
        ["Winged", "Gain ability to fly up to far-away range."],
        ["Poison Gland", "Unarmed attack poisons target."\
            "Mutant player chooses poison."],
        ["Extendable Claws", "Unarmed attack deals d8+level damage. " \
            "Concealable at will."],
        ["Spines", "Ranged attack shoots spines up to nearby range for " \
            "1d6+level damage."],
        ["Sonar", "Instant sound-based echolocation up to far-away."],
        ["Magnetism", "Attract/repel small, metallic object from/to up " \
            "to nearby distance. Ranged attack with object does " \
            "unarmed+level damage."],
        ["Photosynthesis", "Sunlight replaces food."],
        ["Climber", "Advantage on Climbing test."],
        ["Adrenal Gland (R)", "Act first in Combat Initiative."],
        ["Web", "Ranged attack snares prey."],
        ["Exoskeleton (R)", "Gain 2 Armor Points for the next minute."],
        ["Acid Saliva", "Unarmed attack causes level acid damage and " \
            "coats target in corrosive slime."],
        ["Parasite", "Unarmed attack deals d6+level damage and heals " \
            "the Mutant with half the amount."],
        ["Long Tail", "Advantage on Balance test. Ability to grab small " \
            "objects within close range."],
        ["Pheromone Glands", "Advantage on test to influence target."],
        ["Regeneration", "Pass CON test to heal d6+level hit points."],
        ["Spore Cloud (R)", "Advantage on defensive test."],
        ["Fire Breath", "Ranged attacks that breathes fire for d6+level " \
            "damage up to nearby."],
        ["Amphibian", "Breathe underwater for 10 minutes. "\
            "Advantage on test for moving in water."],
        ]

    # choose first random mutation:
    rand_mut_mutation1 = random.choice(mutant_mutations_list)
    # remove first chosen mutation from list so that it does not repeat:
    mutant_mutations_list.pop(mutant_mutations_list.index(rand_mut_mutation1))
    # choose second random mutation:
    rand_mut_mutation2 = random.choice(mutant_mutations_list)

    print "\n"
    print char_name.upper(),"THE MUTANT"
    print "\n"
    print "Sex:", random.choice(
                ["Male","Female","Male-ish","Female-ish",
                "Hermaphrodite","It's complicated."]
                )
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # generate stats according to mutant class
    # needed first, since it influences weapon proficiency
    stat = mutroll()
    stat_list = [stat]
    for num in range(1,6):
        stat = mutroll()
        stat_list.append(stat)
        num = num + 1

    # print their stats and abilities
    print "HP:", rolldN(6) + 4
    print "HP per level/Resting: d6"
    print "Ability die for mutations: d4"
    if stat_list[1] > stat_list[0]:
        rand_mutant_weap_prof = "All ranged and up to medium melee"
        mut_equip_buy_title = "Mut_all_ranged"
    elif stat_list[0] > stat_list[1]:
        rand_mutant_weap_prof = "All melee and up to medium ranged"
        mut_equip_buy_title = "Mut_all_melee"
    else:
         choice = random.choice([[
            "All ranged and up to medium melee","Mut_all_ranged"],
            ["All melee and up to medium ranged", "Mut_all_melee"]])
         rand_mutant_weap_prof = choice[0]
         mut_equip_buy_title = choice[1]
    print "Weapons & Armor:", rand_mutant_weap_prof, \
        "and up to medium armor and small shields"
    print "Attack Damage: 1d6 if armed, 1d4 if unarmed or improvising"

    print "\n"

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"

    print "Special features:"
    print "\tUsed to the Glow: Mutants exposed to harmful " \
        "radiation roll their CON save with Advantage."
    print "\tLeveling up: roll to see if attributes increase. Roll 1d6 to " \
        "determine what attribute to roll twice for. Increase the ability " \
        "die one step on even levels. Gain a random mutation on uneven " \
        "levels, to a max of five. When gaining a sixth mutation, that one "\
        "replaces the old one."
    print "\tAdaptive: Upon leveling up, a mutant can " \
        "swap two attributes around."
    print "\tMutations: To use a mutation, first test the attributes " \
        "that corresponds with what you are attempting to do, then roll " \
        "the Ability Die to check if it decreases a step. If a roll of " \
        "20 is made while using a mutation, the mutation permanently alters " \
        "the mutant's appearance, has the opposite effect, targets an " \
        "ally, etc."
    print "\t\t", rand_mut_mutation1[0], ":", rand_mut_mutation1[1]
    print "\t\t", rand_mut_mutation2[0], ":", rand_mut_mutation2[1]

    start_cash = start_cash = (rolldN(6) + rolldN(6)) * 10

    purchased = buy_equip(start_cash, mut_equip_buy_title)
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "\n"
    print "Ammo:", leftover_money, "slugs"
    print "Equipment:\t"
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

    print "\n\n"

#### ROBOTS ####
# Generate stats for robots
if rand_class == "Robot":

    # robot modules
    robot_module_list = [
        ["Optical Holoflage", "Mimic surroundings to gain advantage " \
            "on stealth test."],
        ["Jet Booster", "Gain ability to fly up to nearby range."],
        ["Toxin Injector", "Unarmed attack poisons target. " \
            "Robot player chooses poison."],
        ["Double Processors", "Advantage on INT/WIS check."],
        ["Multiple Limbs", "Ability to attack twice."],
        ["Laser Beam", "Shoot energy beam up to far-away range " \
            "for d6+level damage."],
        ["Electric Pulse Discharge", "Lowers the Ability Die one step " \
            "to cause d6+level damage to everyone nearby."],
        ["First Aid Procedure", "Test INT to heal d6+level damage " \
            "to organic target."],
        ["Reactive Armor Plating (R)", "Gain 2 Armor Points for " \
            "the next minute."],
        ["Night Vision Optics", "See in the dark for 10 minutes."],
        ["Loudspeaker", "Shout short command with booming voice, can " \
            "be heard for miles."],
        ["Drone Bay", "Release and control small flying drone: 10 STR, " \
            "10 DEX, 10 HP and does d4 damage. All commands requires " \
            "rolling the Ability Die."],
        ["Auto-Repair Prompt", "Repairs self for d6+level health."],
        ["Laser Targeting Systems", "Gain Advantage against one enemy " \
            "until it is defeated. Only one enemy at a time."],
        ["Energy Shield", "All nearby allies gains 2 AP until " \
            "end of the turn."],
        ["Temperature Adjustment Device", "Set fire to/freeze an object. " \
            "Deal d6+level fire/freezing damage to organic target."],
        ["Decontaminate","Refresh target's Radiation Die by one step."],
        ["Anti EMP Padding (R)", "Advantage against EMP-based attacks."],
        ["Plasma Cannon", "Deals 3d6+level damage, and lowers " \
            "Ability Die by two steps."],
        ["Satellite Uplink", "Contact satellite in orbit for cryptic " \
            "information on one subject. Limited to one use per day."],
        ]

    # choose 2 different random modules
    rand_robot_module1 = random.choice(robot_module_list)
    robot_module_list.pop(robot_module_list.index(rand_robot_module1)) #removes first picked mutation from list
    rand_robot_module2 = random.choice(robot_module_list)

    # print their stats and abilities
    print "\n"
    print char_name.upper(),"THE ROBOT"
    print "\n"
    print "Sex:", char_sex
    print "HP:", rolldN(10) + 4
    print "HP per level/Repair: d10 (Robots use Scrap to " \
        "perform self-repair instead of resting)"
    print "Ability die for module use: d4"
    print "Weapons & Armor: Any pre-apocalypse era weapons, " \
        "armor and shields"
    print "Attack Damage: 1d6 if armed, 1d4 if unarmed or " \
        "improvising"

    print "\n"

    rob_stat_list = rand_robotbuy() # point buy stat_list for robots
    print "STR", rob_stat_list[0]
    print "DEX", rob_stat_list[1]
    print "CON", rob_stat_list[2]
    print "INT", rob_stat_list[3]
    print "WIS", rob_stat_list[4]
    print "CHA", rob_stat_list[5]

    print "\n"

    print "Special Features:"
    print "\tMechanical: Robots are immune to all poisons and radiation. " \
        "They don't require air, food, water or sleep."
    print "\tMetal skin: Robots have 2 AP."
    print "\tLeveling up: Roll to see if attributes increase. Decide what " \
        "attribute to roll twice for, then spend one Scrap + level to " \
        "either increase the Ability Die one step or gain a Module of " \
        "choice to a maximum of four. When gaining a fifth module, that " \
        "one replaces an old one."
    print "\tModules: To use a Module, first test the attribute that " \
        "corresponds with what you are attempting to do, then roll the " \
        "Ability Die to check if it decreases a step. If a roll of 20 is " \
        "made while using a Module, the module shuts down temporarily, has " \
        "the opposite effect, targets an ally, etc."
    print "\t\t", rand_robot_module1[0], ":", rand_robot_module1[1]
    print "\t\t", rand_robot_module2[0], ":", rand_robot_module2[1]

    print "\n"

    start_cash = start_cash = rolldN(6) * 10
    purchased = buy_equip(start_cash, "Human")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "\n"
    print "Ammo:", leftover_money, "slugs"
    print "Equipment:\t"
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

    print "\n\n"

#### PSIONICS ####
# Generate stats for psionics
if rand_class == "Psionic":

    # psionic powers
    psionic_power_list = [
        ["Mental Domination", "Target that is close must obey one " \
            "simple command."],
        ["Healing Energy", "Heal nearby target for d6+level HP."],
        ["Nightmare Visions", "Nearby target panics and tries to run " \
            "away and/or hide."],
        ["Cryokinesis", "Nearby target takes 1d6+level cold damage and " \
            "risks paralyzation."],
        ["Pyrokinesis","Nearby target takes 1d6+level fire damage."],
        ["Empathy","Influence nearby target's mood."],
        ["Telepathy","Read nearby target's mind."],
        ["Telekinetic","Manipulate nearby small to medium size object."],
        ["Psi-Blast","Target takes d10+level damage. Up to far-away range."],
        ["Sleep","Nearby target falls asleep."],
        ["Force Field","All nearby allies gain 2 Armor Points for one minute."],
        ["Illusion","Influence what nearby target sees."],
        ["Sound Imitation","Influence what nearby target hears and from " \
            "where."],
        ["Life Leech","Nearby target takes d6+level damage. User heals " \
            "same amount."],
        ["Directional Sense","Psionic knows which way is north, where the " \
            "closest exit is and cannot get lost."],
        ["Clairvoyance","Get a brief glimpse of a place the Psionic has " \
            "been before."],
        ["Levitation","Levitate up to nearby distance."],
        ["Control Light","Bend light to gain Advantage on stealth test."],
        ["Teleportation","Teleport up to nearby distance."],
        ["Weather Control","Change local weather from cloudy to rain, rain " \
            "to thunder etc."],
        ]

    # choose first random psionic power
    rand_psi_pow1 = random.choice(psionic_power_list)
    # removes the first chosen psionic power from list to prevent repeat
    psionic_power_list.pop(psionic_power_list.index(rand_psi_pow1))
    # choose second random psionic power
    rand_psi_pow2 = random.choice(psionic_power_list)

    print "\n"
    print char_name.upper(),"THE PSIONIC"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # print their stats and abilities
    print "HP:", rolldN(4) + 4
    print "HP per level/Resting: d4"
    print "Ability die for psionics: d4"
    print "Weapons & Armor: Light melee and ranged weapons and light armor"
    print "Attack Damage: 1d4 if armed, 1 if unarmed or improvising"

    print "\n"

    print "STR", rolldN(6) + rolldN(6) + 2
    print "DEX", rolldN(6) + rolldN(6) + 2
    print "CON", rolldN(6) + rolldN(6) + 2
    print "INT", roll_4d6_drop_lowest()
    print "WIS", roll_4d6_drop_lowest()
    print "CHA", roll_4d6_drop_lowest()

    print "\n"

    print "Special Features:"
    print "\tMental Fortitude: Roll with advantage when testing to avoid " \
        "damage or effects from Psionic sources."
    print "\tPrecognition: Psionics can choose to reroll one roll per " \
        "session and will do so with Advantage."
    print "\tLeveling up: Roll to see if attributes increase. Roll twice " \
        "for INT and WIS. Increase the Ability die one step on uneven " \
        "levels. Gain a random Psionic Power on even levels, to a max of " \
        "five. When gaining a sixth Psionic Power, that one replaces " \
        "an old one."
    print "\tPsionic Powers: To use a psionic power, first test the " \
        "attribute that corresponds with what you are attempting to do, " \
        "then roll the Ability Die to check if it decreases a step. If a " \
        "roll of 20 is made while using a psionic power, the user blacks " \
        "out, targets an ally, the psionic power has the opposite effect " \
        "etc. Robots or other constructs are immune to psionic powers, " \
        "unless otherwise stated."
    print "\t\t", rand_psi_pow1[0], ":", rand_psi_pow1[1]
    print "\t\t", rand_psi_pow2[0], ":", rand_psi_pow2[1]

    print "\n"

    start_cash = start_cash = (rolldN(6) + rolldN(6)) * 10
    purchased = buy_equip(start_cash, "Psionic")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "\n"
    print "Ammo:", leftover_money, "slugs"
    print "Equipment:\t"
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

    print "\n\n"


#### WARRIOR ####
# Generate stats for a warrior
if rand_class == "Warrior":
    print "\n"
    print char_name.upper(),"THE WARRIOR"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # print their stats and abilities
    print "HP:", rolldN(10) + 4
    print "HP per level/Resting: d10"
    print "Weapons & Armor: any and all"
    print "Attack Damage: 1d8 if armed, 1d6 if unarmed or improvising"

    print "\n"

    stat = roll_3d6()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = rolldN(6) + rolldN(6) + 2
        else:
            stat = roll_3d6()
        stat_list.append(stat)
        num = num + 1

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"
    print "Special Features:"
    print "\tOnce per hour, whilst in combat, a Warrior can regain d8 lost HP."
    print "\tAs part of their action a Warrior can make 1 attack per level."
    print "\tIf a Warrior fails a STR or DEX test and would be dealt " \
        "damage from an attack, they can opt to sunder (destroy) their " \
        "shield - if they have one equipped - and ignore the damage."

    print "\n"

    print "Leveling up: Roll to see if attributes increase. Roll twice for " \
        "STR and DEX."

    print "\n"

    start_cash = roll_3d6() * 10

    # check if starting weapon is 2-handed or a bow
    # one-in-four chance of favoring a 2-handed weapon
    favor_roll = rolldN(6)
    if favor_roll <= 2:
        starting_weapon = random.choice(["Claymore (2H)",
                                        "Warhammer (2H)",
                                        "Battleaxe (2H)"])
    elif 2 < favor_roll < 6:
        starting_weapon = random.choice(["Sword (1H)", "Mace (1H)", "Axe (1H)"])
    else:
        starting_weapon = "Bow\n\t\tQuiver of Arrows (d10 usage die)"
        start_cash = start_cash - 10 #cost of a quiver of arrows

    purchased = buy_equip(start_cash, "Warrior")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "Money:", leftover_money, "coins"
    print "Equipment:\t", starting_weapon
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

#### THIEF ####
# Generate stats for a thief
if rand_class == "Thief":
    print "\n"
    print char_name.upper(),"THE THIEF"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # print their stats and abilities
    print "HP:", rolldN(6) + 4
    print "HP per level/Resting: d6"
    print "Weapons & Armor: All Swords, All Bows, Daggers, Gambeson, " \
        "Leather, Small Shields"
    print "Attack Damage: 1d6 if armed, 1d4 if unarmed or improvising"

    print "\n"

    stat = roll_3d6()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = rolldN(6) + rolldN(6) + 2
        else:
            stat = roll_3d6()
        stat_list.append(stat)
        num = num + 1

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"
    print "Special Features:"
    print "\tRoll with Advantage when testing DEX to avoid damage or " \
        "effects from traps and magical devices."
    print "\tRoll with Advantage when attacking from behind and deals 2d6 " \
        "or 2d4 + the Thief's level damage."
    print "\tRoll with Advantage when performing delicate tasks, climbing, " \
        "hearing sounds, moving silently, understanding written languages " \
        "and opening locks."

    print "\n"

    print "Leveling up: Roll to see if attributes increase. Roll twice for " \
        "DEX or WIS."

    print "\n"

    start_cash = roll_3d6() * 10

    # check if starting weapon is 2-handed or a bow
    # one-in-four chance of favoring a 2-handed weapon
    favor_roll = rolldN(6)
    if favor_roll <= 2:
        starting_weapon = random.choice(["Dagger x2"])
    elif 2 < favor_roll < 6:
        starting_weapon = random.choice(["Sword (1H)","Dagger"])
    else:
        starting_weapon = "Bow\n\t\tQuiver of Arrows (d10 usage die)"
        start_cash = start_cash - 10 #cost of a quiver of arrows

    purchased = buy_equip(start_cash, "Thief")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "Money:", leftover_money, "coins"
    print "Equipment:\t", starting_weapon
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]

#### CLERIC ####
# Generate stats for a cleric
if rand_class == "Cleric":
    print "\n"
    print char_name.upper(),"THE CLERIC"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # print their stats and abilities
    print "HP:", rolldN(8) + 4
    print "HP per level/Resting: d8"
    print "Weapons & Armor: All Blunt Weapons, Gambeson, Leather, " \
        "Chain Mail, All Shields"
    print "Attack Damage: 1d6 if armed, 1d4 if unarmed or improvising"

    print "\n"

    stat = roll_3d6()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = rolldN(6) + rolldN(6) + 2
        else:
            stat = roll_3d6()
        stat_list.append(stat)
        num = num + 1

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"
    print "Special Features:"
    print "\tRoll with Advantage when testing CON to avoid damage from " \
        "poison or being paralyzed."
    print "\tA Cleric can spend an action to banish all Nearby undead by " \
        "testing their WIS and adding the creatures' HD to the roll."
    print "\tDivine Spellcasting: Beginning at second level, Clerics can " \
        "cast a number of Divine Spells per day, see the Spellcasting section."

    print "\n"

    print "Leveling up: Roll to see if attributes increase. Roll twice " \
        "for STR or WIS."

    print "\n"

    start_cash = roll_3d6() * 10

    # check if starting weapon is 2-handed or a bow
    # one-in-four chance of favoring a 2-handed weapon
    favor_roll = rolldN(6)
    if favor_roll <= 2:
        starting_weapon = random.choice(["Warhammer (2H)", "Dire Flail (2H)"])
    else:
        starting_weapon = random.choice(["Mace (1H)", "Flail (1H)", \
            "Morningstar (1H)"])

    purchased = buy_equip(start_cash, "Cleric")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "Money:", leftover_money, "coins"
    print "Equipment:\t", starting_weapon
    for n in range(0, len(purchased_gear_list)):
        print "\t\t", purchased_gear_list[n]
    print "Spellbook:"
    spells = Buy_Spells(rand_class)
    for n in range(0, len(spells)):
        print "\t\t", spells[n]

#### CONJURER ####
# Generate stats for a conjurer
if rand_class == "Conjurer":
    print "\n"
    print char_name.upper(),"THE CONJURER"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"
    # print their stats and abilities
    print "HP:", rolldN(4) + 4
    print "HP per level/Resting: d4"
    print "Weapons & Armor: 1-handed Sword and Staff"
    print "Attack Damage: 1d8 if armed, 1d6 if unarmed or improvising"

    print "\n"

    stat = roll_3d6()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = rolldN(6) + rolldN(6) + 2
        else:
            stat = roll_3d6()
        stat_list.append(stat)
        num = num + 1

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"
    print "Special Features:"
    print "\tRoll with Advantage when testing INT to avoid damage or " \
        "effects from spells or magical devices."
    print "\tArcane Spellcasting: Conjurers can cast a number of Arcane " \
        "Spells per day, see the Spellcasting section."

    print "\n"

    print "Leveling up: Roll to see if attributes increase. Roll twice for " \
        "INT or WIS."

    print "\n"

    start_cash = roll_3d6() * 10

    # check if starting weapon is 2-handed or a bow
    # one-in-four chance of favoring a 2-handed weapon
    favor_roll = rolldN(6)
    if favor_roll <= 3:
        starting_weapon = "Staff (2H)"
    else:
        starting_weapon = "Sword (1H)"

    purchased = buy_equip(start_cash, "Conjurer")
    leftover_money = purchased[0]
    purchased_gear_list = purchased[1]

    print "Money:", leftover_money, "coins"
    print "Equipment:\t", starting_weapon
    for n in range(0, len(purchased_gear_list)):
        print "\t\t",purchased_gear_list[n]
    print "Spellbook:"
    spells = Buy_Spells(rand_class)
    for n in range(0, len(spells)):
        print "\t\t", spells[n]


#### MAZE RAT ####
# Generate stats for a Maze Rat (black hack conversion)
if rand_class == "Maze Rat":
    print "\n"
    print char_name.upper(),"THE MAZE RAT"
    print "\n"
    print "Sex:", char_sex
    print "Appearance:", physical_description
    print "Detail:", physical_detail
    print "Background:", background
    print "Clothing:", clothing
    print "Personality:", personality
    print "Mannerism:", mannerism
    print "\n"

    # check if starting weapon is 2-handed or a bow
    # one-in-four chance of favoring a 2-handed weapon
    favor_roll = rolldN(6)
    if favor_roll <= 2:
        starting_weapon = random.choice(["Claymore (2H)",
                                        "Warhammer (2H)",
                                        "Battleaxe (2H)"])
    elif 2 < favor_roll < 6:
        starting_weapon = random.choice(["Sword (1H)", "Mace (1H)", "Axe (1H)"])
    else:
        starting_weapon = "Bow and Quiver of Arrows (d10 usage die)"

    # Randomly choose feature here
    feature_roll = rolldN(3)
    if feature_roll == 1:
        extraprof = random.choice([
            "all shields",
            "all armors",
            "all weapons",
            ])

        feature = "+1 time per combat, gain advantage on a STR or DEX test " \
            "when attacking or defending." \
            "\n+2 to max hp (already applied) " \
            "\nProficiency with " + extraprof + " (already applied)"
        extrahp = 2

    elif feature_roll == 2:
        feature = "A spell slot that currently contains:\n\t" \
            + rand_maze_rat_spell()
        extrahp = 0
        extraprof = ""
    else:
        path = random.choice([
            "Briarborn: tracking, foraging, survival",
            "Fingersmith: tinkering, picking locks or pockets",
            "Roofrunner: climbing, leaping, balancing",
            "Shadowjack: moving silently, hiding in shadows",
            ])
        feature = "Gain advantage on tests related to the following path:\n\t" \
            + path
        extrahp = 0
        extraprof = ""

    if extraprof != "all weapons":
        weaponprof = starting_weapon
    else:
        weaponprof = extraprof

    if extraprof != "all shields":
        shieldprof = ", small shields"
    else:
        shieldprof = ", " + extraprof

    if extraprof != "all armors":
        armorprof = ", and gambeson"
    else:
        armorprof = ", and " + extraprof

    # print their stats and abilities
    print "HP:", rolldN(6) + 4 + extrahp
    print "HP per level/Resting: d6"

    print "Weapons & Armor: " + weaponprof + shieldprof + armorprof
    print "Attack Damage: 1d6 if armed, 1d4 if unarmed or improvising"

    print "\n"

    stat = roll_3d6()
    stat_list = [stat]
    for num in range(1,6):
        if stat >= 15:
            stat = rolldN(6) + rolldN(6) + 2
        else:
            stat = roll_3d6()
        stat_list.append(stat)
        num = num + 1

    print "STR", stat_list[0]
    print "DEX", stat_list[1]
    print "CON", stat_list[2]
    print "INT", stat_list[3]
    print "WIS", stat_list[4]
    print "CHA", stat_list[5]

    print "\n"
    print "Special Features:"
    print feature
    print "\n"

    print "Leveling up: Roll to see if attributes increase. Roll twice for " \
        "your attribute of choice. On even-numbered levels, choose a class " \
        "feature from the following list: " \
        "\n\t+1 time per combat, gain advantage on a STR or DEX test when " \
        "attacking or defending. Additionally, gain +2 max hp and " \
        "proficiency with all weapons, all armors, or all shields." \
		"\n\t+1 spell slot and cast +1 spell per day." \
		"\n\tChoose one path from the four below. Gain advantage on related " \
        "tests." \
		"\n\t\tBriarborn: tracking, foraging, survival" \
		"\n\t\tFingersmith: tinkering, picking locks or pockets" \
		"\n\t\tRoofrunner: climbing, leaping, balancing" \
		"\n\t\tShadowjack: moving silently, hiding in shadows"

    print "\n"

    print "Money: 0 coins"
    print "Equipment:\t", starting_weapon
