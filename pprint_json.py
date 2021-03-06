import sys
import os
import json


def load_data(filepath):
    with open(filepath, 'r') as f:
        jsondata = json.loads(f.read())
    return jsondata

def pretty_print_json(data):
    print (json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print ("Файл не передан")
        sys.exit()
        
    f = sys.argv[1]
    if os.path.exists(f) is False:
        print ("Файл не найден")
        sys.exit()
        
    jsondata = load_data(f)
    pretty_print_json(jsondata)
    