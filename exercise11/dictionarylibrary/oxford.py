"""Looks up data from the Oxford OED API"""

import requests

APPID = 'afd8fe09'
APPKEY = 'bbce1d0b0f173d1a27bf9ead8caaf565'

def oxfordcheck(query):
    "Check if a word exists at Oxford Dictionaries.  Return the root form of the word if it does."
    language = 'en'
    word_id = query
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()
    try:
        oxfordrequest = requests.get(url, headers = {'app_id': APPID, 'app_key': APPKEY})
        jroot = oxfordrequest.json()
        root = jroot['results'][0]['lexicalEntries'][0]['inflectionOf'][0]['text']
    except:
        return False
    else:
        return root

def oxfordlookup(query):
    "Get the definition of a word in its root form from Oxford Dictionaries if it exists"
    language = 'en'
    word_id = query
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    try:
        oxfordrequest = requests.get(url, headers={'app_id': APPID, 'app_key': APPKEY})
        jdef = oxfordrequest.json()
        tdef = jdef['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    except:
        defintion = False
    else:
        defintion = tdef
    return defintion

def get_definition(query):
    "Get the defintion of a word from the Oxford dictionary"
    lookup = oxfordcheck(query)
    if lookup:
        thedefintion = oxfordlookup(lookup)
    else:
        thedefintion = False
    return thedefintion

def main():
    "The main program"
    question = input('Enter a word to lookup: ')
    answer = get_definition(question)
    print(answer)

if __name__ == "__main__":
    main()
