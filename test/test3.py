import json
from playwright.sync_api import sync_playwright, Playwright
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.gmails import GetOtp

class LoginSection:
    def __init__(self,playwright: Playwright):
        self.browser =None
        self.context =None
        self.page =None
        self.plywright = playwright
    def setup(self):
        self.browser = self.plywright.chromium.launch(headless=False) #storage_state='session.json'
        self.context = self.browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81",storage_state='session2.json')
        self.page = self.context.new_page()

    def UserInput(self):
        try:
            self.page.goto("https://www.uhceservices.com/en/secure/home/ssoBasics")
            self.page.fill('input#username',"Betafits2023") #user input
            self.page.keyboard.press("Enter")
            # self.page.locator('xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/button[1]').click()
            self.page.on("request", lambda request: print(f"Request: {request.header_value}") if request.url == "https://identity.onehealthcareid.com/api/v1/auth/login-options" else None)
            # self.page.on("response", lambda response: print(f"Response: {response.status} {response.finished()}"))
            return self.page.locator("xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/span").text_content()
        except Exception as e:
            print(e)
    def UserPw(self):
        time.sleep(3) 
        self.page.fill('input#login-pwd',"yz_r^PjPp46QLTD")#password input
        self.page.locator('xpath=/html/body/div[1]/div/main/div[1]/form/button').click()
        time.sleep(3)
        
    def otp(self):
        self.page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/button[2]").click() #otp option
        time.sleep(5)
        self.page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/div[1]/div/input").fill(GetOtp())
        self.page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/button").click()
        time.sleep(3)

    def mainLogin(self):
        result = self.UserInput()
        print("result: ",result)
        # self.UserPw()
        try:
            if result == "The Username or email that you entered is incorrect.":
                self.page.reload()
                self.UserInput()
                self.UserPw()
            else:
                self.UserPw()
            if "Select one of the following methods to verify your identity." in self.page.content():
                self.otp()
            else:
                print("no need otp")
                print(self.page.url)
        except Exception as e:
            print(e)
        print(self.context.cookies())
        self.context.storage_state(path='session2.json')
    def testRequest(self):
        response = self.context.request.post("/api/v1/auth/login-options",)

with sync_playwright() as playwright:
    LogSection = LoginSection(playwright)
    LogSection.setup()
    LogSection.mainLogin()