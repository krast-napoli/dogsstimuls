import csv

Stimuls = [
    {'name':'Stimul1', 'num':1, 'length':15000, 'tech':False},
    {'name':'Stimul2', 'num':2, 'length':25000, 'tech':True},
    {'name':'Stimul3', 'num':3, 'length':20000, 'tech':False}
]

with open ('events.tsv', newline="") as file:
    eventIterator = iter(csv.reader(file, delimiter='	'))

    currentStimulStart = 0
    currentStimulEnd = 0
    currentEvent = next(eventIterator, None)

    for stimul in Stimuls:
        currentStimulEnd = currentStimulStart + stimul ['length'] * 1000 #stimul length in ms, event timings in microseconds
        while (currentEvent is not None and int(currentEvent[4]) <= currentStimulEnd):
            if stimul['tech'] == False and int(currentEvent[3]) >= currentStimulStart:
                print (stimul['name'] + currentEvent[0])
                filename = stimul['name']+'.csv'
                with open (filename, 'a') as outputfile:
                    fieldnames = ['EventType', '-', 'EventTypeNumber', 'TimeStart', 'TimeStop', 'Duration', 'firstX', 'firstY', 'lastX', 'lastY']
                    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)

                    writer.writerow({
                                     'EventType':currentEvent[0],
                                     '-':currentEvent[1],
                                     'EventTypeNumber':currentEvent[2],
                                     'TimeStart':currentEvent[3],
                                     'TimeStop':currentEvent[4],
                                     'Duration':currentEvent[5],
                                     'firstX':currentEvent[6],
                                     'firstY':currentEvent[7],
                                     'lastX':currentEvent[8],
                                     'lastY':currentEvent[9]
                                    })
            currentEvent = next(eventIterator, None)
        if (currentEvent is None):
            break
        currentStimulStart = currentStimulEnd
