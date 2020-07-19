import sqlite3
import Chargen
import os

def sql_create_db():
    list_create = sqlite3.connect("chargen_info.db")

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
    starting_dir = os.getcwd()
    return starting_dir


def cataclysm_dir():
    cataclysm_dir = input("What is the location of your Cataclysm game file?\n") + (r"\data\json")
    if cataclysm_dir == "\data\json":
        cataclysm_dir = r"T:\Roguelikes\CDDA Game Launcher\Saves\data\json"
    return cataclysm_dir

def chargen_info():
    pools = "x"
    chargen_points = None
    while not chargen_points:
       chargen_points = input("How many points are you using to build your character?  Default = 6\n") or 6

    while pools != "single" or "multiple" or "other":
        pools = input("Which type of pool are you using?  Single, multiple or other?  Default = single\n")
        if pools == "":
            pools = "single"
            break
        else:
            pools = pools.lower()
            break

    chargen_points = int(chargen_points)

    return chargen_points,pools
def core():


    app_dir = randomizer_dir()
    game_dir = cataclysm_dir()

    chargen_points, pool = chargen_info()

    # Select starting scenario (bias towards default)

    job_title, job_cost = Chargen.class_chargen(game_dir)
    print("\nYour class is {} which costs {} points".format(job_title.replace("_"," ").title(),job_cost))

    #Divide remaining points among traits, stats and skills

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
