quiz = {
    "question1":{
        "question:":"what colour is your bugatti?",
        "answer:":"black"
    },
    "question2:":{
        "question:":"what is the name of your car?",
        "answer:":"bugatti"
    },
    "question3":{
        "question:":"what is the name of your jet?",
        "answer:":"boeing 201"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Enter your answer:")

    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score = score+1
        print("Your score is: " + str(score))
    else:
        print("Wrong!")
        print("The correct answer is: " + value['answer'])
        print("Your score is: " + str(score))

print("You got score:" + str(score) + "out of 3 questions correctly." )
print("Your percentage is: " + str(int(score/3 *100)) + "%")

# error