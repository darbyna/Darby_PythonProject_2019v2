#First we will begin with an introduction. I will concoct a string that will introduce all users to the project. 
Introduction = "Hello Warriors. Welcome to 'Universe of Loz: Battle of the Ages'. Here you will be introduced to a band of heroic warriors known as the Zerxocia. The Zerxocia's arch nemesis, the Pileqs, have decided to begin their conquest of the Universe of Loz. Thus far, the Pileqs have raided several planets for their gold-like substance called 'Xono-rex'. Proceeding each raid, the Pileqs would destroy each planet and insert the Xono-rex into their super-ship, called the Lone-King, to power it. The Lone-King is said to be able to destroy two universes with one blast of its' omega-cannon. It is up to the Zerxocia to stop the Pileqs from obtaining Xono-rex and destroying planets in order to save both their own universe and those surrounding. My name is Niko Darby and I am the creator of this adventure, the overseer of the Universe of Loz. Enjoy."


#Now for a test of the string. Indubitably, this will be inserted into the Notebook and Tests folder for further examination. 
print(Introduction)

#The Introduction has been printed. Now it is time to construct the questions and define different variables.  

#Let us begin by importing the necessary packages for this project. Some may or may not be used. 
import pandas as pd
import numpy as np
import matplotlib as plt

#The necessary packages have been uploaded. It is now time to define some general terms. 
Zerxocia = ("Galiuto", "Rev-Tyz", "Commander Vizil", "Fala-To")
Pileqs = ("Emperor Kret-Po", "Wujo-Bax", "Horschux", "Captain Phantox")
Galiuto = Zerxocia[0]
Rev_Tyz = Zerxocia[1]
Commander_Vizil = Zerxocia[2]
Fala_To = Zerxocia[3]
Emperor_Kret_Po= Pileqs[0]
Wujo_Bax= Pileqs[1]
Horschux= Pileqs[2]
Captain_Phantox= Pileqs[3]

#The above lists of strings will be of utmost importance in the near furture. 
#It is now time to construct a function that will be useful. 
def the_balance() :
    Battle_1 = input("The Great war for the universe of Loz has begun. Galiuto, the leader of the Zerxocia, expeditiously travels to the planet of Zon-noZ to battle Horschux. Horschux is a member of the Pileqs and a demon-warrior that has the power of fire. He has discovered a cache of Xono-rex and plans to procure it all and destroy the planet of Zon-noZ. Galiuto is an expert in all elemental powers.Galiuto's ship lands in Bun-nuB forest where Horschux awaits him with his arsenal. Galiuto exits his ship and confronts Horschux. In order to defeat Horschux, the master of fire, which element should Galiuto use to defeat Horschux? Air, Fire, Water, or Lightning? ")
    if  Battle_1 == "Fire" : 
        print("Horschux: Chuckles, fool, I am immune to fire. Take this! <You have been defeated. Please re-execute the code.>")
    if Battle_1 == "Air" : 
        print("Horschux: Gahh! The wind is absorbing my fire, what is this force! <Horschux loses 25% of health>")
    if Battle_1 == "Water" : 
        print("Horschux: Impossible, nooooo!!! <You have defeated Horschux>")
    if Battle_1 == "Lightning" :
        print("Horschux: Such power, this is infallible! <Horschux loses 75% of health and retreats>") 

    else :
        return "Galiuto: I don't feel like fighting. I am leaving now. <Departs from quarrel>" 
    

#Since the function "the_balance()" is now created. The rest of the code can be concocted. Now print your answer below using the_balance()'s answer input once the code is executed.

#Here is my sample answer: 

the_balance() 

#It is now time for the next question. 
def the_balance2() :
    Battle_2 = input("Horschux has been defeated by Galiuto. Galiuto meditates and watches over his companions with his stream of minds ability. Rev-Tyz is currently on Planet Oy-Boqa fighting Captain Phantox, who has found a mountain filled with Xono-rex. Phantox has the ability to warp whereas Rev-Tyz has super speed and lightning powers. How should Rev-Tyz defeat Phantox? Choose between lightning stun, lightning speed trail, or evasive counter maneuvers.")
    if Battle_2 == "lightning stun" : 
        print("Captain Phantox: I cannot move, what is this? I can feel the lightning going through my cortices! *Fades away* <You have defeated Captain Phantox>")
    if Battle_2 == "lightning speed trail" : 
        print("Captain Phantox: A trail? Hmph. Take this! <You have been defeated. Please re-execute the code.>")
    if Battle_2 == "evasive counter maneuvers" : 
        print("Captain Phantox: You have dodged and countered all of my attacks. I have been defeated. This is enlightening *Fades away* <You have defeated Captain Phantox>")
    else :
        return "Rev-Tyz: I am abandoning this battle *Speeds away* <Departs from quarrel>" 
    

#Once you have submitted an answer to the function below. We will proceed to the next section. To execute this sequence of the game simply type: the_balance2()

the_balance2()

#Now it is time to transition to the next part of the project. One more function will be created and then more techniques will be incorporated in into the project. 

def balance_3() : 
    Battle_3 = input("Rev-Tyz believed that Captain Phantox was defeated and began to walk away slowly. Alas, there was a rumble in Rev-Tyz's senses. Captain Phantox reappeared stronger than ever. His warping abilities were immeasurable. 'Did you really believe that it would be that easy to defeat me? I am called 'Captain' for a reason. I will extract this mountain of its Xono-rex right after I defeat you!' exclamored Captain Phantox. Rev-Tyz stared at the all-powerful Captain Phantox in awe and assumed his fighting position. Captain Phantox initiated his warping strike, yet Rev-Tyz developed a maneuver fast. Which attack will you use? Lightning shield, Circumference of lightning, or Shock wimper?")
    if Battle_3 == "Lightning shield" :
        print("Captain Phantox: Gah! Your shield is immensely powerful, I will need to instantaneously develop a new maneuver <You have succeeded in blocking Captain Phantox's warping strike>")
    if Battle_3 == "Circumference of lightning" :
        print("Captain Phantox: Such power! My warps are unable to surpass the speed of light. I will defeat you! <You have succeeded in blocking Captain Phantox's warping strike>")
    if Battle_3 == "Shock wimper" : 
        print("Captain Phantox: *Chuckles* You wimper in fear with tears of electricity? Pathetic. *Warping blow* <You have been defeated. Please re-execute the code.>")
    else : 
        return ("Rev-Tyz: Another attack? I'm getting out of here. *Speeds away* <Departs from quarrel>")

#It is now time to execute this function. Please execute: balance_3() below. 

balance_3()
                
#The if-then functions compilation is now complete. Now it is time to initiate the try-except + if-then functions compilation. 

def balance_4() : 
    Battle_4 = input("'You must not know that I am Rev-Tyz, the second in command of the Zerxocia. It is quite unfortunate that your attacks are failing. I really expected for scum like you with the title 'Captain' to be a challenge... But you are just a waste of my time.' Rev-Tyz exclamors in a cocky manner. Lightning began to surround Rev-Tyz's body, creating a powerful aura. 'Let us fight til' the end then, second commander Rev-Tyz. The Pileqs will control life as you know it! *Chuckles*'Captain Phantox stated bravely. Rev-Tyz charges in with one of his most powerful attacks. Which will you use? Lightning fury, Speed of light slash, or Angelic blasphemy?")
    try: 
        if Battle_4 == 'Lightning Fury':
            print("'A thousand fists of lightning to your fragile soul!!' Rev-Tyz stated softly yet arrogantly. <Captain Phantox was hit with a powerful blast and is wounded>")
     
        if Battle_4 == 'Speed of light slash':
            print("'An instance of pain, you shall endure.'Rev-Tyz whispers as he strikes down Captain Phantox. <Captain Phantox was hit with a powerful blast and is wounded>")
     
        if Battle_4 == 'Angelic blasphemy' :
            print("'Witness a blinding light of defeat' Rev-Tyz stated as he blinded the entire area with lightning strikes. <Captain Phantox was hit with a powerful blast and is wounded>")
    except: 
         return ("Rev-Tyz: I am too lazy. I'm getting out of here. *Speeds away* <Departs from quarrel>")
        
#Now that the try-except statement has been completed. Another function must be created. To execute the function above type: balance_4().

balance_4()

#The try-except and if-statements have been combined. For the next section, a ".csv" file will be converted into a chart for a more interactive session after an additional function. 

def balance_5(): 
    Interrogation_1 = input("'Your power is rather impressive, Rev-Tyz.' Captain Phantox stated while holding his fatal wound.'As an honorable warrior, I will give you this data sheet that contains the information of the Pileqs. This is my first and last act of kindness and my redemption. Farewell.' Captain Phantox perished to dust and Rev-Tyz obtained the data sheet. What will you do now? Condolences, Meditate, or Focus?")
    try: 
        if Interrogation_1 == 'Condolences':
            print("'You were a worthy opponent Phantox. Rest well.' Rev-Tyz uttered as he began to examine the data sheet.' <You can now examine the data sheet>")
        if Interrogation_1 == 'Meditate': 
            print("Good riddance. Now I must rest and then examine this data sheet.' <You can now examine the data sheet>")
        if Interrogation_1 == 'Focus': 
            print("'Alas, I have obtained the data sheet of the Pileqs. Now I can determine which planets they plan to conquer next. But first I must decipher it. Hmm...' Rev-Tyz stated intelligently. <You can now examine the data sheet>")
    except: 
        return ("Rev-Tyz: Welp, he's gone. I am going to sleep.")
#This instance will now transition into examining the data sheet. 

pd.read_csv('Pileq_XonoRex_File.csv')
pd.sort_index('Pileq_XonoRex_File.csv')
pd.plot(kind= 'bar')
pd.show()

#This will conclude the demo for now please refer to the print below
print("I hope that you enjoyed this demo of 'Universe of Loz: Battle of the Ages'. The full version will release before Friday, December 13th 2019.")