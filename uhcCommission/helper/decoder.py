import regex as re
import json,os

files = fr"{os.path.abspath(os.path.join(os.getcwd(), 'entity'))}\network_log3.json"
with open(files) as f:
    jsonstr = f.read()
json_str = re.sub(r',\s*([\]}])', r'\1', jsonstr)
data = json.loads(json_str)

class Credential:
    def __init__(self):
        self.headers = {}
        self.cooki = {}
        self.payload = {}
        self.cookies = ""
        self.url = ""
        self.Main()

    def GetHeader(self):
        for x in data:
            if x['method'] == "Network.requestWillBeSent":
                if "https://www.uhceservices.com/api/bne/commissions/secure/v1.0/listofcommissions" in x['params']['request']['url']:
                    self.headers = x['params']['request']['headers']  # Menyimpan headers yang benar

    def GetCookies(self):
        for x in data:
            if x['method'] == "Network.requestWillBeSentExtraInfo":
                try:
                    if x['params']['headers'][":path"] == "/api/bne/commissions/secure/v1.0/listofcommissions":
                        self.cookies = x['params']['headers']['cookie']
                except:
                    pass

    def Format(self):
        for cookie in self.cookies.strip().split('; '):
            key, value = cookie.split('=', 1)
            self.cooki[key] = value

    def Main(self):
        self.GetHeader()
        self.GetCookies()
        self.Format()

