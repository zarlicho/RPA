import os
import json
import regex as re

files = fr"{os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)),'entity')}\network_log3.json"
print(files)
with open(files) as f:
    jsonstr = f.read()
json_str = re.sub(r',\s*([\]}])', r'\1', jsonstr)
data = json.loads(json_str)