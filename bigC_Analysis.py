
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import random

time_saver=open('C:/Users/drott/DS_Python/.venv/last_ts','r+')
last_ts=int(time_saver.read())
cur_t=time.gmtime()
cur_ts=time.mktime(cur_t)
if last_ts - cur_ts> 1209600:
    last_ts=cur_ts
    time_saver.seek(0)
    time_saver.writelines(str(last_ts))
    time_saver.truncate()
    time_saver.close()

    
    ground_tenants=["Narayan", "Akash", "Russ","Deepak", "Daniela"]
    high_tenants=["Andreas", "Philipp"]
    tasks=["Ground Floor", "Bathroom 1st floor", "3rd floor", "staircases"]
    random.shuffle(ground_tenants)

    string="Hello this is your automatic cleaning reminder, %s is assigned to %s & %s & %s, %s is assigned to %s and the %s is assigned to %s while %s goes to %s & %s, due date is the upcoming sunday evening. Have fun and Cheers! Python"%(tasks[0],ground_tenants[0],ground_tenants[1],ground_tenants[2],tasks[1],ground_tenants[3],tasks[3],ground_tenants[4],tasks[2],high_tenants[0], high_tenants[1])

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path='C:/Users/drott/DS_Python/chromedriver.exe',chrome_options=options)  # Optional argument, if not specified will search path.
    driver.get('https://web.whatsapp.com/') 
    wait = WebDriverWait(driver, 600) 
    time.sleep(20)
    driver.find_element_by_xpath("//*[@title='Akash Gaurav']").click()
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(string)
    button=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()


    time.sleep(15)
    driver.quit()


