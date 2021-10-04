import re
word = ""
def anti_vowel(word):
  result = re.sub("[aeiou]" , "" , word , flags=re.IGNORECASE)
  return result
#imports re and uses .sub to sub all vowels with space.
word = input("Word : ")
devowel = anti_vowel(word)
print(devowel)
