from appium.webdriver.common.appiumby import AppiumBy
from utilities.common import sleep, check_login, click, send_keys, click_button, logger
from pages.variables.amazonApp_variables import *


class AmazonSignIn:
    def __init__(self, driver):
        self.driver = driver

    def open_amazon_app(self):
        self.driver.activate_app(app_package)
        sleep()

    def click_profile(self):
        try:
            profile = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("androidx.appcompat.app.ActionBar$Tab").instance(1)')
            if profile.is_displayed():
                profile.click()
                click(self.driver, 'new UiSelector().description("sib")')
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    sleep()

    def check_already_login(self):
        try:
            avatar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().resourceId("user_avatar")')
            if avatar.is_displayed():
                return True
        except Exception:
            return False

    def dismiss_notifications(self):
        try:
            notification = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_deny_button")')
            if notification.is_displayed():
                notification.click()
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    sleep()
    def click_profile1(self):
        try:
            profile = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().className("androidx.appcompat.app.ActionBar$Tab").instance(1)')
            if profile.is_displayed():
                profile.click()
                click(self.driver, 'new UiSelector().description("sib")')
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    sleep()
    def select_language_and_continue(self):
        try:
            language_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, language_selector)
            if language_element.is_displayed():
                click(self.driver, english)
                click(self.driver, continue_btn)
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    def click_sign_in(self):
        try:
            signin_bton = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                     'new UiSelector().resourceId("in.amazon.mShop.android.shopping:id/sign_in_button")')
            if signin_bton.is_displayed():
                signin_bton.click()
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

        sleep()

    def handle_cancel_button(self):
        try:
            cancel_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.gms:id/cancel")')
            if cancel_btn.is_displayed():
                cancel_btn.click()
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    def enter_email_and_password(self):
        click_button(self.driver, email_textbox)
        send_keys(self.driver, enterEmail, email, 'c')
        sleep()
        click(self.driver, continue_button)
        sleep()
        send_keys(self.driver, enter_password, password, 'c')
        sleep()
        click_button(self.driver, submit_btn)
        sleep()

    def verify_sign_in(self):
        checker = check_login(login_check, self.driver)
        if not checker:
            raise Exception("Login to Amazon application failed, try again!")
        logger.info("Login to Amazon application successful.")
        sleep()
