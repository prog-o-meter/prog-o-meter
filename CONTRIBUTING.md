# Contributing Guide
Please note this is a work in progress, and I'm trying to get it as detailed as possible as quick as possible. 
If you find something that you think needs more explaining, please point it out, by opening an issue (see how below), and we will work on improving it. Please don't hold back, because you think that you're the only one who don't get it! Most likely, you are not, and everyone else will benefit from you pointing it out. But even if you were the only one, we would wanna improve it. This project is for everyone, also for you!

## How to contribute

### Try to use the prog-o-meter program
The first thing to do, would be opening the program and trying it out, so you know how it feels to use.
Check out the file USER_GUIDE.md for instructions on how to download and use the program

### Find out what you wanna work on
If you look un the issues tab above, there will be a list of things to work on. Look through them, and see if anything catches your eye.
* If you find an issue that you think is interesting, but you aren't excactly sure how to get started, please leave a comment on the issue, and we can communicate on how to get started.
* If you find an issue that you think is interesting, and you know how to get started, please leave a comment, stating that you will be working on this, and assign yourself to the issue 
* If you do not find an issue, that you think is interesting, but you have an idea for something to work on, please add a new issue (see how below). If you know how to get started, just go ahead. If not, we will reply to your issue soon, and discuss how to get started on this task

### Get started
When you know what you wanna work on, it is time to start. We use the github workflow (video description here: https://www.youtube.com/watch?v=PBI2Rz-ZOxU) (I will write up a more thorough explanation of this in the future)
In the future, I intend to write guide specifically for prog-o-meter, but for know, check out this step-by-step tutorial by Jen Weber, on how to contribute (It assumes you have git installed, but it has link to a tutorial, if you dont)
https://medium.com/@jenweber/your-first-open-source-contribution-a-step-by-step-technical-guide-d3aca55cc5a6

__NOTES:__
  * __STEP 3__: I am sorry the guide does not include any information on how to clone on Windows. I will try to find a guide as soon as possible.
  * __STEP 5__: The prog-o-meter is a VERY simple program, and no dependencies are needed. However, you do need to have Python installed on your computer. (And Tkinter, but this is almost always included with Python)
  * __STEP 7__: We do not currently have any tests, so for now ignore this step. (If you are interested in working on writing tests, please let me now).
  
### Commenting your code
__IMPORTANT:__ Please do not let any of the following discourage you from contributing. If you need further explanation of anything, please ask. If you are not sure your contribution follows the guidelines, __DO NOT FRET__, please submit a pull-request regardless, and we will help you make any necessary changes, before we merge. 

No one is perfect! I am 100% sure you will find things in the current code, that do not follow the guidelines below. If you do, please either fix it, and submit a pull request so we can improve, or let us know by opening an issue, so someone else can fix it.

An important part of keeping this project newbie friendly, is that we maintain good documentation. 
A more thorough style guide will be produced as soon as possible, for now here are some guidelines. Also, check out existing code, or feel very free to ask, when you are not sure.
* We document all functions, methods and classes with docstring (Suggested ressources: http://www.pythonforbeginners.com/basics/python-docstrings, https://www.pluralsight.com/guides/python/how-to-write-effective-docstrings)
* Contrary to some styleguides we do comment certain parts of code with inline comments. We comment all control flows, to make it easier for new programmers to understand existing code (#This is an inline comment) We put 8 spaces, before putting the inline comment
* We comment if/elif/else-statements (give an explanation of the condition, and what happens if the block is executed)
```#python
  if self.days >=self.GOAL:        # Disable add_day_button if goal have been reached 
    self.add_day_button.config(state = "disabled") 
```
  * We comment for-statements (give an explanation of the loop condition, and what happens inside the loop)
```#python
  for i in range(self.days):        # Color a rectangle pr. completed day blue (from left to right)
    self.canvas.itemconfig(self.rectangle_list[i], fill = "blue")
```
  * We comment while-statement (give an explanation of the loop condition, and what happens inside the loop)
    Sorry, no current example - will add one as soon as possible
* We give our variables, functions, classes, etc. good descriptive names (This is hard, and I very much appreciate any suggestions for changes of current names, that could be improved).
  * We follow google's naming guidelines (https://google.github.io/styleguide/pyguide.html?showone=Naming#Naming)

# How to in github:

## How to open an issue
1. Right below the blue words lineaba/prog-o-meter, there is a menu line. Select the tab __Issues__ 
2. Click the green button __New Issue__
3. Give the issue a title 
  * If you want help getting started: write "Hi, my name is [your name]"
  * If you have an idea for a new feature, or for how to improve a current feature: Give a descriptive title (Check titles of existing issues for inspiration)
4. Leave a comment
  * If you want help getting started: Introduce yourself, what you are interested in, and your experience, and I will help you find something to work on
  * If you have an idea for a new feature, or for how to improve a current feature: Describe your idea in as much detail as you can. (also, mention if it is something you are interested in working on yourself)
5. Click the green button __Submit new issue__
6. Be patient. I will get back to you as soon as I can!

## How to assign yourself to an issue
  https://help.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/ (just assign your own username, to assign yourself)
