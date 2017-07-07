import requests
from bs4 import BeautifulSoup

""" for use with the NYC DOE Galaxy budget page at:
 https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT=K662&Submit=Enter&PROG_YEAR=2017&POP_SCH=K662
 import ______
 import imp
 imp.reload(____)
 budgetFetch(ATS)
 """


""" TO-DO:
 1. Add more years
 2. Add all the ATS codes
 3. Add better keywords
 4. Add a better seperator
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

keywords = ["CONSULTANTS", "PROFESSIONAL", "ABSENCE", "SUMMER",
		"DEVELOPMENT", "SUPPORT STAFF", 
		"SERVICES", "PROGRAMS"]

def budgetFetch17(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/"+\
	"galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+\
	"&Submit=Enter&PROG_YEAR=2017&POP_SCH="+ATS

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
				print(line)
				with open("Budgets.txt", "a") as text_file:
					text_file.write(line+'\n')

def budgetFetch16(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/"+\
	"galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+\
	"&Submit=Enter&PROG_YEAR=2016&POP_SCH="+ATS

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

		# lame hardcode to remove irrelevant data
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
				print(line)
				with open("Budgets.txt", "a") as text_file:
					text_file.write(line+'\n')

def budgetFetch15(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/"+\
	"galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+\
	"&Submit=Enter&PROG_YEAR=2015&POP_SCH="+ATS

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

		# lame hardcode to remove irrelevant data
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
				print(line)
				with open("Budgets.txt", "a") as text_file:
					text_file.write(line+'\n')


def budgetFetch14(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/"+\
	"galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+\
	"&Submit=Enter&PROG_YEAR=2014&POP_SCH="+ATS

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

		# lame hardcode to remove irrelevant data
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
				print(line)
				with open("Budgets.txt", "a") as text_file:
					text_file.write(line+'\n')


def main():
	for code in codes:
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n\n'+code)
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2017"+'\n\n')	
		budgetFetch17(code)
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2016"+'\n\n')	
		budgetFetch16(code)
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2015"+'\n\n')	
		budgetFetch15(code)
		with open("Budgets.txt", "a") as text_file:
			text_file.write('\n'+"2014"+'\n\n')	
		budgetFetch14(code)
		