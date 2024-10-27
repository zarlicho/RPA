from colorama import Fore,init
from airtable import airtable
import requests as re

class Airtable:
    def __init__(self, baseid, tablename, token):
        self.Baseid = baseid
        self.Tablename = tablename
        self.Token = token
        init()
    
    def Connect(self):
        at = airtable.Airtable(self.Baseid,self.Tablename,self.Token)
        print(Fore.GREEN + "airtable connection success!")
        return at
    
    def GetAllBaseId(self):
        url=f"https://api.airtable.com/v0/meta/bases"
        header = {"Authorization": f"Bearer {self.Token}"}
        response = re.get(url=url,headers=header).json()
        if response["bases"]:
            for x in response["bases"]:
                return x["name"],x["permissionLevel"],x["id"]

    def GetBaseIdByname(self,name):
        names,permissionlevel,id = self.GetAllBaseId()
        if name == names:
            return id
        else:
            return "not found!"

    def GetAllRecords(self):
        con = self.Connect()
        result = [(page) for page in con.get_iter()]
        return [z['filename'] for x in result[0] if x['fields']['Carrier'] == "UHC" for z in x['fields']['File']]
        
    def CreateRecords(self,date,filename,host):
        datas = date.split("-")
        year = datas[0]
        month = datas[1]
        dates = datas[2].split("T")[0]
        con = self.Connect()
        jsondata = {
                        # "Statement":statement,
                        "Commission Statement Date": f"{month}/{dates}/{year}",
                        "Carrier":"UHC",
                        "Format":"XLSX",
                        # "Commission Year":year,
                        # "Commission Month":month,
                        # "Created Date":f"{datetime.date.today().month}/{datetime.date.today().day}/{datetime.date.today().year}",
                        # "Statement Month":{month},
                        # "Statement Year":year,
                        # "Statement Tracker":"UHC",
                    }
        if f"{filename}.xls" in self.GetAllRecords():
            print("file already in airtable!")
        elif f"{filename}.xls" not in self.GetAllRecords():
            jsondata["File"] = [{"url":f"{host}/{filename}.xls"}]
            print(Fore.GREEN + "success upload to airtable!")
            return con.insert(jsondata)

# atb = Airtable(baseid="appI7SJCSBcTKcjUI",tablename="Commission Statements",token="patAxXkcuALCwkpz0.c73c844f87bbe0342881a197463fd32f947c901f55d61eabf86dfd6f4a653b03")

# data = atb.GetAllRecords()
# filename = "UHC_256068_20240409"
# print(data)
# for x in data:
#     if filename in x:
#         print("ada")
#     elif filename not in x:
#         print("file gk ada")