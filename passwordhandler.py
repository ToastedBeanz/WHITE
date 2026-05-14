from player import Player
import json

BASE36_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def toBase36(num):

    if num == 0:
        return "0"
    
    result = ""

    while num > 0:

        num, remainder = divmod(num, 36)

        result = BASE36_CHARS[remainder] + result
    
    return result

def fromBase36(text):
    return int(text, 36)

def generateSaveCode(player):
    data = json.dumps(player.toDict())
    dataBytes = data.encode("utf-8")

    bigNum = int.from_bytes(dataBytes, "big")

    saveCode = toBase36(bigNum)

    return bigNum

def loadSaveCode(code):
    bigNum = fromBase36(code)

    dataBytes = bigNum.to_bytes((bigNum.bit_length() + 7)//8,"big")
    data = dataBytes.decode("utf-8")
    saveData = json.loads(data)
    player = Player(
        inventory=saveData["inventory"],
        name=saveData["name"],
        hp=saveData["hp"],
        maxhp=saveData["maxhp"],
        mp=saveData["mp"],
        maxmp=saveData["maxmp"],
        atk=saveData["atk"],
        defense=saveData["defense"],
        act=saveData["act"],
        chapt=saveData["chapt"]
    )
    return player

def formatCode(code):

    code = code.upper()

    groups = []

    for g in range(0, len(code), 4):
        groups.append(code[g:g+4])
    
    return "-".join(groups)
