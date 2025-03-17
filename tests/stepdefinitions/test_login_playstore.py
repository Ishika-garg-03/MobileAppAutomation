from urllib import request
from pytest_bdd import scenario, feature, scenarios, given, when, then
from pages.variables.root_path_variables import root_path
from pages.variables.scenarioPath_variables import playstore_features
from utilities.common import device_status, pytest_bdd_before_scenario, screenshot, screenshot_compare
from pages.playstore_login import PlaystoreLogin

scenarios(playstore_features)
device_status()

@given("Playstore is launched")
def launch(appium_driver):
    playstore_login = PlaystoreLogin(appium_driver)
    playstore_login.launch_playstore()
    screenshot(appium_driver,f'{root_path}\\screenshots\\login_playstore.png')

@when("Try to perform login actions")
def signin(appium_driver):
    playstore_login = PlaystoreLogin(appium_driver)
    playstore_login.perform_signin()

@then("User should be logged in")
def login(appium_driver):
    playstore_login = PlaystoreLogin(appium_driver)
    playstore_login.verify_login()
    screenshot_compare(appium_driver,f'{root_path}\\screenshots\\login_playstore.png','playstore_login_check')

pytest_bdd_before_scenario(request, feature, scenario)




