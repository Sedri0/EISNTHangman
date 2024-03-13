import json
from random import randint


#Global variables for easy editing
MEDIUMSCORE = 2
HARDSCORE = 4
EASYLIVES = 7
MEDIUMLIVES = 6
HARDLIVES = 5


#Class creation
class hangman:
    def __init__(self):
        self.inGame = True
        self.diff = ""
        self.firstGame = True
        self.rightWords = []
        self.totalGuesses = 0
        self.score = 0
        self.lives = 0
        self.guesses = []
        hangman.difficulty(self)

    #CHEATING
    """def cheater(self):
        print("================")
        print(self.wordToGuess)
        print("================")"""

    #Finds word from Words.json
    def getWord(self):
        if self.firstGame == True:
            with open("ProjetoFinal/Words.json") as data:
                content=json.load(data)
                self.content = content

        length = len(self.content[self.diff])
        word = randint(1,length) #randomly chooses a number to pick from the list
        
        #Finds out what the random numbers word equivalent is
        self.counter=0
        for self.randomWord in self.content[self.diff]:
            self.counter += 1
            if self.counter == word:
                print("============== RANDOM WORD CHOSEN ==============")
                hangman.listCopy(self)
        
    #Copies list to another list 
    def listCopy(self):
        self.randomWord = list(self.randomWord)
        self.wordToGuess = self.randomWord.copy()
        self.length = len(self.wordToGuess)

        #hangman.cheater(self) #CHEAT TO LET ME SEE WHAT THE WORD IS

        x=0
        while self.inGame == True:
            if x < self.length:
                self.wordToGuess[x] = "*" #Makes the list * for appearances sake
                x+=1
            else:
                hangman.game(self)

    #Guessing and compairing
    def game(self):
        position=0
        self.roundGuess = 0
        self.wrongGuess = []
        self.rightGuess = []
        isInWord = False
        self.completeWord = "".join(self.randomWord)
        self.guesses = []
        
        while self.inGame == True:
            if self.lives != 0:
                print(f"Your lives: {self.lives}")
                print("Your word to guess is:")
                print(" ".join(self.wordToGuess))
                print("\n")
                self.guess = input("Choose a letter or the word to guess: ")
                
                self.totalGuesses += 1
                self.roundGuess += 1
                lenGuess = len(list(self.guess))
                position = 0
                self.wasGuessed = True
                #Checks if the word/letter has been guessed before
                hangman.checkGuess(self)

                if self.wasGuessed == False:
                    #Check if guess is the size of the word
                    if lenGuess == self.length:
                        #If the guess is the word
                        if self.guess == "".join(self.randomWord):
                            self.score += int(lenGuess)
                            self.rightGuess.append(self.guess)
                            self.rightWords.append(self.completeWord)
                            print(f"Correct! {self.guess} is the word!")
                            print("\n")
                            print(self.randomWord)
                            print("\n")
                            
                            hangman.wordFinish(self)
                            hangman.notDeath(self)

                        #If the guess isn't the word
                        else:
                            print(f"Incorrect! {self.guess} is NOT the word\n")
                            self.lives = 0
                            self.wrongGuess.append(self.guess) 
                            hangman.death(self)
                    
                    #if guess was letter and not word
                    elif lenGuess == 1:
                        #Check if letter was guessed
                        for letter in self.randomWord:
                            position += 1
                            if self.guess == letter:
                                isInWord = True
                                self.score += 1
                                self.wordToGuess[position - 1] = self.guess
                        
                        #Checks if the guessed letter is in the word
                        if isInWord == True:
                            self.rightGuess.append(self.guess)
                            print(f"Correct! {self.guess} is in the word")
                            

                        #Checks if the guess letter is not in the word
                        if isInWord == False:
                            print(f"Incorrect! {self.guess} is NOT in the word\n")
                            self.wrongGuess.append(self.guess) 
                            self.lives -= 1
                elif self.wasGuessed == True:
                    print(self.wordToGuess)
                    print("Can't repeat guesses, try again!\n")

                else:
                    print("Not a valid guess. Guess 1 letter or the word")
                
                #Checks if you have completed the word
                if self.randomWord == self.wordToGuess:
                    hangman.wordFinish(self)
                    self.rightWords.append(self.completeWord)
                    hangman.notDeath(self)
                #Resets the variable to see if it's in the word or not
                isInWord = False
                
            else:
                hangman.death(self)

    #Checks if guess has been guessed before
    def checkGuess(self):
        self.wasGuessed = False
        num = 0
        guessesLength = len(self.guesses)
        if guessesLength == 0:
            self.guesses.append(self.guess)
            return

        else:
            for check in self.guesses:
                num +=1
                if self.guess == check:
                    self.wasGuessed = True

                    return
                elif num == guessesLength:
                    self.guesses.append(self.guess)
                    return

    #Adding Score when completing a word
    def wordFinish(self):
        if self.diff == "Easy":
            self.score += len(self.wordToGuess)
            hangman.liveReset(self)
        elif self.diff == "Medium":
            self.score += len(self.wordToGuess) + MEDIUMSCORE
            hangman.liveReset(self)
        elif self.diff == "Hard":
            self.score += len(self.wordToGuess) + HARDSCORE
            hangman.liveReset(self)

    #Lives have reached 0
    def death(self):
        self.randomWord = " ".join(self.randomWord)
        self.rightGuess = " ". join(self.rightGuess)
        self.wrongGuess = " ". join(self.wrongGuess)
        self.correctWords = " ". join(self.rightWords)
        totalCorrectWords = len(self.rightWords)

        print("===========================")
        print(f"Your score this game: {self.score}\n")
        print(f"Word to guess: {self.randomWord}")
        print(f"Correct guesses: {self.rightGuess}")
        print(f"Incorrect guesses: {self.wrongGuess}")
        print(f"Total Guesses this game: {self.roundGuess}\n")
        print(f"Words guessed correctly: {self.correctWords} ({totalCorrectWords})\n===========================\n\n")
        print("You have ran out of lives!")
        while self.inGame == True:
            again= input("Play again (1 for yes, 2 for no)? ")
            if again == "1":
                self.firstGame = False
                hangman.liveReset(self)
                hangman.difficulty(self)
            elif again == "2":
                print("Thanks for playing. We hope to see you again!")
                self.inGame = False
                exit
            else:
                print("Invalid option, please try again.\n")
        

    #Still has lives but has finished/guessed the word
    def notDeath(self):
        print("You have completed the word!\n================================\n")
        self.randomWord = " ".join(self.randomWord)
        self.rightGuess = " ". join(self.rightGuess)
        self.wrongGuess = " ". join(self.wrongGuess)
        self.correctWords = " ". join(self.rightWords)
        totalCorrectWords = len(self.rightWords)
        print("===========================")
        print(f"Your score this game: {self.score}")
        print(f"Your lives this game: {self.lives}\n")
        print(f"Word to guess: {self.randomWord}")
        print(f"Correct guesses: {self.rightGuess}")
        print(f"Incorrect guesses: {self.wrongGuess}")
        print(f"Total Guesses this round: {self.roundGuess}\n")
        print(f"Words guessed correctly: {self.correctWords} ({totalCorrectWords})\n===========================\n\n")
        hangman.difficulty(self)

    #Reset lives
    def liveReset(self):
        if self.diff == "Easy":
            self.lives = EASYLIVES
        elif self.diff == "Medium":
            self.lives = MEDIUMLIVES
        elif self.diff == "Hard":
            self.lives = HARDLIVES

    #Choosing a difficulty
    def difficulty(self):
            if self.diff == "":
                while self.inGame == True:
                    self.diff = input("Choose a difficulty:\n1. Easy\n2. Medium\n3. Hard\nChoice (1, 2, 3): ")

                    if self.diff == "1":
                        print("You have chosen to play on Easy.")
                        self.diff = "Easy"
                        self.lives = EASYLIVES
                        hangman.getWord(self)

                    elif self.diff == "2":
                        print("You have chosen to play on Medium.")
                        self.diff = "Medium"
                        self.lives = MEDIUMLIVES
                        hangman.getWord(self)
                                    
                    elif self.diff == "3":
                        print("You have chosen to play on Hard.")
                        self.diff = "Hard"
                        self.lives = HARDLIVES
                        hangman.getWord(self)

                    else:
                        print("Invalid choice, try again.\n\n\n")
            else:
                hangman.getWord(self)

print("Welcome to hangman!")
hangman()



