# helper functions
#from fuzzywuzzy import fuzz
import random
from difflib import SequenceMatcher

def choose_a_bean(examplelist):
    """
    NEED TO ADD OPTION FOR NUMBER OF VARIETIES PERMITTED TO BE SET BY USER AT LATER STAGE
    condenses varieties of the same/similar plant into 1, to avoid a bed full of beans
    :param examplelist: input list of certain plants which could go together
    :return: list with duplicate 'types' removed
    """
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
