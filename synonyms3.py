import requests
from requests.exceptions import HTTPError
from itertools import chain


class TheSaurus:

	# public methods 

	def get_synonym(self, word): 
		return self.__request(word)

	# private methods

	def __request(self, word):
		url_api_1 = ('https://dictionaryapi.com/api/v3/references/thesaurus/json/'+ word +
    		'?key=e82f92fe-187e-488e-b061-25a85d593784')
		url_api_2 = ('https://words.bighugelabs.com/api/2/'+
    		'4fd9fbb5d6c29e00f74b3efbedec7e04/' + word + '/json')
		response_1 = requests.get(url_api_1)
		response_json_1 = response_1.json()
		response_2 = requests.get(url_api_2)
		response_json_2 = response_2.json()
		return self.__pull_data(response_json_1, response_json_2)

	def __pull_data(self, response_json_1, response_json_2):

		pull_syns = []

		# Pull data for API 1
		syns = response_json_1[0]['meta']
		list_of_syns = syns["syns"]
		pull_syns.append(list_of_syns)

		# Pull data for API 2
		if "noun" in response_json_2:
			pull_syns.append(response_json_2['noun']['syn'])

		if "adverb" in response_json_2:
			pull_syns.append(response_json_2['adverb']['syn'])

		return self.__treating(pull_syns)

	def __treating(self, pull_syns): 

		if '[' in pull_syns:
			pull_syns = pull_syns.replace('[','').replace(']', '')

		if "'" in pull_syns:
			pull_syns = pull_syns.replace("'",'')
		return pull_syns


# Calling the class
the_saurus = TheSaurus()

# Input of the word 
word = input('Insert the word:  ')

while not word.isalpha():
    word = input("Error. Please insert an existing word: ")

# Get the synonyms 

saurus = the_saurus.get_synonym(word)
print(type(saurus))

# Cleaning the data
#not_nested_list = list(chain.from_iterable(saurus))
#remove_duplicates = list(dict.fromkeys(not_nested_list))
#synonyms = str(", ".join(saurus))

# Synonyms
print('The synonyms of {} are: {}'.format(word, saurus))

