import csv

Stimuls = [
    {'name':'Stimul1', 'num':1, 'length':15000, 'tech':False},
    {'name':'Stimul2', 'num':2, 'length':25000, 'tech':True},
    {'name':'Stimul3', 'num':3, 'length':20000, 'tech':False}
]

events = """Saccade	-	0	12000	235000	223000	690.0	799.0	1357.0	695.0
Fixation	-	0	235000	445000	210000	1355	699	0	0
Saccade	-	1	445000	637000	192000	1357.0	699.0	622.0	318.0
Fixation	-	1	637000	763000	126000	618	309	0	0"""

eventIterator = iter(csv.reader(events.split('\n'), delimiter='	'))

currentStimulStart = 0
currentStimulEnd = 0
currentEvent = next(eventIterator, None)

for stimul in Stimuls:
    currentStimulEnd = currentStimulStart + stimul ['length'] * 1000 #stimul length in ms, event timings in microseconds
    while (currentEvent is not None and int(currentEvent[4]) <= currentStimulEnd):
        if stimul['tech'] == False and int(currentEvent[3]) >= currentStimulStart:
            print (stimul['name'] + currentEvent[0])
        currentEvent = next(eventIterator, None)
    if (currentEvent is None):
        break
    currentStimulStart = currentStimulEnd
