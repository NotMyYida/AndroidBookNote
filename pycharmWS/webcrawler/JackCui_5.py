from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver.get("https://www.python.org/")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)

# options = webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) '
#                      'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",options=options)
# driver.get("http://www.baidu.com")

url = "http://pythonscraping.com"
# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.PhantomJS(executable_path="F:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get(url)
driver.implicitly_wait(1)
print(driver.get_cookies())
