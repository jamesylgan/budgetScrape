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
 1. Scrape all relevant lines
 2., ganize: pick the useful ones
 3. Return in convenient manner
 """
codes = ["K662", "X301"]

def budgetFetch17(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+"&Submit=Enter&PROG_YEAR=2017&POP_SCH="+ATS

	#budget = []

	keywords = ["CONSULTANTS", "PROFESSIONAL", "ABSENCE", "SUMMER",
			"DEVELOPMENT", "SUPPORT STAFF", 
			"SERVICES", "PROGRAMS"]

	page = requests.get(url)

	if(page.status_code!=200):
		return "ERROR"

	soup = BeautifulSoup(page.content, 'html.parser')

	# good attempt at isolating values and tags, maybe not best way
	"""line = list(soup.children)[87]
	tags = soup.find_all('td', align='left')
	values = soup.find_all('td', align='right')
	tagA = []
	valueA = []

	for tag in tags:
		if(len(tag.get_text())>1):
			if((tag.get_text()[1].isupper()) or ("Total" in tag.get_text())):
				tagA.append(tag.get_text())

	# got it, just the numbers
	for value in values:
		if(value.get_text()[0] == '$'):
			valueA.append(value.get_text())

	print(len(tagA))
	print(len(valueA))"""


	# useful print statements
	#print(soup.prettify())
	#print(soup)
	#print(list(list(soup.children)[84].children))

	lines = []

	# Better looking output: nothing colliding
	for line in soup.find_all('tr', class_='mysection'):
		lineStr = line.get_text()
		if len(lineStr) > 0:
			for i in range(0, len(lineStr)-1):
				if not lineStr[i].isupper() and lineStr[i+1].isupper() and \
				lineStr[i].isalpha() and lineStr[i+1].isalpha():
					lineStr = lineStr[:i+1] + ' ' + lineStr[i+1:]
		"""if len(lineStr) > 4:
			if lineStr[:4] == "SBST":
				lineStr = lineStr[:4] + ' ' + lineStr[4:]
			if lineStr[:4] == "OTPS":
				lineStr = lineStr[:4] + ' ' + lineStr[4:]"""
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



	#print(budget)
	#return budget

def budgetFetch16(ATS):

	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+"&Submit=Enter&PROG_YEAR=2017&POP_SCH="+ATS

	keywords = ["CONSULTANTS", "PROFESSIONAL", "ABSENCE", "SUMMER",
			"DEVELOPMENT", "SUPPORT STAFF", 
			"SERVICES", "PROGRAMS"]

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
			text_file.write('\n\n'+code+'\n\n')
		budgetFetch17(code)