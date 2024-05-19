import random
   
def generate_number():
    
    generated_number = random.randint(1, 100)
    
    
    print("Welcome to the Guessing Game!")
    print("You have a maximum of 10 chances.")
    
    for attempts in range(1, 11):
        user_choice = int(input("Enter your number between 1 and 100: "))
        
        if user_choice < generated_number:
            print("Too low! Try again.")
        elif user_choice > generated_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number in", attempts, "attempts.")
            break
    else:    
        print("Sorry, you've run out of attempts. The number was", generated_number)

generate_number()
