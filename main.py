import tkinter as tk
from PIL import ImageTk, Image  

IMAGE_PATH = "Python Concept Pog.png"
WIDTH, HEIGHT = 1250, 500

class mainMenu:
    def __init__(self, main):
        #Create main window
        self.main = main
        self.main.title("Hangman")
        self.frame = tk.Frame(main, width=WIDTH, height=HEIGHT)
        self.frame.pack()

        #Welcome Message
        self.welcome = tk.Label(self.frame, text="Welcome to hangman!", font=("Helvetica", 40))
        self.welcome.place(x=350, y=10)

        #Play Button
        self.playButton = tk.Button(self.frame, text = "Play", font=("Helvetica", 36), command = self.new_window,)
        self.playButton.place(width = 200, x=500, y=150)

        #Exit Button
        self.exitButton = tk.Button(self.frame, text="Exit", font=("Helvetica", 24), command = exit)
        self.exitButton.place(width = 100, x=550, y=300)

    #Create new window and destroy main window
    def new_window(self):
        self.main.destroy() 
        self.main = tk.Tk() 
        self.app = playGame(self.main) 
        self.main.mainloop()

class playGame:
    def __init__(self, main):
        #Create main window
        self.totalScore = 0
        self.main = main
        self.main.title("Hangman")
        self.frame = tk.Frame(self.main, width = WIDTH, height = HEIGHT)
        
        #Initial Label for Score gets overwritten later by updateScore()
        self.score = tk.Label(self.frame, text=f"Score:  {self.totalScore}", font=("helvetica", 20))
        self.score.place(x=20, y=10)

        #Test Button
        self.testButton = tk.Button(self.frame, text = "Testing", font=("Helvetica", 24), command = self.updateScore)
        self.testButton.place(x=500, y=200)
        self.frame.pack()

        #Exit Button
        self.exitButton = tk.Button(self.frame, text = "Return to main menu", font=("Helvetica", 24), command = self.close_windows)
        self.exitButton.place(x=920, y=10)
        self.frame.pack()
   
    #Update score 
    def updateScore(self):
        self.totalScore += 1
        self.score = tk.Label(self.frame, text=f"Score:  {self.totalScore}", font=("helvetica", 20))
        self.score.place(x=20, y=10)
        
    
    #Close window and return to main menu
    def close_windows(self):
        self.main.destroy() 
        self.main = tk.Tk() 
        self.app = mainMenu(self.main) 
        self.main.mainloop()
        

def main(): 
    window = tk.Tk()
    mainMenu(window)
    window.mainloop()

main()
