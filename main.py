import tkinter as tk

class mainMenu:
    def __init__(self, main):
        #Create main window
        self.main = main
        self.main.title("Hangman")
        self.frame = tk.Frame(main, width = 1200, height = 500)
        self.frame.pack()
        #Welcome Message
        self.welcome = tk.Label(self.frame, text="Welcome to hangman!", font=("Helvetica", 40))
        self.welcome.place(x=320, y=10)
        #Play Button
        self.playButton = tk.Button(self.frame, text = "Play", font=("Helvetica", 36), command = self.new_window,)
        self.playButton.place(width = 200, x=500, y=150)
        #Exit Button
        self.exitButton = tk.Button(self.frame, text="Sair", font=("Helvetica", 24), command = exit)
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
        self.main = main
        self.frame = tk.Frame(self.main, width = 1250, height = 500)
        #Exit Button
        self.exitButton = tk.Button(self.frame, text = 'Exit', font=("Helvetica", 24), command = self.close_windows)
        self.exitButton.place(x=605, y=310)
        self.frame.pack()

def main(): 
    window = tk.Tk()
    app = mainMenu(window)
    window.mainloop()

main()
