# Ms. Tan (1012105) | Hair, Eyes and Skin Manager

salonName = ["Tel Aviv", "Haifa", "Beer Sheva", "Kiryat Malachi", "Eilat"]

#listed by salons.
maleHairs = [[33040, 30060, 32350, 33170, 30210, 33100, 30610],[30320, 30330, 30150, 30900, 30170, 30180, 30820, 30410, 30460],[30350, 30760, 30330, 30560, 30040, 30730, 30470, 30460],[30130, 33040, 30850, 30780, 30040, 30920, 30860],[30250, 30190, 30660, 30870, 30840, 30160, 30640]]
femaleHairs = [[32360, 34400, 31820, 34270, 31860, 34210, 34250, 34490, 31360],[31090, 31190, 31040, 31420, 31330, 31340, 31620, 31660],[31310, 31490, 37810, 31130, 31160, 31500, 31230, 31320, 31560, 34190, 31530],[31060, 34090, 31520, 31880, 31140, 31330, 31440, 31760, 31750],[31810, 31550, 31830, 31840, 31680, 31290, 31270, 31870]]

malePlasticSurgery = [[20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 20008, 20009, 20011, 20012, 20013, 20014, 20015, 20016, 20017, 20018, 20020], [20021, 20022, 20025, 20027, 20028, 20029, 20030, 20031, 20032, 20036, 20037, 20040], [20043, 20044, 20045, 20046, 20047, 20048, 20049, 20050, 20051, 20052, 20053, 20055, 20056, 20057, 20058, 20059, 20060], [20061, 20062, 20063, 20064, 20065, 20066, 20067, 20068, 20069, 20070, 20074, 20075, 20076, 20077, 20080, 20081, 20082, 20083, 20084, 20085, 20086, 20087, 20088, 20089, 20090], [20093, 20094, 20095, 20097, 20098, 20099, 20110], [23000, 23001, 23002, 23003, 23005, 23006, 23008, 23010, 23011, 23012, 23015, 23016, 23017, 23018, 23019, 23020, 23023, 23024, 23025, 23026, 23027, 23028, 23029, 23031, 23032, 23033, 23035, 23038, 23039, 23040, 23041, 23042, 23043, 23044, 23053, 23054, 23056, 23057, 23060, 23061, 23062, 23063, 23067, 23068, 23069, 23072, 23073, 23074, 23075, 23079, 23080, 23081, 23082, 23083, 23084, 23085, 23086, 23087, 23088, 23089, 23090, 23091, 23092, 23095, 23096, 23097, 23099, 24061, 24098, 25006, 25007, 25011, 25014, 25016, 25017, 25021, 25022, 25023, 25024, 25025, 25027, 25033, 25058, 25057, 25049, 25053, 25029, 25020, 25043, 25044, 25063, 25062, 25050, 25080, 25079, 25083, 25055, 25085, 25088, 25089,23000, 23001, 23002, 23003, 23005, 23006, 23008, 23010, 23011, 23012, 23015, 23016, 23017, 23018, 23019, 23020, 23023, 23024, 23025, 23026, 23027, 23028, 23029, 23031, 23032, 23033, 23035, 23038, 23039, 23040, 23041, 23042, 23043, 23044, 23053, 23054, 23056, 23057, 23060, 23061, 23062, 23063, 23067, 23068, 23069, 23072, 23073, 23074, 23075, 23079, 23080, 23081, 23082, 23083, 23084, 23085, 23086, 23087, 23088, 23089, 23090, 23091, 23092, 23095, 23096, 23097, 23099, 25000, 25004, 25005, 25006, 25007, 25008, 25011, 25014, 25015, 25016, 25017, 25020, 25021, 25022, 25023, 25024, 25025, 25026, 25027, 25029, 25033, 25043, 25044, 25045, 25046, 25047, 25048, 25049, 25051, 25053, 25057, 25063, 25062]]
femalePlasticSurgery = [[21002, 21003, 21004, 21005, 21006, 21007, 21008, 21009, 21010, 21011, 21012, 21013, 21014, 21015, 21016, 21017, 21020, 21021, 21023], [21024, 21026, 21027, 21028, 21029, 21030, 21031, 21033, 21036, 21038, 21041, 21042], [21043, 21044, 21045, 21048, 21050, 21052, 21053, 21056, 21058, 21059, 21061, 21062, 21063, 21065, 21073, 21074, 21075], [21077, 21078, 21079, 21080, 21081, 21082, 21083, 21084, 21085, 21089, 21090, 21091, 21092, 21093, 21094, 21095, 21096, 21097, 21098, 24002, 24003, 24004, 24007, 24008, 24011], [24012, 24014, 24015, 24018, 24020, 24021, 24022, 24023, 24027, 24031, 24035, 24037, 24038, 24039, 24041, 24050, 24055, 24058, 24060, 24067, 24068, 24071, 24072, 24073, 24077, 24080, 24081, 24084, 24087, 24088, 24091, 24097, 24099, 25000, 25008, 25015, 25099, 26003, 26004, 26005, 26009, 26014, 26017, 26022, 26023, 26027, 26028, 26029, 26030, 26031, 26032, 26062, 26061, 26053, 26056, 26034, 26026, 26046, 26067, 26066, 26054, 26086, 26085, 25155, 26089, 26091, 26094, 26095,24001, 24002, 24003, 24004, 24007, 24008, 24011, 24012, 24014, 24015, 24018, 24020, 24021, 24023, 24027, 24031, 24035, 24038, 24039, 24041, 24050, 24058, 24060, 24068, 24071, 24072, 24073, 24077, 24084, 24087, 24088, 24091, 24097, 24099, 25006, 25008, 26003, 26004, 26005, 26008, 26009, 26014, 26017, 26022, 26023, 26026, 26027, 26028, 26029, 26030, 26031, 26032, 26034, 26046, 26047, 26048, 26049, 26050, 26051, 26053, 26056, 26058, 26764, 26763, 26762, 26761, 26760, 26759, 25057, 25157, 26066, 26067]]

skinList = [0, 1, 2, 3, 4, 9, 10, 11, 12, 13];

text = "#b#eHey Beautiful!#k\r\nI'm the #rHair, Eyes and Skin Manager!#n#k\r\n"
text += "#bWhat would you like to do with your body?#e\r\n"
text += "#L0#Hair#l\r\n#L1#Eyes#l\r\n#L2#Skin#l\r\n#L3#Hair Color#l\r\n#L4#Eye Color#l\r\n#r#L4#Nothing, I'm fine for now.#l"
selection = sm.sendNext(text)

if selection == 0 or selection == 1: #Hair Selection or Face Selection
    text = "#k#eChoose a #bBarber City#k#b\r\n"
    text += "#L0#Tel Aviv#l\r\n"
    text += "#L1#Haifa#l\r\n"
    text += "#L2#Beer Sheva#l\r\n"
    text += "#L3#Kiryat Malachi#l\r\n"
    text += "#L4#Eilat#l\r\n"
    userSelect = sm.sendNext(text)
    al = chr.getAvatarData().getAvatarLook()
    if selection == 0:
        hairColour = al.getHair() % 10
        if al.getGender() == 0:
            options = maleHairs[userSelect]
        else:
            options = femaleHairs[userSelect]
        options = list(map(lambda x: x + hairColour, options))
        answer = sm.sendAskAvatar("#e#b" + salonName[userSelect] + " Barber Shop!\r\n#gChoose Your New Hairstyle!", False, False, options)
        if answer < len(options):
            sm.changeCharacterLook(options[answer])
    else:
        if al.getGender() == 0:
            options = malePlasticSurgery[userSelect]
        else:
            options = femalePlasticSurgery[userSelect]
        answer = sm.sendAskAvatar("#e#b" + salonName[userSelect] + " Plastic Surgery Facility!\r\n#gChoose Your New Face!", False, False, options)
        if answer < len(options):
            sm.changeCharacterLook(options[answer])

elif selection == 2: #Skin Selection
    answer = sm.sendAskAvatar("#e#b" + salonName[0] + " Skin Facility!\r\n#gChoose Your best matching color!", False, False, skinList)
    if answer < len(skinList):
        sm.changeCharacterLook(skinList[answer])

elif selection == 3: #Hair Selection
    pHair = int(chr.getAvatarData().getAvatarLook().getHair() / 10) * 10
    hairColorList = [pHair, pHair + 1, pHair + 2, pHair + 3, pHair + 4, pHair + 5, pHair +6, pHair + 7]
    answer = sm.sendAskAvatar("#e#b" + salonName[0] + " Skin Facility!\r\n#gChoose Your best matching color!", False, False, hairColorList)
    if answer < len(hairColorList):
        sm.changeCharacterLook(hairColorList[answer])

elif selection == 4: #Eye Color
    pFace = chr.getAvatarData().getAvatarLook().getFace()
    eyeColorList = [pFace, pFace + 100, pFace + 200, pFace + 300, pFace + 400, pFace + 500, pFace +600, pFace + 700]
    answer = sm.sendAskAvatar("#e#b" + salonName[0] + " Eye Color Facility!\r\n#gChoose Your best matching color!", False, False, eyeColorList)
    if answer < len(eyeColorList):
        sm.changeCharacterLook(eyeColorList[answer])

else:
    text = "#b#eNo problem.\r\nI'm sure you look amazing as you are right now!"
    sm.sendNext(text)
    sm.dispose()

sm.sendSayOkay("#b#eEnjoy Beautiful! <3")
sm.dispose()



