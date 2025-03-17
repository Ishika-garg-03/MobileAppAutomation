from urllib import request
from pytest_bdd import scenarios, given, when, then, feature, scenario
from pages.variables.scenarioPath_variables import amazon_signin_features
from pages.login_to_amazon import AmazonSignIn
from utilities.common import pytest_bdd_before_scenario

scenarios(amazon_signin_features)

@given("Amazon application is installed on device")
def check_amazon(appium_driver):
    amazon_signin = AmazonSignIn(appium_driver)
    amazon_signin.open_amazon_app()

@when("Try to login in amazon application")
def amazon_login(appium_driver):
    amazon_signin = AmazonSignIn(appium_driver)
    amazon_signin.click_profile()
    if amazon_signin.check_already_login():
        pass
    else:
        amazon_signin.dismiss_notifications()
        amazon_signin.click_profile1()
        amazon_signin.select_language_and_continue()
        amazon_signin.click_sign_in()
        amazon_signin.handle_cancel_button()
        amazon_signin.enter_email_and_password()

@then("User will be able to access amazon application")
def check_signin(appium_driver):
    amazon_signin = AmazonSignIn(appium_driver)
    amazon_signin.verify_sign_in()

pytest_bdd_before_scenario(request, feature, scenario)