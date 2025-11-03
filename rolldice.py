import random

rolldice = True

while rolldice:
    print(random.randint(1, 6))
    user_input = input("Roll the dice again? (y/n): ").strip().lower()
    if user_input == 'y':
        continue
    else:
        pass
