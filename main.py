import random

words = [
    ["Haus", "house"],
    ["Buch", "book"],
    ["Wasser", "water"],
    ["Schule", "school"],
    ["Freund", "friend"],
    ["Arbeit", "work"],
    ["Familie", "family"],
    ["Stadt", "city"],
    ["Sprache", "language"],
    ["Zeit", "time"]
]

print("German Vocabulary Trainer")

again = "yes"

while again == "yes":
    random.shuffle(words)

    score = 0
    wrong = []

    print("\nLet's start!")

    for word in words:
        answer = input("What is " + word[0] + " in English? ")

        if answer.lower() == word[1]:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong!")
            print("The answer is:", word[1])
            wrong.append(word[0])

    print("\nTraining finished")
    print("Your score:", score, "out of", len(words))

    percent = score / len(words) * 100
    print("Percentage:", round(percent), "%")

    if len(wrong) > 0:
        print("You need to practice these words:")
        for word in wrong:
            print(word)

    again = input("\nDo you want to try again? yes/no: ")

print("Goodbye!")
