
class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.room_number = 0


# Create main function
def main():
    # Create room list
    room_list = []
    room = Room("You are in a courtyard.\nT"
                "here are paths to the east and west and a building to the north.", 5, 3, None, 2)
    room_list.append(room)
    room = Room("You arrived at a clearing in the forest,"
                " there is an abandoned tent.", 2, None, None, None)
    room_list.append(room)
    room = Room("You are at a fork in the road.\n"
                "To the south is the forest and to the north is a shop.", 4, 0, 1, None)
    room_list.append(room)
    room = Room("You are at a fork in the road, yet cannot go south."
                " To the north is a lake.", 6, None, None, 0)
    room_list.append(room)
    room = Room("You arrived at the shop.\n"
                "The shopkeeper refuses to talk without having money.", 7, None, 2, None)
    room_list.append(room)
    room = Room("You approach the building but cannot enter.\n"
                "There seems to be some kind of keyhole.", None, None, 0, None)
    room_list.append(room)
    room = Room("You arrived at the lake.\n"
                "There is an abandoned boat just out of reach in the water.", None, None, 3, None)
    room_list.append(room)
    room = Room("You have gotten into the shop!"
                "The shopkeeper has wares for sale.", None, None, 2, None)

    # Create an item list
    item_list = []
    money = Item()
    money.name = "Money"
    money.description = "You find a pile of cash on the ground."
    money.room_number = 1
    item_list.append(money)
    hook = Item()
    hook.name = "Hook"
    hook.description = "There is a hook for sale on the shelves of the shop."
    hook.room_number = 7
    item_list.append(hook)
    key = Item()
    key.name = "Key"
    key.description = "There is a key lying in the boat, maybe it opens a door somewhere."
    key.room_number = 6
    item_list.append(key)

    # Give variables
    current_room = 0
    done = False

    # Create while function asking for input
    while not done:
        print()
        print(room_list[current_room].description)
        for item in item_list:
            if item.room_number == current_room:
                print(item.description)
        user_choice = input("What do you choose to do?")


        #  # Shop special event
        #  if current_room == 4 and money == 1:
        #      print("The shopkeeper notices your money and is glad to do business.\nAll he has in stock is a hook.")
        #      if user_choice.lower() == "buy" or user_choice.lower() == "buy hook":
        #          print("You bought the hook!")
        #          hook = 1
        #
        #  # Lake special event
        #  elif current_room == 6 and hook == 1:
        #      print("You see the abandoned boat sitting just out of reach. You feel as if you can reach it somehow.")
        #      if user_choice.lower() == "hook" or user_choice.lower() == "use hook":
        #          print("You used the hook to reach the boat! Great idea! Inside the boat you find a key of sorts.")
        #          if user_choice == "take" or user_choice.lower() == "take key":
        #              print("You now have an odd key!")
        #              key = 1
        #
        #  # Building special event
        #  elif current_room == 5 and key == 1:
        #      print("All you see on this building is a weird keyhole.")
        #      if user_choice.lower() == "unlock" or user_choice.lower() == "use key" or user_choice.lower() == "unlock door":
        #          print("Congratulations! You enter a building full of puppies and ice cream.\nYou win!")
        #          done = True

        # Function for north input
        if user_choice.lower() == "n" or user_choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        # Function for east input
        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way?")
            else:
                current_room = next_room

        # Function for south input
        elif user_choice.lower() == "s" or user_choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way?")
            else:
                current_room = next_room

        # Function for west input
        elif user_choice.lower() == "w" or user_choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way?")

            else:
                current_room = next_room

        # Function for quit input
        elif user_choice.lower() == "q" or user_choice.lower() == "quit":
            print()
            print("You have given up, loser.")
            done = True

        # Function ensuring players use valid code
        else:
            print()
            print("I don't understand. Please choose a valid choice.")


main()
