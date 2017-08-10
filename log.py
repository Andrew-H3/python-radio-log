#!/usr/bin/env python3
#python logging program version 0.1
#Andrew-H3 GitHub

import csv

def main():
    print('Python Radio Log 0.1')
    choice = input('new - new entry\nread - read old entrys\nquit - quit\n')
    if choice == 'new':
        makeNewEntry()

    elif choice == 'read':
        readOldEntries()

    elif choice == 'quit':
        exit()

    else:
        print('Choice not recognized')
        main()


def makeNewEntry():
    callSign = input('Call Sign: ')
    frequency = input('Frequency: ')
    date = input('Date: ')
    time = input('Time: ')
    location = input('Location: ')
    notes = input('Notes: ')
    print('Is this correct?','\nCall Sign:',callSign,'\nFrequency:',frequency,'\nDate:',date,'\nTime:',time,'\nLocation:',location,'\nNotes: ', notes)
    isCorrect = input('yes or no\n')
    if isCorrect == 'yes':
        with open('log', 'a') as csvfile:
            writeData = csv.writer(csvfile)
            writeData.writerow([callSign,frequency,date,time,location,notes,])
        main()



        
    elif isCorrect == 'no':
        print('Sorry, please try again.')
        main()

    else:
        print('Input not recognized')
        main()
        
def readOldEntries():
    print('read success')


main()
