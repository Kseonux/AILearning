
# Javascript Object Notation

import json

json_string = '''
    {
    "data1" : ["name": "Founder", "age": 18],
    "data2" : "{"scores": [90, 85, 92]",
    "data3" : ["profile": {"height": 173, "goal": 185}]
    }
'''

data = json.loads(json_string)
print(data)














































