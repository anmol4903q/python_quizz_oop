# Your quiz data in a list of dictionaries, containing questions and answers.
quiz = [
    {"question": "The sun rises in the east.", "answer": "true"},
    {"question": "Fish can fly in the sky like birds.", "answer": "false"},
    {"question": "2 + 2 equals 4.", "answer": "true"},
    {"question": "Cats are bigger than elephants.", "answer": "false"},
    {"question": "Water freezes to become ice.", "answer": "true"},
    {"question": "The moon is made of cheese.", "answer": "false"},
    {"question": "A week has 7 days.", "answer": "true"},
    {"question": "Bananas are blue in color.", "answer": "false"},
    {"question": "We breathe in oxygen.", "answer": "true"},
    {"question": "Birds have wings.", "answer": "true"},
    {"question": "Cars can swim in water.", "answer": "false"},
    {"question": "The earth is round.", "answer": "true"},
    {"question": "Dogs can bark.", "answer": "true"},
    {"question": "The number after 9 is 8.", "answer": "false"},
    {"question": "We sleep at night.", "answer": "true"},
    {"question": "Apples grow on banana trees.", "answer": "false"},
    {"question": "The capital of India is New Delhi.", "answer": "true"},
    {"question": "1 liter is more than 1 milliliter.", "answer": "true"},
    {"question": "Fire is cold.", "answer": "false"},
    {"question": "There are 12 months in a year.", "answer": "true"}
]

# Question class to store the question text and the correct answer
class Question:
    def __init__(self, text, answer):
        self.text = text  # The actual question
        self.answer = answer  # The correct answer (True/False)

# List to hold question objects
question = []
for i in quiz:
    question_txt = i["question"]
    question_ans = i["answer"]
    new_ques = Question(question_txt, question_ans)  # Creating a new Question object
    question.append(new_ques)  # Adding it to the list

# QuizBrain class to control the quiz flow
class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0  # Start from the first question
        self.question_list = q_list  # List of all questions
        
    def next_question(self):
        score = 0  # Initialize score
        total_questions = len(self.question_list)  # Get the total number of questions
        while self.question_num < len(self.question_list):  # While there are questions
            curr_ques = self.question_list[self.question_num]  # Get the current question
            # Ask the user for their answer
            guess = input(f"Q:{self.question_num + 1} : {curr_ques.text} (True/False): ").lower()
            correct_ans = curr_ques.answer  # The correct answer

            if guess == correct_ans:  # Check if the answer is correct
                print("Correct!! 😏 Wow, you nailed it! 😎")
                score += 1  # Increase the score if correct
            else:
                print("Incorrect answer! 😜 Oh, you got it wrong. Shocking, right?")
                print(f"Your total score is {score}. Oh, well...")  # Display score at failure
                break  # End the quiz if the answer is wrong
            
            # If correct, move to the next question
            self.question_num += 1
            print(f"Your total score is {score}. Keep it up! 🤘")
            print()  # Empty line for better readability
        
        # If user answers all questions correctly
        if score == total_questions:
            print("🎉 Congratulations! You've answered all questions correctly! 🏆")
        else:
            print("Better luck next time. 😉")

# Create a QuizBrain object to start the quiz
quiz_game = QuizBrain(question)
quiz_game.next_question()  # Start the quiz by calling the method
