# Spegelmann (9201595) | Cash Shop Manager

char = sm.getChr()
maplePoints = char.getMaplePoints()
face_emoji = {5160000,5160001,5160002,5160003,5160004,5160005,5160006,5160007,5160008,5160009,5160010,5160011,5160012,5160013,5160014,5160015,5160016,5160017,5160034,5160035,5160036}
hat = {5160000}
top = {5160000}
pants = {5160000}
overall = {5160000}
shoes = {5160000}
gloves = {5160000}
weapon = {5160000}
face_accessory = {5160000}
cape = {5160000}

dict = {
    0 : (face_emoji, 1500),
    1 : (hat, 2000),
    2 : (top, 1500),
    3 : (pants, 1500),
    4 : (overall, 2500),
    5 : (shoes, 1250),
    6 : (gloves, 1250),
    7 : (weapon, 2500),
    8 : (face_accessory, 1000),
    9 : (cape, 1500)
}
select = 0 #important for the starting of the while loops (for returning to the main menu)

text = "#b#eYo #h0#!#k\r\nI'm the #rCash Shop Manager!#n#k\r\n"
text += "#b#eYou have " + str(maplePoints) + " Maple Points.#k\r\n"
text += "#eFor the right price I can sell you any #bCash Shop#k item.\r\n"
text += "Click #bNext#k to trade with me."
#text += "#L0#Hair#l\r\n#L1#Eyes#l\r\n#L2#Skin#l\r\n#r#L3#Nothing, I'm fine for now.#l"
sm.sendNext(text)

while select == 0:
    text = "#b#eWhich cash item do you want to buy ?\r\n"
    text += "#L0#Face Emoji \t\t\tPrice: 1500#l\r\n"
    text += "#L1#Hat \t\t\t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L2#Top \t\t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L3#Pants \t\t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L4#Overall \t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L5#Shoes \t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L6#gloves \t\t\t\t\tPrice: 1500#l\r\n"
    text += "#L7#Weapons \t\t\t\tPrice: 1500#l\r\n"
    text += "#L8#Face Accessory \tPrice: 1500#l\r\n"
    text += "#L9#Cape \t\t\t\t\t\tPrice: 1500#l\r\n"
    selection = sm.sendNext(text)

    price = dict[selection][1]
    text = "#b#eEach Item Cost " + str(price) + ".#k\r\n#eYou have #r"+ str(maplePoints) +"#k Maple Points.#b\r\n"
    for i in dict[selection][0]:
        text += "#L" + str(i) + "##v" + str(i) + "#\t#t " + str(i) + "#\r\n"
    text += "#L0##rBack#l"
    select = sm.sendNext(text)
    if select != 0:
        if maplePoints < price:
            sm.sendNext("#eI'm sorry, but you don't have enough Maple Points.")
            select = 0
        else:
            sm.sendNext("#b#eYou Bought #v" + str(select) + "# Successfully.")
            sm.giveItem(select)
            char.addMaplePoint(-price)

sm.sendSayOkay("#b#eBye Beautiful! <3, you selected: ")
sm.dispose()
