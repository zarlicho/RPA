from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from config.Config import Configs
from selenium import webdriver
from colorama import Fore,init
from service.gmails import OTP
import json,os,time,requests

class Login:
    def __init__(self):
        init()
        option = uc.ChromeOptions() 
        option.add_argument("--auto-open-devtools-for-tabs")
        option.add_argument(r"--user-data-dir=C:\chromeprofile")
        option.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        # option.add_argument('--disable-gpu')
        # option.add_argument('--headless')
        self.driver = uc.Chrome(options=option, use_subprocess=True)
        self.driver.set_page_load_timeout(30)
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        self.req = requests.Session()
        self.env = Configs()

    def Setup(self):
        print(Fore.BLUE + 'Setup started')
        try:
            self.driver.get("https://www.uhceservices.com/en/secure/home/ssoBasics")
        except Exception as e:
            print(Fore.RED + str(e))
    def Login(self):
            try:
                username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/div/input")))
                username.send_keys(self.env.usernames)
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div[1]/div/button[1]"))).click()
                time.sleep(2)
                password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/div[2]/div/input")))
                password.send_keys(self.env.password)
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/button"))).click()
            except Exception as e:
                print(Fore.RED + str(e))
                print(Fore.RED + "browser automaticly shutdown!")
                self.driver.close()

    def Otp(self):
        myotp = OTP(self.env.usrgmail, self.env.apppassword)
        otp = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[1]/div/input")))
        otp.send_keys(myotp.GetOtp())
        print(Fore.BLUE + "GET OTP!")
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/button"))).click()

    def SessionExpired(self):
        try:
            print(Fore.YELLOW + "Session expired!")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='optumIdLoginIdentifier']"))).click()
        except Exception as e:
            print(Fore.YELLOW + str(e))    

    def process_browser_log_entry(self,entry):
        response = json.loads(entry['message'])['message']
        return response

    def Home(self):
        if WebDriverWait(self.driver, 20).until(EC.url_to_be("https://www.uhceservices.com/en/secure/home")):
            try:
                # self.driver.get("https://www.uhceservices.com/en/secure/home/ssoBasics#")
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//*[@id='primarynav']/div/ul/li[8]/div/a"))).click()
                # result = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/groupchooser/div/div/div/div/div/div/div/div[2]/div[2]/section/div[2]"))).text
                time.sleep(20)
                logs = self.driver.get_log('performance')
                with open(fr"{os.path.abspath(os.path.join(os.getcwd(), 'entity'))}\network_log3.json", "w", encoding="utf-8") as f: 
                    f.write("[") 
                    for log in logs: 
                        network_log = json.loads(log["message"])["message"] 
                        f.write(json.dumps(network_log)+",") 
                    f.write("]") 
            except Exception as e:
                print(Fore.YELLOW+str(e))

    def GetAllCutomerId(self):
        userAgent = self.driver.execute_script("return navigator.userAgent;")
        self.req.headers.update({"user-agent": userAgent})
        for cookie in self.driver.get_cookies():
            self.req.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
        response = self.req.post("https://obs-prd-ext-hcc-elr.optum.com/obppcustomersearch/api/customersearch/search/internal")
        print(response.content)

    def LoginMain(self):
        try:
            if WebDriverWait(self.driver, 20).until(EC.url_to_be("https://www.uhceservices.com/en/prelogin?err=9002")):
                self.SessionExpired()
        except Exception as e:
            pass
        self.Login()
        try:
            if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/p"))).text == "Select one of the following methods to verify your identity.":     
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/button[2]"))).click()
                time.sleep(5)
                self.Otp()
        except Exception as e:
            print(Fore.YELLOW + str(e))
        self.Home()
        # self.GetAllCutomerId()

    def GetLogin(self):
        self.Setup()
        self.LoginMain()


