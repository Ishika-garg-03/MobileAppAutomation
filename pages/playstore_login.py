from utilities.common import sleep, check_login, click, send_keys, locator_sleep, logger
from pages.variables.playstore_variables import *

class PlaystoreLogin:
    def __init__(self, driver):
        self.driver = driver

    def launch_playstore(self):
        self.driver.activate_app(appPackage)
        sleep()

    def perform_signin(self):
        try:
            if signin_btn.is_displayed():
                click(self.driver, signin_btn)
                locator_sleep(email_textbox, self.driver)
                click(self.driver, email_textbox)
                send_keys(self.driver, enter_email, email, 'a')
                click(self.driver, next_btn)
                sleep()
                send_keys(self.driver, enter_pass, password, 'a')
                click(self.driver, next_btn)
                locator_sleep(agree_btn, self.driver)
                click(self.driver, agree_btn)
                locator_sleep(accept_btn, self.driver)
                click(self.driver, accept_btn)
        except Exception as e:
            logger.error("Signin button not appeared or another error occurred: " + str(e))

    def verify_login(self):
        sleep()
        if not check_login(signin_check, self.driver):
            raise Exception('Playstore Login unsuccessful.')
        logger.info("Playstore login successful")
