from InquirerPy.base.control import Choice
from storage.airtable import airtables
from helper.decoder import Credential
from config.Config import Configs
from InquirerPy import inquirer
from colorama import Fore,init
from web.Logins import Login
import requests,os

class Commissions:
    def __init__(self):
        self.cred = Credential()
        self.env = Configs()
        init()

    def GetFile(self, docid):
        url = "https://www.uhceservices.com/api/bne/commissions/secure/v1.0/xsldownload"
        json_data = {
            'documentId': docid,
            'pageNumber': '1',
            'columns': [
                'Producer ID',
                'Producer Name',
                'Compensation Period Start Date',
                'Compensation Period End Date',
                'General Compensation Type',
                'Market Segment Name',
                'Sales Type',
                'Writing Agent Id',
                'Writing Agent Name',
                'Customer Id',
                'Customer Name',
                'Coverage Type',
                'Bill Effective Date',
                'Billed Premium',
                'Paid Premium',
                'Billed Subscriber Count',
                'Adjustment Type',
                'Issue State',
                'Method',
                'Rate',
                'Split Percentage',
                'Compensation Type',
                'Business Type',
                'Billed Fee Amount',
                'Customer Paid Fee Amount',
                'Paid Amount',
                'Adjustment Date',
                'Adjustment Description',
                'Adjustment Compensation Type',
                'Adjustment Business Type',
                'Adjustment Amount',
                'Legacy Customer Number',
            ],
        }

        response = requests.post(url, cookies=self.cred.cooki, headers=self.cred.headers, json=json_data)
        if response.status_code == 200:
            save_dir = "document"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            file_path = os.path.join(save_dir, f"{docid}.xls")
            with open(file_path, "wb") as file:
                file.write(response.content)
            return (Fore.GREEN + f"file success to download '{file_path}'")
        else:
            return (Fore.RED + f"failed to download file: {response.status_code} "+"\n"+response.content)

    def GetAllCommissions(self, startDate,endDate,host  ):
        url = "https://www.uhceservices.com/api/bne/commissions/secure/v1.0/listofcommissions"
        json_data = {
            'businessSegmentList': [
                'USB',
                'HPJV',
                'UHCOFCA',
                'UHC',
                'UHONE',
            ],
            'payPeriod': {
                'endDate': endDate,
                'startDate': startDate,
            },
            'providerId': '256068',
            'vuBrokerCode': 'AA5318591',
        }
        response = requests.post(url=url,cookies=self.cred.cooki,headers=self.cred.headers,json=json_data)
        for x in response.json()['searchResult']['searchOutput']['documentlist']:
            for y in x["documentAttribute"]:
                if "u_pay_prd" in y["name"]: #time period
                    print(self.GetFile(x["docID"]))
                    newAirtable = airtables.Airtable(baseid=self.env.baseid,tablename=self.env.tablename,token=self.env.token)
                    newAirtable.CreateRecords(y["value"],x["docID"],host)
                    # print(x["docID"])

class UI:
    def __init__(self):
        self.proceed= False
        self.confirm1= False
        self.confirm2= False
        self.confirm3= False

    def main(self):
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Upload",
                "Login",
                Choice(value=None, name="Exit"),
            ],
            default=None,
        ).execute()

        if action == "Upload":
            com = Commissions()
            date = inquirer.text(
                message="insert date range from date to end date example: 2024-03-19/2024-04-2: ",
                multicolumn_complete=True,
            ).execute()
            host = inquirer.text(
                message="insert host: ",
                multicolumn_complete=True,
            ).execute()
            com.GetAllCommissions(endDate=date.split("/")[1],startDate=date.split("/")[0],host=host)
        elif action == "Login":
            web = Login()
            self.proceed = inquirer.confirm(message="Proceed?", default=True).execute()
            if self.proceed == False:
                self.confirm1 = inquirer.confirm(message="do yo want to proses this action?").execute()
            if self.confirm1:
                self.confirm2 = inquirer.confirm(message="for real?").execute()
            if self.confirm2:
                self.confirm3 = inquirer.confirm(message="for last. confirm this").execute()     
            if self.confirm3:
                quit()
            web.GetLogin()
if __name__ == "__main__":
    os.system('cls')
    myui = UI()
    myui.main()