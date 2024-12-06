# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
q = "Where were french fries originally made?"
options = "A) Belgium B) France C) America D) Italy"
print(q, "\n" + options)
answer = input("Enter your answer (A/B/C/D): ").strip().upper()
print("Correct!" if answer == "A" else "Incorrect. The correct answer is A) Belgium.")
