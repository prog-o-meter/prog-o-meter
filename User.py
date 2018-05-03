class User (object):

  """Represents a prog-o-meter user. Tracks and updates progress, and stores user info.
  """

  def __init__(self, display_name = None, new_user = False):
    """Constructor for the User object.

    Args:
      display_name (str): Display name for the user (default: None)
      new_user (bool): Flag indicating whether or not to create a new file. Default = False
    """
    self.display_name = display_name
    self.goal_days = 100
    self.completed_days = 0

    if new_user and display_name != None:        # If this is a new user being created for the first time, create a new file for them and save it.
      self.addDays(0)
    
  def addDays(self, days = 1):
    """Add completed days to the user's progress and write to file.

    Args:
      days (int): # of days to add. Default = 1
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
      days (int): Number of days to remove from the current count. Default = 1
    """
    return self.addDays(days * -1)

  def setName(self, name):
    """Setter for the user's display name.

    Args:
      name (str): New display name
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
      newGoal (int): Total number of days the user is working toward
    """
    # Check that the new goal is an integer here, otherwise it could cause problems down the line that are harder to debug
    if not isinstance(newGoal, int): raise ValueError

    self.goal_days = newGoal

  def getProgress(self):
    """Getter for the user's progress.

    Returns:
      (int, int): Tuple representing how many days the user has completed in their challenge, and the total length of their challenge.
    """
    return (self.completed_days, self.goal_days)
  
  def reachedGoal(self):
    """Determines whether the user has completed their goal or not.

    Returns:
      True if the user has reached their goal, false if not.
    """
    return self.completed_days >= self.goal_days

  def load_progress_from_file(self):
    """Retrieves saved data for the user and loads it into the completed_days attribute.
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