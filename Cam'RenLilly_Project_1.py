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
        gold = 45
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


    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

def calculate_stats(character_class, level):

    #if/elif/else statements used to test conditions and return the right stats accordingly.
    #different classes have different formulas for calculating stats
    if character_class == "Mage":
        strength = 3 + (level * 3)
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
        return (0,0,0)
        
    return (strength, magic, health)

    


    

def save_character(character, filename):

    #file is opened and char_file is filled with the character's stats
    #Ai used to fix error like char_file on line 92
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
    

    


    

def display_character(character):
    if not character:
        print("No character data to display.")
        #returning nothing results in "None"
        return

    print("=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key}: {value}")
    

   
    
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

