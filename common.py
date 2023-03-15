from os import mkdir as _mkdir

def mkdir(path: str):
    try:
        _mkdir(path)
    except FileExistsError:
        pass

NEXTID_PATH = "nextId.txt"

def getNextId() -> int:
    with open(NEXTID_PATH, "a+") as f:
        pass
    with open(NEXTID_PATH, "r") as f:
        r = f.read()
        print("ayaya", r)
        id = int(r or "0")
    with open(NEXTID_PATH, "w") as f:
        f.write(str(id + 1))
    return id
