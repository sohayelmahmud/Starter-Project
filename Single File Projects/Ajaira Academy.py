import random

print("Ajaira Academy")
takerow = int(input("How much test do you want? "))
row = 0
hr = ("________________________________________")
while row < takerow:

    x = random.randint(10, 99)
    y = random.randint(10, 99)

    print("What is " + str(x) + " + " + str(y) + "?")

    result = x+y

    ask = int(input("Your answer: "))

    if ask == result:
        row += 1
        print("Correct! You've gotten ", row, "correct in a row")
        if row != takerow:
            print(hr)

    else:
        row = 0
        print("Incorrect.")
        print("The expected answer is " + str(result))
        print(hr)

print("You have completed ", takerow, " tests.")
print("Congratulations! You mastered addition.")
print(hr)
