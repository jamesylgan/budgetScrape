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


def budgetFetch(ATS):
	
	# figure out URL format
	url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/display2.asp?DDBSSS_INPUT="+ATS+"&Submit=Enter&PROG_YEAR=2017&POP_SCH="+ATS

	#budget = []

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

	for line in soup.find_all('tr', class_='mysection'):
		lines.append(line.get_text())

	keywords = ["CONSULTANTS", "PROFESSIONAL", "ABSENCE", "SUMMER",
				"DEVELOPMENT", "SUPPORT STAFF", 
				"SERVICES", "PROGRAMS"]

	# O(n^2+n), could improve
	for line in lines:
		printed = False
		for term in keywords:
			if (((term) in line) and not printed):
				printed = True
				print(line)

	#print(budget)
	#return budget