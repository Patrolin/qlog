from os import mkdir as _mkdir

def mkdir(path: str):
    try:
        _mkdir(path)
    except FileExistsError:
        pass
