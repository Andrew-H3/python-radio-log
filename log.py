#!/usr/bin/env python3
#python logging program version 0.1
#Andrew-H3 GitHub

import csv
import sys
from time import strftime
import argparse
import ncmode

def main():
	parser = argparse.ArgumentParser(description="log radio contacts")
	parser.add_argument("command", help="what you want to do", choices=["new", "read"])
	parser.add_argument("-n", help="mode for net controllers to log many contacts at once", default=1)
	args = parser.parse_args()
	if args.command == "new":
		if args.n:
			ncmode.ncMode()
		else:
			makeNewEntry()
	elif args.command == "read":
		readOldEntries()



def makeNewEntry():
	callSign = input('Call Sign: ')
	frequency = input('Frequency: ')
	date0 = input('Date (leave blank for current date): ')
	if not date0:
		date = strftime("%m/%d/%Y")
	else:
		date = date0
	time0 = input('Time (leave blank for current time): ')
	if not time0:
		time = strftime("%H:%M")
	else:
		time = time0
	location = input('Location: ')
	notes = input('Notes: ')
	print('Is this correct?','\nCall Sign:',callSign,'\nFrequency:',frequency,'\nDate:',date,'\nTime:',time,'\nLocation:',location,'\nNotes: ', notes)
	isCorrect = input('y or n\n')
	if isCorrect == 'y':
		with open('log', 'a') as csvfile:
			writeData = csv.writer(csvfile, delimiter='~')
			writeData.writerow([callSign,frequency,date,time,location,notes,])
		addAnother()

	elif isCorrect == 'n':
		print('Sorry, please try again.')
		addAnother()

	else:
		print('Input not recognized')
		addAnother()



def addAnother():
	choice = input('Would you like to start a new log?\ny or n\n')
	if choice == 'y':
		makeNewEntry()

	elif choice == 'n':
		sys.exit()

	else:
		print('Invalid option. Quitting...')
		sys.exit()



def readOldEntries():
	print('made it this far :)')
	with open('log', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter='~')
		for row in reader:
			print(', '.join(row))
	sys.exit()


main()
