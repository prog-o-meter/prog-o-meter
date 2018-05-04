class User (object):

    """Represents a user. Gets and updates their progress info.

    Currently, the User object supports some recording of "part goals,"
    but these cannot yet be saved to disk, so use with caution!
    """

    def __init__(self, display_name = None, new_user = False):
        """Constructor for the User object.

        Args:
            display_name (str) -- User's display name (default None)
            new_user (bool) -- Flag indicating whether or not to
            create a new file (default False)
         """
        self.display_name = display_name
        self.goal_days = 100
        self.completed_days = 0
        self.part_goals = []

        # If this is a new user being created for the first time,
        # create a new file for them and save it.
        if new_user:
            self.addDays(0)
        else:        # Otherwise, load days from existing file
            self.load_progress_from_file()
    
    def addDays(self, days = 1):
        """Add completed days to the user's progress and write to file.

        Args:
            days -- # of days to add (default 1)
        """
        self.completed_days += days

        filename = self.getFileName()
        days_text = open(filename, "w")
        days_text.write(str(self.completed_days))
        days_text.close()

        return self.completed_days
  
    def removeDays(self, days = 1):
        """Subtract days from the user's progress and write to file.

        This method is an alias for calling .addDays with a negative value.

        Args:
            days -- Number of days to remove from the current count (default 1)
        """
        return self.addDays(days * -1)

    def setName(self, name):
        """Setter for the user's display name.

        Args:
            name -- New display name
        """
        self.display_name = name
  
    def getName(self):
        """Getter for the user's display name.
        """
        return self.display_name
  
    def getGoal(self):
        """Getter for the total # of days in the user's goal.
        """
        return self.goal_days
    
    def setGoal(self, newGoal):
        """Setter for the # of days in the user's goal.

        Args:
            newGoal -- Total number of days the user is working toward
        """
        # Check that the new goal is an integer here, otherwise it could cause
        # problems down the line that are harder to debug
        if not isinstance(newGoal, int): raise ValueError

        self.goal_days = newGoal
    
    def getPartGoals(self):
        """Getter for the part_goals attribute.
        """
        return self.part_goals
    
    def addPartGoal(self, goal):
        """Append a goal to the part_goals list

        Args:
            goal -- A part goal
        """
        self.part_goals.append(goal)

    def getProgress(self):
        """Getter for the user's progress.

        Returns:
            (int, int) Tuple representing how many days the user has
            completed in their challenge, and the total length of their challenge.
        """
        return (self.completed_days, self.goal_days)
  
    def reachedGoal(self):
        """Determines whether the user has completed their goal or not.

        Returns:
            True if the user has reached their goal, False if not.
        """
        return self.completed_days >= self.goal_days

    def load_progress_from_file(self):
        """Loads saved data from disk into completed_days attribute.

        Returns:
            (int) # of completed days
        """
        filename = self.getFileName()
        days_text = open(filename, "r")
        self.completed_days = int(days_text.read())
        days_text.close()
        return self.completed_days

    def getFileName(self):
        """Private method for determining the file name to load data from and save data to.
        """
        return "".join((self.display_name.lower(), ".txt"))
  
    def __str__(self):
        """String representation of the User object.
        """
        return "User " + str(self.display_name) + "; On day #" + str(self.completed_days)