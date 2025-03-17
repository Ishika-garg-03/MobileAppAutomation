from appium.webdriver.common.appiumby import AppiumBy
from pages.variables.appInstall_variabes import search_icon, search_bar, enter_key, search_text, app_desc, install_btn, \
    uninstall_btn, open_btn
from utilities.common import sleep, check_login, click, send_keys, locator_sleep, logger
from pages.variables.playstore_variables import *
from pages.variables.amazonApp_variables import *


class AmazonInstall:
    def __init__(self, driver):
        self.driver = driver

    def login_to_playstore(self):
        self.driver.activate_app(appPackage)
        login_status = check_login(login_check, self.driver)
        if not login_status:
            raise Exception("Playstore is not open, please launch it!")
        logger.info("Playstore is logged in, proceeding to install Amazon.")

    def search_and_install_amazon(self):
        click(self.driver, search_icon)
        click(self.driver, search_bar)
        send_keys(self.driver, search_text, 'amazon', 'a')
        self.driver.press_keycode(enter_key)
        sleep()

        try:
            open_btn_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, open_btn)
            if open_btn_element.is_displayed():
                logger.info("Amazon application is already installed on your device")
        except Exception:
            logger.info("Proceeding with Amazon installation")
            click(self.driver, app_desc)
            sleep()
            click(self.driver, install_btn)
            locator_sleep(uninstall_btn, self.driver)

    def verify_amazon_installed(self):
        if not self.driver.is_app_installed(app_package):
            raise Exception("Amazon app installation unsuccessful.")
        logger.info("Amazon app is available to launch")
