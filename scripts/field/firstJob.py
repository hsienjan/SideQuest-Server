#making firstJob for the new characters First job Manager

#~~~MAIN WEAPON~~~
HAND_CANNON = 				1532000
GUN = 						1492065
TWO_HANDED_SWORD = 			1402001
ONE_HANDED_SWORD = 			1302007
TWO_HANDED_AXE =   			1412001
ONE_HANDED_AXE =  			1312000
TWO_HANDED_MACE =  			1422000
ONE_HANDED_MACE = 			1322000  #LVL 15
SPEAR =						1432000
POLE_ARM = 					1442000
STAFF =						1382000
WAND = 						1372002 #LVL 18
BOW = 						1452054
CROSSBOW = 					1462047
CLAW = 						1472000
DAGGER = 					1332007
KNUCKLE = 					1482000
SOUL_SHOOTER_AB = 			1222076  #LVL 20
DUAL_BOWGUNS = 				1522000
HEAVY_SWORD_ZERO =     		1562000
LONGS_WORD_ZERO =  			1572000
KATANA_HAYATO =  			1542000
DESPERADO_DEMON_AVENGER = 	1232001
ARM_CANNON_BLASTER =  		1582000
WHIP_BLADE_XENON =     		1242001
CANE = 						1362001
KATARA_DUAL_BLADES =  		1342023
SHINING_ROD_LUMINOUS =     	1212001
FAN_KANNA =  				1552000
BEAST_TAMER_SCEPTER_BT =   	1252001
PSY_LIMITER_KINESIS = 		1262000

#~~~SECONDARY WEAPON~~~
PHANTOM_S = 				1352100
HERO_S = 					1352200
PALADIN_S = 				1352210
DARK_KNIGHT_S = 			1352220
FP_MAGICIAN_S = 			1352230
IL_MAGICIAN_S =		    	1352240
BISHOP_S = 			    	1352250
HUNTER_S =			    	1352260
CROSSBOWMAN_S = 			1352270
BANDIT_S =			    	1352280
ASSASSIN_S = 				1352290
LUMINOUS_S =				1352400
KAISER_S =			    	1352500
ANGELIC_BUSTER_S = 	    	1352600
MECHANICS_S =    			1352700
HAYATO_S = 			    	1352800
BEAST_TAMER_S = 			1352810
JETT_S = 					1352820
BRAWLER_S = 				1352900
GUN_SLINGER_S = 			1352910
CANNONEER_S =				1352920
ARAN_S = 					1352930
EVAN_S = 					1352940
BATTLE_MAGE_S = 			1352950
WILD_HUNTER_S =		    	1352960
CYGNUS_S = 			    	1352970
MIHILE_S = 			    	1098000
DEMON_AVENGER_SLAYER_S = 	1099000
SHADE_S =                   1353100

#~~~USE~~~
BULLETS = 					2330000
ARROWS_FOR_BOW = 			2060004
ARROWS_FOR_CROSSBOW =   	2061004
THROWING_STARS = 			2070010
MERCEDES_ARROW = 			1352000

DEMON_SKILLS = [30011109, 30010110, 30010185]

finalJobID = sm.getChr().getFinalJob()

def finalJob():
    MAPLE_ADMINISTARTOR = 2007

    target_level = 10
    sm.setSpeakerID(MAPLE_ADMINISTARTOR)
    sm.removeEscapeButton()
    char = sm.getChr()
    jobID = int(char.getJob())
    subJobID = char.getSubJob()

    selection = 0
    ap = 0

    sm.setBoxChat()
    sm.sendNext("#b#eWelcome to SideQuest, #h0# !#k \r\nFirst Let's Make you Level #r10!#k\r\nAnd Then Pick Your #gFINAL JOB!#k")
    if char.getLevel() < target_level:
        sm.addLevel(target_level - char.getLevel())
    char.closeUI(2)
    char.closeUI(3)
    #BEGINNER
    if jobID == 0:
        #DUAL_BLADE
        if subJobID == 1:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eBLADE MASTER #l"
            sm.sendNext(text)
            sm.jobAdvance(400)
            char.setFinalJob(434)
            sm.giveItem(DAGGER)
            sm.giveItem(KATARA_DUAL_BLADES)
        #CANNONEER
        elif subJobID == 2:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eCANNONEER #l"
            sm.sendNext(text)
            sm.jobAdvance(501)
            char.setFinalJob(532)
            sm.giveItem(HAND_CANNON)
            sm.giveItem(CANNONEER_S)
        #JETT
        elif subJobID == 10:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eJETT #l"
            sm.sendNext(text)
            sm.jobAdvance(508)
            char.setFinalJob(572)
            sm.giveItem(GUN)
            sm.giveItem(BULLETS, 4800)
            sm.giveItem(JETT_S)
        #adventure (warrior, magician, thief, archer)
        else:
            while True:
                text = "#bSelect the Class That You Want to Become?\r\n"
                text += "#b#L0#Warrior#l\r\n#L1#Magician#l\r\n#L2#Archer#l\r\n#L3#Thief#l\r\n#L4#Pirate#l\r\n"

                selection = sm.sendNext(text)
                text = "#rSelect your #eFINAL JOB:#n\r\n"
                if selection == 0:
                    text += "#b#L0#(FIGHTER => CRUSADER =>) #eHERO#n #l\r\n#L1#(PAGE => WHITEKNIGHT =>) #ePALADIN#n #l\r\n#L2#(SPEARMAN => DRAGONKNIGHT =>) #eDARKKNIGHT#l\r\n#L3##e#rGo Back#l"
                    jobSelection = sm.sendPrev(text)
                    if jobSelection == 0:
                        sm.jobAdvance(100)
                        char.setFinalJob(112)
                        sm.giveItem(TWO_HANDED_SWORD)
                        sm.giveItem(TWO_HANDED_AXE)
                        sm.giveItem(HERO_S)
                    elif jobSelection == 1:
                        sm.jobAdvance(100)
                        char.setFinalJob(122)
                        sm.giveItem(TWO_HANDED_SWORD)
                        sm.giveItem(TWO_HANDED_MACE)
                        sm.giveItem(PALADIN_S)
                    elif jobSelection == 2:
                        sm.jobAdvance(100)
                        char.setFinalJob(132)
                        sm.giveItem(SPEAR)
                        sm.giveItem(POLE_ARM)
                        sm.giveItem(DARK_KNIGHT_S)
                    if jobSelection != 3:
                        break
                elif selection == 1:
                    text += "#b#L0#(F&P WIZARD => MAGE =>) #eFIRE & POISON ARCHMAGE#n #l\r\n#L1#(I&L WIZARD => MAGE =>) #eICE & LIGHTNING ARCHMAGE#n #l\r\n#L2#(CLERIC => PRIEST =>) #eBISHOP#l\r\n#L3##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(200)
                        char.setFinalJob(212)
                        sm.giveItem(FP_MAGICIAN_S)
                    elif jobSelection == 1:
                        sm.jobAdvance(200)
                        char.setFinalJob(222)
                        sm.giveItem(IL_MAGICIAN_S)
                    elif jobSelection == 2:
                        sm.jobAdvance(200)
                        char.setFinalJob(232)
                        sm.giveItem(BISHOP_S)
                    if jobSelection != 3:
                        sm.giveItem(STAFF)
                        sm.giveItem(WAND)
                        break
                elif selection == 2:
                    text += "#b#L0#(HUNTER => RANGER =>) #eBOWMASTER#n #l\r\n#L1#(CROSSBOWMAN => SNIPER =>) #eMARKSMAN#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(300)
                        char.setFinalJob(312)
                        sm.giveItem(BOW)
                        sm.giveItem(ARROWS_FOR_BOW)
                        sm.giveItem(HUNTER_S)
                    elif jobSelection == 1:
                        sm.jobAdvance(300)
                        char.setFinalJob(322)
                        sm.giveItem(CROSSBOW)
                        sm.giveItem(ARROWS_FOR_CROSSBOW)
                        sm.giveItem(CROSSBOWMAN_S)
                    if jobSelection != 2:
                        break
                elif selection == 3:
                    text += "#b#L0#(ASSASSIN => HERMIT =>) #eNIGHTLORD#n #l\r\n#L1#(BANDIT => CHIEFBANDIT =>) #eSHADOWER#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(400)
                        char.setFinalJob(412)
                        sm.giveItem(CLAW)
                        sm.giveItem(THROWING_STARS, 4800)
                        sm.giveItem(ASSASSIN_S)
                    elif jobSelection == 1:
                        sm.jobAdvance(400)
                        char.setFinalJob(422)
                        sm.giveItem(DAGGER)
                        sm.giveItem(BANDIT_S)
                    if jobSelection != 2:
                        break
                elif selection == 4:
                    text += "#b#L0#(BRAWLER => MARAUDER =>) #eBUCCANEER#n #l\r\n#L1#(GUNSLINGER => OUTLAW =>) #eCORSAIR#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(500)
                        char.setFinalJob(512)
                        sm.giveItem(KNUCKLE)
                        sm.giveItem(BRAWLER_S)
                    elif jobSelection == 1:
                        sm.jobAdvance(500)
                        char.setFinalJob(522)
                        sm.giveItem(GUN)
                        sm.giveItem(BULLETS, 4800)
                        sm.giveItem(GUN_SLINGER_S)
                    if jobSelection != 2:
                        break

    #CYGNUS (DAWNWARRIOR, BLAZEWIZARD, WINDARCHER, NIGHTWALKER, THUNDERBREAKER)
    elif jobID == 1000:
        while True:
            text = "#bSelect the Class That You Want to Become?\r\n"
            text += "#b#L0#DAWN WARRIOR#l\r\n#L1#BLAZE WIZARD#l\r\n#L2#WIND ARCHER#l\r\n#L3#NIGHT WALKER#l\r\n#L4#THUNDER BREAKER#l"
            selection = sm.sendNext(text)
            text = "#rSelect your #eFINAL JOB:#n\r\n"
            if selection == 0:
                text += "#b#L0##eDAWN WARRIOR#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1100)
                    char.setFinalJob(1112)
                    sm.giveItem(TWO_HANDED_SWORD)
                    sm.giveItem(ONE_HANDED_SWORD)

                    break
            elif selection == 1:
                text += "#b#L0##eBLAZE WIZARD#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1200)
                    char.setFinalJob(1212)
                    sm.giveItem(STAFF)
                    sm.giveItem(WAND)
                    break
            elif selection == 2:
                text += "#b#L0##eWIND ARCHER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1300)
                    char.setFinalJob(1312)
                    sm.giveItem(BOW)
                    sm.giveItem(ARROWS_FOR_BOW)
                    break
            elif selection == 3:
                text += "#b#L0##eNIGHT WALKER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1400)
                    char.setFinalJob(1412)
                    sm.giveItem(CLAW)
                    sm.giveItem(THROWING_STARS, 4800)
                    break
            elif selection == 4:
                text += "#b#L0##eTHUNDER BREAKER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1500)
                    char.setFinalJob(1512)
                    sm.giveItem(KNUCKLE)
                    break
        sm.giveItem(CYGNUS_S)

    #ARAN
    elif jobID == 2000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eARAN #l"
        sm.sendNext(text)
        sm.jobAdvance(2100)
        char.setFinalJob(2112)
        sm.giveItem(POLE_ARM)
        sm.giveItem(ARAN_S)
        sm.giveSkill(20001295, 1, 1)

#EVAN
    elif jobID == 2001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0#Evan #l"
        sm.sendNext(text)
        sm.jobAdvance(2210)
        char.setFinalJob(2218)
        sm.setSP(65)
        sm.giveItem(STAFF)
        sm.giveItem(WAND)
        sm.giveItem(EVAN_S)

    #MERCEDES - no need to touch the stats.
    elif jobID == 2002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eMERCEDES #l"
        sm.sendNext(text)
        sm.jobAdvance(2300)
        char.setFinalJob(2312)
        sm.giveItem(DUAL_BOWGUNS)
        sm.giveAndEquip(MERCEDES_ARROW)

    #PHANTOM - no need to touch the stats.
    elif jobID == 2003:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0#Phantom #l"
        sm.sendNext(text)
        sm.jobAdvance(2400)
        char.setFinalJob(2412)
        sm.giveItem(CANE)
        sm.giveItem(PHANTOM_S)

    #SHADE
    elif jobID == 2005:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eSHADE #l"
        sm.sendNext(text)
        sm.jobAdvance(2500)
        char.setFinalJob(2512)
        sm.giveItem(KNUCKLE)
        sm.giveItem(SHADE_S)

    #LUMINOUS
    elif jobID == 2004:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eLUMINOUS #l"
        sm.sendNext(text)
        sm.sendAskSelectMenu(0,0)
        sm.jobAdvance(2700)
        char.setFinalJob(2712)
        sm.giveSkill(27000106,5,5)
        sm.giveSkill(27000207,5,5)
        sm.giveSkill(27001100,10,10)
        sm.giveSkill(27001201,10,10)
        sm.giveItem(SHINING_ROD_LUMINOUS)
        sm.giveAndEquip(LUMINOUS_S)

    #DEMON AVENGER/SLAYER
    elif jobID == 3001:
        sm.sendNext("#rSelect your #eFINAL JOB:#b\r\n")
        #DEMON_AVENGER
        if sm.sendAskSelectMenu(1,0) == 0:
            sm.jobAdvance(3101)
            char.setFinalJob(3122)
            sm.giveItem(DESPERADO_DEMON_AVENGER)

        #DEMON_SLAYER
        else:
            sm.giveSkill(30010112, -1)
            sm.jobAdvance(3100)
            char.setFinalJob(3112)
            sm.giveItem(ONE_HANDED_AXE)
            sm.giveItem(TWO_HANDED_MACE)
            sm.giveItem(ONE_HANDED_MACE)
        #sm.giveItem(DEMON_AVENGER_SLAYER_S)
        for i in range(3):
            if not sm.hasSkill(DEMON_SKILLS[i]):
                sm.giveSkill(DEMON_SKILLS[i])

    #BATTLE_MAGE, WILD_HUNTER, MECHANIC, BLASTER
    elif jobID == 3000:
        while True:
            text = "#bSelect the Class That You Want to Become?\r\n"
            text += "#b#L0#BATTLE MAGE#l\r\n#L1#WILD HUNTER#l\r\n#L2#BLASTER#l"

            selection = sm.sendNext(text)
            text = "#rSelect your #eFINAL JOB:#n\r\n"
            if selection == 0:
                text += "#b#L0##eBATTLE MAGE#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3200)
                    char.setFinalJob(3212)
                    sm.giveItem(STAFF)
                    sm.giveItem(BATTLE_MAGE_S)
                    break
            elif selection == 1:
                text += "#b#L0##eWILD HUNTER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3300)
                    char.setFinalJob(3312)
                    sm.giveItem(CROSSBOW)
                    sm.giveItem(WILD_HUNTER_S)
                    sm.giveItem(ARROWS_FOR_CROSSBOW)
                    break

            #elif selection == 2:
            #    text += "#b#L0##eMECHANIC#n #l\r\n#L1##e#rGo Back#l"
            #    jobSelection = sm.sendPrev(text)
            #    if jobSelection == 0:
            #        sm.jobAdvance(3500)
            #        char.setFinalJob(3512)
            #        sm.giveItem(HAND_CANNON)
            #        sm.giveItem(MECHANICS_S)
            #        break
            elif selection == 2:
                text += "#b#L0##eBLASTER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3700)
                    char.setFinalJob(3712)
                    sm.giveItem(ARM_CANNON_BLASTER)
                    break

    #XENON
    elif jobID == 3002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eXENON #l"
        sm.sendNext(text)
        sm.jobAdvance(3600)
        char.setFinalJob(3612)
        sm.giveItem(WHIP_BLADE_XENON)

    #HAYATO
    elif jobID == 4001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eHAYATO #l"
        sm.sendNext(text)
        sm.jobAdvance(4100)
        char.setFinalJob(4112)
        sm.giveItem(KATANA_HAYATO)
        sm.giveItem(HAYATO_S)

    #KANNA
    elif jobID == 4002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKANNA #l"
        sm.sendNext(text)
        sm.jobAdvance(4200)
        char.setFinalJob(4212)
        sm.giveItem(FAN_KANNA)


    #MIHILE
    elif jobID == 5000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eMIHILE #l"
        sm.sendNext(text)
        sm.jobAdvance(5100)
        char.setFinalJob(5112)
        sm.giveItem(ONE_HANDED_SWORD)
        #sm.giveItem(MIHILE_S)

    #KAISER
    elif jobID == 6000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKAISER #l"
        sm.sendNext(text)
        sm.jobAdvance(6100)
        char.setFinalJob(6112)
        sm.giveItem(TWO_HANDED_SWORD)
        sm.giveItem(KAISER_S)

    #ANGELIC_BUSTER
    elif jobID == 6001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eANGELIC BUSTER #l"
        sm.sendNext(text)
        sm.jobAdvance(6500)
        char.setFinalJob(6512)
        sm.giveItem(SOUL_SHOOTER_AB)

    #ZERO
    elif jobID == 10000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eZERO #l"
        sm.sendNext(text)
        sm.jobAdvance(10100)
        char.setFinalJob(10112)
        sm.setSTR(300)
        sm.setAP(200)

    #NEEDS TO FIX BEAST TAMER
    #        BEAST_TAMER(11000, 11000),
    #BEAST_TAMER_1(11200, 11000),
    #BEAST_TAMER_2(11210, 11000),
    #BEAST_TAMER_3(11211, 11000),
    #BEAST_TAMER_4(11212, 11000),
    #BEAST_TAMER
    elif jobID == 11000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eBEAST TAMER #l"
        sm.sendNext(text)
        sm.jobAdvance(11200)
        char.setFinalJob(11212)
        sm.giveItem(BEAST_TAMER_SCEPTER_BT)
        sm.giveItem(BEAST_TAMER_S)

    #KINESIS
    elif jobID == 14000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKINESIS #l"
        selection = sm.sendNext(text)
        sm.jobAdvance(14200)
        char.setFinalJob(14212)
        sm.giveItem(PSY_LIMITER_KINESIS)

    else:
        sm.sendNext("We will update it later.")
        char.setFinalJob(-1)

    if char.getFinalJob() != -1:
        char.closeUI(2)
        sm.sendNext("#r#e#h0##n, #bFrom now on Your Job Will Update #eAutomatically!\r\nI wish you #eGOOD LUCK #nin your Adventure!\r\n#gEnjoy Playing SideQuest!")
        sm.giveMesos(100000)
        sm.giveItem(2000019, 50)
        if jobID != 10000:
            sm.setSTR(4)
            sm.setDEX(4)
            sm.setINT(4)
            sm.setLUK(4)
            sm.addAP(54)
    char.openUI(2)
    char.openUI(3)
    char.completeAnnoyingQuests()
    sm.dispose()


if finalJobID == 0:
    finalJob()

