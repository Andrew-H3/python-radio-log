import sys
from time import strftime
import csv

def ncMode():
	print('Welome to net controller mode.')
	location = input('Location: ')
	frequency = input('Frequency: ')
	date0 = input('Date (leave blank for current date): ')
	if not date0:
		date = strftime("%m/%d/%Y")
	else:
		date = time0
	time0 = input('Time (leave blank for current time): ')
	if not time0:
		time = strftime("%H:%M")
	else:
		time = time0
	print('Is this correct?','\nLocation: ',location,'\nFrequency: ',frequency,'\nDate: ',date,'\nTime: ',time)
	isCorrect = input('y or n')
	if isCorrect == "y":
		individualInfo()
	else:
		ncMode()


def individualInfo():
	callSign = input('Callsign: ')
	notes = input('notes: ')
	submit()

def submit():
	with open('log', 'a') as csvfile:
		writeData = csv.writer(csvfile, delimiter='~')
		writeData.writerow([callSign,frequency,date,time,location,notes,])
	individualInfo()
