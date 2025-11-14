# python script to find companion plants in my garden 2023

import friends as f
import enemies as e

friends = f.friends
goodneighbours = f.neighbours
enemies = e.enemies
badneighbours = e.neighbours
plantfamilies = f.plantfamilies

def findmutuals(coplanting_options):
    """
    :param coplanting_options: input list of desired plants
    :return: dict of best-to-worst coplanters for each input plant
    """
    ranked_options = {}
    for plant in coplanting_options: #for plant in desired plants list
        ranked_options[plant] = []   #new dict entry
        for option in coplanting_options[plant]: #that isnt how dicts work
            mutuals = []
            for other_option in coplanting_options[plant]:
                if other_option is not option:
                    if option in coplanting_options[other_option]:
                        mutuals.append(other_option)
            rank = len(mutuals)
            ranked_options[plant].append((option, rank, mutuals))
        ranked_options[plant].sort(key=lambda x: x[1], reverse=True)
    return ranked_options


ranked = findmutuals(friends)
print(ranked)


def mergeDictionary(friends, enemies):
    """
    Note that the second of the inputs ALWAYS takes precedence
    :param friends: nested dict of plants and recommended companion plants
    :param enemies: nested dict of plants and mutually exclusive plants
    :return: combined nested dict with merging at the innermost level
    """
    plants = {**friends, **enemies}
    for key, value in plants.items():
        if key in friends and key in enemies:
            print(f"{key} in both dicts")
            specificfriends = friends[key]
            specificenemies = enemies[key]
            related = {**specificfriends, **specificenemies}
            print(f"all relationships : {related}")
            for id, value in related.items():
                print(f"id is {id}")
                if id in specificfriends and id in specificenemies:
                    print(f"{id} listed as both friend and enemy")
                    plants[key] = enemies[key]
                else:
                    plants[key] = related
            print(f"{key},{plants[key]}")
    print(plants)
    return plants


plants = mergeDictionary(friends, enemies)
print(plants)
#plants = mergeDictionary(plants, goodneighbours)
#print(plants)
#plants = mergeDictionary(plants, badneighbours)
#print(plants)

#divide list into groupings of similar sizes based on what can plant together, prioritising NOT, then friends, then neutrals
#-loop for enemies
#-loop for friends
#-comparison of friends' friends

def findmutualbesties(plants, modifier):
    for specificplant, friends in plants:
        v = []
        print(f"finding best friend for {specificplant}")
        #look up each 'friend''s co-planting options
        for friend, value in friends:
            p = []
            print(f"how good a friend is {friend,value}?")
            checklist = plants[friend]
            print(f"this plant grows well with {checklist}")
            #check co-planting options against the first list of friends
            for item in checklist:
                print(f"checking if {item} grows well with {specificplant}")
                if item in friends:
                    print(f"{item} grows well with {specificplant} and {friend}! mutual found")
                    #give a score if this particular 'friend' has any mutual friends with original plant
                    p.append(1)
                    print(p)
            score = sum(p)
            print(score)
            v.append(score)
            print(v)
        #replace plants[value] with score based on how many shared besties exist
        friend[value] = v
        print(friend)


#several output methods to compare is fine