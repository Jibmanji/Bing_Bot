from selenium import webdriver
browser = webdriver.Firefox()
browser.get(https://login.live.com/)
email = browser.find_element_by_id(loginfmt)
email.send_keys(jckhendrix@gmail.com)
pwd = browser.find_element_by_id(passwd)
pwd.send_keys(VY65224q$)
pwd.submit