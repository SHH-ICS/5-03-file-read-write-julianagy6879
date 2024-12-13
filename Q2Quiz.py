# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
score = 0

questions = [
    ["Where were french fries originally made?", "a", ["a) Belgium", "b) France", "c) America", "d) Italy"]],
]

for question in questions:
    print(question[0])
    for option in question[2]:
        print(option)
    answer = input("Answer (a/b/c/d): ").lower()
    if answer == question[1]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(f"Score: {score}/{len(questions)}")
