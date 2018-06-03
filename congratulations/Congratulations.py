import webbrowser as webbrowser
from urllib.parse import quote
try:
    import Tkinter as Tk        # Python < 3.0
except ImportError:
    import tkinter as Tk        # Python >= 3.0

class Congratulations(object):
    """Displays a dialog congratulating the user for completing the challenge.

    Allows the user to tweet about their accomplishment.

    TO DO:
        Allow the user to start up a new goal.    
    """

    def __init__(self):
        """Open a Tkinter window with a congratulatory message.
        """
        # Attributes
        self.root = Tk.Toplevel()
        self.root.title("Congratulations!")
        self.challenge_duration = 100        # Set this manually for now. Pass it in as an argument later.
        self.challenge_hashtag = "#100DaysOfCode"

        CANVAS_WIDTH = 300
        CANVAS_HEIGHT = 250
        self.canvas = Tk.Canvas(self.root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
        self.canvas.pack()

        # Text label
        lbl = Tk.Label(self.root, text="Congratulations!\nYou've reached the end of your challenge! You've earned the right to boast a little, so why not tell everyone about your accomplishment?",
        anchor=Tk.CENTER, justify=Tk.CENTER, wraplength=CANVAS_WIDTH-20, padx=10)
        lbl.place(relx=0.0, rely=0.33)

        # Social media button,added the "NO Thanks" Button 
        BTTN_WIDTH = 12
        btn_fb = Tk.Button(self.root, text="Share on Twitter!", compound=Tk.LEFT, command=self.open_twitter_browser, width=BTTN_WIDTH).pack(pady = 5)
        btn_quit = Tk.Button(self.root, text="No Thanks", compound=Tk.LEFT, command=self.close_Window, width=BTTN_WIDTH).pack(pady = 5)
       
        # Tkinter instantiation
        self.root.mainloop()
    
    def open_twitter_browser(self):
        """Opens a new browser tab to the Twitter page for creating a tweet.

        Pre-populates the tweet with a stock message.
        """
        msg = quote("I just completed my " + str(self.challenge_duration) + "-days challenge! "+ self.challenge_hashtag)
        print(self.challenge_hashtag)
        print(msg)
        webbrowser.open_new_tab("https://twitter.com/intent/tweet?text=" + msg)

    def close_Window(self):
        """Closes the celebratory window."""
        self.root.destroy() 

