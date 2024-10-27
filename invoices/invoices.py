import requests
import os

class Invoices:
    def __init__(self,policyNumber):
        self.Number = policyNumber
        self.headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Bearer ZNPGASY5D6ZzI06HLfmIJryMA2nXrAer',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Obpp-Token': 'pRYt9OOnhBuBk3AwEwOTFT6Yj5W0eL2Ac2sGdx7kBPCIuyDlrlSiM1X3m/QSMmT8cGRgWj0YDHTNpS+HdF5FmuGi62954dwNGcKFPifyeFhpqdFYg2Cxqw7IV8xWbsIt0HlG',
            'Origin': 'https://obs-prd-ext-hcc.optum.com',
            'Referer': 'https://obs-prd-ext-hcc.optum.com/',
            'Request-Token': 'C1AGCgYdBgcVJhYUFVBVRj8iKipSXk0UHBMbAh8AAi0UUFVGICAmKTVQQ0YDAAwnBQEbCx0XHS0UUFVGQEM+VEhEW0YN',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-B3-SpanId': '63ae611c0f12fbe6',
            'X-B3-TraceId': '664b47a50329585563ae611c0f12fbe6',
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
            'https://obs-prd-ext-hcc-elr.optum.com/obppcustomersearch/api/customersearch/search/internal',
            headers=self.headers,
            json=json_data,
        )   
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
                'Authorization': 'Bearer ZNPGASY5D6ZzI06HLfmIJryMA2nXrAer',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Obpp-Token': 'pRYt9OOnhBuBk3AwEwOTFT6Yj5W0eL2Ac2sGdx7kBPCIuyDlrlSiM1X3m/QSMmT8cGRgWj0YDHTNpS+HdF5FmuGi62954dwNGcKFPifyeFhpqdFYg2Cxqw7IV8xWbsIt0HlG',
                'Origin': 'https://obs-prd-ext-hcc.optum.com',
                'Referer': 'https://obs-prd-ext-hcc.optum.com/',
                'Request-Token': 'C1AfCBEGCQsCHyYAUkhNNCI7IiFSXk0XAhEsEQMGAAkVACEGAlBVRkBDPlRIRFtGDQ==',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'X-B3-SpanId': '63ae611c0f12fbe6',
                'X-B3-TraceId': '664b47a50329585563ae611c0f12fbe6',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            },
            json=json_data,
        )
        print(response.status_code)
        return response.json()["sourceCustomerNumber"], response.json()["customerName"]

    def GetInvoices(self,custId):
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Bearer HlTdPYP4bCBjlVKGuBHASJEJpAdA5Nvw',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Obpp-Token': 'mHBCWV/kRvzM1jPkzTGVTdM1lA5cHHSssro7QKXV8oFCmPHXTm1VsuCnU3209y/7s+r2xZsISWPsyIrNqkUEkeXtKqkD0h+TR53/xgVDmXsWUY7wwfTofAq99WzmD1sP+mAY',
            'Origin': 'https://obs-prd-ext-hcc.optum.com',
            'Referer': 'https://obs-prd-ext-hcc.optum.com/',
            'Request-Token': 'C1AGCgYdBgcVJhYUFVBVRj8iKipSXk0UHBMbAh8AAi0UUFVGICAmKTVQQ0YDAAwnBQEbCx0XHS0UUFVGQEc2XUZLXkYN',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
            'X-B3-SpanId': '1d43dbae844ebab8',
            'X-B3-TraceId': '664b5ad3b0cae4a01d43dbae844ebab8',
            'sec-ch-ua': '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'invoiceType': 'OPEN',
            'platformId': 'PRIME',
            'srcCustomerId': '01Q0864',
        }

        response = requests.post(
            'https://obs-prd-ext-hcc-ctc.optum.com/obppinvoicelisting/api/invoice/getopeninvoicelist',
            headers=headers,
            json=json_data,
        )
        print(response.content)
        print(response.json())
        # for x in response.json()["openInvoiceListing"]:
        #     yield x["invoiceNumber"]

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

invc = Invoices("12")
# invc.Download()
print(invc.GetInvoices("05Y9691"))
# invc.GetInvoices("01Q0864")
# invc.GetCustNumber("01Q0864")
