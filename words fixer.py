__author__ = 'killo'
input = open("words.txt", "r")
output = open("words2.txt", "w")

output.write(input.readline())

for line in input:
    output.write(line.lower())

input.close()
output.close()
