from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or  "1" in choice:
        how_much = int(choice)
    else:
        dead("You are greedy bastard")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if "0" in choice or "1" in choice:
            how_much = int(choice)
        else:
            dead("You greedy bastard")
                