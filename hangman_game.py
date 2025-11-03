wordlist = ["python", "java", "kotlin", "javascript", "hangman", "programming", "developer", "function", "variable", "condition", "loop", "array", "string", "integer", "boolean", "dictionary", "tuple", "set", "exception", "module", "package", "algorithm", "data", "structure", "object", "class", "inheritance", "polymorphism", "encapsulation", "abstraction", "interface", "constructor", "destructor", "recursion", "iteration", "syntax", "semantics", "compilation", "interpretation", "debugging", "testing", "deployment", "version", "control", "repository", "branch", "merge", "commit", "push", "pull", "clone", "fork", "issue", "bug", "feature", "release", "build", "continuous", "integration", "delivery", "devops", "cloud", "server", "client", "database", "query", "index", "table", "schema", "normalization", "transaction", "backup", "restore", "HTML", "CSS"]
import random
range = len(wordlist)
index = random.randint(0, range - 1)


word = wordlist[index].lower()
chances = 6
guessad = []
print("Welcome to Hangman Game")
print("The word is selected from the hidden wordlist.")
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
        print("Wrong guess")
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