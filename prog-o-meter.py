#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The Prog-o-meter.py program is for tracking progress during a #100DaysofCode challenge (or any other #100DaysofX challenge).

The program gives a graphic overview of ones progress through the challenge, by showing a bar containing 100 fields, showing completed days as colored in, and remaining days as white
Currently, the prog-o-meter only tracks your progress in days, but there are plans for many new features, so stay tuned.
The prog-o-meter is developed as an opensource project, and any contributions are welcome, at https://github.com/lineaba/prog-o-meter
"""

__appname__ = "Prog-o-meter"
__authour__ = "Linea Brink Andersen"
__version__ = "1.0.0"
__license__ = "MIT"

from random import randint
import datetime
from congratulations.Congratulations import Congratulations
try:
    import Tkinter as Tk        # Python < 3.0
except ImportError:
    import tkinter as Tk        # Python >= 3.0
from user import User

class ProgressGUI(object):

    """Class contains all things related to the window displaying the prog-o-meter, including text, buttons and actions linked to buttons.

    Attributes:
        root: a tkinter root.
        user: an object representing the user
        username: the name of the user.
        days: the number of days the user have completed.
        GOAL: The number of days the user is trying to complete (hardcoded to be 100, but might wanna add feature for user to chooses this themselves in the future).
        rectagle_list = a list of all rectangle elements to be displayed on canvas.
    """ 
    
    def __init__(self, user, _logname):
        """Open a Tkinter window showing the prog-o-meter, a greeting text, and a button to add a new day to progress.

        Opens a Tkinter window showing the prog-o-meter belonging to the user with the provided username.
        Window contains a greetings text, a count of days untill goal, and the graphical prog-o-meter.
        Window contains a button, for user to add one new day to their progress.

        Args:
            user: an object representing the logged-in user
        """
        # Attributes
        self.root = Tk.Tk()
        self.root.title("Progress")
        self.user = user
        self.username = user.get_name()
        (self.days, self.GOAL) = user.get_progress()
        self.logname = _logname
        self.rectangle_list = []
        self.encourage = ["Nice Job!", "The force is strong with you!", "Well Done!", "You are doing it!", "Never, never, never give up.", "If you dream it, you can do it.", "Everything you can imagine is real.", "Hope is a waking dream.", "You are the best!", "Always believe in yourself."]
        self.days_remaining = self.GOAL - self.days
        self.completion_date = self.get_completion_date(self.days_remaining-1)
        self.current_greeting = 0
        # Tkinter instantiation
        self.canvas_layout()
        self.button_layout()
        self.prog_o_meter()
        self.progress()
        self.root.protocol("WM_DELETE_WINDOW",lambda: quit())
        self.root.mainloop()


    def canvas_layout(self):
        """Display a Tkinter canvas.

        Creates a 1200x600 px canvas, with a greeting text, and a text stating how many days the user have left untill they reach the goal.

        Attributes:
            CANVAS_WIDTH: The width of the canvas is hardcoded to 1200 px.
            CANVAS_HEIGHT: The height of the canvas is hardcoded to 600 px.
            canvas: The Tkinter canvas widget.
            countdown_text: A text element on the canvas, stating how many days the user have left before reaching their goal.
        """
        self.CANVAS_WIDTH = 1200
        self.CANVAS_HEIGHT = 600
        VERTICAL_TEXT_POSITION = 100
        ENCOURAGEMENT_TEXT_POSITION = 400
        self.canvas = Tk.Canvas(self.root, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.greeting = self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION, text = ("".join(("Hello ", self.username))))
        self.countdown_text = self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION+40, justify = Tk.CENTER, text = "".join(("You have ", str(self.days_remaining), " days left!\n\n", "If you code everyday, you will be done with this project on ", self.completion_date)))
        self.encourage_text = self.canvas.create_text(self.CANVAS_WIDTH/2, ENCOURAGEMENT_TEXT_POSITION+40, justify = Tk.CENTER, text = "")

    def button_layout(self):
        """Display a button with the text "1 more day!" and a button with the text "Log" on the canvas.
        
        Creates and display a button with the text "1 more day!" with the function add_day() as callback function. If user have already reached their goal, the button is displayed, but is disabled. 
        Creates and displays a button with the text "Make log entry", with the function log_entry() as callback function.
       
        Attributes:
            add_day_button: A button with the text "1 more day!", which calls the function add_day
            add_log_button: A button with the text "Make log entry", which calls the function log_entry
            
        """
        self.add_day_button = Tk.Button(self.root, text = "1 more day!", command = self.add_day)
        self.add_day_button.pack()
        if self.days >= self.GOAL:        # Disable add_day_button if goal have been reached
            self.add_day_button.config(state = "disabled")
            self.canvas.itemconfig(self.greeting, text=("".join(("Congrats! ", self.username))))
        self.add_log_button = Tk.Button(self.root, text="Make log entry", command = self.log_entry)
        self.add_log_button.pack()
    def prog_o_meter(self):
        """Display a prog-o-meter on the canvas.

        Displays a progess-o-meter made of white rectangles. There will be one rectangle pr. day in goal. Rectangles will be displayed right up against each other, making them appear as one long rectangles, with horizontal lines sectioning it.
        There will be 50 pixels from left edge of window to first rectangle in prog-o-meter, and 50 pixels from last rectangle to right edge of window.
        Rectangles will be 20 pixels high, and their width will be the CANVAS_WIDTH, minus 100 pixels (distance from right+left edge of window to ends of prog-o-meter) divided by number of days in goal.
        """
        LEFT_BOUNDARY = 50
        RIGHT_BOUNDARY = 50
        RECTANGLE_HEIGHT = 20
        RECTANGLE_WIDENESS = (self.CANVAS_WIDTH-(LEFT_BOUNDARY+RIGHT_BOUNDARY))/self.GOAL
        for _ in range(self.GOAL):        # Create a rectangle for each day and add it to the rectangle_list
            rectangle = self.canvas.create_rectangle(LEFT_BOUNDARY, self.CANVAS_HEIGHT/2, LEFT_BOUNDARY+RECTANGLE_WIDENESS, (self.CANVAS_HEIGHT/2)+RECTANGLE_HEIGHT, fill = "white")
            self.rectangle_list.append(rectangle)
            LEFT_BOUNDARY += RECTANGLE_WIDENESS
    def progress(self):
        """Fill in rectangles in prog-o-meter, to represent the current progress of user.

        Fills in rectangles in prog-o-meter to represent the current progress of user, from left to right.
        Completed days will be filled out with a solid color (currently hardcoded to be blue).
        Remaining days will remain white.
        """
        for i in range(self.days):        # Color a rectangle pr. completed day blue (from left to right)
            self.canvas.itemconfig(self.rectangle_list[i], fill = "blue")
    def get_completion_date(self, days_remaining):
        """Calculate the date at which the challenge will be over.

        Args:
            days_remaining: number of days remaining in the project

        Returns:
            The project completion date as a string
        """

        today = datetime.date.today()
        completion_date = today + datetime.timedelta(days=days_remaining)

        if 4 <= completion_date.day <= 20 or 24 <= completion_date.day <= 30:       # Set the suffix for the day to 'th' if it is between 4 and 20 or between 24 and 30
            suffix = "th"
        else:       # Otherwise, set the suffix for the day to 'st', 'nd' or 'rd' when the day ends with 1, 2 or 3 respectively.
            suffix = ["st", "nd", "rd"][completion_date.day % 10 - 1]

        return datetime.date.strftime(completion_date, "%B %d{0}, %Y".format(suffix))
    def add_day(self):
        """Fill out one more rectangle in prog-o-meter with color, to represent one more day completed.

        Callback function to add_day_button. Fills out one more rectangle (most left-ward white rectangle) with color, to represent another day completed.
        Color will be diferent from current progress, to make the new day stand out.
        (Currently the new-day color is hardcoded to be green, but in the future, user should be able to change this themselves).
        """
        self.user.add_days(1)
        self.days += 1
        self.days_remaining = self.GOAL - self.days
        self.completion_date = self.get_completion_date(self.days_remaining)
        self.canvas.itemconfig(self.rectangle_list[self.days-1], fill = "green")
        self.canvas.itemconfig(self.encourage_text, text = "".join(self.encourage[self.new_no(self.current_greeting)]))
        self.canvas.itemconfig(self.countdown_text, text = "".join(("You have ", str(self.days_remaining), " days left!\n\n", "If you code everyday, you will be done with this project on ", self.completion_date)))
        if self.days >=self.GOAL:        # Disable add_day_button if goal have been reached
            self.add_day_button.config(state = "disabled")
            self.canvas.itemconfig(self.greeting, text=("".join(("Congrats! ", self.username))))
            Congratulations()        # Open congratulations window with link to share on Twitter
    
    def new_no(self, current_greeting):
        """Allows to choose a new encouragement from the list each time the button is clicked so that the encouragements are not repeated.
            Attributes:
            current_greeting: A flag attribute that stores the previous value of the encouragement index chosen so that it does not conflict with the new one.
            Returns: A new generated index that is not repeated
        """
        new = randint(0, 9)        #get a random integer between 0-9
        while new == self.current_greeting:        #get a new random integer if new is the same as current_greeting
            new = randint(0, 9)        #get a new random integer between 0-9
        self.current_greeting = new
        return self.current_greeting
    
    def log_entry(self):
        """Opens a new window for user to make a new log entry. The user can make any number of entries they wish.

        Callback function to add_log_button. Opens a new toplevel window with a text widget and three buttons:
        A button marked "Save" that saves the text the user typed into the widget to the [USERNAME]_log.txt file.
        A button marked "Clear" that clears the text that the user typed into the widget.
        A button marked "Close" that closes the toplevel window.
        """
        log_window = Tk.Toplevel(self.root)

        log_window.title("Write your log entry here:")

        scroll_bar = Tk.Scrollbar(log_window)         #A vertical scroll bar for user's convenience
        text_box = Tk.Text(log_window, height=10, width=50)

        scroll_bar.pack(side=Tk.RIGHT, fill=Tk.Y)
        text_box.pack(fill=Tk.Y)

        scroll_bar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar.set)

        def update_log():
            """Updates the log with the text the user typed into the text widget.
            
            Calls update_log_file to save the text to the [USERNAME]_log.txt file.
            """
            input_value = text_box.get("1.0",'end-1c')
            update_log_file(self.logname, input_value)

        save = Tk.Button(log_window, height=1, width=10, text='Save', command=lambda: update_log())
        clear = Tk.Button(log_window, height=1, width=10, text='Clear', command=lambda: text_box.delete('1.0', Tk.END))
        close = Tk.Button(log_window, height=1, width=10, text='Close', command=lambda: log_window.destroy())

        save.pack(side=Tk.LEFT, expand=True)
        clear.pack(side=Tk.LEFT, expand=True)
        close.pack(side=Tk.LEFT, expand=True)
        
class StartGUI(object):

    """Class contains everything related to starting up the application as a new or returning user.

    Attributes:
        root: a tkinter root.
        choice: The input from the user in the radiobuttons. 1 = returning user, 2 = new user
    """

    def __init__(self):
        """Open a Tkinter window, greeting the user, and prompting the to input their status (new/returning user).

        Opens a Tkinter window to determine the status of the user (new/returning).
        Window contains a greetings text, and two radiobuttons for user input (choice: new/returning user).
        Window contains a submit button, for user to click when status have been set using radio-buttons.
        """
        # Attributes
        self.root = Tk.Tk()
        self.root.title("Welcome!")
        self.choice = Tk.IntVar()
        # Tkinter instantiation
        self.canvas_layout()
        self.input_buttons()
        self.root.protocol("WM_DELETE_WINDOW", lambda: quit())
        self.root.mainloop()

    def canvas_layout(self):
        """Display a Tkinter canvas.

        Creates a 300x50 px canvas with a greeting text.

        Attributes:
            CANVAS_WIDTH: The width of the canvas is hardcoded to 300 px.
            CANVAS_HEIGHT: The height of the canvas is hardcoded to 50 px.
            canvas: The Tkinter canvas widget.
        """
        self.CANVAS_WIDTH = 300
        self.CANVAS_HEIGHT = 50
        VERTICAL_TEXT_POSITION = 20
        self.canvas = Tk.Canvas(self.root, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION, text = "Hello, welcome to the prog-o-meter!")

    def input_buttons(self):
        """Display the buttons on the canvas.

        Displays a set of two radio buttons, for the user to indicate whether they are a new
        or returning user. Window closes when user clicks one of the buttons.

        Attributes:
            BTTN_WIDTH: The width of the radiobuttons is hardcoded to 18 text units.
        """
        BTTN_WIDTH = 18
        Tk.Radiobutton(self.root, text = "I already have a meter", variable = self.choice, value = 1, command = self.close_window, indicatoron = 0, width = BTTN_WIDTH).pack(pady = 5)
        Tk.Radiobutton(self.root, text = "I don't have a meter yet", variable = self.choice, value = 2, command = self.close_window, indicatoron = 0, width = BTTN_WIDTH).pack(pady = 5)
    def close_window(self):
        """Close the Tkinter window."""
        self.root.destroy()
    def get_state(self):
        """Return the user's choice from radio-buttons.

        Returns:
            IntVar (1 for returning user, 2 for new user).
        """
        return self.choice.get()

class UsernameGUI(object):

    """Class contains everything related to the user providing their name, either to create a new prog-o-meter, or to retrieve a saved one.

    Attributes:
        root: a tkinter root.
        user_type: 1 = returning user, 2 = new user
    """

    def __init__(self, _user_type):
        """Open a Tkinter window, greeting the user, and prompting the to input their username.

        Opens a Tkinter window for the user to input their name.
        Window contains a greeting+instruction text, and a entry field (text field) where the user types their name.
        Window contains a submit button, for user to click when they have typed their name.
        It does not matter if user types their name with Capital letter, fully capitalized, or in all lower letters. The name will always be in all lower letters in the name of the text file, where the user's data is stored.
        The user's name will be displayed in a greeting in the window instantiated by the ProgressGUI class, and the format of the name their will be exactly as they typed it in this window.
        That means that if the user types "Linea", first time they use the program, and "linea" second time they use it, the program will open the same .txt storing the data both times, but their name will be displayed differently each time.
        """
        # Attributes
        self.root = Tk.Tk()
        self.root.title("Login")
        self.username = ""
        self.user_type = _user_type
        # Tkinter instantiation
        self.canvas_layout()
        self.input_button()
        self.root.protocol("WM_DELETE_WINDOW", lambda: quit())
        self.root.mainloop()
    def canvas_layout(self):
        """Display a Tkinter canvas.

        Creates a 300x50 px canvas with a greeting text and an entry widget (input field for text).

        Attributes:
            CANVAS_WIDTH: The width of the canvas is hardcoded to 300 px.
            CANVAS_HEIGHT: The height of the canvas is hardcoded to 50 px.
            canvas: The Tkinter canvas widget.
            text_entry: A Tkinter text-entry widget (input field for text)
        """
        self.CANVAS_WIDTH = 300
        self.CANVAS_HEIGHT = 50
        self.canvas = Tk.Canvas(self.root, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.text_entry = Tk.Entry(self.root)
        self.text_entry.pack()
        self.text_entry.focus_force()
        if self.user_type == 1:        # Display appropriate greeting for returning users
            self.canvas.create_text(self.CANVAS_WIDTH/2, 20, text = "Good to see you again! Please enter your name")
        elif self.user_type == 2:        # Display appropriate greeting for new users
            self.canvas.create_text(self.CANVAS_WIDTH/2, 20, text = "Lets get you started! Please enter your name")
    def input_button(self):
        """Display the inout button on the canvas.

        Displays a submit button, for user to click when they have typed in their name.
        When button is clicked, it stores the input name as username, and then closes the Tkinter window.

        Attributes:
            submit_button: Button with the text "Submit", which calls the function save_and_close
        """
        self.submit_button = Tk.Button(self.root, text = "Submit", command = self.save_and_close)
        self.submit_button.pack()
        self.root.bind('<Return>', self.save_and_close)
    def save_and_close(self, event=None):
        """Save input text as username, then close Tkinter window. """
        self.username = self.text_entry.get()
        self.root.destroy()
    def get_name(self):
        """Return the username. """
        return self.username

def update_log_file(_logname, _log_entry):
    """ Updates the file [username]_log.txt, adding user's latest update.

    The timestamp is added above the update, with a newline in between. A newline is also added after the update.
    
    Args: 
        _logname: Name of the file to be updated. Should have format [username]_log.txt (username in all lowercase).
        _log_entry: The text which is to be appended to the file.
    """

    log_text = open(_logname, "a")
    log_text.write("\n"
    + str(datetime.datetime.now()) + "\n"
    "\n"
    + str(_log_entry) + "\n")
    log_text.close()

def main():
    """Mainroutine to run the prog-o-meter program.

    Opens a window, which lets the user choose if they are a new or returning user.
    Opens a new window, which lets the user type their name.
    Opens a new window, which shows the user's progress, and how many days remains of the challenge.
    """
    start_screen = StartGUI()
    user_state = start_screen.get_state()
    name_screen = UsernameGUI(user_state)
    username = name_screen.get_name()
    user = User(username, user_state == 2)
    logname = "".join((username.lower(), "_log.txt"))
    ProgressGUI(user, logname)


if __name__ == '__main__':
    main()
