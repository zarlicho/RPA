# import json
# from playwright.sync_api import sync_playwright
# import time
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from service.gmails import GetOtp

# def handle_element(page, selector):
#     try:
#         element = page.wait_for_selector(selector, timeout=5000)  # Tunggu maksimal 5 detik
#         return element
#     except TimeoutError:
#         return None

# def Login():
#     with sync_playwright() as p:
#         # browser = p.chromium.launch_persistent_context(user_data_dir=r"C:\chromeprofile2", headless=False,slow_mo=500)
#         browser = p.chromium.launch(headless=False) #storage_state='session.json'
#         context = browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",storage_state='session2.json')
#         page = context.new_page()
#         with page.expect_request("**/login") as req:
#             page.goto("https://www.uhceservices.com/en/secure/home")
#             # if page.url == "https://www.uhceservices.com/en/secure/home":
#             print(page.url)
#             try:
#                 # time.sleep(10)
#                 if page.locator("xpath=/html/body/div[3]/div[1]/div/message/div/span").text_content() == "Your session has timed out. You have been successfully signed out of the application.":
#                     page.locator('xpath=/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/span[1]/a/span').click() #user input
#                     page.locator('xpath=/html/body/div[3]/div[5]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/button[2]').click() #user input
#                     time.sleep(3)
#                     print(page.url)
#                     time.sleep(2)
#                 if "One Healthcare ID or Email Address" in page.content():
#                     print(page.content())
#                     page.locator('xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/div/input').fill("Betafits2023") #user input
#                     page.locator('xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/button[1]').click()
#                     # print(page.locator("xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/span").text_content())
#                 # if page.locator("xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/span").text_content == "The Username or email that you entered is incorrect.":
#                     # print(page.locator("xpath=/html/body/div[1]/div/div/main/div[2]/div[1]/div/div[1]/span").text_content())
#                     time.sleep(3) 
#                     page.locator('xpath=/html/body/div[1]/div/main/div[1]/form/div[2]/div/input').fill("yz_r^PjPp46QLTD") #password input
#                     page.locator('xpath=/html/body/div[1]/div/main/div[1]/form/button').click()
#                     time.sleep(5)
#             except Exception as e:
#                 print(e)
#             try:
#                 if page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/p").text_content() == "Select one of the following methods to verify your identity.":
#                     page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/button[2]").click()
#                     time.sleep(5)
#                     page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/div[1]/div/input").fill(GetOtp())
#                     page.locator("xpath=/html/body/div[1]/div/main/div[1]/div/button").click()
#                     time.sleep(4)
#             except Exception as e:
#                 print(e)
#             time.sleep(10)
#             # target_url = "https://www.uhceservices.com/api/bne/commissions/secure/v1.0/listofcommissions"

#             # # Tambahkan event listener untuk response
#             # def handle_response(response):
#             #     if response.url == target_url:
#             #         print(f"Response from {target_url}:")
#             #         print(f"Status: {response.status}")
#             #         print(f"Headers: {response.headers()}")
#             #         print(f"Body: {response.text()}")

#             # page.on("response", handle_response)
#             # page.goto("https://www.uhceservices.com")
#             with page.expect_request("**/home") as fin:
#             # context.storage_state(path='session2.json') #/html/body/div[3]/div/nav/div/navigation/div/nav/div/ul/li[8]/div/a
#                 page.locator("xpath=/html/body/div[3]/div/nav/div/navigation/div/nav/div/ul/li[8]/div/a").click()
#                 page.on("request", lambda request: print(f"Request: {request.url} {request.post_data}{request.response()}"))
#                 page.on("response", lambda response: print(f"Response: {response.status} {response.url}"))
#                 print(page.url)
#                 print(fin.value.redirected_from)
#                 print(fin.value.post_data)
#                 # prinfinontext.request)
#                 print(fin.value.all_headers())
#                 print("cookies: ",context.cookies())
        
#         time.sleep(20)


# def LoginUpwork():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless = False,slow_mo=50)
#         context = browser.new_context(storage_state='session.json')
#         page = context.new_page()
#         page.goto("https://www.upwork.com/nx/find-work/best-matches")
#         time.sleep(10)
#         # page.locator("xpath=/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/div[3]/div/div/div/div/input").fill("arianudin.azis@gmail.com")
#         # page.locator("xpath=/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/button").click()
#         # page.locator("xpath=/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/div[3]/div/div/div/input").fill("Azis290495")
#         # page.locator("xpath=/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/div[5]/div/div[1]/div/label/span").click()
#         # page.locator("xpath=/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/button").click()
#         # time.sleep(20)
#         # context.storage_state(path='session.json')


# # LoginUpwork()
# Login()
    

# from seleniumwire import webdriver  # Import from seleniumwire
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome()
# driver.get('https://web-scraping.dev/product/1')
# # wait for element to appear and click it to trigger background requests
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'load-more-reviews')))
# element.click()
# # Access requests via the `requests` attribute
# for request in driver.requests:
#     if request.response:
#         print(
#             request.url,
#             request.response.status_code,
#             request.response.headers['Content-Type'],
#             request.response.body,
#         )
# driver.quit()
# from InquirerPy import inquirer
# from InquirerPy.base.control import Choice


# def main():
#     action = inquirer.select(
#         message="Select an action:",
#         choices=[
#             "Upload",
#             "Login",
#             Choice(value=None, name="Exit"),
#         ],
#         default=None,
#     ).execute()

#     if action == "Upload":
#         date = inquirer.text(
#             message="insert date range from date to end date example: 2024-03-19/2024-04-2: ",
#             multicolumn_complete=True,
#         ).execute()
#         host = inquirer.text(
#             message="insert host: ",
#             multicolumn_complete=True,
#         ).execute()
#         print(host)
#     elif action == "Login":
#         proceed, service, confirm = False, False, False
#         proceed = inquirer.confirm(message="Proceed?", default=True).execute()
#         if proceed:
#             service = inquirer.confirm(message="do yo want to proses this action?").execute()
#         if service:
#             confirm = inquirer.confirm(message="for real?").execute()
#         print(action)
# if __name__ == "__main__":
#     main()

from colorama import Fore,init
init()
file_path = r"F:\python project\myProject\UpworkProj\RPA_project\test\test3.py"
print(Fore.GREEN + f"file success to download '{file_path}'")