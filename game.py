import random

options=("rock","paper","scissors")
playing=True
played=0
won=0
while playing:
    played+=1
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice(rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print("It's a tie!")
    elif player=="rock" and computer=="scissors":
        print("You Win!")
        won+=1
    elif player=="paper" and computer=="rock":
        print("You Win!")
        won+=1
    elif player=="scissors" and computer=="paper":
        print("You Win!")
        won+=1
    else:
        print("You Lose!")
    if not input("Play again? (yes/no): ").lower()=="yes":
        playing=False
print("You have Played the game for",played,"times and won",won,"times")
print("Thanks for playing!")


