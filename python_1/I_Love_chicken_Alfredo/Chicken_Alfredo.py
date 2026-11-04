questions = [
    ("Who is that behind you?", "Graham"),
    ("how many fingers am I holding up?", "10"),
    ("if up was down and left was right then who was the one who said that?", "you"),
    ("wait", "ok"),
    ("dude i love food", "same"),
    ("what is grahams favorite number?", "36"),
    ("do a backflip right now", "ok"),
    ("wait what was i doing again?", "quiz"),
    ("why did you do that?", "cuz"),
    ("What is 6 * 6?", "36"),
    ("ok that backflip was pretty cool", "thanks"),
    ("how do you calculate the area of a triangle?", "why do i need to know that?"),
    ("what", "huh"),
    ("wait what was your name again?", "uhm"),
    ("what time is it?", "time for you to get a watch"),
    ("How many hours are in a day?", "24"),
    ("do you have any questions so far?", "no"),
    ("im sleepy im gonna take a nap real quick", "ok"),
    ("zzzzzzzzzzz", ""),
    ("zzzzzzzzzzzzzzzzzz", ""),
    ("zzzzzzz", "wake up!"),
    ("huh youre still here?", "yeah mb"),
    ("how many spinning apples can you imagine in your head?", "enough"),
    ("i see a little silhouetto of a man", "scaramouche scaramouche will you do the fandango"),
    ("oh hi there", "hey"),
    ("welp seems like the quiz is ending soon", "sure is pal"),
    ("i guess this is goodbye", "not a goodbye but a see you later"),
    ("*sniffle* *sniffle*", "its ok man"),
    ("what is 1+1?", "2"),
]
score = 0
wrong_answers = []

print("===================================")
print("       WELCOME TO THE QUIZ!")
print("===================================")

player_name = input("What is your name? ")

print("\nGood luck,", player_name + "!")
print("There are", len(questions), "questions.")
print("Type your answer and press Enter.")
print("-----------------------------------")

for number, question_data in enumerate(questions, start=1):
    question = question_data[0]
    correct_answer = question_data[1]

    print(f"\nQuestion {number}: {question}")

    user_answer = input("Your answer: ").strip().lower()

    # Check the answer
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("Correct answer:", correct_answer)

        wrong_answers.append({
            "question": question,
            "your_answer": user_answer,
            "correct_answer": correct_answer
        })

# Calculate final results
total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n===================================")
print("           QUIZ RESULTS")
print("===================================")
print("Player:", player_name)
print("Correct answers:", score)
print("Incorrect answers:", total_questions - score)
print(f"Final score: {percentage:.1f}%")

if percentage == 100:
    print("thats cool m8")
elif percentage >= 80:
    print(" couldve been better")
elif percentage >= 60:
    print("ouch dude")
else:
    print("you failed.")

# Show the questions answered incorrectly
if wrong_answers:
    print("\nQuestions to review:")

    for item in wrong_answers:
        print("\nQuestion:", item["question"])
        print("Your answer:", item["your_answer"])
        print("Correct answer:", item["correct_answer"])
else:
    print("\nYou got every question correct!")

print("\nThanks for playing,", player_name + "!")
