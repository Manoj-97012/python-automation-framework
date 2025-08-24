from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#Approach1
windowid=driver.current_window_handle
print(windowid) #A430BFBF670782B6DB6796C4EA51C6CC

try:
    driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
    WindowIDs = driver.window_handles

    parentchildid = WindowIDs[0]
    childid = WindowIDs[1]

    print(parentchildid, childid)
    driver.switch_to.window(parentchildid)
    print("The title is ",driver.title)

except:
    print("browser is working")

else:
    print("browser is ok")

finally:
    print("exactly")

# approach2

# for window in windowid:
#     driver.switch_to.window(window)
#     if driver.title == "OrangeHRM":
#         driver.close()
