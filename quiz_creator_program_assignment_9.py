#welcome menu for quiz 
def main():
    print("Welcome to Quiz Creator Program!")

    while True:
        try:
          number_of_questions = int(input("Enter how many questions to input: ")) #ask user how many questions in will be inputted
          if number_of_questions > 0: 
             break
          else:
            print("Enter a valid number greater than 0.")
        except ValueError:
            print("Invalid number input.")
        
#create function that will ask for the right answer
def user_questions(number): 
    print(f"For question {number}")
    question = input("Enter your question:\n ").strip() #function that will ask question 
    
    print("\n Enter the choices: ") #prompts the user to enter the 4 choices
    choices = {}
    for option in ['a', 'b', 'c', 'd']:
        answer = input(f" {option}) ").strip()
        choices[option] = answer
    
    while True:
        correct_answer = input("\n Enter the correct answer (a, b, c, d,: )").lower() #inputs the correct answer and stores
        if correct_answer in choices:
            break
        else:
         print("Invalid option. Select from (a, b, c, d,).")
    
    return { #created dictionary to access the inputs easier
        "number": number, 
        "question": question,
        "choices": choices,
        "correct": correct_answer
    }     
    
#start loop, prompting to ask question and the right answer until the prompted number of questions
#export the questions into a file