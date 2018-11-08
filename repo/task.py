
import csv
from csv import reader, writer
with open('us-500.csv', 'rU') as f:
	csvreader = csv.reader(f)
	for row in csvreader:
		print (row[10])

		


f = reader(open('us-500.csv', 'rU'))
fu = writer(open('new.csv', 'w'))
with open('new.csv', 'w') as fu:
	csvwriter = csv.writer(fu)
	for row in f:
		print (csvwriter.writerow(row[10]))


		

