from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(countries):
     countries.sort(key=len)
     shortest = countries[0]
     shortest_words = []
     for item in countries:
          if len(item) == len(shortest):
            shortest_words.append(item)
          else:
              return shortest_words

def most_vowels(country_list):
    ##vowels en count##
    vowels = "aeiouAEIOU"
    count = 0
    country_list_with_vowels = []
    country_list_w_vowels = {}
    for item in country_list:
        count = 0
        for c in item:
            if c in vowels:
                count += 1
        country_list_w_vowels[item] = count
    ##sorteren op meeste vowels
    sorted_values = sorted(country_list_w_vowels.values()) # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in country_list_w_vowels.keys():
            if country_list_w_vowels[k] == i:
                sorted_dict[k] = country_list_w_vowels[k]
    ###Dict keys omzetten naar een lijst (keys staan nu al op volgorde)
    sorted_keys = list(sorted_dict.keys())
    ##len van de list - 3 want top 3
    n = len(sorted_keys) - 3
    ##return [n:] betekent: return de laatste 3
    return sorted_keys[n:]
    
def alphabet_set(country_list):
    alphabet = "abcdefghijklmnopqrstuwvxyz"
    checked_countries = []
    found_letters = []
    for country in country_list:
        containsNewLetter = False
        for c in country:
            character = c.lower()
            if character in alphabet:
                if character not in found_letters:
                    containsNewLetter = True
                    found_letters.append(character)
        if containsNewLetter:
            checked_countries.append(country)
        if len(checked_countries) <= 14 and len(found_letters) == 26:
            return checked_countries 
            ## (f"We we're able to find all the letters within {len(checked_countries)} words.")










# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    """ Write the calls to your functions here. """
    countries = get_countries()
    ##print(shortest_names(countries))
    ##print(most_vowels(countries))
    print(alphabet_set(countries))
        


   
