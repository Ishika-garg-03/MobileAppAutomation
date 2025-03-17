from pytest_bdd import scenarios, given, when, then
from pages.add_to_cart import AddToCart

scenarios('../features/addToCart.feature')


@given("User is signed in on amazon application")
def amazon_login(appium_driver):
    add_to_cart_page = AddToCart(appium_driver)
    add_to_cart_page.login()


@when("Try to search category and add product to cart")
def search_category(appium_driver):
    add_to_cart_page = AddToCart(appium_driver)
    add_to_cart_page.add_to_cart()


@then("Product should be added to the cart")
def product_in_cart(appium_driver):
    add_to_cart_page = AddToCart(appium_driver)
    add_to_cart_page.verify_cart()