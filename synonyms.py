import requests
from itertools import chain
from big_huge_thesaurus import BigHugeTheSaurus
from the_saurus import TheSaurus

# Calling the class
the_saurus = TheSaurus()
the_big_saurus = BigHugeTheSaurus()

# Input of the word 
word = input('Insert the word: ')

while not word.isalpha():
    word = input("Error. Please insert an existing word: ")

# Get the synonyms 
saurus_synonyms = the_saurus.get_synonym(word)
big_synonyms = the_big_saurus.get_synonym(word)
list_of_syns = big_synonyms + saurus_synonyms

# Cleaning the data
not_nested_list = list(chain.from_iterable(list_of_syns))
remove_duplicates = list(dict.fromkeys(not_nested_list))
synonyms = str(", ".join(remove_duplicates))

# Synonyms 
print('The synonyms of {} are: {}'.format(word, synonyms))



