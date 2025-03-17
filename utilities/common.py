import os
import time
from skimage.metrics import structural_similarity as ssim
import cv2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.variables.device_variables import deviceID
from utilities.logger import *
from conftest import appium_driver
from pages.variables.teardownProcess_variables import *
import subprocess
logger = setup_logger()


# Check if app is launched
def launch_check(driver, current_Activity):
    ele1 = driver.current_activity
    if ele1 == current_Activity:
        return True
    return False

def sleep():
    time.sleep(7)


def locator_sleep(item_to_find, appium_driver):
    wait = WebDriverWait(appium_driver, 200)
    by_method = AppiumBy.ANDROID_UIAUTOMATOR
    wait.until(EC.element_to_be_clickable((by_method, item_to_find)))


# check if the device is connected to a network
def is_device_connected():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if deviceID in result.stdout:
        return True
    return False

def device_status():
    logger.info("Checking if Device is on and connected")
    if not is_device_connected():
        pytest.fail("Device is not connected or recognized")
        logger.error("Device is off or not connected to network")
    else:
        logger.info("Found device on and connected to network")

def check_login(key, driver):
    content=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,key)
    assert content.is_displayed()==True
    return True

def displayFunction(appium_driver, button):
    a = appium_driver.find_element(AppiumBy.CLASS_NAME, button).is_displayed()
    assert a, logger.error("Play store is not launched")


def uninstall(appium_driver):
    if appium_driver.is_app_installed(app_package):
        appium_driver.remove_app(app_package)
        print("App Uninstalled")
    else:
        print("App not Found")

def logout(appium_driver):
    appium_driver.terminate_app(ps_package)
    appium_driver.activate_app(ps_package)
    click(appium_driver,profile_icon)
    click(appium_driver,drop_down)
    click(appium_driver,manage)
    click(appium_driver,layout_page)
    click(appium_driver,remove_btn)
    click(appium_driver,confirm_btn)
    appium_driver.terminate_app(settings)
    appium_driver.terminate_app(ps_package)

def click(appium_driver, button):
    appium_driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, button).click()

def send_keys(appium_driver, button, text, code):
    if code == 'a':
        appium_driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, button).send_keys(text)
    elif code == 'c':
        appium_driver.find_element(AppiumBy.CLASS_NAME, button).send_keys(text)

def click_button(appium_driver, button): #xpath
    appium_driver.find_element(AppiumBy.XPATH, button).click()

def click_btn(appium_driver, button): #class
    appium_driver.find_element(AppiumBy.CLASS_NAME, button).click()


def swipe(appium_driver, element_id, direction):
    appium_driver.execute_script('mobile: swipeGesture', {
        'elementId': element_id,
        'direction': direction,
        'percent': 1,
        'speed': 1000
    })


# scroll until element visible
def scroll_until_element_visible(appium_driver, element_locator):
    while True:
        try:
            element = appium_driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, element_locator)
            if element.is_displayed():
                logger.info(f"Element found and is visible: {element_locator}")
                break
        except Exception as e:
            appium_driver.swipe(0, 800, 0, 400)  # Adjust swipe coordinates as necessary
            time.sleep(1)


def screenshot(appium_driver, filename):
    appium_driver.get_screenshot_as_file(filename)


def compare_images(image1_path, image2_path):
    # Read images using OpenCV
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    score, _ = ssim(img1, img2, full=True)
    # print("similarity index is", score)
    return score


def screenshot_compare(appium_driver, reference_image_path, test_case_name):
    timestamp = datetime.now().strftime('%m-%d-%Y_%I-%M-%S_%p')
    screenshot_path = f"{root_path}\\screenshots\\{test_case_name}_{timestamp}.png"
    screenshot(appium_driver, screenshot_path)
    sleep()
    similarity_score = compare_images(screenshot_path, reference_image_path)
    print(f"Similarity score for {test_case_name}: {similarity_score:.2f}")
    if similarity_score >= 0.75:
        print(f"Test case '{test_case_name}' passed.")
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            print(f"Screenshot for '{test_case_name}' removed after passing.")
        return True
    else:
        print(f"Test case '{test_case_name}' failed.")
        failed_screenshot_path = f"screenshots/{test_case_name}_failed_{timestamp}.png"
        os.rename(screenshot_path, failed_screenshot_path)
        print(f"Screenshot for failed test case saved at: {failed_screenshot_path}")
        return False


@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    outcome = yield
    report = outcome.get_result()
    # Extract Given-When-Then steps
    report.scenario = {
        "steps": [{"keyword": step.keyword, "name": step.name} for step in scenario.steps]
    }