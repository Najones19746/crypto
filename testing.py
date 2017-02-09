__author__ = 'killo'
import itertools
import re
import time
import random
import collections
import ngram_score

characterUseOrder = ['e','t','a','o','i','n','s','h','r','d']

def simul_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

#nested loop for brute force
def subCipher(string):
    for commonAlphaPermutation in permutations(topPlainTextChars, len(topPlainTextChars)):
        print commonAlphaPermutation
        for uncommonAlphaPermutation in permutations(alphaString, len(cipherUniqueChar) - len(topPlainTextChars)):
            pass
    for uncommonAlphaPermutation in permutations(alphaString, len(cipherUniqueChar) - len(topPlainTextChars)):
        pass

def mostUsedCharacters(string,numChars):
    stringAsList = list(string)
    topX = collections.Counter(stringAsList).most_common(numChars)
    i=0
    for item in topX:
        topX[i]= item[0]
        i+=1

    return topX

class smartCipher:
    def __init__(self, cipherStrings):
        self.cipherStrings = cipherStrings
        self.matchSet = set( self.cipherStrings[0]) & set(self.cipherStrings[1])
        self.matchCount = len(self.matchSet)
        self.firstCipherMatchPositions = []
        self.secondCipherMatchPositions = []
        self.firstCipherPattern = self.convertString( cipherStrings[0] )
        self.secondCipherPattern = self.convertString( cipherStrings[1] )
        self.firstPossibleWords = []
        self.secondPossibleWords = []
        for item in self.matchSet:
            self.firstCipherMatchPositions.append([index for index, char in enumerate(self.cipherStrings[0]) if char in item])
            self.secondCipherMatchPositions.append([index for index, char in enumerate(self.cipherStrings[1]) if char in item])

        patternFile = open( ("wordsPatterns" + str(len(self.cipherStrings[0]))), "r")
        for line in patternFile:
            wordPattern = line.rstrip().split(',')
            if wordPattern[1] == self.firstCipherPattern:
                self.firstPossibleWords.append(wordPattern[0])
        patternFile.close()

        patternFile = open( ("wordsPatterns" + str(len(self.cipherStrings[1]))), "r")
        for line in patternFile:
            wordPattern = line.rstrip().split(',')

            if wordPattern[1] == self.secondCipherPattern:
                self.secondPossibleWords.append(wordPattern[0])
        patternFile.close()


    def convertString(self,string):
        patternLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
        string = string.rstrip()
        foundChars = []
        computedPattern = ""
        for character in string:
            if character not in foundChars:
                foundChars.append(character)
            computedPattern += patternLetters[foundChars.index(character)]
        return computedPattern


        

#ceasar bullshit for warmup
'''
def ceaser(string, step):
    returnString = ""
    for letter in string:
        if letter.isalpha():
            letterEnc = chr(( ord(letter)+step ) )
            if letterEnc > 'z':
                letterEnc = chr(ord(letterEnc)-26)
            returnString += letterEnc
        else:
            returnString += letter
    return returnString
'''

#B E G I N

alphaString = list("abcdefghijklmnopqrstuvwxyz".upper())
cipher = "tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf".replace(' ', '').replace('?', '').upper()


OGKEY = list('abcdefghijklmnopqrstuvwxyz'.upper())
topChars = mostUsedCharacters(cipher, 5)
print topChars


maxscore = -99e9
parentscore,parentkey = maxscore, OGKEY[:]
plainFitness = ngram_score.ngram_score('english_quadgrams.txt')
# keep going until we are killed by the user
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)
    deciphered = simul_replace( cipher , {k: v for k, v in zip(parentkey, alphaString)})

    parentscore = plainFitness.score(deciphered)
    count = 0

    for i in range(0, len(topChars)):
            parentkey[ parentkey.index( topChars[i] )], parentkey[ alphaString.index(topChars[i]) ] = parentkey[ alphaString.index(topChars[i]) ],parentkey[ parentkey.index( topChars[i] )]

    while count < 1500:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        # swap two characters in the child
        child[a],child[b] = child[b],child[a]
        deciphered = simul_replace( cipher , {k: v for k, v in zip(child, alphaString)})

        score = plainFitness.score(deciphered)
        # if the child was better, replace the parent with it
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count = count+1
    # keep track of best score seen so far
    if parentscore>maxscore:
        maxscore, OGKEY = parentscore, parentkey[:]
        print '\nbest score so far:',maxscore,'on iteration',i
        print '    best key: '+''.join(OGKEY)
        print '    plaintext: '+  simul_replace( cipher , {k: v for k, v in zip(OGKEY, alphaString)})



'''
i = 0
maxScore = -99999999999999999
plainFitness = ngram_score.ngram_score('english_quadgrams.txt')
innerLoopScore = maxScore
while True:
    i += 1
    random.shuffle(keyString)
    plaintext = simul_replace( cipher , {k: v for k, v in zip(keyString, alphaString)})
    #print(plaintext)
    innerLoopScore = plainFitness.score(plaintext)
    count = 0
    while count < 400:
        a = random.randint(0,25)
        b = a
        while b == a:
            b = random.randint(0,25)
        childKey = keyString[:]
        childKey[a], childKey[b] = childKey[b], childKey[a]
        plaintext = simul_replace( cipher , {k: v for k, v in zip(childKey, alphaString)})
        score = plainFitness.score(plaintext)
        if score > innerLoopScore:
            innerLoopScore = score
            keyString = childKey[:]
            count = 0
        count += 1
    if innerLoopScore > maxScore:
        maxScore = innerLoopScore
        OGKEY = keyString[:]
        print 'best score:' + str(maxScore)
        print 'plaintext: ' + simul_replace(cipher, {k: v for k, v in zip(OGKEY, alphaString)})


'''

# brute force attempt
'''
cipherUniqueChar = ''.join(set(cipher))
cipherUniqueChar = ''.join( ch for ch in cipherUniqueChar if ch.isalpha())


#get unique characters
print"Cipher unique Chars: ",
print(cipherUniqueChar)
print "Cipher unique Chars Length:",
print (len(cipherUniqueChar))
# print(len(cipherUniqueChar))

topCipherChars = mostUsedCharacters(cipher,5)
print "Top Cipher Chars: ",
print topCipherChars


topPlainTextChars = characterUseOrder[0: len(topCipherChars)]
print "Top used plaintext chars (Common permutation characters):",
print(topPlainTextChars)

for ch in topPlainTextChars:
    alphaString = alphaString.replace(ch, '')
print "Uncommon Permutation Characters: ",
print(alphaString)
print "starting computation"
t1 = time.time()
subCipher(cipher)
t2 = time.time()
print "finished computation, time: ", (t2-t1)
#subCipher(alphaString)
#for i in range(1,26):

#    print(ceaser(cipher,i))
'''
#smart attempt 1
'''
cipherFormatted = cipher.replace('?', '')

print(cipherFormatted)

cipherWordList = []
for word in cipherFormatted.split():
    cipherWordList.append(word)
print(cipherWordList)
smartCipherFrags = []
for item in itertools.combinations(cipherWordList, 2):
    smartCipherFrags.append( smartCipher(item) )
smartCipherFrags.sort(key=lambda x: x.matchCount, reverse=True)

for item in smartCipherFrags:
    print item.cipherStrings, item.matchCount, item.firstCipherMatchPositions,"::" , item.secondCipherMatchPositions
    print item.firstCipherPattern, item.secondCipherPattern
    print item.firstPossibleWords, item.secondPossibleWords
'''
