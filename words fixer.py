__author__ = 'killo'
'''
input = open("words.txt", "r")


outputList = [0]
for x in range(1,23):
    outputList.append( open(("words" + str(x)), 'w+'))


for line in input:
    outputList[len(line) - 1].write(line)

input.close()
for x in range(1,23):
    outputList[x].close()
'''

def convertString(string):
        patternLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
        string = string.rstrip()
        foundChars = []
        computedPattern = ""
        for character in string:
            if character not in foundChars:
                foundChars.append(character)
            computedPattern += patternLetters[foundChars.index(character)]
        return computedPattern


for x in range(1,23):
    inputFile = open(("words" + str(x)), "r")
    outputFile = open(("wordsPatterns" + str(x)), "w+")
    words = []
    for line in inputFile:
        if line.rstrip().isalpha() and line.lower().rstrip() not in words:
            outputFile.write(line.lower().rstrip() + "," +convertString(line) + "\n")
            words.append(line.rstrip().lower())
    inputFile.close()
    outputFile.close()