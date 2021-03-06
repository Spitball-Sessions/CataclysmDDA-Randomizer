import sqlite3
import Chargen
import os


def sql_create_db():
    list_create = sqlite3.connect("starting_character_info.db")

    list_create.execute("""CREATE TABLE IF NOT EXISTS CLASS
    (
     JOB_NAME   TEXT    NOT NULL,
     JOB_COST   INT     NOT NULL,
     SKILLS     TEXT    NOT NULL
     );""")

    list_create.execute("""CREATE TABLE IF NOT EXISTS TRAITS
    (
     TRAIT_NAME TEXT    NOT NULL,
     TRAIT_COST INT     NOT NULL
     );""")

    list_create.execute("""CREATE TABLE IF NOT EXISTS SKILLS
    (
     SKILL_NAME TEXT    NOT NULL, 
     SKILL_COST INT     NOT NULL
     );""")


def randomizer_dir():
    '''when this program is finished - file should be placed in Cataclysm game dir'''
    starting_dir = os.getcwd()
    return starting_dir


def cataclysm_dir(): #once program complete, add game_dir as input
    '''Find location of CDDA'''
    cataclysm_dir = input("What is the location of your Cataclysm game file?\n") + (r"\data\json")
    if cataclysm_dir == "\data\json":
        cataclysm_dir = r"T:\Roguelikes\CDDA Game Launcher\Saves\data\json"

    #cataclysm_dir = game_dir + (r"\data\json)

    return cataclysm_dir

def starting_character_info(game_dir):
    '''
    Fins out what the player is using for starting builds - defaults to "6" and "single"

    :return: (Chargen Points(default = 6), Chargen Pool Type (default = "single")
    '''
    pools = "x"
    starting_points = None
    disadvantages = 12

    while not starting_points:
       starting_points = input("How many points are you using to build your character?  Default = 6\n") or 6

    while pools != "single" or "multiple" or "other":
        pools = input("Which type of pool are you using?  Single, multiple or other?  Default = single\n")
        if pools == "":
            pools = "single"
            break
        else:
            pools = pools.lower()
            break

    disadvantages = input("How many disadvantage points do you allow?  Default is 12.") or 12

    starting_points = int(starting_points)


    job_points_cost = Chargen.job_choice(game_dir)
    Chargen.allocating_points(starting_points, job_points_cost, disadvantages)

def core():

    app_dir = randomizer_dir()
    game_dir = cataclysm_dir()

    starting_character_info(game_dir)




    #Select traits (max +12 and -12)
    #   Choose how many negative traits player will have (random 0-12)
    #       Select traits and add points to pool
    #   Select how many positive traits player will have (assigned + earned value)
    #       Guarantee at least 1 more beneficial(?) - this seems hard
    #       Decide whether all points should be used or some pushed forward

    #Select stats
    #   Less change to stats unless larger pool

    #Select skills
    #   Skills cost more as improved.  Weight?
    return


if __name__ == '__main__':
    sql_create_db()
    print("DB Created")

    core()
