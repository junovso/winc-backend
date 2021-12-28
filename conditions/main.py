# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time, milkingStatus, cowLocation, season, slurryTank, grassStatus):
    if weather == "sunny" and time == "day" and milkingStatus == True and cowLocation == "pasture" and season == "spring" and slurryTank == False and grassStatus == True:
        return ('take cows to cowshed\nmow grass\ntake cows back to pasture')
    # elif slurryTank == True and cowLocation == "cowshed" and weather != "sunny" and weather != "windy":
    #      return ("fertilize pasture/nmilk cows")
    # elif weather == "sunny" and time == "day" and milkingStatus == True and cowLocation == "pasture" and season == "spring" and slurryTank == False and grassStatus == True:
    #     return ('take cows to cowshed\nmow grass\ntake cows back to pasture')
    elif cowLocation == "pasture" and time == "night" and weather == "rain":
        return ("take cows to cowshed")
    elif milkingStatus == True and cowLocation == "cowshed":
         return ("milk cows")
    elif slurryTank == True and cowLocation == "cowshed" and weather != "sunny" and weather != "windy":
         return ("fertilize pasture")
    elif grassStatus == True and  season == "spring" and weather == "sunny":
        return ("mow grass")
    else: ("wait")
 
print(farm_action("sunny", "day", True, "pasture", "spring", False, True))