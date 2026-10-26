# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 4
# Date: 26 October 2026
# Description: Game of Thrones actor-character guessing game
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

cast = [
    ("Sean Bean", "Ned Stark"),
    ("Mark Addy", "Robert Baratheon"),
    ("Nikolaj Coster-Waldau", "Jaime Lannister"),
    ("Michelle Fairley", "Catelyn Stark"),
    ("Lena Headey", "Cersei Lannister"),
]

def play_guessing_game():
    score = 0
    for actor, character in cast:
        while True:
            print(f"Who played {character}?")
            print("Options:", ", ".join(a for a, _ in cast))
            answer = input("Actor name: ").strip()
            if answer.casefold() == actor.casefold():
                score += 1
                print("Correct!\n")
                break
            print(f"Incorrect. The correct actor is {actor}. Try again.\n")
    print(f"Game finished. Correct character links: {score}/{len(cast)}")

if __name__ == "__main__":
    play_guessing_game()
