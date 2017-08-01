# budgetScrape
Program to scrape NYC DOE school budgets

#
# USAGE INSTRUCTIONS
1. DOWNLOAD PYTHON 3.6, MAKE SURE TO SELECT "ADD PYTHON TO PATH" OPTION, AND RESTART YOUR COMPUTER
	* https://www.python.org/downloads/
2. OPEN UP TERMINAL (CMD IN WINDOWS)
	* IF YOU DO NOT KNOW WHAT THIS IS, SEARCH FOR IT: TOP RIGHT CORNER MAGNIFYING GLASS IN MAC AND WINDOWS KEY FOR WINDOWS
3. TYPE IN "pip install bs4" AND HIT ENTER
	* IF THIS DOES NOT WORK, TYPE "sudo pip install bs4"
	* IF THIS STILL DOES NOT WORK THEN TRY INSTALLING PYTHON AGAIN, SELECT "MODIFY", AND THEN SELECT ADD PYTHON TO PATH AND COMPLETE INSTALLATION.
4. TYPE IN "pip install requests" AND HIT ENTER
	* IF THIS DOES NOT WORK, TYPE "sudo pip install requests"
5. DOWNLOAD THE "budget_webscrape.py" FILE AND MOVE TO DESKTOP
6. USE CD (CD .. GOES UP A FOLDER, CD [FOLDERNAME] GOES DOWN) TO NAVIGATE TO FOLDER CONTAINING BUDGET_WEBSCRAPE.PY
7. ADD SCHOOL ATS CODES INTO A FILE CALLED "schools.txt" SEPERATED BY ONLY NEW LINES, THE FILE MUST BE IN THE SAME FOLDER AS BUDGET_WEBSCRAPE.PY
8. ADD KEYWORDS INTO A FILE CALLED "keywords.txt" SEPERATED BY ONLY NEW LINES, THE FILE MUST BE IN THE SAME FOLDER AS BUDGET_WEBSCRAPE.PY
9. TYPE "python" AND HIT ENTER
10. TYPE "import budget_webscrape" AND HIT ENTER
11. TYPE "budget_webscrape.main()" AND HIT ENTER

#
# FAQ
1. ERRNO13 PERMISSION DENIED
* Please place the file onto your desktop. If you put it somewhere else your computers permissions may deny write access, and the program will crash early.

2. IT WONT CHANGE THE KEYWORDS OR SCHOOLS
* This is because it has already imported the file, and this will need to be done whenever you want to change the keywords or school codes. You have two options to fix this: technical, and simple.
	* Close the terminal window, re-open it and start again from step 9.
	* Type "import imp" and hit enter,
	"imp.reload(budget_webscrape)" and hit enter,
	and type "budget_webscrape.main()" and hit enter.
#
# Copyright
Made by James Gan for Practice Makes Perfect

Available under The MIT License:
Copyright 2017 James Gan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
