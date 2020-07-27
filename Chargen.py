import os
import json
import random



#def classes_data_sort(info):
#    return (info["ident"],info["points"])


def convert_json_to_dict_for_char_class(data_dir):
    '''
    Takes the open json file and converts it into a dict
    :param data_dir: Location of Cataclysm game
    :return: usable dictionary of character jobs and point cost, usable dict of internal names for player jobs and correct names
    '''

    class_dict = {}
    class_name_dict = {}


    os.chdir(data_dir)
    with open("professions.json") as class_json:
        classes = json.load(class_json)

    for i in range(len(classes)):
        if classes[i-1].get("ident") != None:
            class_dict.update({classes[i-1].get("ident"):classes[i-1].get("points")})

    for i in range(len(classes)):
        if classes[i-1].get("ident") != None:
            class_name_dict.update({classes[i-1].get("ident"):classes[i-1].get("name")})

    # print(class_name_dict)

    return class_dict, class_name_dict


def class_selection(game_dir):
    '''
    Using the open json file, picks the player's starting character and class.

    #May need to create an alias function
    :param game_dir: location of Cataclysm game - throughput
    :return: Tuple: (Character Job, Job Cost)
    '''

    classes, class_names = convert_json_to_dict_for_char_class(game_dir)
    list_length = len(classes)
    choice = random.randint(0,list_length-1)
    x = list(classes.items())[choice]
    # print(x)
    y = class_names.get(str(x[0]))
    # print(y)

    print("\nYour class is {} which costs {} points".format(y,x[1]))

    return y,x[1]


def character_points_left(total_points,currently_used):
    '''
    Formula to figure out how many points the player still has left to use for character creation - or if the player has
    used more points than they have left, how many points they still have to make up.

    :param total_points: points derived from starting_character_info() - how many total chargen points the player has
    :param currently_used: points taken from class_selection - how many were used to select the job class
    :return: how many points are left over.
    '''

    leftovers = total_points - currently_used
    '''
    if X < 0:
        print("negative " + str(X))
    elif X == 0:
        print("zero")
    else:
        print("positive " + str(X))
        '''

    max_points = 12 + leftovers  #Combines leftover points from job + max points from disabilities to get max usable points
    print(max_points)
    max_points = list(range((max_points)))
    leftovers = list(range(leftovers))

    usable_points = [x for x in max_points if x not in leftovers] #Max usable range - minimum is if no disability points spent.  Max is if 12 are spent.

    '''This section sets up a weighted list to choose numbers - the curve is highest in the middle and then drops and peaks again.
    The 3 variables allow the weighting to be modular, though the for statement needs a bit more work to be truly robust'''

    points_length = len(usable_points)
    middle = (points_length//2)
    weights_values = [None] * len(usable_points)

    for i in range(len((usable_points))):
        if i == middle:
            weights_values[i-1] = 30
        elif i == middle+1 or i == middle-1:
            weights_values[i-1] = 10
        elif i == middle+2 or i == middle-2:
            weights_values[i-1] = 20
        else:
            weights_values[i-1] = 5

    print(weights_values)


    points_left_for_chargen = random.choices(usable_points,
                                             weights=weights_values,
                                             k=1)

    print(points_left_for_chargen[0])