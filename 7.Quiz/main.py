from question import question

question_prompt = [
    "What is 5x12?\n(a) 75\n(b) 70\n(c) 65\n\n",
    "What is 273/3?\n(a) 81\n(b) 92\n(c) 91\n\n",
    "What is the remader of 300/8\n(a) 4\n(b) 5\n(c) 8\n\n"
]

questions = [
    question(question_prompt[0], "b"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "a")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "Enter: ").lower()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_quiz(questions)