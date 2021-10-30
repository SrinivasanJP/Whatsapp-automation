from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,datetime

launched=False
global driver

def funlist():
    fun=[settimeMessages,repMessages]
    for i in range(len(fun)):
        print(f"{i+1}-",str(fun[i]))
    operation=int(input("Enter index to perform such operation :"))
    fun[operation-1]()
def exit():
    conformation=input("Did you want to exit from this program click 'Y' for Yes or 'N' for No")
    if conformation=='Y'or conformation=='y':
        funlist()
    elif conformation=='N'or conformation=='n':
        print("Thanks for using this program....")
    else:print("Please give correct option");funlist()



def settimeMessages():
    global launched
    global driver
    name=input("Enter name or group pointer :")
    messages=input("Type your wishes which i need to send :")
    iteration=int(input("Enter number of iterations :"))
    settime=input("Enter when i need to send (format hh-mm) 24* :")
    
    nowtimeHour,minute=datetime.datetime.now().hour,datetime.datetime.now().minute
    print(nowtimeHour,minute)
    nowinsecond=(nowtimeHour*60**2)+(minute*60)
    print(nowinsecond)
    assignedHour,assignedminute=int(settime[:2]),int(settime[3:])
    assignedinseconds=(assignedHour*60**2)+(assignedminute*60)
    print(assignedinseconds)
    whensend=assignedinseconds-nowinsecond
    print(type(whensend), whensend)

    time.sleep(whensend)
    if launched==False:
        driver=webdriver.Chrome("chromedriver.exe")
        #driver.maximize_window()
        driver.get("https://web.whatsapp.com/")
        # driver objuct loads web.whatsapp.com
        time.sleep(5)
        launched=True
    pointingname=driver.find_element_by_xpath('//span[@title="{}"]'.format(name)).click()
    text_box=driver.find_element_by_class_name("p3_M1")

    for i in range(iteration):
        time.sleep(2)
        text_box.send_keys(messages)
        time.sleep(2)
        text_box.send_keys(Keys.ENTER)
    exit()


def repMessages():
    global launched,driver
    name=input("Enter name or group pointer :")
    messages=input("Type what i need to send :")
    iteration=int(input("Enter number of iterations : "))
    if launched==False:
        driver=webdriver.Chrome("chromedriver.exe")
        #driver.maximize_window()
        driver.get("https://web.whatsapp.com/")
        # driver objuct loads web.whatsapp.com
        time.sleep(5)
        launched=True
    pointingname=driver.find_element_by_xpath('//span[@title="{}"]'.format(name)).click()
    text_box=driver.find_element_by_class_name("p3_M1")
    
    for i in range(iteration):
        time.sleep(2)
        text_box.send_keys(messages)
        time.sleep(2)
        text_box.send_keys(Keys.ENTER)
    exit()
funlist()