# ENEMIES module

cabbage = ["Cabbage", "Peppers", "Tomato", "Butternut squash", "Pumpkin", "Spaghetti squash",
           "Winter Squash", "Strawberry"]
aubergine = ["Aubergine", "Runner Bean", "Black Bean", "Tomato", "Melon"]
celeriac = ["Celeriac", "Peppers", "Lettuce", "Cucumber", "Parsley", "Carrot",
            "Butternut squash", "Pumpkin", "Spaghetti squash", "Winter squash", "Potatoes"]
beetroot = ["Beetroot", "bean"]
peppers = ["Peppers", "Potatoes"]
mustard = ["Mustard", "Sunflower", "bean", "Mint", "Strawberry"]
melon = ["Melon", "Cucumber", "Sunflower", "squash", "Potatoes", ]
loofah = ["Loofah", "bean"]
tomato = ["Tomato", "Potatoes", "Corn"]

# make a list of all plants once
allplants = set(cabbage + aubergine + celeriac + beetroot + peppers + mustard + melon + loofah + tomato)
hasenemies = ["Cabbage", "Aubergine", "Celeriac", "Beetroot", "Peppers", "Mustard", "Melon", "Loofah", "Tomato"]
plantfamilies = [cabbage, aubergine, celeriac, beetroot, peppers, mustard, melon, loofah, tomato]

needsenemies = []
for plant in allplants:
    if plant not in hasenemies:
        needsenemies.append(plant)

def findenemies(specificplant, modifier):
    nemeses = [specificplant]
    for family in plantfamilies:
        if specificplant in family:
            nemeses.append(family[0])
    plantfamilies.append(list(nemeses))
    return {k: modifier for k in nemeses}


[findenemies(plant, -10000) for plant in needsenemies]
enemies = {str(family[0]): {k: -10000 for k in family[1:]} for family in plantfamilies}

def findbadneighbours(specificplant, modifier):
    possibleenemies = []
    for family in plantfamilies:
        if specificplant in family:
            for plant in family:
                possibleenemies.append(plant)
    possibleenemies = set(possibleenemies)
    possibleenemies=list(possibleenemies)
    possibleenemies.remove(specificplant)
    return {j:modifier for j in possibleenemies}


allplants=list(allplants)
neighbours = {str(plant):findbadneighbours(plant, 10)for plant in allplants}