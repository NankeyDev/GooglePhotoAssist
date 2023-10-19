# Description
**Author:** Nancy Porto
**Description:** Solution that partially automates reassignment of misclassified photo subjects in Google Photos without the use of an API.
**Language:** Python 3.11
**IDE:** Visual Studio Code 2019
**Python Packages:** tkinter, pyautogui

**Description:** This program is a straightforward script designed to assist in the reassignment of photo subjects in Google Photos.

Presently, Google Photos requires manual reassignment of individual photos when its algorithm incorrectly identifies the person or pet within the photo. Unfortunately, Google Photos is not as adept at identifying animals as it is people, leading to numerous misclassifications. To address this, this program offers a solution that partially automates the process of subject reassignment  without the need for an API.

**Reason for Development:**
I developed this program due to Google Photos frequently misidentifying my new cat as my bunny, who had passed away. This tool not only saves me a significant amount of time, but also provided the opportunity to delve into the python libraries tkinter and pyautogui. Given my frequent encounters meeting & photographing new animals, this script has enabled me to overcome Google Photos' limitations and effectively manage the organization of the ever-growing volume of photos in my library.

## Program Requirements & Limitations
- The subject must already be created in Google Photos as an available person or pet. 
- The selected photos must only contain ONE SUBJECT. This does not work for photos containing multiple subjects.

# Instructions

## Setup
1. Launch Google Chrome within the main desktop window, ensuring it is maximized and showing the bookmarks bar.
2. Navigate to Google Photos and find a subset of photos that require subject reassigment. The following criteria must be met:
	- The photos must be arranged in a sequence.
	- Each group should contain only a single subject.
	- Each photo in the group should contain a single subject.
	- The subject must already exist in Google Photos as a recognzied person or pet.
3. Take note of the total photos within the subset, and the exact name of the subject to which you intend to reassign them.
4. Start by selecting the first photo in the sequence, and then click on the 'info' icon located in the upper right-hand corner.
5. Run the program.
6. Enter the total number of photos with the subject and the exact subject name you wish to reassign the photos to. Click 'Rename'. Take care to not move the mouse while the program is running unless you intend to stop the program.
7. Once the process has completed, identify a new subset of photos as described above, rinse, and repeat.

## Stopping the program
- Force the mouse to the farthest upper left corner of the screen. This will relinquish control of the mouse and interrupt the program.

# References
**Docs:** https://tkdocs.com/
**YouTube Video:** https://youtu.be/mop6g-c5HEY

# Future Improvements
- Input Validation
- Modify to reduce hardcoded variables
- Explore use for photos with multiple subjects
- Improve Peformance/Speed
- Make resizing look better
- Improve Visuals & Design
- Put log output text in scroll box