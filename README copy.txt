Math Flashcard Game
—————————————————————————

Files Involved:
————————————
- main.py : A Python program to run the math flashcard game
- results.csv : File that stores the users results (created automatically when game is played)
- README : File with a brief explanation of the code

How to Run:
————————————
	1	Everything needs to be in the same folder, otherwise Python won’t find the files
	2	Open a command prompt in that folder
	3	Run : python3 main.py

How the Game Works:
————————————
- When you start the program, you are asked for your name
- Then you will see a text menu with the following options:
	•	(m)ultiplication
	•	(a)ddition
	•	(r)esults
	•	(q)uit
- Choosing “multiplication” or “addition” will start a round of 5 flashcards
- The game picks random numbers between 0 and 9
- After each question, the program tells you if you are correct or not
- The program will read your current score as: “Your current score is X out of Y”
- At the end of the 5 questions, the program:
	•	Shows your total score for the round
	•	Saves the score in the “results.csv” file
	•	If you play more than once in a day, it only keeps your best score

Results File (results.csv)
————————————
- This file is a comma-separated-values (CSV) file
- The header row is : User_name,Date,Score
- For example:
	•	Tom,2025-11-02,4
	•	 Alice,2025-11-02,2
- If a user plays multiple times on the same day, the highest score for that day is stored

Results Menu Option
————————————
- When you choose (r)esults from the menu:
	•	The program reads “results.csv”
	•	It prints all rows that match your name.
	•	If there are no results for your name, it will tell you 

Defensive Programming and Input Validation
————————————
- The menu only accepts: m, a, r, or q (either upper or lowercase)
- When a number is expected, the program:
	•	Re-prompts until a valid whole number is entered 
	•	The program checks whether “results.csv” exists, and if it doesn’t, it makes the file when saving for the first time

Limitations
————————————
- The program only supports one active user name at a time (this will be the name that was entered when the program starts)
- The “results.csv” file is stored in the same folder as “main.py”
