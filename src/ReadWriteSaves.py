###################################################################################################
# IniParser provides functions for reading and writing ini files for Anyshift software. Also 
# includes hex values for compatible keys
#
# 2023 Menkaura Soft
###################################################################################################

import configparser  # Write and read ini files

def iniReader(file):

    options = {}
    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read(file)
    
    # Save values into dictionay
    options['nascar_mode'] = config['OPTIONS']['nascar racing mode']
    options['seven_gears'] = config['OPTIONS']['seven gears']
    options['rev_button'] = config['OPTIONS']['reverse is button']
    options['neutral'] = config['OPTIONS']['neutral detection']   
    options['neutral_wait_time'] = config['OPTIONS']['neutral delay']
    options['clutch'] = config['OPTIONS']['require clutch']    
    options['clutch_id'] = config['SHIFTER']['clutch id']
    options['clutch_axis'] = config['SHIFTER']['clutch axis']
    options['mem_mode'] = config['OPTIONS']['memory write mode']
    options['process'] = config['OPTIONS']['process name']
    options['db_base_addr'] = config['OPTIONS']['base address']
    options['offset'] = config['OPTIONS']['memory value offset']
    options['joy_id'] = config['SHIFTER']['joystick id']
    options['first'] = config['SHIFTER']['first gear']
    options['second'] = config['SHIFTER']['second gear']
    options['third'] = config['SHIFTER']['third gear']
    options['fourth'] = config['SHIFTER']['fourth gear']
    options['fifth'] = config['SHIFTER']['fifth gear']
    options['sixth'] = config['SHIFTER']['sixth gear']
    options['seventh'] = config['SHIFTER']['seventh gear']
    options['reverse'] = config['SHIFTER']['reverse']
    options['neut_key'] = config['KEYS']['neutral key']
    options['up_key'] = config['KEYS']['upshift']
    options['down_key'] = config['KEYS']['downshift']
    options['rev_key'] = config['KEYS']['reverse']
    options['presskey_timer'] = config['OPTIONS']['presskey timer']
    options['releasekey_timer'] = config['OPTIONS']['releasekey timer']
    options['first_value'] = config['OPTIONS']['first gear value']
    options['second_value'] = config['OPTIONS']['second gear value']
    options['third_value'] = config['OPTIONS']['third gear value']
    options['fourth_value'] = config['OPTIONS']['fourth gear value']
    options['fifth_value'] = config['OPTIONS']['fifth gear value']
    options['sixth_value'] = config['OPTIONS']['sixth gear value']
    options['seventh_value'] = config['OPTIONS']['seventh gear value']
    options['reverse_value'] = config['OPTIONS']['reverse gear value']
    options['neutral_value'] = config['OPTIONS']['neutral value']
    options['bitepoint'] = config['OPTIONS']['clutch bitepoint']
    options['comport'] = config['EXTRAS']['comport']

    return options


def iniWriter(options, upshift, downshift, rev_key, file):
    
    # Create object config
    config = configparser.ConfigParser(allow_no_value=True)

    config['SHIFTER'] = {'; This is the id number of the shifter you want to use': None,
                         'Joystick id': options['joy_id'],
                         '; This is the id number of the controller you wanth to use for clutch': None,
                         'clutch id': options['clutch_id'],
                         '; Selected controller axis for the clutch': None,
                         'clutch axis': options['clutch_axis'],
                         '; Joystick buttons for each gear': None,
                         'first gear': options['first'],
                         'second gear': options['second'],
                         'third gear': options['third'],
                         'fourth gear': options['fourth'],
                         'fifth gear': options['fifth'],
                         'sixth gear': options['sixth'],
                         'seventh gear': options['seventh'],
                         'reverse': options['reverse']
                        }

    config['KEYS'] = {'; Upshift, downshift, neutral and reverse key': None,
                      'upshift': upshift,
                      'downshift': downshift,
                      'reverse': rev_key,
                      'neutral key': options['neut_key']
                     }

    config['OPTIONS'] = {'; True if you have a shifter with seven gears. Seventh gear button must be configured or anyshift will crash ': None,
                         'seven gears': options['seven_gears'],
                         '; True if you want to change to neutral if no gear is selected in shifter. Most old games doesnt support this': None,
                         'neutral detection': options['neutral'],
                         '; Time the shifter must stay in Neutral to engage it': None,
                         'neutral delay': options['neutral_wait_time'],
                         '; True if clutch is needed to change gears': None,
                         'require clutch': options['clutch'],                         
                         '; Percent of the clutch that needs to be pressed to allow gear change': None,
                         'clutch bitepoint': options['bitepoint'],
                         '; True if the game uses a separated button for reverse. Gran Turismo or Nascar Racing for example': None,
                         'reverse is button': options['rev_button'],
                         '; Unique mode for old papyrus games where the game remember the gear you were in when you changed to': None,
                         '; reverse. This will change all way down to first gear and then press reverse to avoid desynchronization': None,
                         'nascar racing mode': options['nascar_mode'],
                         '; Instead of key presses it writes data to memory. I only included it because of Grand Prix 2': None,
                         '; Each game has different memory values. No offical support for this one': None,
                         'memory write mode': options['mem_mode'],
                         '; Name of the process of the game': None,
                         'Process name': options['process'],
                         '; Base address. Ex: 0.74 = 0x01D3A1A0 ': None,
                         'Base address': options['db_base_addr'],
                         '; Memory value offset from base addres ': None,
                         'Memory value offset': options['offset'],
                         '; Values that the game uses for each gear': None,
                         'neutral value': options['neutral_value'],
                         'first gear value': options['first_value'],
                         'second gear value': options['second_value'],
                         'third gear value': options['third_value'],
                         'fourth gear value': options['fourth_value'],
                         'fifth gear value': options['fifth_value'],
                         'sixth gear value': options['sixth_value'],
                         'seventh gear value': options['seventh_value'],
                         'reverse gear value': options['reverse_value'],
                         '; Delays for key presses and releases. Tinker with this if game doesnt detect key presses': None,
                         'presskey timer': options['presskey_timer'],
                         'releasekey timer': options['releasekey_timer'],
                        }    

    config['EXTRAS'] = {
                        '; select arduino com port': None,
                        'comport' : options['comport'],
                       }     

    # Write the file
    with open(file, "w") as configfile:
        config.write(configfile)   