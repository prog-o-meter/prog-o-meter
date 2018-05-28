# Prog-o-Meter Overview

This is a simplified rundown of the various different files involved in the project.
It contains a short explanation of what each file does, and how they are interrelated.
This document should serve as an introduction to the project, but for more details be sure
to check out the files themselves and read the docstrings.

### Root directory

`.gitignore`

Used for management of the Git repository. It specifies which files should not be uploaded
to the repository when you make your Git commits.
NOTE: This file tells git what to ignore, and as a contributor you do not need to worry about it, git will make sure the right things are ignored. 

`CODE_OF_CONDUCT.md`

A code that all contributors to the project are expected to abide by.

`CONTRIBUTING.md`

Information for contributors to the project.
This is a good place for new contributors to start, and learn how to contribute to the prog-o-meter

`contributors.txt`

A list of the people who have contributed to the prog-o-meter project.

`LICENSE`

License information, specifying who is allowed to use the code in this project, and under what conditions.

`prog-o-meter.py`

The main file for the project. Almost everything you need to run the application can be found in here.
This file creates tkinter windows that guide the user through the process of creating a meter or loading
up an existing meter. It then launches the main prog-o-meter window, which lets the user add days
to their progress.

If the user has reached their goal, they are shown a congratulations message, but that message is
not located in this file. If you want to edit the congratulations dialog, you will need to edit
`congratulations/Congratulations.py`.

`README.md`

An introduction to the prog-o-meter project.

`user_guide.md`

Instructions for downloading the code to your computer and getting it up and running.


### congratulations/

`Congratulations.py`

Contains a "Congratulations" class, which the program uses to create a window for congratulating the
user when they have reached the end of their goal. If you want to change the look and feel of the
congratulations message, this is the place to do it.

### docs/

`index.md`

An old version of `README.md`.

`project_overview.md`

This file!

`pull_request_template.md`

This is the text that is shown to contributors when they go to make a pull request.
