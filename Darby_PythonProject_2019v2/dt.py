import colorama
from colorama import Fore, Style

#The following names will be utilized in a future project. I will use them for reference here: 

Introduction = "Hello Warriors. Welcome to 'Loz'. Here you will be introduced to a band of heroic warriors known as the Zerxocia. The Zerxocia's arch nemesis, the Pileqs, have decided to begin their conquest of the Universe of Loz. Thus far, the Pileqs have raided several planets for their gold-like substance called 'Xono-rex'. Proceeding each raid, the Pileqs would destroy each planet and insert the Xono-rex into their super-ship, called the Lone-King, to power it. The Lone-King is said to be able to destroy two universes with one blast of its' omega-cannon. It is up to the Zerxocia to stop the Pileqs from obtaining Xono-rex and destroying planets in order to save both their own universe and those surrounding. My name is Niko Darby and I am the creator of this adventure, the overseer of the Universe of Loz. Enjoy."

Notice = "NOTE TO PLAYERS: Be certain to answer each scenario in the exact spelling and format as provided. Have a grand adventure!"
#First battle instance text files: 

    
B1_Text = (Fore.BLUE + "The Great war for the universe of Loz has begun. Galiuto, the leader of the Zerxocia, expeditiously travels to the planet of Zon-noZ to battle Horschux. Horschux is a member of the Pileqs and a demon-warrior that has the power of fire. He has discovered a cache of Xono-rex and plans to procure it all and destroy the planet of Zon-noZ. Galiuto is an expert in all elemental powers.Galiuto's ship lands in Bun-nuB forest where Horschux awaits him with his arsenal. Galiuto exits his ship and confronts Horschux. In order to defeat Horschux, the master of fire, which element should Galiuto use to defeat Horschux? Air, Fire, Water, or Lightning? ")

Fire = "Fire"
Air = "Air"
Water = "Water"
Lightning = "Lightning"

B1_Choice1 = (Fore.RED + "Horschux: Chuckles, fool, I am immune to fire. Take this! <You have been defeated. Please re-execute the code.>")

B1_Choice2 =  (Fore.YELLOW + "Horschux: Gahh! The wind is absorbing my fire, what is this force! <Horschux loses 25% of health>")

B1_Choice3 =  (Fore.GREEN + "Horschux: Impossible, nooooo!!! <You have defeated Horschux>")

B1_Choice4 =  (Fore.YELLOW + "Horschux: Such power, this is infallible! <Horschux loses 75% of health and retreats>") 

B1_Else =  (Fore.YELLOW + "Galiuto: I don't feel like fighting. I am leaving now. <Departs from quarrel>")

#Second battle instance text files: 

B2_Text = (Fore.BLUE + "Horschux has been defeated by Galiuto. Galiuto meditates and watches over his companions with his stream of minds ability. Rev-Tyz is currently on Planet Oy-Boqa fighting Captain Phantox, who has found a mountain filled with Xono-rex. Phantox has the ability to warp whereas Rev-Tyz has super speed and lightning powers. How should Rev-Tyz defeat Phantox? Choose between lightning stun, lightning speed trail, or evasive counter maneuvers.")

Stun = "lightning stun"
Trail = "lightning speed trail"
Counter = "evasive counter maneuvers"

B2_Choice1 = (Fore.GREEN + "Captain Phantox: I cannot move, what is this? I can feel the lightning going through my cortices! *Fades away* <You have defeated Captain Phantox>")

B2_Choice2 = (Fore.RED + "Captain Phantox: A trail? Hmph. Take this! <You have been defeated. Please re-execute the code.>")

B2_Choice3 = (Fore.GREEN + "Captain Phantox: You have dodged and countered all of my attacks. I have been defeated. This is enlightening *Fades away* <You have defeated Captain Phantox>")

B2_Else =  (Fore.YELLOW + "Rev-Tyz: I am abandoning this battle *Speeds away* <Departs from quarrel>")
    

#Third battle instance text files:

B3_Text = (Fore.BLUE + "Rev-Tyz believed that Captain Phantox was defeated and began to walk away slowly. Alas, there was a rumble in Rev-Tyz's senses. Captain Phantox reappeared stronger than ever. His warping abilities were immeasurable. 'Did you really believe that it would be that easy to defeat me? I am called 'Captain' for a reason. I will extract this mountain of its Xono-rex right after I defeat you!' exclamored Captain Phantox. Rev-Tyz stared at the all-powerful Captain Phantox in awe and assumed his fighting position. Captain Phantox initiated his warping strike, yet Rev-Tyz developed a maneuver fast. Which attack will you use? Lightning shield, Circumference of lightning, or Shock wimper?")

Shield = "Lightning shield"
Circumference = "Circumference of lightning"
Wimper = "Shock wimper"

B3_Choice1 = (Fore.GREEN + "Captain Phantox: Gah! Your shield is immensely powerful, I will need to instantaneously develop a new maneuver <You have succeeded in blocking Captain Phantox's warping strike>")

B3_Choice2 =  (Fore.GREEN + "Captain Phantox: Such power! My warps are unable to surpass the speed of light. I will defeat you! <You have succeeded in blocking Captain Phantox's warping strike>")

B3_Choice3 = (Fore.RED + "Captain Phantox: *Chuckles* You wimper in fear with tears of electricity? Pathetic. *Warping blow* <You have been defeated. Please re-execute the code.>")

B3_Else= (Fore.YELLOW + "Rev-Tyz: Another attack? I'm getting out of here. *Speeds away* <Departs from quarrel>")

#Fourth battle instance text files: 

B4_Text =  (Fore.BLUE + "'You must not know that I am Rev-Tyz, the second in command of the Zerxocia. It is quite unfortunate that your attacks are failing. I really expected for scum like you with the title 'Captain' to be a challenge... But you are just a waste of my time.' Rev-Tyz exclamors in a cocky manner. Lightning began to surround Rev-Tyz's body, creating a powerful aura. 'Let us fight til' the end then, second commander Rev-Tyz. The Pileqs will control life as you know it! *Chuckles*'Captain Phantox stated bravely. Rev-Tyz charges in with one of his most powerful attacks. Which will you use? Lightning fury, Speed of light slash, or Angelic blasphemy?")

Fury = "Lightning fury"
Slash = "Speed of light slash"
Blasphemy = "Angelic blasphemy"

B4_Choice1 =  (Fore.GREEN + "'A thousand fists of lightning to your fragile soul!!' Rev-Tyz stated softly yet arrogantly. <Captain Phantox was hit with a powerful blast and is wounded>")
     
B4_Choice2 = (Fore.GREEN + "'An instance of pain, you shall endure.'Rev-Tyz whispers as he strikes down Captain Phantox. <Captain Phantox was hit with a powerful blast and is wounded>")

B4_Choice3 = (Fore.GREEN + "'Witness a blinding light of defeat' Rev-Tyz stated as he blinded the entire area with lightning strikes. <Captain Phantox was hit with a powerful blast and is wounded>")

B4_Else =  (Fore.YELLOW + "Rev-Tyz: I am too lazy. I'm getting out of here. *Speeds away* <Departs from quarrel>")

#First interrogation instance text files: 

I5_Text = (Fore.BLUE + "'Your power is rather impressive, Rev-Tyz.' Captain Phantox stated while holding his fatal wound.'As an honorable warrior, I will give you this data sheet that contains the information of the Pileqs. This is my first and last act of kindness and my redemption. Farewell.' Captain Phantox perished to dust and Rev-Tyz obtained the data sheet. What will you do now? Condolences, Meditate, or Focus?")

Focus = "Focus"
Meditate = "Meditate"
Condolences = "Condolences" 

I5_Choice1 = (Fore.GREEN + "'You were a worthy opponent Phantox. Rest well.' Rev-Tyz uttered as he began to examine the data sheet.' <You can now examine the data sheet>")

I5_Choice2 =  (Fore.GREEN + "Good riddance. Now I must rest and then examine this data sheet.' <You can now examine the data sheet>")

I5_Choice3 =  (Fore.GREEN + "'Alas, I have obtained the data sheet of the Pileqs. Now I can determine which planets they plan to conquer next. But first I must decipher it. Hmm...' Rev-Tyz stated intelligently. <You can now examine the data sheet>")

I5_Except = (Fore.YELLOW + "Rev-Tyz: Welp, he's gone. I am going to sleep.")

#Second interrogation instance text files: 

I6_Text = (Fore.BLUE + "'This is madness. The Pileqs have such extraordinary data. They will be able to conquer the universe instantaneously. I need to report this to the Zerxocia headquarters.' Rev-Tyz stated after examining the data. He took out his communicator and began his transmission. What will you say? Report the news, Brag about battle, or Troll?")

Report = "Report the news"
Brag = "Brag about battle"
Troll = "Troll"

I6_Choice1 = (Fore.GREEN + "'Attention members of Zerxocia, I have obtained the data sheet of the Pileqs. Their chances of conquering the universe are infallible. We must bring the war to them or life in the Universe of Loz is done for.' Rev-Tyz stated urgently. <You have completed this chapter>")

I6_Choice2 =  (Fore.GREEN + "'Members of Zerxocia, I have defeated Captain Phantox. According to the files I procured from his remnants, he was one of the most powerful members of the Pileqs. *Chuckles* Also, I have the data sheet of the Pileqs and they are becoming too powerful for us to handle. Their statistics for conquering the universe are infallible!' Rev-Tyz stated in a pompous manner. < You have completed this chapter>")

I6_Choice3 = (Fore.RED + "Beep bop boop, all members of Zerxocia. Beep bop, are you there? Beep boop *End transmission* <You have been defeated. Please re-execute the code>")

I6_Except = (Fore.YELLOW + "'Rev-Tyz: I'm bored. Time to rest.'")



