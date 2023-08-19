class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.objects = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_object(self, obj):
        self.objects.append(obj)

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def main():
    # Create rooms
    kitchen = Room("Kitchen", "You are in a dimly lit kitchen.")
    living_room = Room("Living Room", "You are in a cozy living room.")
    hallway = Room("Hallway", "You are in a narrow hallway.")
    garden = Room("Garden", "You are in a beautiful garden.")

    # Define room exits
    kitchen.add_exit("north", living_room)
    living_room.add_exit("south", kitchen)
    living_room.add_exit("east", hallway)
    hallway.add_exit("west", living_room)
    hallway.add_exit("north", garden)
    garden.add_exit("south", hallway)

    # Create objects
    knife = Object("Knife", "A sharp kitchen knife.")
    book = Object("Book", "An old dusty book.")

    # Add objects to rooms
    kitchen.add_object(knife)
    living_room.add_object(book)

    current_room = kitchen

    while True:
        print("\n" + current_room.name)
        print(current_room.description)

        if current_room.objects:
            print("You see the following objects:")
            for obj in current_room.objects:
                print("- " + obj.name)

        direction = input("Where do you want to go? (Enter a direction or 'quit'): ")

        if direction == "quit":
            print("Thanks for playing!")
            break
        elif direction in current_room.exits:
            current_room = current_room.exits[direction]
        else:
            print("You can't go that way!")

if __name__ == "__main__":
    main()
