from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*=shop]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)