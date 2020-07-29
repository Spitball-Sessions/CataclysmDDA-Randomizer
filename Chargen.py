import os, json, random
import collections


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


def job_choice(game_dir):
    """
    Using the open json file, picks the player's starting character and class.

    #May need to create an alias function
    :param game_dir: location of Cataclysm game - throughput
    :return: Tuple: (Character Job, Job Cost)
    """

    classes, class_names = convert_json_to_dict_for_char_class(game_dir)
    list_length = len(classes)
    choice = random.randint(0,list_length-1)
    x = list(classes.items())[choice]  # x is class names & points cost

    y = class_names.get(str(x[0]))  # y is class names in real text

    if type(y) == dict:
        if "male" in y.keys():
            y = y.get("male")

    job_name = y
    job_cost = x[1]

    print("\nYour class is {} which costs {} points".format(job_name,job_cost))

    return job_cost


def assigning_points_to_each_category(chargen_points):
    """
    Splits the remaining chargen points into pools to spent on stats, advantages and skills.

    :param chargen_points: Total usable chargen points from previous function
    :return: a dict showing how many points can be spent on stats, advantages and skills, respectively.
    """

    attribute_names = ("stats", "advantages", "skills")
    att_weights = (15,65,20)

    list = random.choices(attribute_names,weights=att_weights,k=chargen_points)
    attribute_values={"stats":0,"advantages":0,"skills":0}

    print(list)
    for i in range(len(list)):
        if list[i] == attribute_names[0]:
            attribute_values[attribute_names[0]]+=1
        elif list[i] ==attribute_names[1]:
            attribute_values[attribute_names[1]]+=1
        elif list [i] == attribute_names[2]:
            attribute_values[attribute_names[2]]+=1

    return attribute_values


def allocating_points(total_points, currently_used, disadvantages):
    """
    Formula to figure out how many points the player still has left to use for character creation - or if the player has
    used more points than they have left, how many points they still have to make up.

    :param total_points: points derived from starting_character_info() - how many total chargen points the player has
    :param currently_used: points taken from job_choice - how many were used to select the job class
    :return: how many disadvantage points were used and how many character points are left
    """

    leftovers = total_points - currently_used
    max_points = disadvantages + leftovers  # Combines leftover points from job + max points from disabilities to get max usable points
    max_points_list = list(range(1, max_points+1))
    leftovers_list = list(range(1, leftovers))

    '''
    if leftovers < 0:
        print("negative " + str(leftovers))
    elif leftovers == 0:
        print("zero")
    else:
        print("positive " + str(leftovers))
    '''

    usable_points = [x for x in max_points_list if x not in leftovers_list]  # Max usable range - minimum is if no disability points spent.  Max is if 12 are spent.

    '''This section sets up a weighted list to choose numbers - the curve is highest in the middle and then drops and peaks again.
    The 3 variables allow the weighting to be modular, though the for statement needs a bit more work to be truly robust'''

    points_length = len(usable_points)
    weights_values = [None] * points_length

    for i in range(len(usable_points)):
        if i == 0 or i == 1:
            weights_values[i] = 30
        elif i >= 2 and i <= points_length//3:
            weights_values[i] = 10
        elif i != points_length-1:
            weights_values[i] = 5
        else:
            weights_values[i] = 20

    points_left_for_chargen = random.choices(usable_points,
                                             weights=weights_values,
                                             k=1)

    disad_points = points_left_for_chargen[0] - leftovers   # how many points used in disadvantages
    chargen_points = points_left_for_chargen[0]     # how many points remain for chargen - including disadvantages.

    attribute_assignment = assigning_points_to_each_category(chargen_points)
    print(disad_points, attribute_assignment)

    return disad_points, attribute_assignment
