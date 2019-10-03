import xml.etree.ElementTree as ET
import csv

xml_file = ''
tree = ET.parse(xml_file)
root = tree.getroot()
finder = root.findall('./plugins/plugin')

with open('gcdsTesting.csv','w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['Name', 'Value', 'Notes'])
	for f in finder:
		attrib = f.attrib
		if 'google.GooglePlugin' in attrib['class']:
			writer.writerow(['GSUITE SETTINGS'])
			googleDomain = f[0][0].text
			writer.writerow(['Google Domain:', googleDomain])
			exclusions = f[0].findall('./exclude')
			if exclusions != []:
				writer.writerow([''])
				count = 1
				for x in exclusions:
					match = x[0].text
					matchType = x[1].text
					exFilter = x[2].text
					writer.writerow([f'Google Exclusion Rule {count}'])
					writer.writerow(['Match', match])
					writer.writerow(['Type', matchType])
					writer.writerow(['Filter', exFilter])
					writer.writerow([''])
					count += 1
		if 'ldap.LDAPPlugin' in attrib['class']:
			writer.writerow(['LDAP SETTINGS'])
			serverType = f[0][0].text
			hostname = f[0][2].text
			port = f[0][3].text
			basedn = f[0][4].text
			authUser = f[0][6].text
			primaryKey = f[0][8].text
			mailAttrib = f[0][9].text
			currMachine = f[0][10].text
			writer.writerow(['Server Type', serverType])
			writer.writerow(['Local Hostname', currMachine])
			writer.writerow(['Local IP', hostname])
			writer.writerow(['BaseDN', basedn])
			writer.writerow(['Authorized User', authUser])
			writer.writerow(['Primary Key Attribute', primaryKey])