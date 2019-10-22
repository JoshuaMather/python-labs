win = False
word = "yellow"
count = 0
guesses = ""
answer = "______"

while count < 10 and win == False:
    count +=1
    guess = input("\nEnter guess " + str(count) + "/10: ")
    guesses += guess
    tmp = ""
    for i in range(0, len(word)):
        if (guess == word[i]):
            tmp += word[i]
        else:
            tmp += answer[i]
    if (answer != tmp):
        print("Good guess")
        count -= 1
        answer = tmp
    else:
        print("Not a good guess")
    if answer == word:
        print("You win")
        win = True
    print(answer)

print("Amount of guesses left: ", str(10 - count))
print("Your guesses: " + guesses)
print("Your word: " + answer)
print("The word: " + word)
