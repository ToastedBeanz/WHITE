currentNode = None

Map = {
    "start": {
        "desc": "You are in a decently small box, made of wood. why? idk. but you need to find a way out. there is a door in front (north) of you. no items.",
        "items": [],
        "exits": {
            "north": "hallway"
        }
    },
    "hallway": {
        "desc": "You are in a long hallway, there are doors on the left and right of you, and the door you came through is behind you. there is a door in front (north) of you. no items.",
        "items": [],
        "exits": {
            "north": "living room",
            "south": "start",
            "east": "kitchen",
            "west": "bedroom"
        }
    },
}

def getnode(node):
    return Map[node]

def setnode(currentnode, cardinalDirection):
    if cardinalDirection in Map[currentnode]["exits"]:
        return Map[currentnode]["exits"][cardinalDirection]
    else:
        print("Invalid direction.")
        return currentnode


    
