def the_balance() :
    
    
    
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    
    
    
    Battle_1 = input(Fore.BLUE + "The Great war for the universe of Loz has begun. Galiuto, the leader of the Zerxocia, expeditiously travels to the planet of Zon-noZ to battle Horschux. Horschux is a member of the Pileqs and a demon-warrior that has the power of fire. He has discovered a cache of Xono-rex and plans to procure it all and destroy the planet of Zon-noZ. Galiuto is an expert in all elemental powers.Galiuto's ship lands in Bun-nuB forest where Horschux awaits him with his arsenal. Galiuto exits his ship and confronts Horschux. In order to defeat Horschux, the master of fire, which element should Galiuto use to defeat Horschux? Air, Fire, Water, or Lightning? ")
    if  Battle_1 == "Fire" : 
        print(Fore.RED + "Horschux: Chuckles, fool, I am immune to fire. Take this! <You have been defeated. Please re-execute the code.>")
        assert (Battle_1 == "Fire") == True
    if Battle_1 == "Air" : 
        print(Fore.YELLOW + "Horschux: Gahh! The wind is absorbing my fire, what is this force! <Horschux loses 25% of health>")
        assert (Battle_1 == "Air") == True 
    if Battle_1 == "Water" : 
        print(Fore.GREEN + "Horschux: Impossible, nooooo!!! <You have defeated Horschux>")
        assert (Battle_1 == "Water") == True
    if Battle_1 == "Lightning" :
        print(Fore.YELLOW + "Horschux: Such power, this is infallible! <Horschux loses 75% of health and retreats>") 
        assert (Battle_1 == "Lightning") == True

    else :
        return "Galiuto: I don't feel like fighting. I am leaving now. <Departs from quarrel>" 
    
    
    
    
    
    
    
    
    
    
def the_balance2() :
    
    
    
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    
    
    
    Battle_2 = input(Fore.BLUE + "Horschux has been defeated by Galiuto. Galiuto meditates and watches over his companions with his stream of minds ability. Rev-Tyz is currently on Planet Oy-Boqa fighting Captain Phantox, who has found a mountain filled with Xono-rex. Phantox has the ability to warp whereas Rev-Tyz has super speed and lightning powers. How should Rev-Tyz defeat Phantox? Choose between lightning stun, lightning speed trail, or evasive counter maneuvers.")
    if Battle_2 == "lightning stun" : 
        print(Fore.GREEN + "Captain Phantox: I cannot move, what is this? I can feel the lightning going through my cortices! *Fades away* <You have defeated Captain Phantox>")
        assert (Battle_2 == "lightning stun") == True
    if Battle_2 == "lightning speed trail" : 
        print(Fore.RED + "Captain Phantox: A trail? Hmph. Take this! <You have been defeated. Please re-execute the code.>")
        assert (Battle_2 == "lightning speed trail") == True
    if Battle_2 == "evasive counter maneuvers" : 
        print(Fore.GREEN + "Captain Phantox: You have dodged and countered all of my attacks. I have been defeated. This is enlightening *Fades away* <You have defeated Captain Phantox>")
        assert (Battle_2 == "evasive counter maneuvers") == True
    else :
        return (Fore.YELLOW + "Rev-Tyz: I am abandoning this battle *Speeds away* <Departs from quarrel>")
    
    
    
    
    
    
    
    
    
    
    
def balance_3() : 
    
    
    
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    
    
    
    Battle_3 = input(Fore.BLUE + "Rev-Tyz believed that Captain Phantox was defeated and began to walk away slowly. Alas, there was a rumble in Rev-Tyz's senses. Captain Phantox reappeared stronger than ever. His warping abilities were immeasurable. 'Did you really believe that it would be that easy to defeat me? I am called 'Captain' for a reason. I will extract this mountain of its Xono-rex right after I defeat you!' exclamored Captain Phantox. Rev-Tyz stared at the all-powerful Captain Phantox in awe and assumed his fighting position. Captain Phantox initiated his warping strike, yet Rev-Tyz developed a maneuver fast. Which attack will you use? Lightning shield, Circumference of lightning, or Shock wimper?")
    if Battle_3 == "Lightning shield" :
        print(Fore.GREEN + "Captain Phantox: Gah! Your shield is immensely powerful, I will need to instantaneously develop a new maneuver <You have succeeded in blocking Captain Phantox's warping strike>")
        assert (Battle_3 == "Lightning shield") == True
    if Battle_3 == "Circumference of lightning" :
        print(Fore.GREEN + "Captain Phantox: Such power! My warps are unable to surpass the speed of light. I will defeat you! <You have succeeded in blocking Captain Phantox's warping strike>")
        assert (Battle_3 == "Circumference of lightning") == True
    if Battle_3 == "Shock wimper" : 
        print(Fore.RED + "Captain Phantox: *Chuckles* You wimper in fear with tears of electricity? Pathetic. *Warping blow* <You have been defeated. Please re-execute the code.>")
        assert (Battle_3 == "Shock wimper") == True
    else : 
        return (Fore.YELLOW + "Rev-Tyz: Another attack? I'm getting out of here. *Speeds away* <Departs from quarrel>")
    
    
    
    
    
    
    
def balance_4() : 
    
    
    
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    
    
    
    Battle_4 = input(Fore.BLUE + "'You must not know that I am Rev-Tyz, the second in command of the Zerxocia. It is quite unfortunate that your attacks are failing. I really expected for scum like you with the title 'Captain' to be a challenge... But you are just a waste of my time.' Rev-Tyz exclamors in a cocky manner. Lightning began to surround Rev-Tyz's body, creating a powerful aura. 'Let us fight til' the end then, second commander Rev-Tyz. The Pileqs will control life as you know it! *Chuckles*'Captain Phantox stated bravely. Rev-Tyz charges in with one of his most powerful attacks. Which will you use? Lightning fury, Speed of light slash, or Angelic blasphemy?")
    try: 
        if Battle_4 == 'Lightning fury':
            print(Fore.GREEN + "'A thousand fists of lightning to your fragile soul!!' Rev-Tyz stated softly yet arrogantly. <Captain Phantox was hit with a powerful blast and is wounded>")
            assert (Battle_4 == "Lightning fury") == True
     
        if Battle_4 == 'Speed of light slash':
            print(Fore.GREEN + "'An instance of pain, you shall endure.'Rev-Tyz whispers as he strikes down Captain Phantox. <Captain Phantox was hit with a powerful blast and is wounded>")
            assert (Battle_4 == 'Speed of light slash') == True
     
        if Battle_4 == 'Angelic blasphemy' :
            print(Fore.GREEN + "'Witness a blinding light of defeat' Rev-Tyz stated as he blinded the entire area with lightning strikes. <Captain Phantox was hit with a powerful blast and is wounded>")
            assert (Battle_4 == "Angelic blasphemy") == True
    except: 
         return (Fore.YELLOW + "Rev-Tyz: I am too lazy. I'm getting out of here. *Speeds away* <Departs from quarrel>")

        
        
        
        
        
        
        
def balance_5(): 
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    Interrogation_1 = input(Fore.BLUE + "'Your power is rather impressive, Rev-Tyz.' Captain Phantox stated while holding his fatal wound.'As an honorable warrior, I will give you this data sheet that contains the information of the Pileqs. This is my first and last act of kindness and my redemption. Farewell.' Captain Phantox perished to dust and Rev-Tyz obtained the data sheet. What will you do now? Condolences, Meditate, or Focus?")
    try: 
        if Interrogation_1 == 'Condolences':
            print(Fore.GREEN + "'You were a worthy opponent Phantox. Rest well.' Rev-Tyz uttered as he began to examine the data sheet.' <You can now examine the data sheet>")
            assert (Interrogation_1 == 'Condolences') == True 
        if Interrogation_1 == 'Meditate': 
            print(Fore.GREEN + "Good riddance. Now I must rest and then examine this data sheet.' <You can now examine the data sheet>")
            assert (Interrogation_1 == 'Meditate') == True
        if Interrogation_1 == 'Focus': 
            print(Fore.GREEN + "'Alas, I have obtained the data sheet of the Pileqs. Now I can determine which planets they plan to conquer next. But first I must decipher it. Hmm...' Rev-Tyz stated intelligently. <You can now examine the data sheet>")
            assert (Interrogation_1 == 'Focus') == True 
    except: 
        return (Fore.YELLOW + "Rev-Tyz: Welp, he's gone. I am going to sleep.")

    
    
    
    
    
    
    
def balance_6():
    """
    This function will allow players to input one of the selections printed in quotations within the "if" statements.
    
    """
    Interrogation_2 = input(Fore.BLUE + "'This is madness. The Pileqs have such extraordinary data. They will be able to conquer the universe instantaneously. I need to report this to the Zerxocia headquarters.' Rev-Tyz stated after examining the data. He took out his communicator and began his transmission. What will you say? Report the news, Brag about battle, or Troll?")
    try:
        if Interrogation_2 == 'Report the news':
            print(Fore.GREEN + "'Attention members of Zerxocia, I have obtained the data sheet of the Pileqs. Their chances of conquering the universe are infallible. We must bring the war to them or life in the Universe of Loz is done for.' Rev-Tyz stated urgently. <You have completed this chapter>")
            assert (Interrogation_2 == 'Report the news') == True
        if Interrogation_2 == 'Brag about battle':
            print(Fore.GREEN + "'Members of Zerxocia, I have defeated Captain Phantox. According to the files I procured from his remnants, he was one of the most powerful members of the Pileqs. *Chuckles* Also, I have the data sheet of the Pileqs and they are becoming too powerful for us to handle. Their statistics for conquering the universe are infallible!' Rev-Tyz stated in a pompous manner. < You have completed this chapter>")
            assert (Interrogation_2 == 'Brag about battle') == True 
        if Interrogation_2 == 'Troll':
            print(Fore.RED + "Beep bop boop, all members of Zerxocia. Beep bop, are you there? Beep boop *End transmission* <You have been defeated. Please re-execute the code>")
            assert (Interrogation_2 == 'Troll') == True 
    except: 
        return (Fore.YELLOW + "'Rev-Tyz: I'm bored. Time to rest.'")
    
    