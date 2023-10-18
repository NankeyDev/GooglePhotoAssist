import pyautogui as pag
import tkinter as tk

# Author: Nancy Porto
# Description: This program is a simple script to help me reassign the subject of photos in Google Photos.
# Google photos currently makes you manually reassign photos if their algorithm incorrectly identifies the subject.
# Google photos is not currently as adept at identfiying animals as people. 
# This program allows me to more quickly manually reassign photo subjects without the use of an available API.
# Fixes the problem: Google keeps identifying my new cat as my bunny. 

# INSTRUCTIONS

# FORCE STOP
# ----------
# Force the mouse to the upper left of screen to force python library to stop running

# SETUP
# ----------
# This is set to be utilized on my main ultrawide monitor
# Using Chrome browser with bookmarks showing
# Full-size window

#   ;jkl;
# Resolution of a screen,Origin is in upper left of screen (0,0)

# mouseCoordinates = pag.displayMousePosition()

# Speed adjustments
pag.PAUSE = 1.0
intervalNum = 0.3
# photoCount = input("Enter number of photos: ")

# Hardcoded x and y coordinates
nextIconLocationWidth = 2150
nextIconLocationHeight = 500

# X,Y coordinate for most recently chosen subject 
recentSubjectWidth = 2269
recentSubjectHeight = 268

# pag.moveTo(pag.locateCenterOnScreen('editIcon.jpg'))
editIconXCoord = 2524
editIconYCoord = 268

# pag.moveTo(pag.locateCenterOnScreen('removeIcon.jpg'))
removeIconXCoord = 2226
removeIconYCoord = 182

# pag.moveTo(pag.locateCenterOnScreen('addIcon.jpg'))
addIconXCoord = 2223
addIconYCoord = 229

# pag.moveTo(pag.locateCenterOnScreen('doneButton.jpg'))
doneButtonXCoord = 2523
doneButtonYCoord = 145

# Informational Purposes
print(pag.size())
width, height = pag.size()

def reassignSubject():
    # Edit People & Pets
    pag.moveTo(editIconXCoord, editIconYCoord)
    pag.click(clicks = 1, interval = intervalNum)

    # Remove current photo subject
    pag.moveTo(removeIconXCoord, removeIconYCoord)
    pag.click(clicks=1, interval=intervalNum)

    # Add new photo subject
    pag.moveTo(addIconXCoord, addIconYCoord)
    pag.click(clicks=1, interval=intervalNum)

    # Add recent subject (will be Mimi)
    pag.moveTo(recentSubjectWidth, recentSubjectHeight)
    pag.click(clicks=1, interval=intervalNum)

    # Click on 'Done'
    pag.moveTo(doneButtonXCoord, doneButtonYCoord)
    pag.click(clicks=1, interval=intervalNum)

    # Go to next photo
    pag.press('right')

def getMousePosition():
    x, y = pag.position()

# for x in range(photoCount+1):
#     print("Count: " + str(x+1))
#     reassignSubject()


# GUI
window = tk.Tk()
window.title('Google Photo Helper')
window.geometry('300x150')
photoCountLabel = tk.Label(text="Number of Photos: ")
photoCountEntry = tk.Entry()

photoCountLabel.pack()
photoCountEntry.pack()
# photoCount = p

print("End")