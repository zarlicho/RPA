import requests
import os
import time

class Invoices:
    def __init__(self,policyNumber):
        self.Number = policyNumber
        self.headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Bearer Sfudp3rT9CpksrpW6hbn99oO8rw6YXuh',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Obpp-Token': 'vaT47j+rluviyzv4r3qPCdzMUAiF5Kf997l+MJdme17OJ2EHWyqroyg77uxZc7Ga8tsbTSupUhmSlCSjzLjycnc2LpN22DwEUAie/63wwnZ0KSX7BlgHdXNM/B1a3kOVLnUz',
            'Origin': 'https://obs-prd-ext-hcc.optum.com',
            'Referer': 'https://obs-prd-ext-hcc.optum.com/',
            'Request-Token': '',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-B3-SpanId': '5b4dd6c9da2f0ab4',
            'X-B3-TraceId': '6650b42e729aafa15b4dd6c9da2f0ab4',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

    def GetAllCutomerId(self):
        json_data = {
            'customerId': '',
            'customerName': '',
            'customerPolicyNumber': '',
        }
        response = requests.post(
            'https://obs-prd-ext-hcc-ctc.optum.com/obppcustomersearch/api/customersearch/search/internal',
            headers=self.headers,
            json=json_data,
        )   
        print(response.content)
        for x in response.json():
            yield x["customerId"]

    def GetCustNumber(self, custId):
        json_data = {
            'platformId': 'PRIME',
            'srcCustomerNbr': f'{custId}',
        }

        response = requests.post(
            'https://obs-prd-ext-hcc-ctc.optum.com/obppaccountsummary/api/accountsummary/getaccountsummary',
            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
                'Access-Control-Allow-Origin': '*',
                'Authorization': 'Bearer TfI7pdFaL7bdtPFP0ZnaovTQl08UKSNZ',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Obpp-Token': '9OsNRlxQECwYz5dLQatDCQlNs/QrvC8rysJKal8SpPcu0M3txcGmcitpYOrqZ/zXNGhSUzkId+1thmu5s5LmlLCaNUr0J6IUs51+9wnajn/8CY4y+EBEv39YB24xN0VnAckU',
                'Origin': 'https://obs-prd-ext-hcc.optum.com',
                'Referer': 'https://obs-prd-ext-hcc.optum.com/',
                'Request-Token': 'C1AfCBEGCQsCHyYAUkhNNCI7IiFSXk0XAhEsEQMGAAkVACEGAlBVRkBBOVNAQVlGDQ==',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'X-B3-SpanId': '3dc961b0009ff574',
                'X-B3-TraceId': '6650c72b641fe0803dc961b0009ff574',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            },
            json=json_data,
        )
        print(response.status_code)
        print(response.content)
        return response.json()["sourceCustomerNumber"], response.json()["customerName"]

    def GetInvoices(self,custId):
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Bearer hYjeFP7842KWgTQqmhHa7Sl3hp61T5ud',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Obpp-Token': 'C42gyjHxLnzLqWPKNQMeXu2C0xPePGSznK/3DHoXxIjS8ShEUJGz5Wccpe/Ywj16DTYxwdGkbctvxnizbQkDzGFx8Y0ig+5Ec6AUhRyvjP7Uey+wAnnMyW4bkwVFSEj7la9O',
            'Origin': 'https://obs-prd-ext-hcc.optum.com',
            'Referer': 'https://obs-prd-ext-hcc.optum.com/',
            'Request-Token': 'C1AGCgYdBgcVJhYUFVBVRj8iKipSXk0UHBMbAh8AAi0UUFVGICAmKTVQQ0YDAAwnBQEbCx0XHS0UUFVGQEM+VEhEW0YN',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-B3-SpanId': 'cfc76d6d65090ed4',
            'X-B3-TraceId': '6650d0d5fc9935afcfc76d6d65090ed4',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'invoiceType': 'OPEN',
            'platformId': 'PRIME',
            'srcCustomerId': '1607124',
        }

        response = requests.post(
            'https://obs-prd-ext-hcc-elr.optum.com/obppinvoicelisting/api/invoice/getopeninvoicelist',
            headers=headers,
            json=json_data,
        )
        print(response.content)
        # print(response.json())

        for x in response.json()["openInvoiceListing"]:
            yield x["invoiceNumber"]

    def GetFile(self, invNumber,custNumber,custName):
        json_data = {
            'lineItemTypeCode': '',
            'benefitGroupId': '',
            'cprocInvcId': '',
            'invoiceStatementNumber': f'{invNumber}',
            'populationId': '',
            'benefitStatusId': '',
            'planNumber': '',
            'policyName': '',
            'policyNumber': '',
            'presentmentType': '',
            'sequenceNumber': '',
            'srcSystemCode': '110',
            'tierCode': '',
            'customerNumber': f'{custNumber}',
            'customerName': f'{custName}',
        }

        response = requests.post(
            'https://obs-prd-ext-hcc-elr.optum.com/obppeligibilityinvoicedetail/api/eligibility/invoice/brms/getdetails/getcsv',
            headers=self.headers,
            json=json_data,
        )
        if response.status_code == 200:
            save_dir = "document"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            file_path = os.path.join(save_dir,f'invoice_{invNumber}.csv')
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"file success to download '{file_path}'")
        else:
            print(f"failed to download file: {response.status_code} "+"\n"+response.content)

        print(response.content)

    def Download(self):
        for x in self.GetAllCutomerId():
            for invoice in self.GetInvoices(x):
                custNumber,custName = self.GetCustNumber(x)
                self.GetFile(invNumber=invoice,custNumber=custNumber,custName=custName)
                time.sleep(4)
invc = Invoices("12")
invc.Download()
# invc.GetInvoices("05Y9691")
# invc.GetInvoices("01Q0864")
# invc.GetCustNumber("01Q0864")
# invc.GetCustNumber("03V7036")
# for x in invc.GetAllCutomerId():
#     print(x)