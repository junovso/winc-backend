from helpers import get_countries
__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {}
    passport["name"] = name
    passport["date_of_birth"] = date_of_birth
    passport["place_of_birth"] = place_of_birth
    passport["height"] = height
    passport["nationality"] = nationality
    return passport

def add_stamp(passport, country):
    if "stamps" in passport:
        visited_countries = passport["stamps"]
        if country in visited_countries:
            return passport
        elif country not in visited_countries:
            if country == passport["nationality"]:
                return passport
            else:
                visited_countries.append(country)
                return passport
    else:
        passport["stamps"] = [country]
        return passport




print(create_passport("Juno", "2020-12-08", "amsterdam", "185", "Zambia" ))

passport2 = {'name': 'Juno', 'date of birth': '2020-12-08', 'place of birth': 'amsterdam', 'height': '185', 'nationality': 'Netherlands', 'stamps':['Bulgaria']}
country2 = "Bulgaria"
print(add_stamp(passport2, country2))
