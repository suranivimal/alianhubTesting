# import configparser
# import os
#
# import pytest
# from pageObjects.LoginPage import LoginPage
# from pageObjects.DashBoard import Dashboard
# from utilities.readProperties import ReadConfig
# from utilities.customlogger import LogGen
# from utilities import XLUtils
# import time
#
#
# class TestLoginPageDDT:
#     baseUrl = ReadConfig.get_application_url()
#     path = os.path.join(os.path.dirname(__file__), '..', 'TestData', 'LoginData.xlsx')
#     config = configparser.ConfigParser()
#     config.read(path)
#     logger = LogGen.loggen()
#
#     @pytest.mark.regression
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_login_ddt(self, setup):
#         self.logger.info("******* Starting Login DDT Test **********")
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.driver.maximize_window()
#         self.lps = LoginPage(self.driver)
#
#         self.rows = XLUtils.get_row_count(self.path, 'Sheet1')
#         print('Number of rows...', self.rows)
#         lst_status = []
#
#         for r in range(2, self.rows + 1):
#             self.user = XLUtils.read_data(self.path, 'Sheet1', r, 1)
#             self.password = XLUtils.read_data(self.path, 'Sheet1', r, 2)
#             self.exp = XLUtils.read_data(self.path, 'Sheet1', r, 3)
#             time.sleep(30)
#             self.lps.set_email_id(self.user)
#             time.sleep(30)
#             self.lps.set_password(self.password)
#             time.sleep(30)
#             self.lps.click_on_login_button()
#             print(f"User: {self.user}, Password: {self.password}, Expected: {self.exp}")
#             time.sleep(15)
#
#             act_title1 = self.driver.title
#             exp_title1 = "Alian Hub | Home"
#
#             if act_title1 == exp_title1:
#                 if self.exp == 'Pass':
#                     self.logger.info("**** Passed 1****")
#                     self.dashboard_page = Dashboard(self.driver)
#                     self.dashboard_page.click_on_profile()
#                     self.logger.info("**** Profile ****")
#                     self.driver.implicitly_wait(40)
#                     self.dashboard_page.click_on_logout()
#                     lst_status.append("Pass")
#                     XLUtils.write_data(self.path, 'Sheet1', r, 3, "Pass")
#                 elif self.exp == 'Fail':
#                     self.logger.info("**** Failed 1****")
#                     lst_status.append("Fail")
#                     XLUtils.write_data(self.path, 'Sheet1', r, 3, "Fail")
#             elif act_title1 != exp_title1:
#                 if self.exp == 'Pass':
#                     self.logger.info("**** Failed ****")
#                     lst_status.append("Fail")
#                     XLUtils.write_data(self.path, 'Sheet1', r, 3, "Fail")
#                 elif self.exp == 'Fail':
#                     self.logger.info("**** Passed ****")
#                     lst_status.append("Pass")
#                     XLUtils.write_data(self.path, 'Sheet1', r, 3, "Pass")
#             print(lst_status)
#
#         if "Fail" not in lst_status:
#             self.logger.info("******* DDT Login test passed **********")
#             self.driver.close()
#             assert True
#         else:
#             self.logger.error("******* DDT Login test failed **********")
#             self.driver.close()
#             assert False
#
#         self.logger.info("******* End of Login DDT Test **********")
#         self.logger.info("**************** Completed  TC_Login_Page_DDT *************")
