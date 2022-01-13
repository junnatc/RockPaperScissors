import time
import random
import startMenu

lose = ("The Computer Wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7

while True:
  print("To begin fill in the below information")
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  print("Access granted")
  time.sleep(0.4)
  print("Loading...")
  time.sleep(0.4)
  startMenu.startMenu()

  while True:
    rps = input("Rock, Paper, Scissors?  ")
    rps = rps.lower()
    computer = ("rock", "paper", "scissors")
    computer = random.choice(computer)

    #rock if statements
    if rps == "rock" and computer == "paper":
      print("The computer chose", computer)
      print(lose, "\n\n")
      lives -= 1
    if rps == "rock" and computer == "scissors":
      print("The computer chose", computer)
      print(win, "\n\n")
      score += 1

    #paper if statements
    if rps == "paper" and computer == "scissors":
      print("The computer chose", computer)
      print(lose, "\n\n")
      lives -= 1
    if rps == "paper" and computer == "rock":
      print("The computer chose", computer)
      print(win, "\n\n")
      score += 1

    #scissors if statements
    if rps == "scissors" and computer == "rock":
      print("The computer chose", computer)
      print(lose, "\n\n")
      lives -= 1
    if rps == "scissors" and computer == "paper":
      print("The computer chose", computer)
      print(win, "\n\n")
      score += 1

    #duplicates
    if rps == "rock" and computer == "rock":
      print("The computer chose", computer)
      print("You Drew\n\n")
      drew += 1
    
    if rps == "paper" and computer == "paper":
      print("The computer chose", computer)
      print("You Drew\n\n")
      drew += 1

    if rps == "scissors" and computer == "scissors":
      print("The computer chose", computer)
      print("You Drew\n\n")
      drew += 1

    #system
    if rps == "rules":
      print("\n*********************************")
      print("Rules")
      print("*********************************")
      print("-Rock loses against Paper")
      print("-Paper beats Rock")
      print("-Paper loses against Scissors")
      print("-Scissors beats paper")
      print("-Scissors loses against Rock")
      print("*********************************\n")

    if rps == "lives":
      print("You have", lives, "more live(s)\n")
    if rps == "score":
      print("The score is", score, "\n")
    if rps == "draw":
      print("There have been", drew, "draw(s)\n")
    
    #info 
    if rps == "info":
      print("\n*********************************\n")
      print("To display your lives, type 'lives'")
      print("To display the score, type 'score'")
      print("To display the number of draws, type 'draw'")
      print("\n*********************************\n")

    #lives
    if lives == 0 or rps == "test":
      print("\nThanks for playing!")
      print("You have run out of lives")
      print("You won", score, "time(s)")
      print("You drew", drew, "time(s)")
      stop = input("\nPress enter to exit")
      exit()

    if computer_lives == 0:
      print("\nThanks for playing!")
      print("The computer lost all its lives. You Win!")
      print("You won", score, "time(s)")
      print("There was a draw", drew, "time(s)")
      stop = input("\nPress enter to exit")
      exit()

    #exit
    if rps == "exit":
      lives = 5
      score = 0
      drew = 0
      computer_lives = 7  
      break
    


