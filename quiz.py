
def question_one():
    answer1 = input("The question is - What is the capital of Croatia? ").strip().lower()
    correct_answer1 = "zagreb"
    if answer1 == correct_answer1:
        return "That is the correct answer!"
    else:
        return f"That is the wrong answer. The correct answer is {correct_answer1}"

def question_two():
    answer2 = input("What is the name of the largest Hindu temple in India? ").strip().lower()
    correct_answer2 = "sri ranganathaswamy temple"
    if answer2 == correct_answer2:
        return "That is the correct answer!"
    else:
        return f"That is the wrong answer. The correct answer is {correct_answer2}"
    
def question_three():
    answer3 = input("What is the fear of long words called? ").strip().lower()
    correct_answer3 = "Hippopotomonstrosesquippedaliophobia"
    if answer3 == correct_answer3:
        return "That is the correct answer!"
    else:
        return f"That is the wrong answer. The correct answer is {correct_answer3}"

def run_quiz():
    print("Welcome to this quiz!")
    print(question_one())
    print(question_two())
    print(question_three())

if __name__ == "__main__":
    run_quiz()
    