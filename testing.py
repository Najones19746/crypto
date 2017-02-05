__author__ = 'killo'
import enchant
import itertools
import re
import time
import collections

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
        self.matchCount = len( set( self.cipherStrings[0]) & set(self.cipherStrings[1]) )
        

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

alphaString = "abcdefghijklmnopqrstuvwxyz"

cipher = "tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf"

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
    print item.cipherStrings, item.matchCount