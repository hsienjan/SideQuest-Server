#making firstJob for the new characters

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
        #TODO we need to check about the AP for each class
    #BEGINNER
    if jobID == 0:
        #DUAL_BLADE
        if char.getSubJob() == 1:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eBLADE MASTER #l"
            sm.sendNext(text)
            sm.jobAdvance(400)
            char.setFinalJob(434)
        #CANNONEER
        elif subJobID == 2:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eCANNONEER #l"
            sm.sendNext(text)
            sm.jobAdvance(501)
            char.setFinalJob(532)
            sm.giveAndEquip(1532000)
        #JETT
        elif subJobID == 10:
            text = "#rSelect your #eFINAL JOB:#b\r\n"
            text += "#b#L0##eJETT #l"
            sm.sendNext(text)
            sm.jobAdvance(508)
            char.setFinalJob(572)
            sm.giveAndEquip(1492065)
            sm.giveItem(2330000, 4000)
        #adventure (warrior, magician, thief, archer)
        else:
            while True:
                text = "#bSelect the Class That You Want to Become?\r\n"
                text += "#b#L0#Warrior#l\r\n#L1#Magician#l\r\n#L2#Archer#l\r\n#L3#Thief#l\r\n#L4#Pirate#l\r\n"

                selection = sm.sendNext(text)
                text = "#rSelect your #eFINAL JOB:#n\r\n"
                if (selection == 0):
                    text += "#b#L0#(FIGHTER => CRUSADER =>) #eHERO#n #l\r\n#L1#(PAGE => WHITEKNIGHT =>) #ePALADIN#n #l\r\n#L2#(SPEARMAN => DRAGONKNIGHT =>) #eDARKKNIGHT#l\r\n#L3##e#rGo Back#l"
                    jobSelection = sm.sendPrev(text)
                    if jobSelection == 0:
                        sm.jobAdvance(100)
                        char.setFinalJob(112)
                        sm.giveAndEquip(1402001)
                        sm.giveItem(1412001)
                    elif jobSelection == 1:
                        sm.jobAdvance(100)
                        char.setFinalJob(122)
                        sm.giveAndEquip(1402001)
                        sm.giveItem(1422000)
                    elif jobSelection == 2:
                        sm.jobAdvance(100)
                        char.setFinalJob(132)
                        sm.giveAndEquip(1432000)
                        sm.giveItem(1442000)

                    if jobSelection != 3:
                        break
                elif selection == 1:
                    text += "#b#L0#(F&P WIZARD => MAGE =>) #eFIRE & POISON ARCHMAGE#n #l\r\n#L1#(I&L WIZARD => MAGE =>) #eICE & LIGHTNING ARCHMAGE#n #l\r\n#L2#(CLERIC => PRIEST =>) #eBISHOP#l\r\n#L3##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(200)
                        char.setFinalJob(212)
                    elif jobSelection == 1:
                        sm.jobAdvance(200)
                        char.setFinalJob(222)
                    elif jobSelection == 2:
                        sm.jobAdvance(200)
                        char.setFinalJob(232)
                    if jobSelection != 3:
                        sm.giveAndEquip(1382000)
                        sm.giveItem(1372002)
                        break
                elif selection == 2:
                    text += "#b#L0#(HUNTER => RANGER =>) #eBOWMASTER#n #l\r\n#L1#(CROSSBOWMAN => SNIPER =>) #eMARKSMAN#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(300)
                        char.setFinalJob(312)
                        sm.giveAndEquip(1452054)
                        sm.giveItem(2060004, 5000)

                    elif jobSelection == 1:
                        sm.jobAdvance(300)
                        char.setFinalJob(322)
                        sm.giveAndEquip(1462047)
                        sm.giveItem(2061004, 5000)
                    if jobSelection != 2:
                        break
                elif selection == 3:
                    text += "#b#L0#(ASSASSIN => HERMIT =>) #eNIGHTLORD#n #l\r\n#L1#(BANDIT => CHIEFBANDIT =>) #eSHADOWER#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(400)
                        char.setFinalJob(412)
                        sm.giveAndEquip(1472000)
                        sm.giveItem(2070010, 4000)
                    elif jobSelection == 1:
                        sm.jobAdvance(400)
                        char.setFinalJob(422)
                        sm.giveAndEquip(1332102)
                    if jobSelection != 2:
                        break
                elif selection == 4:
                    text += "#b#L0#(BRAWLER => MARAUDER =>) #eBUCCANEER#n #l\r\n#L1#(GUNSLINGER => OUTLAW =>) #eCORSAIR#n #l\r\n#L2##e#rGo Back#l"
                    jobSelection = sm.sendNext(text)
                    if jobSelection == 0:
                        sm.jobAdvance(500)
                        char.setFinalJob(512)
                        sm.giveAndEquip(1482000)
                    elif jobSelection == 1:
                        sm.jobAdvance(500)
                        char.setFinalJob(522)
                        sm.giveAndEquip(1492065)
                        sm.giveItem(2330000, 4000)
                    if jobSelection != 2:
                        break

    #CYGNUS (DAWNWARRIOR, BLAZEWIZARD, WINDARCHER, NIGHTWALKER, THUNDERBREAKER)
    elif jobID == 1000:
        while True:
            text = "#bSelect the Class That You Want to Become?\r\n"
            text += "#b#L0#DAWN WARRIOR#l\r\n#L1#BLAZE WIZARD#l\r\n#L2#WIND ARCHER#l\r\n#L3#NIGHT WALKER#l\r\n#L4#THUNDER BREAKER#l"
            selection = sm.sendNext(text)
            text = "#rSelect your #eFINAL JOB:#n\r\n"
            if (selection == 0):
                text += "#b#L0##eDAWN WARRIOR#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1100)
                    char.setFinalJob(1112)
                    break
            elif selection == 1:
                text += "#b#L0##eBLAZE WIZARD#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1200)
                    char.setFinalJob(1212)
                    break
            elif selection == 2:
                text += "#b#L0##eWIND ARCHER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1300)
                    char.setFinalJob(1312)
                    break
            elif selection == 3:
                text += "#b#L0##eNIGHT WALKER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1400)
                    char.setFinalJob(1412)
                    break
            elif selection == 4:
                text += "#b#L0##eTHUNDER BREAKER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(1500)
                    char.setFinalJob(1512)
                    sm.giveAndEquip(1482000)
                    break

    #ARAN
    elif jobID == 2000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eARAN #l"
        selection = sm.sendNext(text)
        sm.jobAdvance(2100)
        char.setFinalJob(2112)

    #EVAN
    elif jobID == 2001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0#Evan #l"
        sm.sendNext(text)
        sm.jobAdvance(2210)
        char.setFinalJob(2218)
        sm.setSP(65)


    #MERCEDES - no need to touch the stats.
    elif jobID == 2002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eMERCEDES #l"
        sm.sendNext(text)
        sm.jobAdvance(2300)
        char.setFinalJob(2312)

    #PHANTOM - no need to touch the stats.
    elif jobID == 2003:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0#Phantom #l"
        sm.sendNext(text)
        sm.jobAdvance(2400)
        char.setFinalJob(2412)
        sm.giveAndEquip(1362001)
        sm.giveAndEquip(1352100)
        sm.giveItem(1142375)

    #SHADE
    elif jobID == 2005:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eSHADE #l"
        sm.sendNext(text)
        sm.jobAdvance(2500)
        char.setFinalJob(2512)
        sm.giveAndEquip(1482000)
        sm.giveItem(1353100)

    #LUMINOUS
    elif jobID == 2004:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eLUMINOUS #l"
        sm.sendNext(text)
        sm.sendAskSelectMenu(0,0)
        sm.jobAdvance(2700)
        char.setFinalJob(2712)

    #DEMON AVENGER/SLAYER
    elif jobID == 3001:
        sm.sendNext("#rSelect your #eFINAL JOB:#b\r\n")
        #DEMON_AVENGER
        if sm.sendAskSelectMenu(1,0) == 0:
            sm.jobAdvance(3101)
            char.setFinalJob(3122)
            sm.giveAndEquip(1232001)
            sm.giveAndEquip(1099006)

        #DEMON_SLAYER
        else:
            sm.giveSkill(30010112, -1)
            sm.jobAdvance(3100)
            char.setFinalJob(3112)
            sm.giveAndEquip(1322122)
            sm.giveAndEquip(1099000)

        sm.giveItem(1142341)
        sm.giveItem(1142553)
        for i in range(3):
            if not sm.hasSkill(DEMON_SKILLS[i]):
                sm.giveSkill(DEMON_SKILLS[i])

    #BATTLE_MAGE, WILD_HUNTER, MECHANIC, BLASTER
    elif jobID == 3000:
        while True:
            text = "#bSelect the Class That You Want to Become?\r\n"
            text += "#b#L0#BATTLE MAGE#l\r\n#L1#WILD HUNTER#l\r\n#L2#MECHANIC#l\r\n#L3#BLASTER#l"

            selection = sm.sendNext(text)
            text = "#rSelect your #eFINAL JOB:#n\r\n"
            if (selection == 0):
                text += "#b#L0##eBATTLE MAGE#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3200)
                    char.setFinalJob(3212)
                    break
            elif selection == 1:
                text += "#b#L0##eWILD HUNTER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3300)
                    char.setFinalJob(3312)
                    break
            #TODO check if cannoneer needs bullets
            elif selection == 2:
                text += "#b#L0##eMECHANIC#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3500)
                    char.setFinalJob(3512)
                    sm.giveAndEquip(1532000)
                    break
            elif selection == 3:
                text += "#b#L0##eBLASTER#n #l\r\n#L1##e#rGo Back#l"
                jobSelection = sm.sendPrev(text)
                if jobSelection == 0:
                    sm.jobAdvance(3700)
                    char.setFinalJob(3712)
                    break

    #XENON
    elif jobID == 3002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eXENON #l"
        sm.sendNext(text)
        sm.jobAdvance(3600)
        char.setFinalJob(3612)

    #HAYATO
    elif jobID == 4001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eHAYATO #l"
        sm.sendNext(text)
        sm.jobAdvance(4100)
        char.setFinalJob(4112)
        sm.giveAndEquip(1542048)

    #KANNA
    elif jobID == 4002:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKANNA #l"
        sm.sendNext(text)
        sm.jobAdvance(4200)
        char.setFinalJob(4212)

    #MIHILE
    elif jobID == 5000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eMIHILE #l"
        sm.sendNext(text)
        sm.jobAdvance(5100)
        char.setFinalJob(5112)

    #KAISER
    elif jobID == 6000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKAISER #l"
        sm.sendNext(text)
        sm.jobAdvance(6100)
        char.setFinalJob(6112)

    #ANGELIC_BUSTER
    elif jobID == 6001:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eANGELIC BUSTER #l"
        sm.sendNext(text)
        sm.jobAdvance(6500)
        char.setFinalJob(6512)
        sm.giveAndEquip(1222076)

    #ZERO
    elif jobID == 10000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eZERO #l"
        sm.sendNext(text)
        sm.jobAdvance(10100)
        char.setFinalJob(10112)

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

    #KINESIS
    elif jobID == 14000:
        text = "#rSelect your #eFINAL JOB:#b\r\n"
        text += "#b#L0##eKINESIS #l"
        selection = sm.sendNext(text)
        sm.jobAdvance(14200)
        char.setFinalJob(14212)

    sm.sendNext("#r#e#h0##n, #bFrom now on Your Job Will Update #eAutomatically!\r\nI wish you #eGOOD LUCK #nin your Adventure!\r\n#gEnjoy Playing SideQuest!")
    sm.giveMesos(100000)
    sm.giveItem(2000019, 50)
    sm.setSTR(4)
    sm.setDEX(4)
    sm.setINT(4)
    sm.setLUK(4)
    sm.setAP(54)
    sm.dispose()


if finalJobID == 0:
    finalJob()

