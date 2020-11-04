from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage
from utilities.baseClass import BaseClass


class CheckOutPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutFinal = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def addProductToCart(self, name):
        log = self.getLogger()
        products = CheckOutPage.getProductTitles(self)
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == name:
                # add product to the cart
                product.find_element_by_xpath("div/button").click()
                log.info("Text received from application is " + productName)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def getCheckOutFinal(self):
        self.driver.find_element(*CheckOutPage.checkOutFinal).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

