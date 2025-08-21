from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:\\browserdriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# count number of rows and colums
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("No for rows:", rows)
print("No for columns:", columns)

# read specific rows and colums
# data_1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[7]/td[2]").text
# data_2=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[7]/td[3]").text
# print("Author name:",data_1)
# print("Subject name:",data_2)
#
# # read all rows and column's data
# for r in range(2, rows+1 ):
#     for c in range(1, columns+1):
#         get_data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(get_data, end ='  ')
#         print( )

# read the based on condition (List books and whose author)

for r in range(2, rows+1 ):
    Author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    print(Author)
    if Author == "Mukesh":
        bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        print(bookname)

