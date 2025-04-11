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

def export_questions_to_file(filename="quiz_data.txt"): #export the questions into a file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        count = sum(1 for line in lines if line.strip().startswith("#QUESTION_") and "_START" in line)
        return count
    except FileNotFoundError:
        return 0
    
#counts the number of questions inputted
def get_existing_question_count(filename="quiz_data.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        count = sum(1 for line in lines if line.strip().startswith("#QUESTION_") and "_START" in line)
        return count
    except FileNotFoundError:
        return 0
    
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
            
    starting_number = get_existing_question_count() + 1

    for i in range(number_of_questions):
        question_number = starting_number + i
        question_data = user_questions(question_number)
        export_questions_to_file(question_data)
        print(f"\nInputted question {question_number} saved.\n")
        
    print(f"{number_of_questions} question(s) added and exported to file.\n")
    
if __name__ == "__main__":
    main()