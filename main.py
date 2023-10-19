import pyautogui as pag;
import tkinter as tk;
from tkinter import ttk;

# Author: Nancy Porto
# Description: Solution that partially automates reassignment of misclassified photo subjects in Google Photos without the use of an API.
# Instructions: See instructions.md
# Language: Python 3.11

# Resolution of a screen, Origin is in upper left of screen (0,0);
# mouseCoordinates = pag.displayMousePosition();

# Speed adjustments
pag.PAUSE = 1.0;
intervalNum = 0.2;
intervalNum2 = 1.0

# Hardcoded x and y coordinates
nextIconLocationWidth = 2150;
nextIconLocationHeight = 500;

# X,Y coordinate for most recently chosen subject 
recentSubjectWidth = 2269;
recentSubjectHeight = 268;

# X,Y coordinate for search icon 
searchIconXCoord = 2480;
searchIconYCoord = 130;

# X,Y coordinate for searched subject 
searchSubjectXCoord = 2230;
searchSubjectYCoord = 195;

# X,Y coordinate for edit icon
editIconXCoord = 2524;
editIconYCoord = 268;

# X,Y coordinate for remove icon
removeIconXCoord = 2226;
removeIconYCoord = 182;

# X,Y coordinate for add icon
addIconXCoord = 2223;
addIconYCoord = 229;

# X,Y coordinate for done button
doneButtonXCoord = 2523;
doneButtonYCoord = 145;

print(pag.size());
width, height = pag.size();

def reassignSubject():
    # Edit People & Pets
    pag.moveTo(editIconXCoord, editIconYCoord);
    pag.click(clicks = 1, interval = intervalNum);

    # Remove current photo subject
    pag.moveTo(removeIconXCoord, removeIconYCoord);
    pag.click(clicks=1, interval=intervalNum);

    # Add new photo subject
    pag.moveTo(addIconXCoord, addIconYCoord);
    pag.click(clicks=1, interval=intervalNum);

    # Click on search icon
    pag.moveTo(searchIconXCoord, searchIconYCoord);
    pag.click(clicks=1, interval=intervalNum);

    # Type in subject name
    pag.write(photoSubjectInput.get())

    # Select subject
    pag.moveTo(searchSubjectXCoord, searchSubjectYCoord);
    pag.click(clicks=1, interval=intervalNum2);

    # Click on 'Done'
    pag.moveTo(doneButtonXCoord, doneButtonYCoord);
    pag.click(clicks=1, interval=intervalNum2);

    # Go to next photo
    pag.press('right');

def getMousePosition():
    x, y = pag.position();

startRow = 5;
runCount = 0;

def runProgram():
    photoCount = int(photoCountInput.get());
    counter = 0;
    for x in range(photoCount):
        reassignSubject();
        counter += 1;
        print("Count: " + str(x+1));
    outputText = "Count: " + str(counter);
    outputLabel = ttk.Label(content, text=outputText, font='Calibri 8');
    global runCount;
    rowNum = startRow + runCount;
    outputLabel.grid(column = 0, row = rowNum, columnspan = 2, rowspan = 1);
    runCount += 1;
    print("End");

# GUI
window = tk.Tk();
window.title('Google Photo Helper');
window.geometry('400x150');
content = ttk.Frame(window);

# Labels
titleLabel = ttk.Label(content, text='Google Photos', font='Calibri 20 bold');
titleLabel2 = ttk.Label(content, text='Subject Reassignment', font='Calibri 12 bold')
photoCountLabel = ttk.Label(content, text='Photo count: ', font='Calibri 12 bold');
photoSubjectLabel = ttk.Label(content, text='Subject name: ', font='Calibri 12 bold');

# Input
photoCountInput = ttk.Entry(content);
photoSubjectInput = ttk.Entry(content);

# Button
button = ttk.Button(content, text = 'Rename', command = runProgram);

# Grid
content.grid(column = 0, row = 0);
titleLabel.grid(column = 0, row = 0, columnspan = 2, rowspan = 1);
titleLabel2.grid(column = 0, row = 1, columnspan = 2, rowspan = 1);
photoCountLabel.grid(column = 0, row = 2);
photoSubjectLabel.grid(column = 0, row = 3);
photoCountInput.grid(column = 1, row = 2);
photoSubjectInput.grid(column = 1, row = 3);
button.grid(column = 1, row = 4);

window.columnconfigure(0, weight = 1);
window.rowconfigure(0, weight = 1);
content.columnconfigure(0, weight = 3);
content.columnconfigure(1, weight = 1);
content.rowconfigure(1, weight = 1);

# Run Program
window.mainloop();
