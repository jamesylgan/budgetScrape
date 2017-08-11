# budgetScrape
Program to scrape NYC DOE school budgets from:
1. https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT=K662&Submit=Enter&PROG_YEAR=2017&POP_SCH=K662
2. http://schools.nyc.gov/Common/Templates/MainTemplate/CommonMainTemplate.aspx?NRMODE=Published&NRNODEGUID=%7b9E62DB6A-8687-40E3-93D0-5FF6FA11C46D%7d&NRORIGINALURL=%2fAboutUs%2ffunding%2fschoolbudgets%2fGalaxyAllocationFY2017%2ehtm%3fBSSS_INPUT%3d04K211&NRCACHEHINT=Guest&BSSS_INPUT=04K211


#
# USAGE INSTRUCTIONS
# First Time Use (A.K.A If you have never run the program on the computer you are using)
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
	* THE GREEN "CLONE OR DOWNLOAD" BUTTON ABOVE AND TO THE RIGHT -> DOWNLOAD ZIP -> UNZIP FILE -> MOVE TO DESKTOP
6. MOVE TO STEP 7
	
# Returning Users	
7. IN THE TERMINAL, USE CD COMMANDS ("cd .." GOES UP A FOLDER, "cd [FOLDERNAME]" GOES DOWN) TO NAVIGATE TO FOLDER CONTAINING BUDGET_WEBSCRAPE.PY
	![example_cd](https://user-images.githubusercontent.com/8934469/28842126-7634234e-76ca-11e7-9d98-619bcfae4362.png)
8. ADD SCHOOL ATS CODES INTO A FILE CALLED "schools.txt" SEPARATED BY ONLY NEW LINES, THE FILE MUST BE IN THE SAME FOLDER AS BUDGET_WEBSCRAPE.PY. EXAMPLE PROVIDED.
9. ADD KEYWORDS INTO A FILE CALLED "keywords.txt" SEPARATED BY ONLY NEW LINES, THE FILE MUST BE IN THE SAME FOLDER AS BUDGET_WEBSCRAPE.PY. EXAMPLE PROVIDED.
10. TYPE "python" AND HIT ENTER
11. TYPE "import budget_webscrape" AND HIT ENTER
12. TYPE "budget_webscrape.main()" AND HIT ENTER

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
	
3. IT ISN'T DOING ANYTHING
* You might have created the schools.txt and keywords.txt incorrectly: make sure they are in plain text format and the right filetype. In Windows, using textpad will generally work. Microsoft Office, for example, will often not work. Try editing the example files I provided, only using textpad.

4. IT IS GIVING ME WEIRD BUDGET LINES
* This would require programming changes. You can edit the code if you trust yourself, or become create, or do things manually. e.g. subtotal lines for groups of things, you could include "subtotal" to get those lines too.

5. WHERE IS THE BUDGET?
* You might have left the old "Budgets.txt" file in the folder before running the program again! This will add on the results to the bottom of the old file. Instead, try deleting or moving the old "Budgets.txt" file before running the program.

6. IT IS ONLY DOING 2017-2014
* Yeah. That happens. Unfortunately, you will have to go into "budget_webscrape.py" and edit the code at the bottom to fix that. Good luck :)
