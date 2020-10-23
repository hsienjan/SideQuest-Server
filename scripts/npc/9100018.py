# Shiro


def finalJob():
    MAPLE_ADMINISTARTOR = 2007

    target_level = 10

    sm.setSpeakerID(MAPLE_ADMINISTARTOR)
    sm.removeEscapeButton()
    sm.lockInGameUI(True)
    mesoReward = 5000

    #r#o"+ str(slimeid) +"##k.
    #if it's normal beginner job = 0, subjob = 0 (warrior, magician, thief, archer)
    #dual blade subjob = 1

    char = sm.getChr()

    #text += str(sm.getChr().getJob())
    #selection = sm.sendNext(text)
    selection = 0
    ap = 0
    #beginner choice
    jobID = int(char.getJob())
    subJobID = char.getSubJob()
    finalJobID = char.getFinalJob()

    sm.sendNext("#b#eWelcome to SideQuest, #h0# !#k \r\nClick Next to select your #rJOB#k ;)")
    if char.getLevel() < target_level:
        sm.addLevel(target_level - char.getLevel())
    #BEGINNER
    if jobID == 0:
        #dual-blade
        if char.getSubJob() == 1:
            text = "#rSelect your #eFINAL JOB:#b\r\n \r\n"
            text += "#b#L0#Blade Master #l"
            selection = sm.sendNext(text)
            sm.jobAdvance(400)
            char.setFinalJob(434)
        #something else
        elif subJobID == 2:
            pass
        #adventure (warrior, magician, thief, archer)
        else:
            text = "#bWhat do you wanna be ?"
            text += "#b#L0#Warrior #l\r\n#L1#Magician #l\r\n#L2#Thief #l\r\n"

            selection = sm.sendPrev(text)

            sm.jobAdvance(400)
            char.setFinalJob(434)

    sm.sendNext("#r#h0##k, #bI wish you #eGOOD LUCK #n#bin your Adventure!")
    sm.lockInGameUI(False)
    sm.dispose()


if finalJobID == 0:
    finalJob()