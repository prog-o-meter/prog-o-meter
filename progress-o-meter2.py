# -*- coding: utf-8 -*-
"""
The progress-o-meter is a visual time-keeper, that let's you monitor your progress through #100daysofcode

Written by: Linea Brink Andersen
Version: 1
"""

import Tkinter as Tk

class ProgressGUI(object):
    
    """Class contains all things related to the window displaying the progress-o-meter, including text, buttons and actions linked to buttons.
    
    Attributes:
        root: a tkinter root.
        filename: the name of the .txt file storing the user's number of days.
        username: the name of the user.
        days: the number of days the user have completed.
        GOAL: The number of days the user is trying to complete (hardcoded to be 100, but might wanna add feature for user to chooses this themselves in the future).
        rectagle_list = a list of all rectangle elements to be displayed on canvas.
    """ 
    
    def __init__(self, _days, _filename, _username):
        """Open a Tkinter window showing the progress-o-meter, a greeting text, and a button to add a new day to progress.
        
        Opens a Tkinter window showing the progress-o-meter belonging to the user with the provided username.
        Window contains a greetings text, a count of days untill goal, and the graphical progress-o-meter.
        Window contains a button, for user to add one new day to their progress. 
        
        Args:
            _days: number of days currently completed by the user
            _filename: name of file storing user's progress
            _username: name of user
        """
        # Attributes
        self.root = Tk.Tk()
        self.filename = _filename
        self.username = _username
        self.days = _days
        self.GOAL = 100
        self.rectangle_list = []
        # Tkinter instantiation 
        self.canvas_layout()
        self.button_layout()
        self.progress_o_meter()
        self.progress()
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
        self.canvas = Tk.Canvas(self.root, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION, text = ("".join(("Hello ", self.username))))
        self.countdown_text = self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION+20, text = "".join(("You have ", str(self.GOAL-self.days), " days left!")))
    def button_layout(self):
        """Display a button with the text "1 more day!" on the canvas.
        
        Creates and display a button with the text "1 more day!" with the function add_day() as callback function. If user have already reached their goal, the button is displayed, but is disabled. 
       
        Attributes:
            add_day_button: A button with the text "1 more day!", which calls the function add_day
        """
        self.add_day_button = Tk.Button(self.root, text = "1 more day!", command = self.add_day)
        self.add_day_button.pack()
        if self.days >= self.GOAL:        # Disable add_day_button if goal have been reached
            self.add_day_button.config(state = "disabled")
    def progress_o_meter(self):
        """Display a progress-o-meter on the canvas. 
        
        Displays a progess-o-meter made of white rectangles. There will be one rectangle pr. day in goal. Rectangles will be displayed right up against each other, making them appear as one long rectangles, with horizontal lines sectioning it. 
        There will be 50 pixels from left edge of window to first rectangle in progress-o-meter, and 50 pixels from last rectangle to right edge of window.
        Rectangles will be 20 pixels high, and their width will be the CANVAS_WIDTH, minus 100 pixels (distance from right+left edge of window to ends of progress-o-meter) divided by number of days in goal.
        """
        LEFT_BOUNDARY = 50
        RIGHT_BOUNDARY = 50
        RECTANGLE_HEIGHT = 20
        RECTANGLE_WIDENESS = (self.CANVAS_WIDTH-(LEFT_BOUNDARY+RIGHT_BOUNDARY))/self.GOAL
        for i in range(self.GOAL):        # Create a rectangle for each day and add it to the rectangle_list
            rectangle = self.canvas.create_rectangle(LEFT_BOUNDARY, self.CANVAS_HEIGHT/2, LEFT_BOUNDARY+RECTANGLE_WIDENESS, (self.CANVAS_HEIGHT/2)+RECTANGLE_HEIGHT, fill = "white")
            self.rectangle_list.append(rectangle)
            LEFT_BOUNDARY += RECTANGLE_WIDENESS 
    def progress(self):
        """Fill in rectangles in progress-o-meter, to represent the current progress of user.
        
        Fills in rectangles in progress-o-meter to represent the current progress of user, from left to right.
        Completed days will be filled out with a solid color (currently hardcoded to be blue).
        Remaining days will remain white.
        """
        for i in range(self.days):        # Color a rectangle pr. completed day blue (from left to right)
            self.canvas.itemconfig(self.rectangle_list[i], fill = "blue") 
    def add_day(self):
        """Fill out one more rectangle in progress-o-meter with color, to represent one more day completed.
        
        Callback function to add_day_button. Fills out one more rectangle (most left-ward white rectangle) with color, to represent another day completed.
        Color will be diferent from current progress, to make the new day stand out.
        (Currently the new-day color is hardcoded to be green, but in the future, user should be able to change this themselves).
        """
        self.days += 1
        self.canvas.itemconfig(self.rectangle_list[self.days-1], fill = "green")
        update_days_file(self.filename, self.days)
        ###print self.days
        ###print type(self.days)
        self.canvas.itemconfig(self.countdown_text, text = "".join(("You have ", str(self.GOAL-self.days), " days left!")))
        if self.days >=self.GOAL:        # Disable add_day_button if goal have been reached 
            ###print "YOU ARE DONE!"
            self.add_day_button.config(state = "disabled")             

class StartGUI(object):
   
    """Class contains everything related to starting up the application as a new or returning user. 
    
    Attributes:
        root: a tkinter root.
        choice: The input from the user in the radiobuttons. 1 = returning user, 2 = new user
    """
    
    def __init__(self):
        """Open a Tkinter window, greeting the user, and prompting the to input their status (new/returning user).
        
        Opens a Tkinter window for determine the status of the user (new/returning).
        Window contains a greetings text, and two radiobuttons for user input (choice: new/returning user).
        Window contains a submit button, for user to click when status have been set using radio-buttons.
        """
        # Attributes
        self.root = Tk.Tk()
        self.choice = Tk.IntVar()
        # Tkinter instantiation
        self.canvas_layout()
        self.input_buttons()
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
        self.canvas.create_text(self.CANVAS_WIDTH/2, VERTICAL_TEXT_POSITION, text = "Hello, welcome to the progress-o-meter!")
    def input_buttons(self):
        """Displ
        
        CANVAS_WIDTH: The width of the canvas is hardcoded to 1200 px.
        CANVAS_HEIGHT: The height of the canvas is hardcoded to 600 px.
        canvas: The Tkinter canvas widget.
        """
        Tk.Radiobutton(self.root, text = "I already have a meter", variable = self.v, value = 1).pack(anchor = "w")
        Tk.Radiobutton(self.root, text = "I don't have a meter yet", variable = self.v, value = 2).pack(anchor = "w")
        self.submit_button = Tk.Button(self.root, text = "Submit", command = self.finish)
        self.submit_button.pack()
    def finish(self):
        self.root.destroy()
    def get_state(self):
        return self.v.get()
    
class UsernameGUI(object):
    def __init__(self, _choice):
        self.root = Tk.Tk()
        self.CANVAS_WIDTH = 300
        self.CANVAS_HEIGHT = 50 
        self.canvas = Tk.Canvas(self.root, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.e = Tk.Entry(self.root)
        self.e.pack()
        self.submit_button = Tk.Button(self.root, text = "Submit", command = self.save_and_close)
        self.submit_button.pack()
        self.username = ""
        if _choice == 1:
            self.canvas.create_text(self.CANVAS_WIDTH/2, 20, text = "Good to see you again! Please enter your name")
        elif _choice == 2:
            self.canvas.create_text(self.CANVAS_WIDTH/2, 20, text = "Lets get you started! Please enter your name")
        self.root.mainloop()
    def save_and_close(self):
        self.username = self.e.get()
        self.root.destroy()
    def get_name(self):
        return self.username
            
def update_days_file(_filename, _days):
    days_text = open(_filename, "w")
    days_text.write(str(_days))
    days_text.close()
  
def read_days_file(_filename):
    days_text = open(_filename, "r")
    days = days_text.read()
    days_text.close() 
    return days

def main():
    start_screen = StartGUI()
    choice = start_screen.get_state()
    ###print choice
    name_screen = UsernameGUI(choice)
    username = name_screen.get_name()
    filename = "".join((username.lower(), ".txt"))
    ###print username
    if choice == 2:
        update_days_file(filename, "0")
    days = read_days_file(filename)
    ###print type(days)
    days = int(days)
    ###print "days: ", days
    ProgressGUI(days, filename, username)
    
    
main()
   