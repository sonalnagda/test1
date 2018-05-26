from selenium.webdriver.common.by import By
from base.seleniumdriver import SeleniumDriver

class LoginPage(SeleniumDriver):
    super().__init__(driver)
    def __init__(self, driver):
        self.driver = driver
    #locators
    __login_link="Login"
    __email_feild="user_email"
    __password_feild="user_password"
    __loginButton="commit"

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self.__login_link)

    def emailfeild(self, email):
        return self.driver.find_element(By.ID, self.__email_feild)

    def passworffeild(self):
        return self.driver.find_element(By.ID, self.__password_feild)

    def loginbutton(self):
        return self.driver.find_element(By.NAME, self.__loginButton)

    def clickLoginlink(self):
        self.__getLoginlink().click()

    def enter_email(self, email):
        self.__email_feild().send_keys(email)

    def enter_password(self, password):
        self.__password_feild().send_keys(password)

    def clickLoginButton(self):
        self.__loginButton().click()


    def login(self, email,password):
       self.clickLoginlink()
       self.enter_email(email)
       self.enter_password(password)
       self.loginbutton()

