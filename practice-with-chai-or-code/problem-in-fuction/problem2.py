import random


print("1 - rock  2 - paper  3 - scissors")

while True:
    try:
        user_input = int(input("Enter your choice: "))
        if user_input not in [1, 2, 3]:
            raise ValueError("Invalid choice. Please enter 1, 2, or 3.")
        break
    except ValueError as e:
        print(e)

computer = random.randint(1, 3)
print(f"Computer chose: {computer}")
if user_input == computer:
    print("It's a tie!")
elif user_input == 1 and computer == 2:
    print("Computer wins!")
elif user_input == 1 and computer == 3:
    print("You win!")
elif user_input == 2 and computer == 1:
    print("You win!")
elif user_input == 2 and computer == 3:
    print("Computer wins!")
elif user_input == 3 and computer == 1:
    print("Computer wins!")
elif user_input == 3 and computer == 2:
    print("You win!")
