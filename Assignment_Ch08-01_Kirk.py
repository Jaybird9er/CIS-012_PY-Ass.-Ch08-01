def createList(listSize):
    timeList = [0] * listSize
    return timeList

def fillList(listSize, timeList):
    while listSize > 0:
        timeList[listSize - 1] = listSize - 1
        listSize -= 1

def collectUserInputTime():
    callInput = input("Enter the time the call starts in 24-hour notation:\n")
    callList = callInput.split(":")
    startHour = callList[0]
    startMinute = callList[1]
    return startHour, startMinute

def validateUserInputTime(startHour, startMinute):
    for hour in hoursList:
        if int(startHour) == hour:
           startHour = int(startHour)
    for minute in minutesList:
        if int(startMinute) == minute:
              startMinute = int(startMinute)
    if isinstance(startHour, int) and isinstance(startMinute, int):
        return True, startHour, startMinute
    else:
        return False

def collectUserInputDay():
    dayInput = input("Enter the first two letters of the day of the week:\n")
    firstDayCharacter = dayInput[:1].lower()
    secondDayCharacter = dayInput[1:].lower()
    return firstDayCharacter, secondDayCharacter

def validateUserInputDay(firstDayCharacter, secondDayCharacter):
    for dayChar in daysList:
        if firstDayCharacter + secondDayCharacter == dayChar:
            return True
    return False

def collectUserInputCallLength():
    callLen = input("Enter the length of the call in (hours:minutes):\n")
    callLenList = callLen.split(":")
    callLengthHour = callLenList[0]
    callLengthMinute  = callLenList[1]
    return callLengthHour, callLengthMinute

def validateUserInputCallLength(callLengthHour, callLengthMinute):
    for callHour in hoursList:
        if int(callLengthHour) >= 0:
           callLengthHour = int(callLengthHour)
    for callMinute in minutesList:
        if int(callLengthMinute) >= 0:
              callLengthMinute = int(callLengthMinute)
        
    if isinstance(callLengthHour, int) and isinstance(callLengthMinute, int):
        return True, callLengthHour, callLengthMinute
    else:
        return False

def calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute):
    if firstDayCharacter + secondDayCharacter == daysList[5] or firstDayCharacter + secondDayCharacter == daysList[6]:
        totalCost = float(callLengthHour * 60 + callLengthMinute) * 0.15
        return totalCost
    elif ((int(startHour) >= 8 and int(startHour) < 18) and (int(startMinute) >= 00)) or (int(startHour) == 18 and int(startMinute) == 0):
        totalCost = float(callLengthHour * 60 + callLengthMinute) * 0.40
        return totalCost
    else:
        totalCost = float(callLengthHour * 60 + callLengthMinute) * 0.25
        return totalCost

def collectUserInputYesNo():
    yesOrNo = input("Do you want to repeat the program (y/n)?\n")
    return yesOrNo.lower()

def validateUserInputYesNo(yesOrNo):
    if yesOrNo == responseList[0] or yesOrNo == responseList[1]:
        return True
    else:
        return False
    

hoursList = createList(24)
fillList (24, hoursList)
minutesList = createList(60)
fillList (60, minutesList)
daysList = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
responseList = ['y', 'n']


timeVals = collectUserInputTime()
dayChars = collectUserInputDay()
callMins = collectUserInputCallLength()
callCost = calculateTotalCost(timeVals[0],timeVals[1],dayChars[0],dayChars[1],callMins[0],callMins[1])
print("${:.2f}".format(callCost))
