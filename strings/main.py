# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = "peter knekkebreud"
player2 = "danny phantom"
goal_0 = 32
goal_1 = 54
scorers = f"{player1} scored in minute {goal_0}, \n {player2} finished the match in minute {goal_1}"
print(scorers)

#part 2

player = "peter knekkebreud"
first_name = player[:5]
print(first_name)

lastName = player[player.find(" "):]
print(len(lastName) - 1)

shortenedFirstName = player.replace("peter", "P.")
print(shortenedFirstName)

chant = (first_name + "!" + " ") * len(first_name)
print(chant.strip())