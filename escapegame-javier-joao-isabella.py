# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "blue door",
    "type": "door",
}

door_b = {
    "name": "pink door",
    "type": "door",
}

door_c = {
    "name": "red door",
    "type": "door",
}

door_d = {
    "name": "green door",
    "type": "door",
}

scissors = {
    "name": "pair of scissors",
    "type": "key",
}

stag_head = {
    "name": "stag head",
    "type": "furniture",
}

key_a = {
    "name": "key for blue door",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for pink door",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for red door",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for green door",
    "type": "key",
    "target": door_d,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "blue bedroom",
    "type": "room",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

lamp = {
    "name": "lamp",
    "type": "furniture",
}

fireplace = {
    "name": "fireplace",
    "type": "furniture",
}

wardrobe = {
    "name": "wardrobe",
    "type": "furniture",
}

fridge = {
    "name": "fridge",
    "type": "furniture",
}

dog = {
    "name": "dog",
    "type": "furniture",
}

car = {
    "name": "car",
    "type": "door",
}

bedroom_2 = {
    "name": "pink bedroom",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

chicken_wings = {
    "name": "chicken wings",
    "type": "key",
}

brush = {
    "name": "brush",
    "type": "key",
}

cleaning_stuff = {
    "name": "cleaning stuff",
    "type": "furniture",
}

car_key = {
    "name": "key for car",
    "type": "key",
    "target": car,
}

painting = {
    "name": "painting",
    "type": "furniture",
}

frame = {
    "name": "frame",
    "type": "key",
}

cot = {
    "name": "cot",
    "type": "furniture",
}

lighter = {
    "name": "lighter",
    "type": "key",
}

candle = {
    "name": "candle",
    "type": "key",
}

chest_of_drawers = {
    "name": "chest of drawers",
    "type": "furniture",
}

locker_key = {
    "name": "key for locker",
    "type": "key",
}

front_yard = {
    "name": "front yard",
    "type": "room",
}

notebook = {
    "name": "notebook",
    "type": "furniture",
}

outside = {
  "name": "outside"
}

# define which items/rooms are related

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, front_yard, outside]

all_doors = [door_a, door_b, door_c, door_d, car]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a, fireplace, cleaning_stuff, stag_head],
    "blue bedroom": [door_a, door_b, door_c, queen_bed, wardrobe, lamp],
    "pink bedroom": [door_b, painting, cot, notebook, chest_of_drawers],
    "chest of drawers": [candle],
    "candle": [key_d],
    "notebook": [key_c],
    "cot": [lighter],
    "painting": [frame],
    "cleaning stuff": [brush],
    "queen bed": [chicken_wings],
    "lamp": [key_d],
    "living room": [door_c, door_d, fridge, dining_table, lighter],
    "dining table": [chicken_wings],
    "piano": [scissors],
    "fireplace": [locker_key],
    "wardrobe": [key_b],
    "couch": [key_a],
    "fridge": [car_key],
    "front yard": [car, dog, door_d],
    "car": [outside],
    "blue door": [game_room, bedroom_1],
    "pink door": [bedroom_1, bedroom_2],
    "red door": [bedroom_1, living_room],
    "green door": [living_room, front_yard],
}

#define the global variables.
dog_interaction = False
frame_in_fireplace = False
fireplace_on = False
bat_interaction = False
fridge_locker = False
fridge_unlocked = False



# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.")
    print("You don't remember why you are here and what had happened before.")
    print("You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    global fireplace_on, dog_interaction, frame_in_fireplace, bat_interaction, fridge_locker, fridge_unlocked
    game_state["current_room"] = room

    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
        return

    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore', 'inventory' or try actions with objects in the room? Type 'tutorial' for further explanation.").strip().lower()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "inventory":
            check_inventory()
            play_room(room)
        elif intended_action == "tutorial":
            tutorial()
            play_room(room)

        elif "couch" in intended_action and "scissors" in intended_action:
            couch_in_room = any(item["name"] == "couch" for item in object_relations[room["name"]])
            if not couch_in_room:
                print("There's no couch here in this room.")
                play_room(room)
            elif not any(item["name"] == "pair of scissors" for item in game_state["keys_collected"]):
                print("You have no pair of scissors in your inventory")
                play_room(room)
            else:
                item_name = "couch"
                game_state["keys_collected"].remove(scissors)
                examine_item(item_name)

        elif "brush" in intended_action and "wardrobe" in intended_action:
            wardrobe_in_room = any(item["name"] == "wardrobe" for item in object_relations[room["name"]])
            if not wardrobe_in_room:
                print("There's no wardrobe here in this room.")
                play_room(room)
            elif not any(item["name"] == "brush" for item in game_state["keys_collected"]):
                print("You have no brush in your inventory")
                play_room(room)
            else:
                bat_interaction = True
                print("Great, the bat flew away. I can now investigate what is inside the wardrobe!")
                game_state["keys_collected"].remove(brush)
                play_room(room)

        elif "wardrobe" in intended_action:
            wardrobe_in_room = any(item["name"] == "wardrobe" for item in object_relations[room["name"]])
            if not wardrobe_in_room:
                print("There's no wardrobe here in this room.")
                play_room(room)
            else:
                if bat_interaction:
                      enter_code = input("There's a safe here. It asks for a 5 digit code.   ").strip().lower()
                      if enter_code == "94936":
                          item_name = "wardrobe"
                          print("Wow, genius! We have the key. But no money, unfortunatelly.")
                          examine_item(item_name)
                      else:
                          print("This is not the right code")
                          play_room(room)
                else:
                      print("There`s a bat inside it. I will not touch there")
                      play_room(room)

        elif "couch" in intended_action:
            print("It doesn't feel comfy. There's something odd inside the cushion.")
            play_room(room)

        elif "piano" in intended_action:
            piano_in_room = any(item["name"] == "piano" for item in object_relations[room["name"]])
            if not piano_in_room:
                print("There's no piano here in this room.")
                play_room(room)
            else:
                play_piano = input("Would you like playing some music? yes or no? ").strip().lower()
                if play_piano == "yes":
                    item_name = "piano"
                    print("Oops! Something felt from the inside.")
                    examine_item(item_name)
                else:
                    print("I must find the exit, I don't have the time for a concert now!")
                    play_room(room)

        elif "stag" in intended_action or "head" in intended_action:
            stag_in_room = any(item["name"] == "stag head" for item in object_relations[room["name"]])
            if not stag_in_room:
                print("I saw a stag head in the game room! It was nice!")
                play_room(room)
            else:
                print("It's a beautiful animal, indeed!")
                play_room(room)


        elif "lamp" in intended_action:
            lamp_in_room = any(item["name"] == "lamp" for item in object_relations[room["name"]])
            if not lamp_in_room:
                print("There's no lamp here in this room.")
                play_room(room)
            else:
                turn_on_lamp = input("Would you like turning the lamp on? yes or no? ").strip().lower()
                if turn_on_lamp == "yes":
                    print("Strange. The light projects the numbers 3, 7 and 6 on the ceiling. What could it mean?")
                    play_room(room)
                else:
                    print("Better saving electricity. Let's continue exploring then!")
                    play_room(room)


        elif "bed" in intended_action:
            bed_in_room = any(item["name"] == "queen bed" for item in object_relations[room["name"]])
            if not bed_in_room:
                print("There's no bed here in this room.")
                play_room(room)
            else:
                print("Theres a note here, saying ^2. What does it mean? ")
                play_room(room)


        elif "chicken" in intended_action and "dog" in intended_action:
                dog_in_room = any(item["name"] == "dog" for item in object_relations[room["name"]])
                if not dog_in_room:
                    print("I can hear a dog outside. But in this room there's no dog!")
                    play_room(room)
                elif not any(item["name"] == "chicken wings" for item in game_state["keys_collected"]):
                    print("You brough no chicken wings with you.")
                    play_room(room)
                else:
                    dog_interaction = True
                    print("These chicken wings really did the trick. The dog absolutely loved it! I can reach the car now!")
                    game_state["keys_collected"].remove(chicken_wings)
                    play_room(room)


        elif "lighter" in intended_action and "fireplace" in intended_action:
            fireplace_in_room = any(item["name"] == "fireplace" for item in object_relations[room["name"]])
            if not fireplace_in_room:
                print("There's no fireplace here in this room.")
                play_room(room)
            elif not any(item["name"] == "lighter" for item in game_state["keys_collected"]):
                print("You have no lighter in your inventory.")
                play_room(room)
            else:
                if not frame_in_fireplace:
                    print("I can't set fire using a lighter with the logs!")
                    play_room(room)
                else:
                    fireplace_on = True
                    item_name = "fireplace"
                    print("This frame is extremely inflammable. It's melting the wall. Oh, a key felt from it!")
                    game_state["keys_collected"].remove(lighter)
                    examine_item(item_name)


        elif "candle" in intended_action and "fireplace" in intended_action:
            fireplace_in_room = any(item["name"] == "fireplace" for item in object_relations[room["name"]])
            if not fireplace_in_room:
                print("There's no fireplace here in this room.")
            elif not any(item["name"] == "candle" for item in game_state["keys_collected"]):
                print("You have no candle in your inventory.")
                play_room(room)
            else:
                if not fridge_locker:
                    print("I can't see much of a use with an unlit candle!")
                    play_room(room)
                else:
                    item_name = "candle"
                    print("This strong fire is melting the candle wax! There's something inside it!")
                    object_relations["game room"].append(candle)
                    game_state["keys_collected"].remove(candle)
                    examine_item(item_name)

        elif "cot" in intended_action:
            cot_in_room = any(item["name"] == "cot" for item in object_relations[room["name"]])
            if not cot_in_room:
                print("There's no cot here in this room.")
                play_room(room)
            else:
                print("There's a lighter under the sheets!")
                item_name = "cot"
                examine_item(item_name)

        elif "drawer" in intended_action or "drawers" in intended_action:
            drawer_in_room = any(item["name"] == "chest of drawers" for item in object_relations[room["name"]])
            if not drawer_in_room:
                print("There's no drawer here in this room.")
            else:
                item_name = "chest of drawers"
                examine_item(item_name)

        elif "blue door" in intended_action:
            door_in_room = any(item["name"] == "blue door" for item in object_relations[room["name"]])
            if not door_in_room:
                print("There's no door here in this room.")
                play_room(room)
            else:
                item_name = "blue door"
                examine_item(item_name)

        elif "red door" in intended_action:
            door_in_room = any(item["name"] == "red door" for item in object_relations[room["name"]])
            if not door_in_room:
                print("There's no door here in this room.")
                play_room(room)
            else:
                item_name = "red door"
                examine_item(item_name)

        elif "green door" in intended_action:
            door_in_room = any(item["name"] == "green door" for item in object_relations[room["name"]])
            if not door_in_room:
                print("There's no door here in this room.")
                play_room(room)
            else:
                item_name = "green door"
                examine_item(item_name)

        elif "pink door" in intended_action:
            door_in_room = any(item["name"] == "pink door" for item in object_relations[room["name"]])
            if not door_in_room:
                print("There's no door here in this room.")
                play_room(room)
            else:
                item_name = "pink door"
                examine_item(item_name)



        elif "notebook" in intended_action or "note" in intended_action:
            notebook_in_room = any(item["name"] == "notebook" for item in object_relations[room["name"]])
            if not notebook_in_room:
                print("There's no notebook here in this room.")
                play_room(room)
            else:
                enter_password = input("It says 'The Romans would love it, but don't square please'. It asks for a password. Could you guess is? ").strip().lower()
                if enter_password == "iiiviivi":
                    print("Presto! We opened it!")
                    item_name = "notebook"
                    examine_item(item_name)
                else:
                    print("This is not the right password")
                    play_room(room)




        elif "frame" in intended_action and "fireplace" in intended_action:
            fireplace_in_room = any(item["name"] == "fireplace" for item in object_relations[room["name"]])
            if not fireplace_in_room:
                print("There's no fireplace here in this room.")
                play_room(room)
            elif not any(item["name"] == "frame" for item in game_state["keys_collected"]):
                print("You have no frame in your inventory.")
                play_room(room)
            else:
                frame_in_fireplace = True
                fridge_locker = True
                print("I think I can burn that. This painting is gross!")
                game_state["keys_collected"].remove(frame)
                play_room(room)


        elif "fridge" in intended_action:
              fridge_in_room = any(item["name"] == "fridge" for item in object_relations[room["name"]])
              if not fridge_in_room:
                    print("There's no fridge here in this room.")
                    play_room(room)
              else:
                  if fridge_unlocked:
                    examine_item(item_name)
                  elif fridge_locker:
                    print("Oh my god, there are car keys inside! Which type of person does that?")
                    game_state["keys_collected"].remove(locker_key)
                    fridge_unlocked = True
                    item_name = "fridge"
                    examine_item(item_name)
                  else:
                        print("It has a locker. I can`t open it!")
                        play_room(room)


        elif "fireplace" in intended_action:
            fireplace_in_room = any(item["name"] == "fireplace" for item in object_relations[room["name"]])
            if not fireplace_in_room:
                print("There's no fireplace here in this room.")
                play_room(room)
            else:
                if not fireplace_on:
                    print("It's a fireplace with logs in. It would be nice to set some fire in!")
                    play_room(room)
                else:
                    print("It's very warm now. However, I cannot stay any longer. I must find the exit.")
                    play_room(room)


        elif "painting" in intended_action:
            painting_in_room = any(item["name"] == "painting" for item in object_relations[room["name"]])
            if not painting_in_room:
                print("There's no painting here in this room.")
                play_room(room)
            else:
                touch_paiting = input("Would you touch the painting and feel its texture? yes or no? ").strip().lower()
                if touch_paiting == "yes":
                    item_name = "painting"
                    print("Argh! It's a gross painting. I have to get rid of this horrendous frame.")
                    examine_item(item_name)
                else:
                    print("I don't really like this painting! I'd prefer touching something else.")
                    play_room(room)

        elif "dog" in intended_action:
                dog_in_room = any(item["name"] == "dog" for item in object_relations[room["name"]])
                if not dog_in_room:
                      print("I can hear a dog outside. But in this room there's no dog!")
                      play_room(room)
                else:
                    if dog_interaction:
                      print("The dog is now happy with his chicken.")
                      play_room(room)
                    else:
                      print("I cannot pass if this angry dog is there.")
                      play_room(room)

        elif "cleaning" in intended_action:
            cleaning_in_room = any(item["name"] == "cleaning stuff" for item in object_relations[room["name"]])
            if not cleaning_in_room:
                print("There are no cleaning stuff here!")
                play_room(room)
            else:
                item_name = "cleaning stuff"
                print("This brush might be useful")
                examine_item(item_name)


        elif "car" in intended_action:
            car_in_room = any(item["name"] == "car" for item in object_relations[room["name"]])
            if not car_in_room:
                print("There's no car here in this room.")
                play_room(room)
            else:
                if not dog_interaction:
                  print("I cannot access the car with this dog on my way!")
                  play_room(room)
                else:
                    item_name = "car"
                    print("This car can be my exit from this place.")
                    examine_item(item_name)

        elif "dining" in intended_action or "table" in intended_action:
              dining_in_room = any(item["name"] == "dining table" for item in object_relations[room["name"]])
              if not dining_in_room:
                  print("There's no dining table here in this room.")
                  play_room(room)
              else:
                  try_chicken = input("There are some chicken wings here. Do you want to try? ")
                  if try_chicken == "yes":
                      print("They're cold! Thats disgusting!")
                      play_room(room)
                  else:
                        print("I will not eat that. But I can save for later!")
                        item_name = "dining table"
                        examine_item(item_name)


        elif "door" in intended_action:
            check_door = input("which door do you want to examine?" ).strip().lower()
            if "blue" in check_door:
                door_in_room = any(item["name"] == "blue door" for item in object_relations[room["name"]])
                if door_in_room:
                    item_name = "blue door"
                    examine_item(item_name)

            elif "pink" in check_door:
                door_in_room = any(item["name"] == "pink door" for item in object_relations[room["name"]])
                if door_in_room:
                    item_name = "pink door"
                    examine_item(item_name)
                else:
                    print("I cannot see any door with this particular colour!")
                    play_room(room)
            elif "red" in check_door:
                door_in_room = any(item["name"] == "red door" for item in object_relations[room["name"]])
                if door_in_room:
                    item_name = "red door"
                    examine_item(item_name)
                else:
                    print("I cannot see any door with this particular colour!")
                    play_room(room)
            elif "green" in check_door:
                door_in_room = any(item["name"] == "green door" for item in object_relations[room["name"]])
                if door_in_room:
                    item_name = "green door"
                    examine_item(item_name)
                else:
                    print("I cannot see any door with this particular colour!")
                    play_room(room)
            elif "car" in check_door:
                door_in_room = any(item["name"] == "car" for item in object_relations[room["name"]])
                if door_in_room:
                    item_name = "car"
                    examine_item(item_name)
                else:
                    print("I cannot see any car here!")
                    play_room(room)
            else:
                print("I cannot see any door with this particular colour!")
                play_room(room)

        else:
            print("Not sure what you mean. You can explore, check inventory or interact with the room's objects.")
            play_room(room)

        linebreak()

def check_inventory():
    list_of_keys = game_state['keys_collected']
    if len(list_of_keys) == 0:
        print("You check your pockets. They don't seem to have left you with any of your belongings.")
    else:
        print("You check your pockets, you find:" )
        for key in list_of_keys:
            print(key['name'])
    linebreak()


def tutorial():
    print("Welcome to the escape game. You can type 'explore' to see all the objects in the room, or 'inventory' to check all the objects in your pockets,")
    print("or you can try actions with the objects and assemble them: e.g 'Use scissors to cut the couch!'.")

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    explore_message = "You explore the room. This is " + room["name"] + ". You find "
    for item in object_relations[room["name"]]:
      explore_message += str(item["name"]) + ", "
    explore_message = explore_message[:-2]+"."
    print(explore_message)
    linebreak()

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the second room.
    """
    connected_rooms = object_relations[door["name"]]

    if connected_rooms[0] == current_room:
      return connected_rooms[1]
    else:
      return connected_rooms[0]


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if "target" in key and key["target"] == item:
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break
            linebreak()

    if(output is None):
        print("The item you requested is not found in the current room.")
        linebreak()

    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        linebreak()
        game_state["current_room"] = next_room
    play_room(game_state["current_room"])


game_state = INIT_GAME_STATE.copy()

start_game()