#!/usr/bin/env python3
#python logging program version 0.1
#Andrew-H3 GitHub

import csv
from sys import argv

def main():
	if (len(argv)) == 1:
		helptext()

	else:
		startup()


def startup():
    print('Python Radio Log 0.1')
    if argv[1] == 'new':
        makeNewEntry()

    elif argv[1] == 'read':
        readOldEntries()

    else:
        help()


def helptext():
	print('''
usage: prcl <command>

new  - create a new log
read - read existing logs
''')
	exit(0)



def makeNewEntry():
	callSign = input('Call Sign: ')
	frequency = input('Frequency: ')
	date = input('Date: ')
	time = input('Time: ')
	location = input('Location: ')
	notes = input('Notes: ')
	print('Is this correct?','\nCall Sign:',callSign,'\nFrequency:',frequency,'\nDate:',date,'\nTime:',time,'\nLocation:',location,'\nNotes: ', notes)
	isCorrect = input('y or n\n')
	if isCorrect == 'y':
		with open('log', 'a') as csvfile:
			writeData = csv.writer(csvfile)
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
		exit()

	else:
		print('Invalid option. Quitting...')



def readOldEntries():
    print('read success')


main()
