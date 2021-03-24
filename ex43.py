class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):       
        pass
    player =  input("Enter player name:   ")

    def play(self):
        print("--------------------------------------------------------")
        print(f"The spaceship has been invaded, it is now time to escape.\nYou meet Gothon standing there.")       
        CentralCorridor.enter(Engine.player)
        pass

class Death(Scene):
    def enter(self):
        print("--------------------------------------------------------")
        print(f"Sorry,{Engine.player},You died.")
        pass

class CentralCorridor(Scene):
    def enter(self):
        print("--------------------------------------------------------")
        print(f"You are now in the central corridor {Engine.player}")
        print("The monster wants to hear a joke. Choose one so that the monster can let you pass.")
        print("1. I ate a clock yesterday, it was very time-consuming. ")
        print("OR")
        print("2. Did you hear about the monkeys who shared an Amazon account? They were Prime mates.")
        corridorDecision = input("> ")
        if corridorDecision == "1":
            print(f"{Engine.player}, that was a funny joke.\nYou get access to the laser weopon room.")
            LaserWeaponArmory.enter(Engine.player)
        else:
            Death.enter(Engine.player)
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        print("--------------------------------------------------------")
        print(f"The Laser Weaopn Armory is packed with weapons.")
        print(f"The neutron bomb will be ideal.")
        print(f"You need to enter the correct passcode to open the lock to get the Neutron bomb./n")
        print(f"Remember You only get 1 chance or you die.")
        passcode = input("> ")
        if len(passcode) < 4 :
            print("Passcode too short!")
            Death.enter(Engine.player)
        elif len(passcode) > 4 :
            print("Why did you have to make it that long.")
            Death.enter(Engine.player)
        elif passcode == "1234" :
            print("That is correct!\nYou take the bomb and head for the bridge.")
            TheBridge.enter(Engine.player)
        else:
            print("Wrong passcode! Good bye!")
            Death.enter(Engine.player)
        pass

class TheBridge(Scene):
    def enter(self):
        print("--------------------------------------------------------")
        print(f"This is the most crucial place. You have to place the bomb and escape.")
        print(f"{Engine.player}, where do you place the bomb? ")
        print("1. At the core computer.")
        print("2. On the head alien.")
        placement = input("> ")
        if placement == "1":
            print("Nice! They did not notice. You got away scot free. Now head to the escape pod.")
            EscapePod.enter(Engine.player)
        else:
            print(f"You must be as dumb as your name, {Engine.player}")


        pass

class EscapePod(Scene):
    def enter(self):
        print(f"Congratulations {Engine.player} you escaped")
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()