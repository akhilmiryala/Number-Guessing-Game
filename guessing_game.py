import random


def start_game():
  print("Welcome to the Number Guessing Game!")
  solution = random.randint(1,10)
  guess = input("Please enter a number between 1 to 10 as a guess  ")
  guess = int(guess)
  number_Of_Attempts = 1
  while guess != solution:
    if guess > solution:
      print("it's lower")
    elif guess < solution:
      print("it's higher")
    guess = input("enter a new number as a guess between 1 to 10   ")
    guess = int(guess)
    number_Of_Attempts += 1
  print("Got it")
  print("It took you {} attempts".format(number_Of_Attempts))
  print("The game is now ending")
  return


    # """Psuedo-code Hints
    
    # When the program starts, we want to:
    # ------------------------------------
    # 1. Display an intro/welcome message to the player.
    # 2. Store a random number as the answer/solution.
    # 3. Continuously prompt the player for a guess.
    #   a. If the guess greater than the solution, display to the player "It's lower".
    #   b. If the guess is less than the solution, display to the player "It's higher".
    
    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    #      and show how many attempts it took them to get the correct number.
    # 5. Let the player know the game is ending, or something that indicates the game is over.
    
    # ( You can add more features/enhancements if you'd like to. )
    # """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()