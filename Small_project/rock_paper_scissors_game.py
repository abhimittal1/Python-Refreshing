import random

def play():
    print("\n🎮 Rock, Paper, Scissors Game!")
    user = input("Choose [rock, paper, scissors]: ").strip().lower()
    options = ['rock', 'paper', 'scissors']
    
    if user not in options:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        return

    computer = random.choice(options)
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        print("😐 It's a draw!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("✅ You win!")
    else:
        print("❌ You lose!")

# 🎯 Play the game in a loop
while True:
    play()
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("👋 Thanks for playing!")
        break
