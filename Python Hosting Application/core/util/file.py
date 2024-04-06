import os

def getFolder():
    return os.path.dirname(os.path.abspath(__file__))[:-10]

if __name__ == "__main__":
    print(getFolder())
