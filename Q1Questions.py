# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
filehandle = open("testFile.txt",'w')
Question = input("What is your question?" )
filehandle.write(Question +'\n')
for i in range (4):
answer = input ("Options:")
filehandle.write(answer +'\n')
answer = input("Correct answer?")
filehandle.write(answer +'\n')
filehandle.close()
