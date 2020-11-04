from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import CheckOutPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the cart titles")
        checkoutpage.addProductToCart("Blackberry")

        checkoutpage.getCheckOutButton().click()
        # creating confirm page object
        confirmpage = checkoutpage.getCheckOutFinal()
        confirmpage.getLocation().send_keys("ind")

        self.verifyLinkPresence("India")
        confirmpage.getCountry().click()
        confirmpage.getCheckBox().click()
        confirmpage.getPurchaseButton().click()

        successString = confirmpage.getSuccessAlert().text

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successString
        log.info("string appeared on the page is: " + successString)

        # get screenshot
        self.driver.get_screenshot_as_file("screen.png")