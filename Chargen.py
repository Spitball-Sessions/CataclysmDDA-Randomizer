import os
import json
import random



#def classes_data_sort(info):
#    return (info["ident"],info["points"])


def convert_json_to_dict_for_char_class(data_dir):
    class_dict = {}

    os.chdir(data_dir)
    with open("professions.json") as class_json:
        classes = json.load(class_json)

    for i in range(len(classes)):
        if classes[i-1].get("ident") != None:
            class_dict.update({classes[i-1].get("ident"):classes[i-1].get("points")})
#   for i in class_dict.items():
#      print("{}: {}".format(i[0].replace("_"," ").title(),i[1]))

    return class_dict


def class_chargen(game_dir):

    classes = convert_json_to_dict_for_char_class(game_dir)
    list_length = len(classes)
    choice = random.randint(0,list_length-1)
    x = list(classes.items())[choice]

    return x[0],x[1]