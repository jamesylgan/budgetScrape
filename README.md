# budgetScrape
Program to scrape NYC DOE school budgets

#
# USAGE INSTRUCTIONS
1. DOWNLOAD PYTHON 3.6
2. OPEN UP TERMINAL (CMD IN WINDOWS)
3. TYPE IN "PIP INSTALL BS4" AND HIT ENTER
	IF THIS DOES NOT WORK, TYPE "SUDO PIP INSTALL BS4"
4. TYPE IN "PIP INSTALL REQUESTS" AND HIT ENTER
	IF THIS DOES NOT WORK, TYPE "SUDO PIP INSTALL REQUESTS"
5. USE CD (CD .. GOES UP A FOLDER, CD [FOLDERNAME] GOES DOWN) TO NAVIGATE TO FOLDER CONTAINING BUDGET_WEBSCRAPE.PY
6. TYPE "python" AND HIT ENTER
7. TYPE "import budget_webscrape" AND HIT ENTER
8. TYPE "budget_webscrape.main()" AND HIT ENTER

#
# FAQ
1. ERRNO13 PERMISSION DENIED
* Please place the file onto your desktop. If you put it somewhere else your computers permissions may deny write access, and the program will crash early.

2. IT WONT CHANGE THE KEYWORDS OR SCHOOLS
* You have two options: technical, and simple.
  a. Close the terminal window, re-open it and start from step 6.
  b. Type "import imp" and hit enter,
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
