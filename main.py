"""
CIS*1500 Assignment - Math Flashcard Game

We confirm that the work presented in this assignment is our own and that we have followed all
academic integrity guidelines for this course. We have not copied code from other students,
online sources, or AI tools without proper acknowledgment.
"""

import random
import csv
import datetime


def show_main_menu():
    """
    Show the main menu and return a valid choice.
    """
    while True:
        print("\nSelect one of the options:")
        print("(m)ultiplication")
        print("(a)ddition")
        print("(r)esults")
        print("(q)uit")

        choice = input("Enter your choice: ").strip().lower()
        if choice in ("m", "a", "r", "q"):
            return choice
        else:
            print("Invalid choice. Please enter m, a, r, or q.")


def make_addition_flashcard():
    """Make and return a random addition question and its answer."""
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    question = f"What is {a} + {b}? "
    return question, a + b


def make_multiplication_flashcard():
    """Make and return a random multiplication question and its answer."""
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    question = f"What is {a} X {b}? "
    return question, a * b


def get_integer_input(prompt):
    """
    Ask until user enters a valid integer.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_results(filename="results.csv"):
    """
    Read all rows from results.csv or return empty list if file doesn't exist.
    """
    rows = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            #handles "User_name, Date, Score"
            reader = csv.DictReader(f, skipinitialspace=True)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print("File couldn't be found. Please enter a valid file.")
        pass
    return rows


def save_results(rows, filename="results.csv"):
    """
    Put all results into results.csv in the format:
    User_name, Date, Score
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        # header
        f.write("User_name, Date, Score\n")
        # rows
        for row in rows:
            line = f"{row['User_name']}, {row['Date']}, {row['Score']}\n"
            f.write(line)


def update_user_results(user_name, score, filename="results.csv"):
    """
    Update results.csv so there is only one record per
    user per day and the best score for that day is kept
    for that user
    """
    today = datetime.date.today()
    date_str = f"{today.year}-{today.month}-{today.day}"  # e.g. 2025-11-1
    rows = read_results(filename)

    updated = False
    for row in rows:
        if row["User_name"] == user_name and row["Date"] == date_str:
            # already have a record for this user today
            try:
                old_score = int(row["Score"])
            except ValueError:
                old_score = 0

            if score > old_score:
                row["Score"] = str(score)
            updated = True
            break

    if not updated:
        #This means it the first game for this user today
        rows.append({
            "User_name": user_name,
            "Date": date_str,
            "Score": str(score)
        })

    save_results(rows, filename)


def show_user_results(name, filename="results.csv"):
    """
    Show all stored results for the given user.
    """
    rows = read_results(filename)

    print(f"\nResults for {name}:")
    found = False
    for row in rows:
        if row["User_name"] == name:
            print(f"  {row['User_name']}, {row['Date']}, {row['Score']}")
            found = True

    if not found:
        print("  No results found.")


def play_round(operation, user_name):
    """
    Play 5 flashcards of the chosen operation and update score and results.
    """
    score = 0
    total = 0

    print(f"\nStarting a new round of {operation} flashcards!")

    for _ in range(5):
        print(f"\nYour current score is {score} out of {total}")

        if operation == "addition":
            question, correct_answer = make_addition_flashcard()
        else:
            question, correct_answer = make_multiplication_flashcard()

        user_answer = get_integer_input(question)
        total += 1

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect, the correct answer was {correct_answer}.")

    print(f"\nRound complete! Your final score: {score} out of {total}")
    update_user_results(user_name, score)
    #This lets the user read their score before going back
    input("Press Enter to return to the main menu:")


def get_user_name():
    """
    Ask the player for their name and this can't be empty.
    """
    while True:
        name = input("Please enter your name: ").strip().lower()
        if name:
            return name
        print("Name cannot be empty. Try again.")


def main():
    """
    Main game loop.
    """
    print("Math Flashcard Game!\n-----------------------")
    user_name = get_user_name()

    while True:
        choice = show_main_menu()

        if choice == "m":
            play_round("multiplication", user_name)
        elif choice == "a":
            play_round("addition", user_name)
        elif choice == "r":
            # allow checking any name, not just the current user
            name = input("Enter a name to view results: ").strip().lower()
            if not name:
                name = user_name
            show_user_results(name)
        elif choice == "q":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
