import json
from random import randint

#Chooses difficulty
class hangman:
    def __init__(self):
        self.inGame = True
        hangman.difficulty(self)

    #Finds word from Words.json
    def getWord(self):
        with open("ProjetoFinal/Words.json") as data:
            content=json.load(data)
        
        word = randint(1,3) #randomly chooses a number to pick from the list
        
        #Finds out what the random numbers word equivalent is
        counter=0
        for self.randomWord in content[self.diff]:
            counter += 1
            if counter == word:
                print("============== RANDOM WORD CHOSEN ==============")
                hangman.listCopy(self)
        
    #Copies list to another list 
    def listCopy(self):
        self.randomWord = list(self.randomWord)
        self.wordToGuess = self.randomWord.copy()
        length = len(self.wordToGuess)
        x=0
        while self.inGame == True:
            if x < length:
                self.wordToGuess[x] = "*" #Makes the list * for appearance
                x+=1
            else:
                hangman.game(self)

    #Guessing and compairing
    def game(self):
        position=0
        self.totalGuesses = 0
        self.wrongGuess = []
        self.rightGuess = []
        isInWord = False
        
        while self.inGame == True:
            self.guess = input("Choose a letter to guess: ")
            self.totalGuesses += 1
            position = 0
            #Check if letter was guessed
            for letter in self.randomWord:
                position += 1
                if self.guess == letter:
                    isInWord = True
                    self.wordToGuess[position - 1] = self.guess
            
            #Checks if the guessed letter is in the word
            if isInWord == True:
                self.rightGuess.append(self.guess)
                print(f"Correct! {self.guess} is in the word")
                print("\n")
                print(self.wordToGuess)
                print("\n")

            #Checks if the guess letter is not in the word
            if isInWord == False:
                print(f"Incorrect! {self.guess} is NOT in the word\n")
                self.wrongGuess.append(self.guess) 
                self.inGame = False
                hangman.ending(self)
            
            #Checks if you have completed the word
            if self.randomWord == self.wordToGuess:
                print("You have won the game!\n================================\n")
                self.inGame = False
                hangman.ending(self)
            #Resets the variable to see if it's in the word or not
            isInWord = False
    
    #Finisher for the game
    def ending(self):
        self.randomWord = " ".join(self.randomWord)
        self.wrongGuess = " ". join(self.wrongGuess)
        self.rightGuess = " ". join(self.rightGuess)

        print(f"Word to guess: {self.randomWord}")
        print(f"Incorrect guesses: {self.wrongGuess}")
        print(f"Correct guesses: {self.rightGuess}")
        print(f"Total Guesses: {self.totalGuesses}\n\n")
        again = 0 
        while again != "2":
            again= input("Play again (1 for yes, 2 for no)? ")
            if again == "1":
                difficulty()
            elif again == "2":
                print("Thanks for playing. We hope to see you again!")
                exit
            else:
                print("Invalid option, please try again.\n")

    #Choosing a difficulty
    def difficulty(self):
            while self.inGame == True:
                self.diff = input("Choose a difficulty:\n1. Easy\n2. Medium\n3. Hard\nChoice (1, 2, 3): ")

                if self.diff == "1":
                    print("You have chosen to play on Easy.")
                    self.diff = "Easy"
                    hangman.getWord(self)
                elif self.diff == "2":
                    print("You have chosen to play on Medium.")
                    self.diff = "Medium"
                    hangman.getWord(self)
                                
                elif self.diff == "3":
                    print("You have chosen to play on Hard.")
                    self.diff = "Hard"
                    hangman.getWord(self)

                else:
                    print("Invalid choice, try again.\n\n\n")

print("Welcome to hangman!")
hangman()



