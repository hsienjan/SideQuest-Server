rightShoulderID = 9390610

sm.openGolluxPortal("phase3", 12)
if not sm.golluxMapAlreadyVisited():
    sm.spawnMob(rightShoulderID)
if not sm.hasMobsInField():
    sm.openGolluxPortal("clear", 7)
    sm.openGolluxPortal("phase3", 12)
sm.addCurrentGolluxMap()
sm.waitForMobDeath(rightShoulderID)
sm.showFieldEffect("Map/EffectTW.img/arisan/clear")
sm.addClearedGolluxMap()
sm.openGolluxPortal("clear", 7)