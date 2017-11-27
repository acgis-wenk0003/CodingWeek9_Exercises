# File: ListTupleDict.py
# Author:
# Date:
# Purpose: Learn about Lists, Tuples and Dicts by creating functions
#          that deal with days of the week using these types.
#          NOTE:  For day numbers 1=Monday, ..., 7=Sunday

import sys
import inspect

listDays = ['Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday','Sunday']
tupleDays = ('Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday','Sunday')
dictDays = {1:'Monday', 2:'Tuesday', 3:'Wednesday',
            4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}

def main():
    test_getDayNameFromList()
    test_getDayNameFromTuple()
    test_getDayNameFromDict()
    test_getDayNamesFromList()
    test_getDayNamesFromTuple()
    test_getDayNamesFromDict()
    print "\n%i of %i tests passed" % (testPassed, testCount)

def getDayNameFromList(dayNumber):
    return listDays[dayNumber]

def getDayNameFromTuple(dayNumber):
    return tupleDays[dayNumber]

def getDayNameFromDict(dayNumber):
    return dictDays[dayNumber]

def getDayNamesFromList(firstDayNumber, lastDayNumber):
    return listDays[0:]

def getDayNamesFromTuple(firstDayNumber, lastDayNumber):
    return tupleDays[0:]

def getDayNamesFromDict(firstDayNumber, lastDayNumber):
    return dictDays

# ------------------------------------------------------------------------------
# Tests setup
# ------------------------------------------------------------------------------
dayNumber = 2
firstDayNumber = 3
lastDayNumber = 6
testCount = 6
testPassed = 0
fmtPassed = "Passed: %s"
fmtFailed = "Failed: %s\n  Expected: %s\n  Actual: %s"

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------
def test_getDayNameFromList():
    expect = 'Wednesday'
    actual = getDayNameFromList(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNameFromTuple():
    expect = 'Wednesday'
    actual = getDayNameFromTuple(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNameFromDict():
    expect = 'Tuesday'
    actual = getDayNameFromDict(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromList():
    expect = listDays[0:]
    actual = getDayNamesFromList(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromTuple():
    expect = tupleDays[0:]
    actual = getDayNamesFromTuple(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromDict():
    expect = dictDays
    actual = getDayNamesFromDict(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def printTestResult(funcName, expect, actual):
    global testPassed
    if actual == expect:
        print fmtPassed % funcName
        testPassed += 1
    else:
        print fmtFailed % (funcName, expect, actual)

if __name__ == '__main__':
    main()
