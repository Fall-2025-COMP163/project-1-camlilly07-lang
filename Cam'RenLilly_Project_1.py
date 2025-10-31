"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Cam'Ren]
Date: [10/23/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""


def create_character(name, character_class):
    #.capitalize() method is used to ensure the first letter of the character class is uppercase 
    character_class = character_class.capitalize()

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    if character_class == "Mage":
        gold = 40
    elif character_class == "Warrior":
        gold = 60
    elif character_class == "Rogue":
        gold = 70
    elif character_class == "Cleric":
        gold = 50
    else:
        gold = 40
    
    #dictionary of all of the defined variables is returned
    character =  {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
        }
    return character


    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold







 
    
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

def calculate_stats(character_class, level):

    #if/elif/else statements used to test conditions and return the right stats accordingly.
    #different classes have different formulas for calculating stats
    if character_class == "Mage":
        strength = 3 + level
        magic = 20 + (level * 5)
        health = 30 + (level * 10)
    elif character_class == "Warrior":
        strength = 20 + (level * 4)
        magic = 5 + (level * 2)
        health = 45 + (level * 10)
    elif character_class == "Rogue":
        strength = 10 + (level * 3)
        magic = 5 + (level * 5)
        health = 25 + (level * 10)
    elif character_class == "Cleric":
        strength = 12 + (level * 3)
        magic = 10 + (level * 4)
        health = 40 + (level * 10)
    else:
        print('Invalid character class')
        
    return (strength, magic, health)

    """
    
    
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)


    

def save_character(character, filename):
    import os
    #file is opened and char_file is filled with the character's stats
    #Ai used to fix error like char_file on line 92
    if not isinstance(character, dict) or not filename:
        return False
    
    directory = os.path.dirname(filename)

    if directory and not os.path.exists(directory):
        return False
    
   
        #with closes the file automatically after the block of code finishes
    with open(filename, "w",) as char_file:
        char_file.write(f"Character Name: {character['name']}\n")
        char_file.write(f"Class: {character['class']}\n")
        char_file.write(f"Level: {character['level']}\n")
        char_file.write(f"Strength: {character['strength']}\n")
        char_file.write(f"Magic: {character['magic']}\n")
        char_file.write(f"Health: {character['health']}\n")
        char_file.write(f"Gold: {character['gold']}\n")
    
    return True
    

    

"""
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
        import os
        #checks to see if the file exists and returns None if it doesn't
        if not os.path.exists(filename):
            return None

        with open(filename, "r",) as char_file:
            #Reads all the lines in char_file
            lines = char_file.readlines()
        #curly brackets used for dictionary
        char_dict = {}
        key_dict = {
        "name": "name",
        "class": "class",
        "level": "level",
        "strength": "strength",
        "magic": "magic",
        "health": "health",
        "gold": "gold"
          }

        for line in lines:
            if ':' in line:
                #strip() removes any whitespace or newlines 
                #split() will split the line into parts using on the first colon
                key, value = line.strip().split(": ", 1)
                key = key.lower().replace("character ", "")
                value = value.strip()
                normalized_key = key_dict.get(key, key.lower())
                char_dict[normalized_key] = value

        for key in ["level", "strength", "magic", "health", "gold"]:
                    if key in char_dict:
                        char_dict[key] = int(char_dict[key])
        return char_dict
    #Ai was used to make the except work by using  FileNotFoundError
    #FileNotFoundError will occur when a file is opened that doesn't exist.

    

"""
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    if not character:
        print("No character data to display.")
        #returning nothing results in "None"
        return

    print("=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key}: {value}")
    

    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    
#Ai recommended that the stats should be recalculated when leveling up for more consistency
def level_up(character):

    if not character or "level" not in character:
        return
    
    #increases character level
    character['level'] += 1
    #This line calls the calculate_stats function to get the new stats based on the updated level
    strength, magic, health = calculate_stats(character['class'], character['level'])
    #all of these stats are updated in the character dictionary from the new calculated stats
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    character['gold'] += 40



    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Jos�", "Warrior")
    display_character(char)
    save_character(char, "special_char_test_30.txt")
    loaded = load_character("special_char_test_30.txt")
    display_character(loaded)
   
    

    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
