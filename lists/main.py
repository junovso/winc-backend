# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(list):
    list.sort()
    return(list)

lijst = ["aaaaa", "zzzzz", "xxxxx", "bbbb"]
print(alphabetical_order(lijst))

def won_golden_globe(movie):
    list_of_winners = ["jaws", "e.t. the extra-terrestrial", "star wars: episode iv - a new hope", "memoirs of a geisha"]
    if movie.lower() in list_of_winners:
        return(True)
    else:
        return(False)

print(won_golden_globe("JEFF"))

list_of_toto_albums = ["Fahrenheit",
"The Seventh One",
"Toto XX",
"Falling in Between",
"35th Anniversary - Live in Poland",
"Toto XIV",
"Old Is New",
"40 Tours Around the Sun",
"With a Little Help from My Friends"]

uncleaned_list = [
"jaws",
"e.t. the extra-terrestrial",
"star wars: episode iv - a new hope",
"memoirs of a geisha",
"Fahrenheit",
"The Seventh One",
"Toto XX",
"Falling in Between",
"35th Anniversary - Live in Poland",
"Toto XIV",
"Old Is New",
"40 Tours Around the Sun",
"With a Little Help from My Friends"]

def remove_toto_albums(uncleaned_list):
    for songs in list_of_toto_albums:
        if songs in uncleaned_list: uncleaned_list.remove(songs)
    return(uncleaned_list) 

print(remove_toto_albums(uncleaned_list))