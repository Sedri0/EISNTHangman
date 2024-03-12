import json
import random

test=0
position=0



#Choosing a difficulty
while True:
    diff = input("Choose a difficulty:\n1. Easy\n2. Medium\n3. Hard\nChoice (1, 2, 3): ")

    if diff == "1":
        print("You have chosen to play on Easy.")
        diff = "Easy"
        break

    elif diff == "2":
        print("You have chosen to play on Medium.")
        diff = "Medium"
        break
        
    elif diff == "3":
        print("You have chosen to play on Hard.")
        diff = "Hard"
        break

    else:
        print("Invalid choice, try again.\n\n\n")

#Gameplay itself
with open("Words.json") as data:
    content=json.load(data)
    
    
    word = random.randint(1,3) #randomly chooses a number to pick from the list
    
    #Finds out what the random numbers word equivalent is
    for i in content[diff]:
        test += 1
        if test == word:
            break

print("============== RANDOM WORD CHOSEN ==============")
i = list(i)
wordToGuess = i.copy()
length = len(wordToGuess)
x=0
while True:
    if x < length:
        wordToGuess[x] = "*"
        x+=1
    else:
        break



while True:
    wrongGuess = []
    rightGuess = []
    guess = input("Choose a letter to guess: ")
    
    for letter in i:
        position += 1
        isInWord = False
        if guess == letter:
            print(f"Correct! {guess} is in the word")
            isInWord = True
            rightGuess.append(guess)
            wordToGuess[position - 1] = guess

    if isInWord == False:
        print(f"Incorrect! {guess} is NOT in the word")
        wrongGuess.append(guess) 
        break
    

        
    
print(wordToGuess)
print(wrongGuess)
print(rightGuess)
