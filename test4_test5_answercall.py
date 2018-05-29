from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://app.onsip.com/app/#/call")

def login(email,password):

    time.sleep(10)
    username = driver.find_element_by_xpath("/html//input[@id='login-username']")
    username.click()
    username.send_keys(email)
    time.sleep(3)
    password_feild = driver.find_element_by_xpath("/html//input[@id='login-password']")
    password_feild.click()
    password_feild.send_keys(password)
    time.sleep(3)
    login_button = driver.find_element_by_xpath("//form[@id='login__form']//div[@class='page-form__action']//input[@value='Log In']")
    login_button.click()
    time.sleep(3)




username1 ="srnagda@avaya123.onsip.com"
password1 ="mayurbhai"

username2="sonalnagda89@avaya123.onsip.com"
password2="mayurbhai"

#login in to user one
login(username1,password1)
print("user A registered")
#login in to user 2
login(username2,password2)
print("user B registered")

start_new_call = driver.find_element_by_xpath("//div[@id='new-call-button']/button[1]")
start_new_call.click()
time.sleep(3)

called_party = driver.find_element_by_xpath("/html//input[@id='new-call__target']")
called_party.click()
called_party.send_keys(username1)
place_call = driver.find_element_by_xpath("//div[@id='view']/new-call//call-block-footer//button[@title='Make an audio call']")
place_call.click()
print("user A is alerting")

parent_handle = parentHandle = driver.current_window_handle
print("Parent Handle: " + parentHandle)
handles = driver.window_handles


for handle in handles:
    print("Handle: " + handle)
    if handle not in parentHandle:
        driver.switch_to.window(handle)
        print("Switched to window:: " + handle)
        answer_call = driver.find_element_by_xpath(
            "//div[@id='view']//call/div[@class='session']//call-block-footer//button[@title='Answer the call (audio only)']")
        answer_call.click()
        print("user A answers the call")
        end_call = driver.find_element_by_xpath(
            "//div[@id='view']/call-page/section[@class='app-view']//div[@class='session']//call-block-footer//button[@title='End Call']")
        end_call.click()
        print("Call ended")
        time.sleep(2)
        break




