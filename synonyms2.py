import requests
from requests.exceptions import HTTPError


class TheSaurus:

	# public methods 

	def get_synonym(self, word): 
		return self.__request(word)

	# private methods

	def __request(self, word):
		url = ('https://dictionaryapi.com/api/v3/references/thesaurus/json/'+ word +
    		'?key=e82f92fe-187e-488e-b061-25a85d593784')
		response = requests.get(url)
		response_json = response.json()
		return self.__pull_data(response_json)

	def __pull_data(self, response_json):
		pull_syns = response_json[0]['meta']
		list_of_syns = str(pull_syns["syns"])
		return self.__treating(list_of_syns)

	def __treating(self,list_of_syns): 

		if '[' in list_of_syns:
			list_of_syns = list_of_syns.replace('[','').replace(']', '')

		if "'" in list_of_syns:
			list_of_syns = list_of_syns.replace("'",'')

		return list_of_syns

# Calling the class

the_saurus = TheSaurus()

# Input of the word 
word = input('Insert the word:  ')

while not word.isalpha():
    word = input("Error. Please insert an existing word: ")

synonyms = the_saurus.get_synonym(word)

print('The synonyms of {} are: {}'.format(word, synonyms))


class BigHugeTheSaurus:

	# public methods 

	def get_synonym(self, word): 
		return self.__request(word)

	# private methods

	def __request(self, word):
		url = ('https://words.bighugelabs.com/api/2/'+
    		'4fd9fbb5d6c29e00f74b3efbedec7e04/' + word + '/json')
		response = requests.get(url)
		response_json = response.json()
		return self.__pull_data(response_json)

	def __pull_data(self, response_json):
		pull_syns = []
		if "noun" in response_json:
			pull_syns.append(response_json['noun']['syn'])

		if "adverb" in response_json:
			pull_syns.append(response_json['adverb']['syn'])

		pull_syns = str(pull_syns)
		return self.__treating(pull_syns)

	def __treating(self, pull_syns): 

		if '[' in pull_syns:
			pull_syns = pull_syns.replace('[','').replace(']', '')

		if "'" in pull_syns:
			pull_syns = pull_syns.replace("'",'')

		return pull_syns


# Calling the class

the_big_saurus = BigHugeTheSaurus()

# Input of the word 
word = input('Insert the word:  ')

while not word.isalpha():
    word = input("Error. Please insert an existing word: ")

synonyms = the_big_saurus.get_synonym(word)

print('The synonyms of {} are: {}'.format(word, synonyms))



# Check HTTP status codes
'''
for url in ['https://www.dictionaryapi.com/api/v3/references/thesaurus/json/umpire?key=your-api-key']:
	try:
		response = requests.get('https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}'+
			format(syn) + 'key=e82f92fe-187e-488e-b061-25a85d593784')

		response.raise_for_status()

	except HTTPError as http_err:
	    print(f'HTTP error occurred: {http_err}')  
	except Exception as err:
	    print(f'Other error occurred: {err}')  
	else:
		print('Success')
'''
