import dt
import imports_necessary
import colorama
from colorama import Fore, Style

def the_balance() :
    
    
    
    """
    This function will allow players to input one of the selections printed within the "if" statements.
    
    """
    
    
    Battle_1 = input(dt.B1_Text)
    try: 
        if Battle_1 == dt.Fire : 
            print(dt.B1_Choice1)
            assert (Battle_1 == dt.Fire) == True
        if Battle_1 == dt.Air : 
            print(dt.B1_Choice2)
            assert (Battle_1 == dt.Air) == True
        if Battle_1 == dt.Water : 
            print(dt.B1_Choice3)
            assert (Battle_1 == dt.Water) == True
        if Battle_1 == dt.Lightning :
            print(dt.B1_Choice4) 
            assert (Battle_1 == dt.Lightning) == True
    except:
        return(dt.B1_Else) 
    
    next
    print(Style.RESET_ALL)
    next
    
    Battle_2 = input(dt.B2_Text)
    try: 
        if Battle_2 == dt.Stun:
            print(dt.B2_Choice1)
            assert (Battle_2 == dt.Stun) == True
        if Battle_2 == dt.Trail: 
            print(dt.B2_Choice2)
            assert (Battle_2 == dt.Trail) == False
        if Battle_2 == dt.Counter :
            print(dt.B2_Choice3)
            assert (Battle_2 == dt.Counter) == True
    except:
        return (dt.B2_Else )
    
    next
    print(Style.RESET_ALL)
    next
        
    Battle_3 = input(dt.B3_Text)
    try: 
        if Battle_3 == dt.Shield :
            print(dt.B3_Choice1)
            assert (Battle_3 == dt.Shield) == True
        if Battle_3 == dt.Circumference :
            print(dt.B3_Choice2)
            assert (Battle_3 == dt.Circumference) == True
        if Battle_3 == dt.Wimper : 
            print(dt.B3_Choice3)
            assert (Battle_3 == dt.Wimper) == True
    except:
        return (dt.B3_Else)
    
    
    next
    print(Style.RESET_ALL)
    next
                
    
    Battle_4 = input(dt.B4_Text)
    try: 
        if Battle_4 == dt.Fury:
            print(dt.B4_Choice1)
            assert (Battle_4 == dt.Fury) == True 
        if Battle_4 == dt.Slash:
            print(dt.B4_Choice2)
            assert (Battle_4 == dt.Slash) == True
        if Battle_4 == dt.Blasphemy :
            print(dt.B4_Choice3)
            assert (Battle_4 == dt.Blasphemy) == True
    except:
         return (dt.B4_Else)

    
    next
    print(Style.RESET_ALL)
    next
    
    Interrogation_1 = input(dt.I5_Text)
    try: 
        if Interrogation_1 == dt.Condolences:
            print(dt.I5_Choice1)
            assert (Interrogation_1 == dt.Condolences) == True 
        if Interrogation_1 == dt.Meditate: 
            print(dt.I5_Choice2)
            assert (Interrogation_1 == dt.Meditate) == True
        if Interrogation_1 == dt.Focus: 
            print(dt.I5_Choice3)
            assert (Interrogation_1 == dt.Focus) == True 
    except: 
        return (dt.I5_Except)

    next
    
    import chart_necessary 
    
    next 
    
    print(Style.RESET_ALL)
    
    next
    
    Interrogation_2 = input(dt.I6_Text)
    try:
        if Interrogation_2 == dt.Report: 
            print(dt.I6_Choice1)
            assert (Interrogation_2 == dt.Report) == True
        if Interrogation_2 == dt.Brag:
            print(dt.I6_Choice2)    
            assert (Interrogation_2 == dt.Brag) == True 
        if Interrogation_2 == dt.Troll:
            print(dt.I6_Choice3)
            assert (Interrogation_2 == dt.Troll) == True 
    except: 
        return (dt.I6_Except)
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

    
    

    
    
        
        
        
        
    
    
    
    
    
    

    
