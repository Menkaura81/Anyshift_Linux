from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time  # Delays

#region KEYPRESSES
# (code by Menkaura)
# Function to send key presses for upshift
def KeyPress_up(options):
    time.sleep(float(options['presskey_timer']))    
    pressKey(options['up_key'])  # press
    time.sleep(float(options['releasekey_timer']))
    releaseKey(options['up_key'])  # release


# Function to send key presses for downshift
def KeyPress_down(options):
    time.sleep(float(options['presskey_timer']))
    pressKey(options['down_key'])  # press
    time.sleep(float(options['releasekey_timer']))
    releaseKey(options['down_key'])  # release


# Function to send key presses for reverse is button mode. Two separate functions, one for press...
def KeyPress_rev(options):
    time.sleep(float(options['presskey_timer']))
    pressKey(options['rev_key'])  # press


# ... And another to release
def KeyRelease_rev(options):
    time.sleep(float(options['releasekey_timer']))
    releaseKey(options['rev_key'])  # release


# Function to apply sequential logic to h-shifter inputs, and make the necessary key presses
# Flag for avoiding first shifting bug when running nascar mode 
first_time = True
def sendKeystrokes(gear_selected, actual_gear, options):
    global first_time
    if options['nascar_mode'] == True:
        if options['rev_button'] == True and gear_selected == -1:
            while actual_gear != 1:
                KeyPress_down(options)
                actual_gear -= 1
            KeyPress_rev(options) 
            act_gear = 1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == True:  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up(options)                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down(options)
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up(options)
                                first_time = False   
                        else:
                            act_gear += 1
                            KeyPress_up(options)                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down(options)
    else:
        # Press key selected for reverse
        if options['rev_button'] == True and gear_selected == -1:
            KeyPress_rev(options) 
            act_gear = -1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == True:  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up(options)                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down(options)
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up(options)
                                first_time = False  
                        else:
                            act_gear += 1
                            KeyPress_up(options)                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down(options)                            
    return act_gear