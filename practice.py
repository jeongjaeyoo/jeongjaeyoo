from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

login_url = 'https://nid.naver.com/nidlogin.login'
driver.get(login_url)
time.sleep(2)

my_id = 'wjdwo503'
my_pw = 'wjdrud477!'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

button = driver.find_element_by_id('log.login')
button.click()
time.sleep(1)

comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

menu = driver.find_element_by_id('menuLink90')
menu.click()
time.sleep(1)

for i in range(1, 16):
    XPath = "/html/body/div[1]/div/div[4]/table/tbody/tr[" + str(i) + "]/td[1]/div[3]/div/a"

    driver.switch_to.frame('cafe_main')
    time.sleep(1)

    writing = driver.find_element_by_xpath(XPath)
    writing.click()
    time.sleep(1)

    content = driver.find_element_by_css_selector('div.se-component-content').text
    print(content)
    # 뒤로 가기
    driver.back()
    time.sleep(1)

driver.close()