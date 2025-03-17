from pages.variables.scenarioPath_variables import amazon_install_features
from utilities.common import pytest_bdd_before_scenario
from urllib import request
from pytest_bdd import scenario, feature, scenarios,given,when,then
from pages.amazon_install import AmazonInstall

scenarios(amazon_install_features)

@given("User is logged in on playstore")
def is_login(appium_driver):
    amazon_install = AmazonInstall(appium_driver)
    amazon_install.login_to_playstore()

@when("Try to search and install amazon application")
def search_install_amazon(appium_driver):
    amazon_install = AmazonInstall(appium_driver)
    amazon_install.search_and_install_amazon()

@then("Amazon application should be installed")
def check_if_amazon(appium_driver):
    amazon_install = AmazonInstall(appium_driver)
    amazon_install.verify_amazon_installed()

pytest_bdd_before_scenario(request, feature, scenario)