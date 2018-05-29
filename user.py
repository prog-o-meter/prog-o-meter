"""
This module contains the User object, which is used to represent
a prog-o-meter user.

Associated with the user are several attributes, including their
display name and their current progress in their challenge.

User progress through the challenge can be updated by calling the
add_days and remove_days methods. The new progress status is automatically
written to disk each time these functions are called, which means
if adding or removing multiple days it is preferrable to pass in an argument
with the total number of days you wish to add, rather than call the
function multiple times.

The part_goals functionality of the class is not yet used by
any other part of the program, but is included in order to accomodate
their inclusion in the future (see https://github.com/lineaba/prog-o-meter/issues/33).
"""

class User(object):

    """Represents a user. Gets and updates their progress info.

    Currently, the User object supports some recording of "part goals,"
    but these cannot yet be saved to disk, so use with caution!
    """

    def __init__(self, display_name=None, new_user=False):
        """Constructor for the User object.

        Args:
            display_name (str): User's display name (default None)
            new_user (bool): Flag indicating whether or not to
            create a new file (default False)
         """
        self.display_name = display_name
        self.goal_days = 100
        self.completed_days = 0
        self.part_goals = []

        # If this is a new user being created for the first time,
        # create a new file for them and save it.
        if new_user:
            self.add_days(0)
        else:        # Otherwise, load days from existing file
            self.load_progress_from_file()

    def add_days(self, days=1):
        """Add completed days to the user's progress and write to file.

        Args:
            days: # of days to add (default 1)
        """
        self.completed_days += days

        filename = self.get_file_name()
        days_text = open(filename, "w")
        days_text.write(str(self.completed_days))
        days_text.close()

        return self.completed_days

    def remove_days(self, days=1):
        """Subtract days from the user's progress and write to file.

        This method is an alias for calling .add_days with a negative value.

        Args:
            days: Number of days to remove from the current count (default 1)
        """
        return self.add_days(days * -1)

    def set_name(self, name):
        """Setter for the user's display name.

        Args:
            name: New display name
        """
        self.display_name = name

    def get_name(self):
        """Getter for the user's display name.
        """
        return self.display_name

    def get_goal(self):
        """Getter for the total # of days in the user's goal.
        """
        return self.goal_days

    def set_goal(self, new_goal):
        """Setter for the # of days in the user's goal.

        Args:
            new_goal: Total number of days the user is working toward
        """
        # Check that the new goal is an integer here, otherwise it could cause
        # problems down the line that are harder to debug
        if not isinstance(new_goal, int):
            raise ValueError

        self.goal_days = new_goal

    def get_part_goals(self):
        """Getter for the part_goals attribute.
        """
        return self.part_goals

    def add_part_goal(self, goal):
        """Append a goal to the part_goals list

        Args:
            goal: A part goal
        """
        self.part_goals.append(goal)

    def get_progress(self):
        """Getter for the user's progress.

        Returns:
            (int, int) Tuple representing how many days the user has
            completed in their challenge, and the total length of their challenge.
        """
        return (self.completed_days, self.goal_days)

    def reached_goal(self):
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
        filename = self.get_file_name()
        days_text = open(filename, "r")
        self.completed_days = int(days_text.read())
        days_text.close()
        return self.completed_days

    def get_file_name(self):
        """Private method for determining the file name to load data from and save data to.
        """
        return "".join((self.display_name.lower(), ".txt"))

    def __str__(self):
        """String representation of the User object.
        """
        return "User " + str(self.display_name) + "; On day #" + str(self.completed_days)

    def __repr__(self):
        """String representation of the user object.
        """
        return "User: " + str(self.display_name)
