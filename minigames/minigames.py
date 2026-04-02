import random

riddles = [
    {
    "Question": "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?",
    "Answer": "0.05"
},
{
    "Question": "What is the answer to the Ultimate Question of Life, the Universe, and Everything",
    "Answer": "42"
},
{
  "Question": "There is a locked safe, requiring a 4 number combination to open",
    "Answer": "7624"  #DO NOT CHANGE THIS NUMBER, IT LINKS TO A ROOM DESCRIPTION
},
{
   "Question": "There are 6 sisters. Each sister has 1 brother. How many brothers are in the sisters family?",
    "Answer": "1"   
},
{  
    "Question": "What can fill an entire room without taking up any space?",
    "Answer": "Light" 
}
#Riddles that will be used in the game, this is a list of dictionaries consisting of questions and answers

]



def higher_lower(index):
    #This is the code for our higher or lower game, It starts us off with 3 lives and gets a random integer which is checked aganist our own choice
    #It checks to make sure the entered input is an interger and if not it returns an error
    lives = 3
    computer_guess = random.randint(1,9)
    while lives > 0:
        user_input = input("Guess a number between 0 and 10: ")

        try:
            user_input = int(user_input)
        except:
            print("Enter an integer number")
            return False

        if user_input == computer_guess:
            print("Your guess is correct")
            return True
        elif user_input > computer_guess:
            lives -= 1
            print("Your guess is too high")
            print(f"You have {lives} guesses remaining")
        elif user_input < computer_guess:
            lives -= 1
            print("Your guess is too low")
            print(f"You have {lives} guesses remaining")   
    if lives == 0:    
        print("You are out of guesses")
        return False

def rock_paper_scissors(index):
    #This function just checks the user input to see if it is valid input and then get the computer to make a choice and passes the determination of a winner
    #to the determine winner functiom
    user_action = input("A computer challenges you to rock paper scissors.\nWhat do you choose: ")
    print(user_action.lower())

    if not (user_action.lower() == "rock" or user_action.lower() == "paper" or user_action.lower() == "scissors"):
        print("Thats not how you play rock paper scissors")
        return False

    rps = ["rock", "paper", "scissors"]
    computer_action = random.choice(rps)
    return determine_winner(user_action, computer_action)


def determine_winner(user_action, computer_action):
    #It takes valid inputs from the rock paper scissors function and compares them to our statements to determine a winner
    if user_action == computer_action:
        print(f"Both selected {user_action}. The computer counts this as a loss for you?")
        return False
    elif user_action.lower() == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            return True
        else:
            print("Paper covers rock! You lose.")
            return False
    elif user_action.lower() == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            return True
        else:
            print("Scissors cuts paper! You lose.")
            return False
    elif user_action.lower() == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            return True
        else:
            print("Rock smashes scissors! You lose.")
            return False

def sequences_game(index):
    #This piece of code is a game to check matching sequences
    potential_sequence_direction = ["left", "right"]
    clicks = 0
    lives = 3
    computer_guess = random.choices(population=potential_sequence_direction, k= 4)
    sequence = []
    answer = []
    for direction in computer_guess:
            sequence.append(direction)
    for _ in range(len(sequence)):
            answer += "_"
    while clicks < 4:
        user_input = input("Guess a direction either left or right: ").lower()
        if user_input == "left" or user_input == "right":
            for position in range(len(sequence)):
                item = sequence[position]
                if item == user_input:
                    answer[position] = item
                    clicks += 1 
                else:
                    lives -= 1
            print(f"The correct sqeuence is: {answer}")
            if clicks == 4:       
                return print("Treasure unlocked")
            elif lives == 0:
                return print("Lockpick broken")
        else:
             print("Invalid Entry, Please only type in left or right")

"""
def riddle_answers(questions=riddles):
     computer_choice = random.choice(questions)
     print(computer_choice["question"])
     user_answer = input("What do you think the answer is: ")
     if computer_choice["answer"] == user_answer:
          print("That is correct")
     else:
          print("That is incorrect")
          print(computer_choice["answer"])
"""

def riddle(index, riddle = riddles):
    #This game checks the riddles list for a riddle and then compares the users answers to those in the riddles list
    print(f'Riddle me this: {riddle[index]["Question"]}')
    user_answer = input("What do you think the answer is: ")
    if riddle[index]["Answer"] == user_answer:
        return True #correct
    else:
        return False #incorrect

            







