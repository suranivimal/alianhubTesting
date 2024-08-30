import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.DashBoard import Dashboard
from utilities.readProperities import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils
import time


class Test_Login_Page_DDT:
    baseUrl = ReadConfig.getApplicationUrl()
    path = "C:\\Users\\Alian Testing\\PycharmProjects\\alianhubTesting\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lps = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(30)
            self.lps.setUserName(self.user)
            time.sleep(30)
            self.lps.setPassword(self.password)
            time.sleep(30)
            self.lps.clickOnLogin()
            print(f"User: {self.user}, Password: {self.password}, Expected: {self.exp}")
            time.sleep(15)

            act_title1 = self.driver.title
            exp_title1 = "Alian Hub | Home"

            if act_title1 == exp_title1:
                if self.exp == 'Pass':
                    self.logger.info("**** Passed 1****")
                    self.dashboard_page = Dashboard(self.driver)
                    self.dashboard_page.clickOnProfile()
                    self.logger.info("**** Profile ****")
                    self.driver.implicitly_wait(40)
                    self.dashboard_page.clickOnLogout()
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 3, "Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** Failed 1****")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 3, "Fail")
            elif act_title1 != exp_title1:
                if self.exp == 'Pass':
                    self.logger.info("**** Failed ****")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 3, "Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** Passed ****")
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 3, "Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_Login_Page_DDT *************")
