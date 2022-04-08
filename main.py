import random
from word_list import common_words
from word_list import dictionary
import os


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def start_screen():
  print("~~~~~~~~~~~~~ WORDLE LITE ~~~~~~~~~~~~~\n\nThe off-brand, home-grown version you never asked for but got anyway!")
  print("Instead of the pretty color system, we are going to use symbols \nto denote the feedback on the guessed words.\n ")
  print("$ = green; correct letter AND correct place\n? = yellow; correct letter but wrong place\n- = grey; wrong letter, it is not in the word\n")
  print("Remember: Words with double letters can be tricky in WORDLE\n")
  ready = input("Ready to play? ").lower()
  if ready == "no" or ready == "nope" or ready == "nah":
      clear()
      print("Too bad, starting anyway lol\n")
  elif ready == "yes" or ready == "yeah" or ready == "yep":
      clear()
      print("That's the spirit! Good luck\n")
  else:
      clear()
      print("Cool beans. Let's go\n")
  play_game()

def play_game():
  lives = 6
  chosen_word = random.choice(common_words)
  guess_feedback = ["x","x","x","x","x"]
  display_feedback = " ".join(guess_feedback)
  spaced_chosen = " ".join(chosen_word[i:i+1] for i in range(0,len(chosen_word),1))
  not_in_word = ""
  spaced_not_in_word = ""
  guess_history = ""
  end_of_game = False
  while not end_of_game: 
      guess_word = input("Guess a word: ").lower()
      if guess_word not in dictionary:
          print(f"\nNO BUENO: '{guess_word}' is not a real 5-letter word. Try again\n")
      else:
          lives -= 1
          spaced_guess = " ".join(guess_word[i:i+1] for i in range(0,len(chosen_word),1))
          for letter in range(0,len(chosen_word)):
              if guess_word[letter] == chosen_word[letter]:
                  #print("Correct Place: GREEN")
                  #print(letter)
                  guess_feedback[letter] = "$"
                  display_feedback = " ".join(guess_feedback)
              elif guess_word[letter] in chosen_word:
                  #print("Correct Letter: YELLOW")
                  guess_feedback[letter] = "?"
                  display_feedback = " ".join(guess_feedback)
              else:
                  #print("Not in word: GREY")
                  guess_feedback[letter] = "-"
                  display_feedback = " ".join(guess_feedback)
                  if guess_word[letter] not in not_in_word:
                      not_in_word += guess_word[letter]
                  spaced_not_in_word = " ".join(not_in_word[i:i+1] for i in range(0,len(not_in_word),1))
    
          clear()
          guess_history += spaced_guess + "\n" + display_feedback + "\n\n"
          print(guess_history)
          if display_feedback == "$ $ $ $ $":
              end_of_game = True
              if lives == 5:
                  print(f"Hole in ONE! Unbelievable! The word was indeed '{chosen_word}'")
                  print(f"You got the word in {6-lives} guess!! Are you a word wizard?!")
              if lives == 4:
                  print(f"You are a Wordle Master! The word was indeed '{chosen_word}'")
                  print(f"You got the word in just {6-lives} guesses! Simply incredible!")
              if lives == 3:
                  print(f"Winner Winner! You are hot stuff. The word was indeed '{chosen_word}'")
                  print(f"You got the word in {6-lives} guesses. Nice job!")
              if lives == 2:
                  print(f"Winner! The word was indeed '{chosen_word}'")
                  print(f"You got the word in {6-lives} guesses")
              if lives == 1:
                  print(f"Nice! The word was indeed '{chosen_word}'")
                  print(f"Took you {6-lives} guesses, but you got it.")
              if lives == 0:
                  print(f"Phew!! The word was indeed '{chosen_word}'")
                  print(f"{6-lives} guesses. Close call, but at least you didn't lose ;)")
              next_step = input("\nType 'play' if you want to play again\nType 'help' if you want to return to starting screen with instructions\nType anything else to exit the game\n\n")
              if next_step == "play" or next_step == "'play'":
                clear()
                play_game()
              elif next_step == "help" or next_step == "'help'":
                clear()
                start_screen()
              else:
                clear()
                print("Thanks for playing Wordle Lite! Cya next time :)")
          if lives == 0 and end_of_game == False:
              end_of_game = True
              print(f"You lose :(\nThe word was '{chosen_word}'")
              next_step = input("\nType 'play' if you want to play again\nType 'help' if you want to return to starting screen with instructions\nType anything else to exit the game\n\n")
              if next_step == "play" or next_step == "'play'":
                clear()
                play_game()
              elif next_step == "help" or next_step == "'help'":
                clear()
                start_screen()
              else:
                clear()
                print("Thanks for playing Wordle Lite! Cya next time :)")
          if not end_of_game:
              print(f"These letters are NOT in the word:\n {spaced_not_in_word}\n")

start_screen()
