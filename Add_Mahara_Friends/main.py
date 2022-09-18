from cmd import PROMPT
from operator import truediv
from xml.sax.handler import DTDHandler
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
from getpass import getpass 

phrases = []
ignoreList = []

with open("IgnoreList.txt") as document:
    for line in document:
        ignoreList.append(line)

with open("Phrases.txt") as document:
    for line in document:
        phrases.append(line)

username=input("Username: ")
password = getpass('Password: ')

options = Options()
options.headless = True

path = "./geckodriver.exe"
driver = webdriver.Firefox(options=options, executable_path=path)
driver.get("https://portfolio.bbbaden.ch")

usernameLogin = driver.find_element(By.ID, "login_login_username")
usernameLogin.send_keys(username)

passwordLogin = driver.find_element(By.ID, "login_login_password")
passwordLogin.send_keys(password)

loginButton = driver.find_element(By.ID, "login_submit")
loginButton.click()

for i in range(5000):
     
    if ignoreList.__contains__(str(i) + "\n"):
        print("The user with the ID " + str(i) + " is on the ignore list! Skipping...")
        continue
        
    link = "https://portfolio.bbbaden.ch/user/requestfriendship.php?id=" + str(i) + "&returnto=view"

    driver.get(link)

    try:
        friendRequestEntry = driver.find_element(By.ID, "requestfriendship_message")
    except:
        print("The user with the ID " + str(i) + " was already added or doesn't exist!")
        continue
    
    friendRequestEntry.send_keys(phrases[random.randint(0, len(phrases) - 1)])

    friendRequestButton = driver.find_element(By.ID, "requestfriendship_submit")
    friendRequestButton.click()
         
    print("The user with the ID " + str(i) + " was added succesfully")
