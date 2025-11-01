Game Concept:
Welcome to a classic fantasy RPG world where players can create unique characters to embark on epic adventures. The world is filled with warriors, mages, rogues, and clerics—each with their own strengths and magical abilities.

Design Choices:
Each class was designed with different strengths to reflect traditional RPG archetypes:

I used the basic classes that was provided in the documentation

I used my knowledge I gained from playing games like Elden Ring.
- Warrior: High strength and health, low magic. A great choice for combat.
- Mage: High magic, low strength, moderate health. Reigns supreme in spell-casting.
- Rogue: Balanced strength and magic, lower health. Agile and versatile.
- Cleric: Moderate strength, strong magic, high health. resilient.



Creativity:
with the use of Ai I used
- Stat Recalculation on Level-Up: When a character levels up, their stats are recalculated using the same logic as character creation, ensuring consistency and scalability.
- Flexible File Saving/Loading: Characters can be saved to and loaded from text files using a structured format. The system handles missing files and malformed input gracefully

Ai Usage:
- Designing and refining the save_character() function, especially for file I/O error handling.
- Improving key normalization logic in load_character() to handle variations in file formatting.
- Recommending stat recalculation during level-up for consistency.


How to run:
1. Ensure you have Python 3 installed on your system.
2. Save the main program file as `project1_starter.py`.
3. Open a terminal or command prompt and navigate to the directory containing the file.
4. Run the program using:
To run automated tests (if using pytest):
Save the test file as test_project1.py in the same directory.
Run: pytest test_project1.py
