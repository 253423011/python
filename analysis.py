import sys
import json

def analysis(a,b):
    times = 0
    minutes = 0
    with open(a, 'r') as f:
        lines = json.load(f)
        for line in lines:
            if line['user_id'] == int(b):
                times += 1
                minutes += line['minutes']

    return times,minutes

if __name__ == "__main__":
    print(analysis(sys.argv[1],sys.argv[2]))


