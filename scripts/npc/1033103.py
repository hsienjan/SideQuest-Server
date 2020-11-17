# Klas (1033103) | Help Manager

text = "#b#eCommand Manager:\r\n"
text += "#r#e@h/help/commands#k   #n=>  #bDisplay the Commands.\r\n"
text += "#r#e@train/training/maps#k #n=>  #bOpen the trainer NPC.\r\n"
text += "#r#e@city/town/home#k       #n=>  #bReturn to the Main City.\r\n"
text += "#r#e@event#k                         #n=>  #bEnter Event when it's open.\r\n"
text += "#r#e@roll#k                             #n=>  #bRolling your luck."

sm.sendNext(text)
sm.dispose()
