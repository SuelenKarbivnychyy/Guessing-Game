import random
from termcolor import colored
# from color import colored
from dictionary import list_of_words

# introduction about the game

name = input("Hello there, What is your name? > ")
name = name.title()
# print()
print(f"Hi {name}, it's nice to have you here!")
print()
welcome = "Welcome to the Wordle game!!! \n"
x = welcome.center(75)
print(x)

print("The goal of this game is to guess what is the randomly selected five-letter word! The rules of the game are:\n.You will have 5 tries to guess the word!\n.Only alphabetic letters are accept! \n.No word with in more than 5 letters lenght is accept! \n.And no words with in less than 5 letters lenght is accept. \n.If you guess the correct word, the correct word will display, If in your guess have the rigth letter in the right spot, it shows up in green as a hint.For a correct letter in the wrong spot, it shows up in yellow. A letter that isn't in the word in any spot a _ underscore will be posted. \nGood luck.")
# end of introdutction

#creating a function to display some clues depending on the player's guess

def game(guess, word):
  position = 0
  clue = ""  
  for letter in guess:
    if letter == word[position]:   
      clue += colored(letter, "green")      
    elif letter in word:           
      clue += colored(letter, "yellow")
    else:      
      clue += "_"
    position += 1   
  print(clue)
  return guess == word   
#end of the function to dysplay clues   

#(if you want to play just one round uncoment line 28) 
# Getting a random word and saving it to the variable random_word
# random_word = random.choice(list_of_words)


#If the player didnt guessed correctly and if player still has turn left
#(if it's just one round incomented lines 54 55)
# chances = 0
# guessed_correctly = False

#delet lines 59 60 if it's just one round and undent all the rest of the code.

play_again = "Yes"
while play_again.startswith("Y"): 
  random_word = random.choice(list_of_words)
  # random_word = "happy" 
  chances = 0
  guessed_correctly = False
  
  while chances <= 4 and not guessed_correctly :
    print()
    print(f"This is your attempt number {chances + 1}.")
    player_guess = input("Please enter a 5 letters word: > ")
    player_guess = player_guess.lower()  

     
    if not player_guess.isalpha(): #Checking if the input is not a string
      print(colored("Only alphabetic letters accept!", "red"))
      continue
    if len(player_guess) < 5 or len(player_guess) > 5: #checking if the input is correct length
      print(colored("Only 5 letters words accepted", "red"))    
      continue
      # 68: check if the word is at the list
    if player_guess not in list_of_words:
      print(colored("Not in the list, You didn't miss any chances, keep playing!", "blue"))
      continue
      
    chances += 1    

    #Updating the guessed_correcly condition with the players guess 
    guessed_correctly = game(player_guess, random_word)  
    
  # Checking if player guessed correctly
  if guessed_correctly == True:
    print()
    print(colored(f"Congrats, You won with in {chances} guess \o/, the Word is: {random_word}!", "blue"))  
    print()
  else:      
      print(colored(f"\nYou are out of guess! The correctly word was: > {random_word}", "blue"))
      print()


  # (if its just one round delet all code bellow but 93)
  play_again = input("Do you want to play again? Enter 'Yes' for play again or 'No' to exit: > ")
  play_again = play_again.title()
  if play_again.startswith("Y"):    
    print()
    # random_word = random.choice(list_of_words)
    print(colored("Lest play again \o/ ...\n", "green"))
    
  else:  
    print()
    print(colored("Thanks for playing! Goodbye", "yellow")) 