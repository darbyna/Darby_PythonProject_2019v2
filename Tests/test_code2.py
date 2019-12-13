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
    

#Once you have submitted an answer to the function below. We will proceed to the next section.

the_balance2()