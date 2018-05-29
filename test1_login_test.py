from selenium import webdriver
import time
driver = webdriver.Firefox()
#var_def

url = "https://manage.plivo.com/accounts/login/"
email = "plivoiview@gmail.com"
password = "Plivo@123"
user_name_xpath = "//input[@id='id_username']"
password_xpath = "//input[@id='id_password']"
Login_button_xpath = "//button[@id='login-sub']"
driver.get(url)
time.sleep(10)
email_feild = driver.find_element_by_xpath(user_name_xpath)
email_feild.send_keys(email)
print("email id entered")
password_feild = driver.find_element_by_xpath(password_xpath)
password_feild.send_keys(password)
print("Password entered")

Button = driver.find_element_by_xpath(Login_button_xpath)
Button.click()
time.sleep(10)
Dashboard = driver.find_element_by_xpath("//a[@href='/dashboard/'][contains(text(),'Dashboard')]")
if Dashboard is not None:
    print("login succesful")
else:
    print("login failed")


#Create Endpoint_Variables

Endpoint_xpath = "//a[@href='/endpoint/']"
New_endpoint_xpath = "//a[@href='/endpoint/create/']"
new_username_xpath = "//input[@id='id_username']"
new_password_xpath = "//input[@id='id_password']"
new_alias_xpath = "//input[@id='id_alias']"
Add_button_xpath = "//input[@type='submit']"

#Add first_endpoint
Button1= driver.find_element_by_xpath(Endpoint_xpath)
Button1.click()
time.sleep(3)

Button2 = driver.find_element_by_xpath(New_endpoint_xpath)
Button2.click()
time.sleep(3)

New_Username = driver.find_element_by_xpath(new_username_xpath)
New_Username.click()
New_Username.send_keys("test2")
time.sleep(5)
New_Password = driver.find_element_by_xpath(new_password_xpath)
New_Password.click()
New_Password.send_keys("test2")
time.sleep(5)
New_alias = driver.find_element_by_xpath(new_alias_xpath)
New_alias.click()
New_alias.send_keys("test2")
time.sleep(5)
Add = driver.find_element_by_xpath(Add_button_xpath)
Add.click()
time.sleep(5)
#Add_second_endpoint

print("First Endpoint added")
Button1= driver.find_element_by_xpath(Endpoint_xpath)
Button1.click()

New_Username = driver.find_element_by_xpath(new_username_xpath)
New_Username.click()
New_Username.send_keys("test3")
time.sleep(5)
New_Password = driver.find_element_by_xpath(new_password_xpath)
New_Password.click()
New_Password.send_keys("test3")
time.sleep(5)
New_alias = driver.find_element_by_xpath(new_alias_xpath)
New_alias.click()
New_alias.send_keys("test3")
time.sleep(5)
Add = driver.find_element_by_xpath(Add_button_xpath)
Add.click()
time.sleep(5)

print("Second endpoint added")

avaya123.onsip.com

