import requests
from bs4 import BeautifulSoup

""" for use with the NYC DOE Galaxy budget page at:
https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT=K662&Submit=Enter&PROG_YEAR=2017&POP_SCH=K662
http://schools.nyc.gov/Common/Templates/MainTemplate/CommonMainTemplate.aspx?NRMODE=Published&NRNODEGUID=%7b9E62DB6A-8687-40E3-93D0-5FF6FA11C46D%7d&NRORIGINALURL=%2fAboutUs%2ffunding%2fschoolbudgets%2fGalaxyAllocationFY2017%2ehtm%3fBSSS_INPUT%3d04K211&NRCACHEHINT=Guest&BSSS_INPUT=04K211

TO-DO:
 3. School Name
 5. Add in better specification
 6. Make quicker
 
 NOTE: Functions copy a lot of code in case formatting differs year to year.

 Time spent: 4.5 hours
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

"""

codes = []
keywords = []

with open ('schools.txt', 'rb') as fp:
	content = fp.readlines()
for line in content:
	line = str(line.strip())[2:8]
	codes.append(line)

with open ('keywords.txt', 'rb') as fp:
	content = fp.readlines()
for line in content:
	line = str(line.strip())[2:8]
	keywords.append(line)

def budgetFetch(ATS, year):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/"+\
	"galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS[2:]+\
	"&Submit=Enter&PROG_YEAR="+year+"&POP_SCH="+ATS[2:]

	page = requests.get(url)

	if(page.status_code!=200):
		return "ERROR"

	soup = BeautifulSoup(page.content, 'html.parser')

	lines = []

	# Better looking output: nothing colliding
	for line in soup.find_all('tr', class_='mysection'):
		lineStr = line.get_text()
		if len(lineStr) > 0:
			for i in range(0, len(lineStr)-1):
				if not lineStr[i].isupper() and lineStr[i+1].isupper() and \
				lineStr[i].isalpha() and lineStr[i+1].isalpha():
					lineStr = lineStr[:i+1] + ' ' + lineStr[i+1:]

		# lame hardcode
		lineStr = lineStr.replace("0.00", "")
		lineStr = lineStr.replace("1.00", "")
		lineStr = lineStr.replace("2.00", "")
		lineStr = lineStr.replace("3.00", "")
		lineStr = lineStr.replace("4.00", "")
		lineStr = lineStr.replace("5.00", "")
		lineStr = lineStr.replace("6.00", "")
		lineStr = lineStr.replace("7.00", "")
		lineStr = lineStr.replace("8.00", "")
		lineStr = lineStr.replace("9.00", "")
		lineStr = lineStr.replace("0.50", "")
		lineStr = lineStr.replace("OTPS", "")
		lineStr = lineStr.replace("SBST", "")
		lines.append(lineStr)

	# O(n^2+n), could improve
	for line in lines:
		printed = False
		for term in keywords:
			if (((term) in line) and not printed):
				printed = True
				#print(line)
				with open("Budgets.txt", "a") as text_file:
					text_file.write(line+'\n')
	
	linesTotal = []

	printedP = False

	# Finding total and principal
	# Better looking output: nothing colliding
	# O(n^2+n), could improve
	for line in soup.find_all('tr', class_='myschool'):
		lineStr = line.get_text()
		if len(lineStr) > 0:
			for i in range(0, len(lineStr)-1):
				if not lineStr[i].isupper() and lineStr[i+1].isupper() and \
				lineStr[i].isalpha() and lineStr[i+1].isalpha():
					lineStr = lineStr[:i+1] + ' ' + lineStr[i+1:]

		# lame hardcode
		lineStr = lineStr.replace("OTPS", "")
		lineStr = lineStr.replace("SBST", "")
		lineStr = lineStr.replace(ATS, "")

		# add total
		if '$' in lineStr:
			lineStr = lineStr.replace("$", " $")
			lineStr = "Positions & Total Budget: $ "+lineStr
			linesTotal.append(lineStr)

		# add principal
		if printedP is False:
			if ((", " in lineStr) and not lineStr[lineStr.find(',')-1].isupper()):
				lineStr = "Principal: $ "+lineStr
				linesTotal.append(lineStr.strip())
				printedP = True

	for line in linesTotal:
		with open("Budgets.txt", "a") as text_file:
			text_file.write(line+'\n')

def FSF(ATS, year):
	# figure out URL format
	url = "http://schools.nyc.gov/AboutUs/funding/schoolbudgets/GalaxyAllocationFY"+\
			year+".htm?BSSS_INPUT="+ATS[2:]

	page = requests.get(url)

	if(page.status_code!=200):
		return "ERROR"

	soup = BeautifulSoup(page.content, 'html.parser')

	lines = []

	seen = False

	for line in soup.find_all('tr'):
		lineStr = line.get_text()
		# find FSF funding
		if "TL Fair Student Funding" in lineStr:
			if seen == False:
				seen = True
			elif seen == True:
				lineStr = lineStr.replace("                        ", " $ ")
				lines.append(lineStr)
				
		# O(n^2+n), could improve
		for term in keywords:
			seenterm = False
			if term in lineStr:
				if seenTerm == False:
					seenTerm = True
				elif seenTerm == True:
					lineStr = lineStr.replace("                        ", " $ ")
					# Better looking output: nothing colliding
					if len(lineStr) > 0:
						for i in range(0, len(lineStr)-1):
							if not lineStr[i].isupper() and lineStr[i+1].isupper() and \
							lineStr[i].isalpha() and lineStr[i+1].isalpha():
								lineStr = lineStr[:i+1] + ' ' + lineStr[i+1:]
						lines.append(lineStr)

	for line in lines:
		printedF = False
		with open("Budgets.txt", "a") as text_file:
			text_file.write(line+'\n')
	
def main():
	print("Running...")
	for code in codes:
		print("Running for: "+code)
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n\n'+code)
		# Paste below here to add a new year
			
		# Copy from here to add a new year
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2017"+'\n\n')	
		budgetFetch(code,"2017")
		FSF(code,"2017")
		# Copy to here to add a new year
		
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2016"+'\n\n')	
		budgetFetch(code,"2016")
		FSF(code,"2016")
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2015"+'\n\n')	
		budgetFetch(code,"2015")
		FSF(code,"2015")
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2014"+'\n\n')	
		budgetFetch(code,"2014")
		FSF(code,"2014")
	print("Done!")
