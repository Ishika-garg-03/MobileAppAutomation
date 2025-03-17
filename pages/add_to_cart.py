from pages.variables.amazonApp_variables import app_package
from utilities.common import logger, click, scroll_until_element_visible, sleep, check_login


class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        try:
            self.driver.activate_app(app_package)
            logger.info("The App is activated!")
            check_login('new UiSelector().description("Your Amazon.com Tab 2 of 5")', self.driver)
            logger.info("User is signed in on amazon application proceed to search category")
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")
        sleep()
        try:
            check_login('new UiSelector().description("Your Amazon.com Tab 2 of 6")', self.driver)
            logger.info("User is signed in on amazon application proceed to search category")
        except Exception as e:
            logger.error(f"Error encountered: {str(e)}")

    def add_to_cart(self):
      try:
          try:
            try:
                click(self.driver, 'new UiSelector().description("Browse menu Tab 5 of 5")')
                click(self.driver, 'new UiSelector().description("Browse menu Tab 5 of 5")')
                sleep()
            except Exception as E:
                logger.error("5 of 5 failed now trying 4 of 5")
                click(self.driver, 'new UiSelector().description("Browse menu Tab 4 of 5")')
                click(self.driver, 'new UiSelector().description("Browse menu Tab 4 of 5")')
                sleep()
          except Exception as E:
            logger.error("5 of 5 failed now trying 5 of 6")
            click(self.driver, 'new UiSelector().description("Browse menu Tab 5 of 6")')
            click(self.driver, 'new UiSelector().description("Browse menu Tab 5 of 6")')
          scroll_until_element_visible(self.driver, 'new UiSelector().text("Groceries & Pet Supplies")')
          click(self.driver,'new UiSelector().text("Groceries & Pet Supplies")')
          click(self.driver,'new UiSelector().resourceId("sbdgr")')
          sleep()
          click(self.driver,'new UiSelector().text("Beverages")')
          sleep()
          click(self.driver,'new UiSelector().resourceId("acsProductBlockV1-0").instance(0)')
          sleep()
          scroll_until_element_visible(self.driver,'new UiSelector().resourceId("add-to-cart-button")')
          sleep()
          click(self.driver,'new UiSelector().resourceId("add-to-cart-button")')
      except Exception as e:
        logger.error(f"Error encountered: {str(e)}")


    def verify_cart(self):
        click(self.driver, 'new UiSelector().resourceId("in.amazon.mShop.android.shopping:id/cart_count")')
        sleep()