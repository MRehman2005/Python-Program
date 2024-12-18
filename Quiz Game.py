# Making Dictionary 
quiz = [
    {
        "question":"What's The Capital of Pakistan",
        "option":["A) Lahore","B) Islamabad","C) Karachi","D) Multan"],
        "answer" :"B"
    },
    {
        "question":"Which Programing language Is known as The language of Web",
        "option":["A) Java","B) C++","C) python","D) Javascript"],
        "answer": "D"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "option": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "option": ["A) Gold", "B) Oxygen", "C) Hydrogen", "D) Iron"],
        "answer": "B"
    }
]
# Function to run the quiz
def run_quiz():
    print("Your Quiz is Start..")
    print("Enter Your Answer With A,B,C,D")
    print("-"*30)
    score = 0
    for index,question in enumerate(quiz):
        print(f"\nQuestion{index+1} :{question['question']}")
        for option in question['option']:
            print(option)
            
            
        while True:
                userAnswer = input().strip().upper()
                if userAnswer in ['A','B','C','D']:
                    break
                else:
                    print("invalid Input Pleace enter A,B,C,D ")
                    
        if userAnswer == question['answer']:
            print("correct Answer")
            score+=1
        else:
            print("Worng Answer")
    print(f"The Total Score You Get is :{score}/{len(quiz) }")


run_quiz()

