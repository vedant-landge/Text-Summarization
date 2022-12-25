from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome("C:\\Users\\USER\\Downloads\\chromedriver.exe")
driver.get("https://www.facebook.com/DYPIUAkurdi/reviews")
time.sleep(5)
l=[]
for i in range(2,153):
    try:
        res = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div/div['+str(i)+']/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/span/div/div')
        l.append(res.text)
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div/div['+str(i)+']/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/span/div/div'))
            )
            res = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div/div[' + str(
                                          i) + ']/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/span/div/div')
            print(res.text)
            l.append(res.text)
        except:
            pass

driver.close()
with open('output.txt','w') as f:
    for i in l:
        print(i)
        f.writelines(i)