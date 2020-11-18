# easter | Training Manager script

text = "#e#bHi There #h0# !#k\r\n I'm The #rTraining Manager!#k#n\r\n"
text += "#eSelect the Type of the Training Grounds:#n#b#e\r\n"
text += "#L0#Level 10 ~ 99#l\r\n"
text += "#L1#Level 100 ~ 199#l\r\n"
text += "#L2#Level 200 ~ 250#l\r\n"
text += "#L3#Bosses#l\r\n"
text += "\r\n#k#eYou can call me with the commands:\r\n#r@training, @train, @maps#n"
selection = sm.sendNext(text)


if selection == 0:
    text = "#eSelect a Training Map (Level 10 ~ 99):#n\r\n"
    text += "#r[Recommend LV] - [Monster Name] (Monster LV)#b#e\r\n"

    text += "#L100040300#Level 10 - Flaming Mixed Golems (19)#l\r\n"
    text += "#L101030100#Level 20 - Curse Eye (27)#l\r\n"
    text += "#L101070100#Level 25 - Firefly Slime (30)#l\r\n"
    text += "#L101071200#Level 30 - Mystic Wisp (32)#l\r\n"
    text += "#L120041800#Level 35 - Seashell Octopus Slime (42)#l\r\n"
    text += "#L141030100#Level 40 - Possible-Evil seal (53)#l\r\n"
    text += "#L102030000#Level 45 - Wild Boar (55)#l\r\n"
    text += "#L102040301#Level 50 - Skeledog (62)#l\r\n"
    text += "#L105010000#Level 55 - Copper Drake (66)#l\r\n"
    text += "#L200010301#Level 60 - Jr. lucida (72)#l\r\n"
    text += "#L200010302#Level 65 - Lucida (73)#l\r\n"
    text += "#L230020101#Level 70 - Krip (77)#l\r\n"
    text += "#L211040000#Level 75 - Dark Pepe (79)#l\r\n"
    text += "#L260020700#Level 80 - Sand Rat (89)#l\r\n"
    text += "#L261010003#Level 85 - Triple Rumo (93)#l\r\n"
    text += "#L261020401#Level 90 - Saitie (95)#l\r\n"
    text += "#L261020500#Level 90 - Neo Huroid (95)#l\r\n"
    text += "#L300030200#Level 95 - Ancient Fairy (100)#l\r\n"
    sm.warp(sm.sendNext(text))

elif selection == 1:
    text = "#eSelect a Training Map (Level 100 ~ 199):#n\r\n"
    text += "#r[Recommend LV] - [Monster Name] (Monster LV)#b#e\r\n"

    text += "#L240010100#Level 100 - Dark Rash (104)#l\r\n"
    text += "#L240010200#Level 105 - Hobi (105)#l\r\n"
    text += "#L220011000#Level 110 - Toy Trojan (113)#l\r\n"
    text += "#L220020100#Level 110 - Robo (113)#l\r\n"
    text += "#L220030100#Level 115 - Master Robo (114)#l\r\n"
    text += "#L211040600#Level 120 - Dark Yeti and Pepe (121)#l\r\n"
    text += "#L250020300#Level 125 - Wooden Targer Dummy (126)#l\r\n"
    text += "#L224000142#Level 135 - Yellow King Goblin (140)#l\r\n"
    text += "#L240030102#Level 140 - Dark Cornian (142)#l\r\n"
    text += "#L240040521#Level 150 - Nest Golem (150)#l\r\n"
    text += "#L271010100#Level 160 - Mutant Snail (162)#l\r\n"
    text += "#L271000200#Level 165 - Mutant Tiru (165)#l\r\n"
    text += "#L271010300#Level 170 - Mutant Slime (166)#l\r\n"
    text += "#L273010000#Level 190 - Swollen Stump (190)#l\r\n"
    text += "#L273030100#Level 195 - Pillaging Iron Boar (193)#l\r\n"
    text += "#L273040100#Level 195 - Sinister Rocky Mask (195)#l\r\n"
    text += "#L273060100#Level 195 - Ancient Golem (196)#l\r\n"
    text += "#L273060300#Level 195 - Ancient Golem (198)#l\r\n"
    text += "#L310070130#Level 199 - Chaseroid Red (204)#l\r\n"
    text += "#L310070160#Level 199 - Chaseroid Blue (208)#l\r\n"

    sm.warp(sm.sendNext(text))

elif selection == 2:
    text = "#eSelect a Training Map (Level 100 ~ 199):#n\r\n"
    text += "#r[Recommend LV] - [Monster Name] (Monster LV)#b#e\r\n"

    text += "#L105300301#Level 220 - Dark Demon Wolfrider (228)#l\r\n"
    text += "#L310070200#Level 210 - Modded Deliverbot (212)#l\r\n"
    text += "#L100040300#Level 10 - Flaming Mixed Golems (19)#l\r\n"
    text += "#L101030100#Level 20 - Curse Eye (27)#l\r\n"
    text += "#L101070100#Level 25 - Firefly Slime (30)#l\r\n"
    text += "#L101071200#Level 30 - Mystic Wisp (32)#l\r\n"
    text += "#L120041800#Level 35 - Seashell Octopus Slime (42)#l\r\n"
    text += "#L141030100#Level 40 - Possible-Evil seal (53)#l\r\n"
    text += "#L102030000#Level 45 - Wild Boar (55)#l\r\n"
    text += "#L102040301#Level 50 - Skeledog (62)#l\r\n"
    text += "#L105010000#Level 55 - Copper Drake (66)#l\r\n"
    text += "#L200010301#Level 60 - Jr. lucida (72)#l\r\n"
    text += "#L200010302#Level 65 - Lucida (73)#l\r\n"
    text += "#L230020101#Level 70 - Krip (77)#l\r\n"
    text += "#L211040000#Level 75 - Dark Pepe (79)#l\r\n"
    text += "#L260020700#Level 80 - Sand Rat (89)#l\r\n"
    text += "#L261010003#Level 85 - Triple Rumo (93#l\r\n"
    text += "#L261020401#Level 90 - Saitie (95)#l\r\n"
    text += "#L261020500#Level 90 - Neo Huroid (95)#l\r\n"
    text += "#L300030200#Level 95 - Ancient Fairy (100)#l\r\n"
    text += "#L240010100#Level 99 - Dark Rash (104)#l\r\n"
    text += "#L240010200#Level 99 - Hobi (105)#l\r\n"
    sm.warp(sm.sendNext(text))

elif selection == 3:
    text = "#eSelect a Boss Map:#n\r\n"
    text += "#r[Recommend LV] - [Monster Name] (Monster LV)#b#e\r\n"
    text += "#L211042300#Zakum#l\r\n"
    text += "#L240050400#Horntail#l\r\n"
    text += "#L270050000#Pink Bean#l\r\n"
    text += "#L262030000#Hilla#l\r\n"
    text += "#L211070000#Von Leon#l\r\n"
    text += "#L272020110#Arkarium#l\r\n"
    text += "#L271040000#Cygnus#l\r\n"
    text += "#L105200000#Root Abyss#l\r\n"
    text += "#L401060000#Magnus#l\r\n"
    text += "#L350060300#Lotus#l\r\n"
    text += "#L105300303#Damian#l\r\n"
    text += "#L450004000#Lucid#l\r\n"
    sm.warp(sm.sendNext(text))

sm.dispose()