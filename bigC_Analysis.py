# this app serves as an automatic cleaning reminder for my house mates and me
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import random
from sheetsAPI import sheets    #contains the class for the google sheets api

#on branch "feature"

#Declare the lists for the tenants groud and the cleaning tasks as well as the msg
ground_tenants=[]
high_tenants=[]
tasks=["Ground Floor", "Bathroom 1st floor", "3rd floor", "staircases"]
msg=[]
# Open the file that contains the ms since the epoch of the last time the script was fully executed
# Fully executed means the if-statement below was entered
time_saver=open('./last_ts.txt','r+')
last_ts=int(time_saver.read())
cur_ts=int(time.mktime(time.gmtime()))
last_ts=1
# if the time (in ms) between the time saved in the last_ts.txt-file 
# and the current time exceeds 1814400 ms (3 weeks time) enter the loop
if cur_ts - last_ts > 1814400:

    # Overwrite the time in the last_ts.txt-file with the current one
    # as the new reference
    time_saver.seek(0)
    time_saver.writelines(str(cur_ts))
    time_saver.truncate()
    time_saver.close()

    # Call the constructor of the class sheets and connect to 
    # the goolge sheets-api and the sheet and read the values 
    # with the room no and tenants from it
    sheet=sheets()
    sheet.authenticate()
    values=sheet.getSheetValue()
    for row in values:
        # here comes a loop that assigns the right name 
        # to the lists of ground_tenants & high_tenants based on the room no. 
        # the separation is needed because the ground_tenants and high_tenants 
        # have tasks that are seperated from another
        # ground_tenants contain the tenants that live on ground and first floor
        # high_tenants contain the tenants that live on second floor
        if(len(row)==2):
            if row[0]=="C-E1" or row[0]=="C-E2" or row[0]=="C-O1" or row[0]=="C-O2" or row[0]=="C-O3":
                ground_tenants.append(row[1])
            else:
                high_tenants.append(row[1])
        
    # shuffle the order of ground_tenant to assure that not everyone needs 
    # to do the same task everytime
    random.shuffle(ground_tenants)

    # construct the string for the msg 
    string="Hello this is your automatic cleaning reminder, %s is assigned to %s & %s & %s, %s is assigned to %s and the %s is assigned to %s while %s goes to %s & %s, due date is the upcoming sunday evening. \n Toilet paper is bought by %s Have fun and Cheers! Python"%(tasks[0],ground_tenants[0],ground_tenants[1],ground_tenants[2],tasks[1],ground_tenants[3],tasks[3],ground_tenants[4],tasks[2],high_tenants[0], high_tenants[1], ground_tenants[0])
    msg.append(string)
    # ADD MSG WITH LINK TO FILE 
    string="If you are new to this WG and can't find your name in the msg above or moved out and want to remove your name go to https://docs.google.com/spreadsheets/d/1zVb-aFqBkjslnahPpIy25WvsQyD2s00tnN3Ma-zRhMg/edit?usp=sharing"
    msg.append(string)
    # open chrome, start whatsapp and sent the string in a msg
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:/Users/drott/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Chrome(executable_path='C:/Users/drott/DS_Python/.venv/chromedriver.exe',chrome_options=options)  # Optional argument, if not specified will search path.
    driver.get('https://web.whatsapp.com/') 
    wait = WebDriverWait(driver, 600) 
    time.sleep(20)
    #driver.find_element_by_xpath("//*[@title='Im freihoefl 17']").click()
    driver.find_element_by_xpath("//*[@title='Narayan']").click()
    for row in msg:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(row)
        button=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

    time.sleep(15)
    driver.quit()


