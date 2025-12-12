import os
os.chdir(os.path.dirname(__file__))

import json

with open("gugugaga.json", "r") as f:
    data = json.load(f)

with open("nguakak.json", "w") as f:
    json.dump(data, f)

































