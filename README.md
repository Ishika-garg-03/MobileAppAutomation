# Mobile App Automation - Amazon App
 
This project automates various tasks on the Amazon mobile application for testing purposes. The automation includes tasks like logging into the Play Store, searching for and downloading the Amazon app, launching the app, logging into Amazon, and adding different products from various categories to the cart.
 
The project leverages Pytest, Pytest-BDD, Appium, and several other tools for efficient automation testing.
 
## Table of Contents
 
- [Introduction](#introduction)
- [Project Setup](#project-setup)
- [Task Implementations](#task-implementations)
- [Technologies Used](#technologies-used)
- [Running Tests](#running-tests)
- [Logs and Reports](#logs-and-reports)

 
## Introduction
 
The goal of this project is to automate the process of interacting with the **Amazon mobile application** on an Android device. The tasks automated in this project help ensure that the critical features of the app work seamlessly and efficiently.
 
## Project Setup
 
Follow the steps below to set up the environment for running the tests.
 
### Prerequisites
 
1. **Python** (>=3.10)
2. **PyCharm** IDE (or any preferred IDE)
3. **Android Studio** (for Android emulator and debugging)
4. **Appium Server** (for automating mobile actions)
5. **Appium Inspector** (for inspecting mobile app elements)
6. **Appium** Python client library
7. **Pytest** and **Pytest-BDD** for writing and executing tests
8. **Android SDK** and **ADB** tools for Android device interaction
9. **pytest_report** for test report generation
 
### Install Required Dependencies
 
Clone the repository and install the necessary Python dependencies:
 
```bash
git clone <your-repo-url>
cd <your-project-directory>
pip install -r requirements.txt
```
 
Make sure to also install **Appium** and configure the Android emulator or device properly.
 
### Setting Up Appium Server
 
1. Install **Appium** globally:
   ```bash
   npm install -g appium
   ```
2. Start the Appium server:
   ```bash
   appium
   ```
 
## Task Implementations
 
The following tasks have been automated in the project:
 
1. **Login to Google Play Store**: 
   - Automated login to the Google Play Store to access the app store.
2. **Search and Download Amazon from Play Store**:
   - Search for the Amazon app on the Play Store and automate its download and installation on an Android device/emulator.
 
3. **Launch Amazon App**:
   - Launch the Amazon app after successful installation.
 
4. **Login to Amazon**:
   - Automate the login process to Amazon using pre-configured user credentials.
 
5. **Add Products from Different Categories to Cart**:
   - Search for various products across different categories and add them to the shopping cart.
 
## Technologies Used
 
- **PyCharm**: Python IDE used for writing and executing the test scripts.
- **Pytest**: Framework used for organizing and executing the tests.
- **Pytest-BDD**: A behavior-driven development (BDD) extension for Pytest, used for writing tests in a more readable and natural language format.
- **Appium**: An open-source tool used for automating mobile applications, both on Android and iOS.
- **Android Studio**: IDE used to manage Android emulators and Android SDKs.
- **Appium Inspector**: Tool for inspecting the mobile app and its elements.
- **pytest_report**: Plugin used to generate detailed test execution reports.
- **Android Logs**: Capturing device logs during the test execution.
- **Command Line Logs**: Capturing command-line output logs for debugging and traceability.
 
## Running Tests
 
To run the tests, follow these steps:
 
1. **Ensure that the Appium server is running**. If not, start it by running `appium` from the terminal.
2. Open **PyCharm** (or your preferred IDE) and run the tests using **Pytest**.
   ```bash
   pytest <your_test_file>.py
   ```
 
You can run all the tests or individual test files based on your need.
 
### Running Tests with BDD
 
If using **Pytest-BDD**, tests are written in a more natural language format using **.feature** files. These files contain the Gherkin syntax with **Given-When-Then** steps.
 
Example `.feature` file:
 
```gherkin
Feature: Login Amazon

  @id:amazon_login
  Scenario: Go to Amazon and login
    Given Amazon application is installed on device
    When Try to login in amazon application
    Then User will be able to access amazon application
```
 
You can run these BDD-style tests by executing:
 
```bash
pytest -m "id:amazon_login" -v -s
```
 
This will execute the tests and generate reports in HTML format. You can also customize the output and execution formats according to your needs.
 
## Logs and Reports
 
### Android Logs
 
During test execution, Android logs are captured for debugging and analyzing test behavior. Logs can be found in the `logs/` directory or in the **Appium Inspector**.
 
### Command Line Logs
 
Command-line output logs are also captured and stored, helping with test traceability and debugging any issues with the execution.
 
### Test Reports
 
Test reports are enhanced with a **description column**, providing more context and insights into each step and scenario during test execution. The reports will give a detailed summary of the tests executed, their status (pass/fail), and logs associated with them.
 
Example of running the tests with reports:
 
```bash
pytest --html=report.html
```
 
This will generate an HTML report after the test execution is completed, including a description column for each step in the test.
 


 
### Customization Tips:
- Update the **project setup instructions** based on your specific project structure.
- Add or remove any tools, dependencies, or steps based on your project’s workflow.
- Ensure that you have a **requirements.txt** file listing all dependencies (e.g., pytest, appium-python-client).
- If you want to change the sender email while sending reports make sure to change the app key.
 
