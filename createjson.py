import json
import random
graphMode = [["POCA",	"POUA",	'Length',	'Angle',	'Area', ],
             ["Length"	, "Area"	, 'POCA',	'Angle',	"POUA"],
             ["Angle",	"Area",	"POUA",	'Length',	'POCA'],
             ['POUA',	'POCA',	'Angle',	'Length',	'Area'],
             ['Length',	'POCA',	'Area',	'POUA',	'Angle'],
             ['Area',	'Angle',	'Length',	'POUA',	'POCA'],
             ['POUA',	'Angle',	'POCA',	'Area',	'Length'],
             ['POCA',	'Length',	'POUA',	'Area',	'Angle'],
             ['Area',	'Length',	'Angle',	'POCA',	'POUA'],
             ['Angle',	'POUA',	'Area',	'POCA'	, 'Length']]

POCA = [7, 34, 18, 8, 30, 27, 26, 9, 21, 33, 23, 6, 22, 1, 2, 12, 5, 36, 31,
        15, 19, 25, 28, 11, 37, 20, 32, 17, 13, 24, 38, 4, 29, 16, 14, 3, 10, 35]

POUA = [36, 4, 7, 9, 6, 5, 15, 14, 2, 16, 31, 32, 29, 13, 22, 34, 12, 33, 23,
        30, 20, 10, 1, 27, 3, 17, 24, 38, 18, 35, 25, 21, 28, 26, 19, 8, 37, 11]

Length = [12, 38, 17, 5, 37, 27, 13, 30, 4, 6, 33, 14, 29, 32, 36, 9, 10, 1,
          26, 31, 22, 2, 3, 15, 21, 8, 25, 7, 19, 34, 11, 20, 28, 23, 35, 24, 16, 18]

Angle = [30, 13, 3, 10, 14, 5, 36, 4, 15, 33, 27, 16, 21, 32, 12, 24, 34, 6,
         29, 9, 2, 18, 20, 17, 26, 25, 8, 7, 35, 38, 22, 28, 11, 1, 37, 19, 23, 31]

Area = [7, 5, 3, 38, 15, 34, 9, 29, 22, 35, 37, 1, 36, 2, 6, 28, 8, 33, 25,
        14, 16, 27, 32, 21, 11, 20, 31, 12, 13, 4, 26, 30, 18, 24, 23, 19, 17, 10]

randPropDict = {"POCA": [28, 15, 16, 30, 32, 22, 7, 20, 18, 37, 21, 4, 9, 36, 2, 34, 11, 27, 35, 14, 33, 5, 25, 26, 19, 0, 13, 17, 6, 1, 10, 8, 23, 12, 24, 3, 29, 31],
                "POUA": [30, 36, 9, 2, 17, 1, 21, 15, 22, 0, 35, 6, 31, 34, 19, 8, 20, 16, 33, 3, 28, 25, 5, 11, 10, 4, 14, 23, 26, 7, 37, 12, 13, 27, 32, 29, 24, 18],
                'Length': [4, 19, 10, 15, 23, 18, 12, 26, 20, 31, 1, 3, 14, 9, 21, 11, 28, 29, 27, 2, 34, 25, 17, 24, 6, 33, 37, 13, 7, 8, 30, 32, 36, 5, 0, 16, 35, 22],
                "Angle":  [10, 33, 31, 25, 19, 15, 24, 2, 17, 29, 36, 26, 16, 21, 37, 4, 13, 22, 3, 18, 27, 32, 30, 28, 6, 12, 35, 9, 7, 0, 1, 5, 23, 34, 20, 11, 8, 14],
                "Area": [16, 14, 11, 34, 23, 24, 27, 9, 36, 30, 32, 5, 31, 37, 10, 2, 19, 26, 1, 4, 20, 7, 6, 28, 13, 12, 33, 17, 15, 35, 25, 29, 18, 3, 22, 8, 21, 0]}


proportionArray = [[0.05, 0.1, 0.4, 0.7, 0.6, 0.35, 0.85, 0.25, 0.9, 0.65, 0.15, 0.75, 0.2, 0.55, 0.5, 0.95, 0.8, 0.3, 0.45],
                   [0.8, 0.45, 0.5, 0.3, 0.2, 0.95, 0.15, 0.55, 0.9, 0.75,
                    0.85, 0.65, 0.6, 0.25, 0.4, 0.35, 0.05, 0.7, 0.1],
                   [0.7, 0.35, 0.1, 0.25, 0.05, 0.65, 0.4, 0.75, 0.6, 0.55,
                    0.85, 0.95, 0.9, 0.3, 0.15, 0.45, 0.2, 0.8, 0.5],
                   [0.2, 0.5, 0.15, 0.8, 0.9, 0.45, 0.85, 0.3, 0.6, 0.95,
                    0.4, 0.55, 0.05, 0.75, 0.1, 0.65, 0.7, 0.25, 0.35],
                   [0.25, 0.65, 0.35, 0.75, 0.7, 0.55, 0.1, 0.95, 0.05,
                    0.3, 0.4, 0.45, 0.6, 0.8, 0.85, 0.5, 0.9, 0.2, 0.15],
                   [0.9, 0.15, 0.85, 0.2, 0.6, 0.5, 0.4, 0.8, 0.05, 0.45,
                    0.1, 0.3, 0.7, 0.95, 0.35, 0.55, 0.25, 0.75, 0.65],
                   [0.75, 0.55, 0.65, 0.95, 0.25, 0.3, 0.35, 0.45, 0.7,
                    0.8, 0.1, 0.5, 0.05, 0.2, 0.4, 0.15, 0.6, 0.9, 0.85],
                   [0.6, 0.85, 0.4, 0.9, 0.05, 0.15, 0.1, 0.2, 0.7, 0.5,
                    0.35, 0.8, 0.25, 0.45, 0.65, 0.3, 0.75, 0.95, 0.55],
                   [0.95, 0.3, 0.55, 0.45, 0.75, 0.8, 0.65, 0.5, 0.25, 0.2,
                    0.35, 0.15, 0.7, 0.9, 0.1, 0.85, 0.05, 0.6, 0.4],
                   [0.05, 0.4, 0.1, 0.6, 0.7, 0.85, 0.35, 0.9, 0.25, 0.15,
                    0.65, 0.2, 0.75, 0.5, 0.55, 0.8, 0.95, 0.45, 0.3],
                   [0.45, 0.8, 0.3, 0.5, 0.95, 0.2, 0.55, 0.15, 0.75, 0.9,
                    0.65, 0.85, 0.25, 0.6, 0.35, 0.4, 0.7, 0.05, 0.1],
                   [0.7, 0.1, 0.35, 0.05, 0.25, 0.4, 0.65, 0.6, 0.75, 0.85,
                    0.55, 0.9, 0.95, 0.15, 0.3, 0.2, 0.45, 0.5, 0.8],
                   [0.5, 0.2, 0.8, 0.15, 0.45, 0.9, 0.3, 0.85, 0.95, 0.6,
                    0.55, 0.4, 0.75, 0.05, 0.65, 0.1, 0.25, 0.7, 0.35],
                   [0.25, 0.35, 0.65, 0.7, 0.75, 0.1, 0.55, 0.05, 0.95,
                    0.4, 0.3, 0.6, 0.45, 0.85, 0.8, 0.9, 0.5, 0.15, 0.2],
                   [0.15, 0.9, 0.2, 0.85, 0.5, 0.6, 0.8, 0.4, 0.45, 0.05,
                    0.3, 0.1, 0.95, 0.7, 0.55, 0.35, 0.75, 0.25, 0.65],
                   [0.75, 0.65, 0.55, 0.25, 0.95, 0.35, 0.3, 0.7, 0.45,
                    0.1, 0.8, 0.05, 0.5, 0.4, 0.2, 0.6, 0.15, 0.85, 0.9],
                   [0.85, 0.6, 0.9, 0.4, 0.15, 0.05, 0.2, 0.1, 0.5, 0.7,
                    0.8, 0.35, 0.45, 0.25, 0.3, 0.65, 0.95, 0.75, 0.55],
                   [0.95, 0.55, 0.3, 0.75, 0.45, 0.65, 0.8, 0.25, 0.5,
                    0.35, 0.2, 0.7, 0.15, 0.1, 0.9, 0.05, 0.85, 0.4, 0.6],
                   [0.4, 0.05, 0.6, 0.1, 0.85, 0.7, 0.9, 0.35, 0.15, 0.25,
                    0.2, 0.65, 0.5, 0.75, 0.8, 0.55, 0.45, 0.95, 0.3],
                   [0.45, 0.3, 0.8, 0.95, 0.5, 0.55, 0.2, 0.75, 0.15, 0.65,
                    0.9, 0.25, 0.85, 0.35, 0.6, 0.7, 0.4, 0.1, 0.05],
                   [0.1, 0.7, 0.05, 0.35, 0.4, 0.25, 0.6, 0.65, 0.85, 0.75,
                    0.9, 0.55, 0.15, 0.95, 0.2, 0.3, 0.5, 0.45, 0.8],
                   [0.5, 0.8, 0.2, 0.45, 0.15, 0.3, 0.9, 0.95, 0.85, 0.55,
                    0.6, 0.75, 0.4, 0.65, 0.05, 0.25, 0.1, 0.35, 0.7],
                   [0.35, 0.25, 0.7, 0.65, 0.1, 0.75, 0.05, 0.55, 0.4,
                    0.95, 0.6, 0.3, 0.85, 0.45, 0.9, 0.8, 0.15, 0.5, 0.2],
                   [0.15, 0.2, 0.9, 0.5, 0.85, 0.8, 0.6, 0.45, 0.4, 0.3,
                    0.05, 0.95, 0.1, 0.55, 0.7, 0.75, 0.35, 0.65, 0.25],
                   [0.65, 0.75, 0.25, 0.55, 0.35, 0.95, 0.7, 0.3, 0.1,
                    0.45, 0.05, 0.8, 0.4, 0.5, 0.6, 0.2, 0.85, 0.15, 0.9],
                   [0.85, 0.9, 0.6, 0.15, 0.4, 0.2, 0.05, 0.5, 0.1, 0.8,
                    0.7, 0.45, 0.35, 0.3, 0.25, 0.95, 0.65, 0.55, 0.75],
                   [0.55, 0.95, 0.75, 0.3, 0.65, 0.45, 0.25, 0.8, 0.35,
                    0.5, 0.7, 0.2, 0.1, 0.15, 0.05, 0.9, 0.4, 0.85, 0.6],
                   [0.4, 0.6, 0.05, 0.85, 0.1, 0.9, 0.7, 0.15, 0.35, 0.2,
                    0.25, 0.5, 0.65, 0.8, 0.75, 0.45, 0.55, 0.3, 0.95],
                   [0.3, 0.45, 0.95, 0.8, 0.55, 0.5, 0.75, 0.2, 0.65, 0.15,
                    0.25, 0.9, 0.35, 0.85, 0.7, 0.6, 0.1, 0.4, 0.05],
                   [0.1, 0.05, 0.7, 0.4, 0.35, 0.6, 0.25, 0.85, 0.65, 0.9,
                    0.75, 0.15, 0.55, 0.2, 0.95, 0.5, 0.3, 0.8, 0.45],
                   [0.8, 0.5, 0.45, 0.2, 0.3, 0.15, 0.95, 0.9, 0.55, 0.85,
                    0.75, 0.6, 0.65, 0.4, 0.25, 0.05, 0.35, 0.1, 0.7],
                   [0.35, 0.7, 0.25, 0.1, 0.65, 0.05, 0.75, 0.4, 0.55, 0.6,
                    0.95, 0.85, 0.3, 0.9, 0.45, 0.15, 0.8, 0.2, 0.5],
                   [0.2, 0.15, 0.5, 0.9, 0.8, 0.85, 0.45, 0.6, 0.3, 0.4,
                    0.95, 0.05, 0.55, 0.1, 0.75, 0.7, 0.65, 0.35, 0.25],
                   [0.65, 0.25, 0.75, 0.35, 0.55, 0.7, 0.95, 0.1, 0.3,
                    0.05, 0.45, 0.4, 0.8, 0.6, 0.5, 0.85, 0.2, 0.9, 0.15],
                   [0.9, 0.85, 0.15, 0.6, 0.2, 0.4, 0.5, 0.05, 0.8, 0.1,
                    0.45, 0.7, 0.3, 0.35, 0.95, 0.25, 0.55, 0.65, 0.75],
                   [0.55, 0.75, 0.95, 0.65, 0.3, 0.25, 0.45, 0.35, 0.8,
                    0.7, 0.5, 0.1, 0.2, 0.05, 0.15, 0.4, 0.9, 0.6, 0.85],
                   [0.6, 0.4, 0.85, 0.05, 0.9, 0.1, 0.15, 0.7, 0.2, 0.35,
                    0.5, 0.25, 0.8, 0.65, 0.45, 0.75, 0.3, 0.55, 0.95],
                   [0.3, 0.95, 0.45, 0.55, 0.8, 0.75, 0.5, 0.65, 0.2, 0.25, 0.15, 0.35, 0.9, 0.7, 0.85, 0.1, 0.6, 0.05, 0.4]]


sizeOfLarge = {"POCA": [150, 300], "POUA": [150, 300], "Length": [
    150, 300], "Angle": [70, 150], "Area": [60, 83]}
participantNum = 38
stimuliData = {}
participants = []
for i in range(participantNum):

    stimuliData[i] = []
    for num, k in enumerate(graphMode[i % 10]):

        # stimuliData[i].append({"sectionID": k})

        # propNum = randPropDict[k][i]
        # stimuliSizeArray = []
        # stimuliData[i].append({"proportionOrder": proportionArray[propNum]})

        # For dictionary called sizes:
        # POCA, POUA, Length - This is the pixels for length
        # Angle - This is degress
        # Area - pixels for radius
        # Third number is whether the larger goes first or second
        # 0 means first, 1 means second

        if k == "POCA" or k == "POUA" or k == "Area":
            propNum = randPropDict[k][i]
            stimuliSizeArray = []
            props = proportionArray[propNum]
            for p in props:
                largerStimuli = random.randint(
                    sizeOfLarge[k][0], sizeOfLarge[k][1])
                smallerStimuli = int(largerStimuli*p)

                stimuliSizeArray.append(
                    (largerStimuli, smallerStimuli, random.randint(0, 1)))
            if k == "POCA" or k == "POUA":
                stimuliData[i].append({k: ({"proportionOrder": proportionArray[propNum]}, {"sizes": stimuliSizeArray}, {
                    "Question": "The one marked with a 100 is 100 blocks high. How high is the one marked with a ?. Type your answer below."})})
            if k == "Area":
                stimuliData[i].append({k: ({"proportionOrder": proportionArray[propNum]}, {"sizes": stimuliSizeArray}, {
                    "Question": "The one marked with a 100 is 100 blocks big. How big is the one marked with a ?. Type your answer below."})})

        if k == "Angle":
            propNum = randPropDict[k][i]
            stimuliSizeArray = []
            props = proportionArray[propNum]
            for p in props:
                largerStimuli = random.randint(
                    sizeOfLarge[k][0], sizeOfLarge[k][1])
                smallerStimuli = int(largerStimuli*p)
                # Need to know how much to rotate the angle. Between 0 and 360 Degrees
                #  the last two random ints are the rotation for the first and second angle
                stimuliSizeArray.append(
                    (largerStimuli, smallerStimuli, random.randint(0, 1), random.randint(0, 360), random.randint(0, 360)))
            stimuliData[i].append({k: ({"proportionOrder": proportionArray[propNum]}, {"sizes": stimuliSizeArray}, {
                "Question": "The one marked with a 100 is 100 blocks wide. How wide is the one marked with a ?. Type your answer below."})})

        if k == "Length":
            propNum = randPropDict[k][i]
            stimuliSizeArray = []
            props = proportionArray[propNum]
            for p in props:
                largerStimuli = random.randint(
                    sizeOfLarge[k][0], sizeOfLarge[k][1])
                smallerStimuli = int(largerStimuli*p)
                largeStart = 0
                smallStart = 0
                largeEnd = 0
                smallEnd = 0
                while largeStart == smallStart or smallEnd == largeEnd:
                    largeSize = largerStimuli
                    smallSize = smallerStimuli
                    largeStart = random.randint(0, 300 - largeSize)
                    largeEnd = largeStart + largeSize
                    smallStart = random.randint(0, 300 - smallSize)
                    smallEnd = smallStart + smallEnd
                    # last two numbers are pixel starting points for the bottom
                stimuliSizeArray.append(
                    (largerStimuli, smallerStimuli, random.randint(0, 1), largeStart, smallStart))
            stimuliData[i].append({k: ({"proportionOrder": proportionArray[propNum]}, {"sizes": stimuliSizeArray}, {
                "Question": "The one marked with a 100 is 100 blocks long. How long is the one marked with a ?. Type your answer below."})})


with open('dataForWebsite.json', 'w') as outfile:
    json.dump(stimuliData,  outfile, indent=4)
