import customtkinter as ctk
from PIL import Image
from random import randint
import json

ctk.set_appearance_mode("light")

EASYLIVES = 7
MEDIUMLIVES = 6
HARDLIVES = 5

COLOUR="#EAEAEA"



class App(ctk.CTk):
    width = 1250
    height = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firstGame = True
        self.firstGuess=True
        self.score = 0
        self.diff = "Easy"
        self.wordToGuess=[]
        self.progWord=[]
        self.wrongGuesses=[]
        self.totalGuesses=[]
        self.deadge = False
        self.inGame = True
        self.font=ctk.CTkFont(family="Helvetica", size=24, weight = "bold")
        self.wordFont=ctk.CTkFont(family="Helvetica", size=52, weight = "bold")

        #Create window
        self.title("Jack's Hangman")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False,False)
        
        #Default background
        self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/FullHP_200x500png.png"), size = (200, 500))
        self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
        self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
        
        #Pick difficulty
        self.difficulty()

        #Load Health image
        #self.showHealth()

        #Show Score (needs to be updated constantly)
        self.showScore()

        #Button to quit the program
        self.quitButton = ctk.CTkButton(self, text="QUIT", font=self.font, command=exit, width=70, height=50)
        self.quitButton.place(relx=0.93, y=5, anchor=ctk.NW)
        
        #Button for testing score
        self.buttonTest = ctk.CTkButton(self, text="Test +1 score", font=self.font, command=self.addScore)
        self.buttonTest.place(x=5, rely=0.5, anchor=ctk.NW)

        #Button for testing hp image changing
        self.buttonHealthTest = ctk.CTkButton(self, text="Change HP test", font=self.font, command=self.changeHP)
        self.buttonHealthTest.place(x=5, rely=0.6, anchor=ctk.NW)

        #Button for testing letter updates
        self.buttonLetterChange = ctk.CTkButton(self, text="Change Letters", font=self.font, command=self.changeLetters)
        self.buttonLetterChange.place(x=5, rely=0.7, anchor=ctk.NW)

        self.buttonLetterUpdate = ctk.CTkButton(self, text="Update Letters", font=self.font, command=self.hardLetters)
        self.buttonLetterUpdate.place(x=5, rely=0.8, anchor=ctk.NW)

    #Update the letter list and get word
    def getWord(self):
        if self.firstGame == True:
            with open("ProjetoFinal/Words.json") as data:
                content=json.load(data)
                self.content = content

        length = len(self.content[self.diff])
        word = randint(1,length) #randomly chooses a number to pick from the list
        
        self.counter=0
        for self.randomWord in self.content[self.diff]:
            self.counter+=1
            if self.counter == word:
                self.randomWord = list(self.randomWord)
                self.wordToGuess = self.randomWord.copy()
                self.progWord = self.randomWord.copy()
                self.length = len(self.progWord)
                x=0
                while x < self.length:
                    self.progWord[x]="_"
                    x+=1

    #Update the letters
    def changeLetters(self):
        self.guess=self.textInput.get(1.0, "end-1c")
        self.guess=self.guess.lower()
        guessing = True
        self.isInWord=False
        position = 0
        self.checkGuess()
        if self.wasGuessed == False:
            while guessing == True:
                for letter in self.wordToGuess:
                    position+=1
                    if self.guess == letter:
                        self.isInWord = True
                        self.score += 1
                        self.progWord[position-1] = self.guess
                        guessing = False
                        self.showScore()
                    if position > len(self.progWord):
                        guessing=False
            if self.isInWord == False:
                self.wrongGuess = ctk.CTkLabel(self, text="Wrong guess!", width=200, height=50, font=self.font)
                self.lives-=1
                self.showHealth()
                self.wrongGuess.place(relx=0.6,y=5, anchor=ctk.NW)
                self.after(500, self.wrongGuess.destroy)
        else:
            self.wasGuessLabel = ctk.CTkLabel(self, text="Can't repeat guesses!", width=200, height=50, font=self.font)
            self.wasGuessLabel.place(relx=0.6,y=5, anchor=ctk.NW)
            self.after(500, self.wasGuessLabel.destroy)

        if self.diff == "Easy":
            self.easyLetters()
        elif self.diff == "Medium":
            self.mediumLetters()
        elif self.diff == "Hard":
            self.hardLetters()

    #Checks if guess was checked already
    def checkGuess(self):
        self.wasGuessed = False

        if self.firstGuess==True:
            self.totalGuesses.append(self.guess)
            self.firstGuess = False
        else:
            for i in self.totalGuesses:
                if i == self.guess:
                    self.totalGuesses.append(self.guess)
                    self.wasGuessed=True
                    break

    #Score counter
    def showScore(self):
        self.scoreCounter = ctk.CTkLabel(self, text=f"Score: {self.score}", font=(self.font), text_color="black")
        self.scoreCounter.place(x=5,y=5, anchor=ctk.NW)
    
    #Change Health and update health image
    def changeHP(self):
        self.lives -= 1
        self.showHealth()

    #Change score update
    def addScore(self):
        self.score += 1
        self.showScore()

    #Update health image
    def showHealth(self):
        if self.diff == "Easy":
            if self.lives == 7:
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/FullHP_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 6:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/6Head_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 5:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/5HeadBody_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 4:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/4HeadBodyOneLeg_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 3:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/3HeadBodyBothLegs_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 2:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/2HeadBodyBothLegsOneArm_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 1:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/1HeadBodyBothLegsBothArms_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 0:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/0HeadBodyBothLegsBothArmsFace_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
                self.deadgeLabel = ctk.CTkLabel(self, text="You're deadge!", font=self.font)
                self.deadgeLabel.place(x=250, y=130)
                self.deadge=True
                self.playAgain()

        elif self.diff == "Medium":
            if self.lives == 6:
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/FullHP_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 5:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/6Head_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 4:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/5HeadBody_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 3:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/3HeadBodyBothLegs_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 2:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/2HeadBodyBothLegsOneArm_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 1:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/1HeadBodyBothLegsBothArms_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 0:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/0HeadBodyBothLegsBothArmsFace_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
                self.deadgeLabel = ctk.CTkLabel(self, text="You're deadge!", font=self.font)
                self.deadgeLabel.place(x=250, y=130)
                self.deadge=True
                self.playAgain()

        elif self.diff == "Hard":
            if self.lives == 5:
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/FullHP_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 4:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/6Head_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 3:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/5HeadBody_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)

            elif self.lives == 2:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/3HeadBodyBothLegs_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 1:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/1HeadBodyBothLegsBothArms_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
            
            elif self.lives == 0:
                self.bgImageFrame.place_forget()
                self.bgImage = ctk.CTkImage(Image.open("ProjetoFinal/Images/0HeadBodyBothLegsBothArmsFace_200x500png.png"), size = (200, 500))
                self.bgImageFrame = ctk.CTkLabel(self, text="", image=self.bgImage)
                self.bgImageFrame.place(x=200, y=0, anchor=ctk.NW)
                self.deadgeLabel = ctk.CTkLabel(self, text="You're deadge!", font=self.font)
                self.deadgeLabel.place(x=250, y=130)
                self.deadge=True
                self.playAgain()
    
    #If diff set to easy
    def easy(self):
        self.lives = EASYLIVES
        self.diff = "Easy"
        self.getWord()
        self.easyLetters()

    #Shows the letters if easy
    def easyLetters(self):
        self.diffFrame.pack_forget()
        self.easyFrame = ctk.CTkFrame(self, width=500, height=250, fg_color=COLOUR)
        self.letterOne = ctk.CTkLabel(self.easyFrame, text=self.progWord[0], font = self.wordFont)
        self.letterTwo = ctk.CTkLabel(self.easyFrame, text=self.progWord[1], font = self.wordFont)
        self.letterThree = ctk.CTkLabel(self.easyFrame, text=self.progWord[2], font = self.wordFont)
        self.letterFour = ctk.CTkLabel(self.easyFrame, text=self.progWord[3], font = self.wordFont)

        self.easyFrame.place(x=550, y=200, anchor=ctk.NW)
        self.letterOne.place(x=0, y=0, anchor=ctk.NW)
        self.letterTwo.place(x=100, y=0, anchor=ctk.NW)
        self.letterThree.place(x=200, y=0, anchor=ctk.NW)
        self.letterFour.place(x=300, y=0, anchor=ctk.NW)
    
    #If diff set to medium
    def medium(self):
        self.diff = "Medium"
        self.lives = MEDIUMLIVES
        self.getWord()
        self.mediumLetters()

    #Shows the letters if medium    
    def mediumLetters(self):
        self.diffFrame.pack_forget()
        self.mediumFrame = ctk.CTkFrame(self, width=500, height=250, fg_color=COLOUR)
        self.letterOne = ctk.CTkLabel(self.mediumFrame, text=self.progWord[0], font = self.wordFont)
        self.letterTwo = ctk.CTkLabel(self.mediumFrame, text=self.progWord[1], font = self.wordFont)
        self.letterThree = ctk.CTkLabel(self.mediumFrame, text=self.progWord[2], font = self.wordFont)
        self.letterFour = ctk.CTkLabel(self.mediumFrame, text=self.progWord[3], font = self.wordFont)
        self.letterFive = ctk.CTkLabel(self.mediumFrame, text=self.progWord[4], font = self.wordFont)

        self.mediumFrame.place(x=550, y=200, anchor=ctk.NW)
        self.letterOne.place(x=0, y=0, anchor=ctk.NW)
        self.letterTwo.place(x=100, y=0, anchor=ctk.NW)
        self.letterThree.place(x=200, y=0, anchor=ctk.NW)
        self.letterFour.place(x=300, y=0, anchor=ctk.NW)
        self.letterFive.place(x=400, y=0, anchor=ctk.NW)

    #If diff set to hard
    def hard(self):
        self.diff = "Hard"
        self.lives = HARDLIVES
        self.getWord()
        self.hardLetters()

    #Shows the letters if hard      
    def hardLetters(self):
        self.diffFrame.place_forget()
        self.hardFrame = ctk.CTkFrame(self, width=600, height=250, fg_color=COLOUR)
        self.letterOne = ctk.CTkLabel(self.hardFrame, text=self.progWord[0], font = self.wordFont)
        self.letterTwo = ctk.CTkLabel(self.hardFrame, text=self.progWord[1], font = self.wordFont)
        self.letterThree = ctk.CTkLabel(self.hardFrame, text=self.progWord[2], font = self.wordFont)
        self.letterFour = ctk.CTkLabel(self.hardFrame, text=self.progWord[3], font = self.wordFont)
        self.letterFive = ctk.CTkLabel(self.hardFrame, text=self.progWord[4], font = self.wordFont)
        self.letterSix = ctk.CTkLabel(self.hardFrame, text=self.progWord[5], font = self.wordFont)

        self.hardFrame.place(x=550, y=200, anchor=ctk.NW)
        self.letterOne.place(x=0, y=0, anchor=ctk.NW)
        self.letterTwo.place(x=100, y=0, anchor=ctk.NW)
        self.letterThree.place(x=200, y=0, anchor=ctk.NW)
        self.letterFour.place(x=300, y=0, anchor=ctk.NW)
        self.letterFive.place(x=400, y=0, anchor=ctk.NW)
        self.letterSix.place(x=500, y=0, anchor=ctk.NW)

        self.textInputLabel = ctk.CTkLabel(self.hardFrame,text="Letter/word to guess:", width=100, height=50)
        self.textInputLabel.place(x=0, y=100)
        self.textInput = ctk.CTkTextbox(self.hardFrame, width=100, height=10)
        self.textInput.place(x=140,y=110)
        self.textInputButton = ctk.CTkButton(self.hardFrame, text="Guess!", width=50, height=10, command=self.changeLetters)
        self.textInputButton.place(x=250, y= 115)
            
    #Choosing difficulty
    def difficulty(self):
        #resets score, and destroys tryagain frame if dead
        if self.deadge == True:
            self.tryAgainFrame.place_forget()
            self.score=0
        #Buttons for creating difficulty
        self.diffFrame = ctk.CTkFrame(self, width=600, height=500, fg_color=COLOUR)
        self.diffLabel = ctk.CTkLabel(self.diffFrame, text="Select your difficulty", font=self.font)
        self.diffButtonEasy = ctk.CTkButton(self.diffFrame, text="Easy", font=self.font, command = self.easy)
        self.diffButtonMedium = ctk.CTkButton(self.diffFrame, text="Medium", font=self.font, command = self.medium)
        self.diffButtonHard = ctk.CTkButton(self.diffFrame, text="Hard", font=self.font, command = self.hard)

        self.diffFrame.place(x=650, y=0, anchor=ctk.NW)
        self.diffLabel.place(x=0, y=100, anchor=ctk.NW)
        self.diffButtonEasy.place(x=0, y=150, anchor=ctk.NW)
        self.diffButtonMedium.place(x=0, y=250, anchor=ctk.NW)
        self.diffButtonHard.place(x=0, y=350, anchor=ctk.NW)

    #Play again if deadge
    def playAgain(self):
        if self.diff == "Easy":
            self.easyFrame.place_forget()
        elif self.diff == "Medium":
            self.mediumFrame.place_forget()
        elif self.diff == "Hard":
            self.hardFrame.place_forget()
        
        self.tryAgainFrame = ctk.CTkFrame(self, width=500, height=250, fg_color=COLOUR)
        self.tryAgainLabel = ctk.CTkLabel(self.tryAgainFrame, text="Play again?")
        self.tryAgainButtonY = ctk.CTkButton(self.tryAgainFrame, text="Yes", command=self.difficulty)
        self.tryAgainButtonN = ctk.CTkButton(self.tryAgainFrame, text="No", command=self.difficulty)

        self.tryAgainFrame.place(x=550, y=200, anchor=ctk.NW)
        self.tryAgainLabel.place(x=0, y=0, anchor=ctk.NW)
        self.tryAgainButtonY.place(x=100, y=0, anchor=ctk.NW)
        self.tryAgainButtonN.place(x=200, y=0, anchor=ctk.NW)



app = App()
app.mainloop()
