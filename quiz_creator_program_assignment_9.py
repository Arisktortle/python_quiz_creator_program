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
        
#create a function that will ask question 
#create function that will ask for the right answer
#start loop, prompting to ask question and the right answer until the prompted number of questions
#export the questions into a file