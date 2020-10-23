
MAPLE_ADMINISTARTOR = 2007

target_level = 10

sm.setSpeakerID(MAPLE_ADMINISTARTOR)
sm.removeEscapeButton()

selection = sm.sendNext("Where would you like to go? \r\n#L0#Lith Harbor#l\r\n#L1#Henesys#l\r\n#L2#Kerning City#l"
       + "\r\n#L3#Ellinia#l\r\n#L4#Perion#l")


sm.dispose()
