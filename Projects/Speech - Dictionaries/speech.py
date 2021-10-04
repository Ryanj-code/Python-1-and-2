import pprint
#Import pprint(prettyprint)

speech = open('mlk.txt', 'r')
speech = speech.read()
speech = speech.lower()
#Opens and reads the speech

speech = speech.replace('.', '')
speech = speech.replace(',', '')
speech = speech.replace('?', '')
speech = speech.replace('!', '')
speech = speech.replace('-', '')
#Replaces all these punctuations with blank

words = speech.split()
print(words)
#Print words after words is set speech that is splitted(smaller pieces).

DictionaryWords = {}
#Sets DictionaryWords to a blank dictionary.

for i in range(len(words)):
  if words[i] in DictionaryWords:
    DictionaryWords[words[i]] += 1
  else:
    DictionaryWords[words[i]] = 1
#Loops through speech, adds the word if it is not in the dictionary, else do not add the word.

pprint.pprint(DictionaryWords)
#Use pprints to print the dictionary out in alphabetical order. 
