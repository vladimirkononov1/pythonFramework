import pytest

from pageObjects.homePage import HomePage
from testData.homePageData import HomePageData
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        log = self.getLogger()
        log.info("The name is: " + getData["name"])
        log.info("Email is: " + getData["email"])
        log.info("Gender is: " + getData["gender"])
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckBox().click()
        homepage.getPassword().send_keys(getData["password"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text

        assert "success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param