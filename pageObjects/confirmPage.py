from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    successAlert = (By.CLASS_NAME, "alert-success")

    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccessAlert(self):
        return self.driver.find_element(*ConfirmPage.successAlert)