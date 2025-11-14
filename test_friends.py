# FRIENDS module for TESTING 10/4/24

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

#grouping and data structuring - will be from user input file later, with UPPER() and fuzzy checks
all_plants = list(set(list(
    cabbage + aubergine + celeriac + beetroot + peppers + mustard + melon + loofah + courgette + tomato + carrot)))
plant_families = {"Cabbage": cabbage, "Aubergine": aubergine, "Celeriac": celeriac, "Beetroot": beetroot,
                  "Peppers": peppers, "Mustard": mustard, "Melon": melon, "Loofah": loofah, "Courgette": courgette,
                  "Tomato": tomato, "Carrot": carrot}

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


def test_find_friends():
    assert find_friends("Garlic", plant_families) == ['Garlic', 'Aubergine', 'Carrot', 'Peppers', 'Cabbage', 'Melon']
    assert find_friends("Tomato", plant_families) == ['Tomato', 'Carrot', 'Peppers', 'Potatoes', 'Celeriac']


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


def test_find_good_neighbours_level_1():
    assert find_good_neighbours_level_1("Celeriac") == {'Black bean': 0, 'Runner beans': 0, 'Tomato': 0, 'Cabbage': 0, 'Leek': 0}


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


def test_find_good_neighbours_level_2():
    assert find_good_neighbours_level_2("Celeriac") == {}

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
