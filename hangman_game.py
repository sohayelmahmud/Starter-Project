word = "Pyhton".lower()
chances = 6
guessad = []
print("Welcome to Hangman Game")
done = False

while not done:
    for char in word:
        if char.lower() in guessad:
            print(char, end=" ")
        else:
            print("_", end=" ")

    guess = input(f"You have {chances} left. \nGuess a character: ").lower().strip()
    guessad.append(guess.lower().strip())

    if guess.lower().strip() not in word:
        chances -= 1
        print("Wrong")
        if chances == 0:
            break

    done = True
    for char in word:
        if char.lower().strip() not in guessad:
            done = False

if done:
    print(f"You Win! The word is {word}")
else:
    print("You Lose")














# while chances > 0:
#     failed = 0
#     for char in word:
#         if char in guessad:
#             print(char, end=" ")
#         else:
#             print("_", end=" ")
#             failed += 1
#     print()

#     if failed == 0:
#         print("You Win")
#         break

#     guess = input("Guess a character: ").lower().strip
#     guessad.append(guess)

#     if guess not in word:
#         chances -= 1
#         print("Wrong")
#         print(f"You have {chances} more chances")

#         if chances == 0:
#             print("You Lose")