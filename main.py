import sys
from MusicNow import Manager
import json
import MNConst

# Get incoming data and parse to json
def __read_input():
    result = ''
    if len(sys.argv < 2):
        return result
    try:
        result = json.loads(sys.argv[1])
    except ValueError:
        pass
    return result
    
def main():
    # Only allow to run if it is main app
    if __name__ != "__main__":
        return
    
    # Get expected JSON data
    json = __read_input()
    if json == '':
        return
    
    