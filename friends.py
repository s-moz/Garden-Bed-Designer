# FRIENDS module

# data
cabbage = ["Cabbage", "Celeriac", "Beetroot", "Melon", "Thyme", "Nasturtium", "Oregano", "Dill", "Carrot", "Onion",
           "Garlic", "Celery", "Chamomile", "Rosemary", "Potatoes", "Sage"]
aubergine = ["Aubergine", "Potatoes", "Onion", "Garlic", "Mint", "Nasturtium", "Chickpea", "Lettuce", "Sweet pea",
             "Thyme", "Peppers", "Bean", "Spinach"]
celeriac = ["Celeriac", "Cabbage", "Leek", "Tomato", "Black bean", "Runner beans"]
beetroot = ["Beetroot", "Cabbage", "Peppers", "Mustard", "Lettuce", "Chickpea", "Mint",
            "Radish", "Onion", "Sage"]
peppers = ["Peppers", "Thyme", "Rosemary", "Lettuce", "Cucumber", "Nasturtium", "Oregano", "Tomato", "bean", "Dill",
           "Marjoram", "Parsley", "Carrot", "squash", "Radish", "Garlic", "Onion", "Physalis"]
mustard = ["Mustard", "Thyme", "Sweet pea", "Rosemary", "Chickpea", "Cucumber", "Mint", "Onion", "Celery"]
melon = ["Melon", "Sweet pea", "Lettuce", "Leek", "Chickpea", "Chamomile", "Nasturtium", "Oregano", "bean", "Carrot",
         "Lavender", "Mint", "Radish", "Garlic", "Onion"]
loofah = ["Loofah", "Nasturtium", "Oregano", "Carrot", "squash", "Mint", "Onion"]
courgette = ["Courgette", "Radish", "Dill", "Oregano", "Nasturtium"]
tomato = ["Tomato", "Potatoes"]
carrot = ["Carrot", "Onion", "Garlic", "Bean", "Lettuce", "chickpeas", "Radish", "Tomato"]

# grouping and data structuring
messy_plants = cabbage + aubergine + celeriac + beetroot + peppers + mustard + melon + loofah + courgette + tomato + carrot
all_plants = [set([item.capitalize for item in messy_plants])]
print(messy_plants)
print(all_plants)

from fuzzywuzzy import fuzz
import random

def choose_a_bean(examplelist):
    listoutput = []
    for str1 in examplelist:
        choices = [str1]
        print(choices)
        for str2 in examplelist:
            partial_ratio = fuzz.partial_ratio(str1, str2)
            print(partial_ratio)
            if partial_ratio == 100:
                choices.append(str2)
        print(choices)
        listoutput.append(random.choice(choices))
        print(listoutput)
    return listoutput

from difflib import SequenceMatcher
def choose_a_bean2(examplelist):
    listoutput = []
    examplelist = list(set(examplelist))
    for str1 in examplelist:
        choices = [str1]
        for str2 in examplelist:
            if str2 in choices:
                examplelist.remove(str2)
            else:
                match = SequenceMatcher(None, str1, str2).find_longest_match(0, len(str1), 0, len(str2))
                #overlap = str1[match.a:match.a + match.size]
                #print(overlap)
                if match.size > 2:
                    userinput = input("conflate {str1} and {str2}? y/n")
                    if userinput == "y":
                        choices.append(str2)
                        examplelist.remove(str2)
                    elif userinput not in ["n", "y"]:
                        raise Exception("sorry, input not recognised")
        listoutput.append(random.choice(choices))
    return list(set(listoutput))


all_plants = cabbage + aubergine + celeriac + beetroot + peppers + mustard + melon + loofah + courgette + tomato + carrot
neat_plants = []
for item in all_plants:
    neat_plants.append(item.capitalize())
neat_plants = list(set(neat_plants))
print(neat_plants)
# implement when all the input stuff is fixed, delete above line: all_plants = [entry.casefold() for entry in all_plants]
# all_plants should draw on user input in a file format such as .txt or .xml
# plant_families = {family[0]:family for family in inputlist}
plant_families = {"Cabbage": cabbage, "Aubergine": aubergine, "Celeriac": celeriac, "Beetroot": beetroot,
                  "Peppers": peppers, "Mustard": mustard, "Melon": melon, "Loofah": loofah, "Courgette": courgette,
                  "Tomato": tomato, "Carrot": carrot}


# has_friends = plant_families.keys()

# cross-referencing lists to maximise correlations...
def find_friends(specific_plant: str, plant_families: dict) -> list:
    """
    inputs friendless plant, looks through extant lists to compile its own family, and adds to plant_families.
    :param specific_plant: str input for friendless plant
    plant_families: dict of families sans our beloved specific_plant's
    """
    best_friends = []
    for family in plant_families:
        if specific_plant in plant_families[family]:
            best_friends.append(family)
    best_friends = list(set(best_friends))
    if specific_plant in plant_families.keys():
        possible_friends = list(set(list(plant_families[specific_plant] + best_friends)))
    else:
        possible_friends = list(set(best_friends))
    # possible_friends := plant_families[specific_plant] + best_friends
    while specific_plant in possible_friends:
        possible_friends.remove(specific_plant)
    return list([specific_plant] + possible_friends)


# testing question: what happens if you input a plant that already has a family? does this work?
# if so, next two lines need replacing with; plant_families=[find_friends(plant) for plant in all_plants]
# needs_friends = [p for p in all_plants if p not in has_friends]
# [find_friends(plant) for plant in needs_friends]
for plant in all_plants:
    plant_families[plant] = find_friends(plant, plant_families)

# assigning quantifier at base level for friendships
# friends = {family[0]: {k: 1000 for k in family[1:]} for family in plant_families.values()}
# def assign_proximity(plant_families: str, modifier: int):
#    """
#   alternative to above line if preferred
#    assigns base level friendship qualifier to all plants
#    :param plant_families: comprehensive dict of all plant friendships
#    :param modifier: tbc, int to display basic level friendship
#    :return: plant_families updated with base level modifiers
#    """
#    proximities = {}
#    for plant, family in plant_families.items():
#        baseprox = {p: modifier for p in family}
#        proximities[plant] = baseprox
#        print(proximities)
#    return proximities


# [assign_proximity(plant_families,100)]

# ranking which friends are best
# def find_good_neighbours(specific_plant, modifier):
#    """
#    checks coplanting options against each other to see if they're also compatible
#    :param specific_plant:
#    :param modifier:
#    :return:
#    """
#    possible_friends = []
#    for friend in plant_families[specific_plant][1:]: #look through the coplanting options, to choose our lookup plants
#    #for family in plant_families.values(): #look through eg beetroot's, then beans's... coplanters
#        if specific_plant in plant_families[friend].values(): #if our main cabbage guy is there
#            for plant in plant_families.values():
#                possible_friends.append(plant) #add the other guys that also grow well
#                #check if these correlate to the coplanting options in line 76
#                #if they are there multiple times give them a better score OK I FEEL LIKE IM GOING ON A TANGENT
#    possible_friends = list(set(possible_friends))
#    possible_friends.remove(specific_plant)
#    return {j:modifier for j in possible_friends}

# copied above fn to allow me to chase the tangent

# ranking which friends are best
import numpy as np


def find_good_neighbours_level_1(specific_plant):
    """
    ranks the coplanting options for a specific plant based on maximising growth-compatibility with each other
    ie checks if a coplanting option grows well with many other coplanting options
    this tells you the coplants with the most breadth
    :param specific_plant:
    :param modifier:
    :return:
    """
    possible_friends = []
    friends_ranked = {}
    family = plant_families[specific_plant]  # list of plants which grow well alonside our boy
    # rank the friend based on how many in-laws there are with our initial plant
    for friend in family[1:]:  # iterate through these coplanting options
        in_laws = plant_families[friend][:]  # locate what grows well with each option
        print(in_laws)
        in_laws.remove(friend)
        in_laws.remove(specific_plant)
        mutuals = []
        for plant in in_laws:
            if plant in family:  # check if any of these co-planters also grow well with our initial plant
                mutuals.append(plant)  # list any guys that do
        friends_ranked[friend] = len(mutuals)
    print(friends_ranked) #rank this specific plant based on how many mutuals it has with other coplants
    keys = list(friends_ranked.keys())
    values = list(friends_ranked.values())
    sorted_value_index = np.argsort(values)[::-1]
    friends_ranked = {keys[i]: values[i] for i in sorted_value_index}
    print(friends_ranked)
    return friends_ranked


coplanters = [find_good_neighbours_level_1(specific_plant) for specific_plant in all_plants]

def find_good_neighbours_level_2(specific_plant):
    """
    ranks the coplanting options for a specific plant
    ie counts how many instances of crossover there are among the coplanting options
    this tells you specifically how many plants each coplant grows well with
    :param specific_plant:
    :param modifier:
    :return:
    """
    possible_friends = []
    family = plant_families[specific_plant]  # list of plants which grow well alonside our boy
    # rank the friend based on how many in-laws there are with our initial plant
    for friend in family[1:]:  # iterate through these coplanting options
        in_laws = plant_families[friend][:]  # locate what grows well with each option
        in_laws.remove(friend)
        in_laws.remove(specific_plant)
        mutuals = []
        for plant in in_laws:
            if plant in family:  # check if any of these co-planters also grow well with our initial plant
                mutuals.append(plant)  # list any guys that do
        # next we rank the friend based on how many in-laws a plant has with the other coplanters?
        possible_friends.extend(mutuals)
    from collections import Counter
    rankings = Counter(possible_friends)  # this gives eg. "Cabbage":4, indicating C grows well with 4 of our coplanters
    keys = list(rankings.keys())
    values = list(rankings.values())
    sorted_value_index = np.argsort(values)[::-1]
    neighbours_ranked = {keys[i]: values[i] for i in sorted_value_index}
    return neighbours_ranked


good_neighbours = {specific_plant: find_good_neighbours_level_2(specific_plant) for specific_plant in all_plants}
print(f"good neighbours is {good_neighbours}")


def rank_neighbours(plant, plant_families):
    family = plant_families.values()
    numerals = list(range(len(family)))
    modifier = 0
    rankings = {neighbour: modifier for neighbour in family[1:]}
    print(rankings)
    for numeral in numerals:
        specific_plant = family[numeral]
        print(f"checking {specific_plant} against...")
        numbers = numerals.copy()
        numbers.remove(numeral)
        for number in numbers:
            neighbour = family[number]
            print(neighbour)
            if specific_plant in plant_families[neighbour]:
                print("yup that list contains our guy. what about...")
                modifier = 1
            else:
                print("not good together, let's try...")
                modifier = 0
            print(rankings[neighbour])
            rankings[neighbour] = rankings[neighbour] + modifier
            print(rankings[neighbour])


#all_plants = list(all_plants)
#neighbours = {str(plant): find_good_neighbours(plant, 10) for plant in all_plants}
