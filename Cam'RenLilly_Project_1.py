"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Cam'Ren]
Date: [10/23/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None

     #.capitalize() method is used to ensure the first letter of the character class is uppercase 
    character_class = character_class.capitalize()

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None
    
     character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 40
    }
    return character

   

def calculate_stats(character_class, level):
    #if/elif/else statements used to test conditions and return the right stats accordingly.
    #different classes have different formulas for calculating stats
    strength = 10
    stength = 12
    health = 30


    if character_class == "mage":
        strength += 15
        magic += 40
        health += 30
    elif character_class == "warrior":
        strength += 50
        magic += 10
        health += 40
    elif character_class == "rogue":
        strength += 25
        magic += 20
        health += 60
    elif character_class == "cleric":
        strength += 15
        magic += 25
        health += 30
    else:
        print('invalid')
        return calculate_stats('Mage', level)

    return strength, magic, health

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
    

    

    

def load_character(filename):
        import os
        #checks to see if the file exists and returns None if it doesn't
        if not os.path.exists(filename):
            return None
        
        #opens the file then reads it then closes file.
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        character = {}

        for line in lines:
            if ": " not in line:
                continue
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace("character ", "")
            if value.isdigit():
                value = int(value)
            character[key] = value

        if len(character) == 0:
            return None

        return character
        
def display_character(character):

    print("=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key}: {value}")
    
    
#Ai recommended that the stats should be recalculated when leveling up for more consistency
def level_up(character):
    #increases character level
    character['level'] += 1
    #This line calls the calculate_stats function to get the new stats based on the updated level
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"\n{character['name']} earned a level up your level is now {character['level']}.")


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
