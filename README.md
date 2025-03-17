# 🚀 **Automated Amazon Application Flow**

Welcome to the **Automated Amazon Application Flow**! This project automates a real user's journey within the **Amazon mobile application**, from logging into the **Google Play Store**, installing the app, signing into **Amazon**, and adding products to the cart. 🛒📱

This is the perfect project for those looking to automate app testing on mobile platforms using modern tools like **Appium**, **Pytest**, and **Pytest-BDD**. 

---

### 🌟 **Key Features**:
- **🎮 Automated Play Store Login**: Seamlessly logs into the Google Play Store using **Appium** and an Android emulator.
- **📲 App Installation**: Searches for and installs the Amazon app from the Play Store automatically.
- **🛍️ Amazon Sign-In**: Automates the login process to Amazon with pre-configured credentials.
- **🛒 Add Product to Cart**: Automates browsing through various Amazon product categories and adds them to the shopping cart.
  
With these automations, this project ensures that the critical features of the Amazon app are tested effectively and efficiently.

---

### 🔧 **Technologies Used**:
- **Appium**: Open-source tool for automating mobile applications on Android and iOS.
- **Selenium**: Automates browser interactions for Amazon's website when necessary.
- **Python**: The core language for writing automation scripts and controlling the app flow.
- **Appium Inspector**: Tool for inspecting app elements to facilitate mobile automation.
- **Pytest**: Framework for organizing and executing tests.
- **Pytest-BDD**: Extension to Pytest that allows you to write tests in **Gherkin** syntax.
- **Android Studio**: IDE for managing Android emulators and SDKs.
- **Android Emulator**: Simulates mobile environments for testing.
- **pytest_report**: Plugin used for generating detailed reports on test execution.

---

### 🏁 **Setup**:
Follow these steps to get up and running:

1. **Clone the Repository**  
   Clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/amazon-automation-flow.git
   cd amazon-automation-flow
   ```

2. **Install Dependencies**  
   Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Android Emulator**  
   - Install **Android Studio** and set up an Android emulator.
   - Ensure that **ADB** tools are properly configured.

4. **Install Appium**  
   Install **Appium** globally to run mobile tests.
   ```bash
   npm install -g appium
   ```

5. **Start the Appium Server**  
   Run the Appium server to interact with the mobile application.
   ```bash
   appium
   ```

6. **Run the Automation Scripts**  
   You can run the tests with Pytest and see the magic unfold! 💫
   ```bash
   pytest <your_test_file>.py
   ```

---

### 📝 **Task Implementations**:

The following tasks are automated in this project:

1. **Login to Google Play Store**:  
   Automates logging into the Google Play Store to gain access to the app store.

2. **Search and Download Amazon App**:  
   Searches for the Amazon app on the Play Store and automates its download and installation.

3. **Launch the Amazon App**:  
   After installation, the script launches the Amazon app on the emulator.

4. **Login to Amazon**:  
   Automatically logs into the Amazon app using pre-configured credentials.

5. **Add Products from Various Categories to Cart**:  
   Automates product searches in different categories and adds them to the shopping cart.

---

### 🏃‍♂️ **Running Tests with BDD**:

If you're using **Pytest-BDD**, you can write your tests using **Gherkin syntax** in `.feature` files. These files make it easy to express tests in a natural language format.

Example `.feature` file:

```gherkin
Feature: Login Amazon

  @id:amazon_login
  Scenario: Go to Amazon and login
    Given Amazon application is installed on device
    When User tries to login in amazon application
    Then User should be able to access amazon application
```

To run the BDD tests:
```bash
pytest -m "id:amazon_login" -v -s
```

This command will execute the test scenarios and generate detailed test reports in HTML format.

---

### 📊 **Logs and Reports**:

- **Android Logs**: Android logs are captured during the test execution and can be found in the `logs/` directory or via **Appium Inspector**.
  
- **Command Line Logs**: Command-line output logs are captured to help with debugging and traceability.
  
- **Test Reports**: Use `pytest` to generate HTML reports with a detailed breakdown of the tests executed. Example:
  ```bash
  pytest --html=report.html
  ```

These reports include information on each test step, execution status (pass/fail), and logs, making it easier to understand test results.

---

### 🛠 **Customization Tips**:

- **Project Setup**: Feel free to modify the project setup instructions based on your environment and workflow.
- **Requirements File**: Ensure your **`requirements.txt`** contains all the necessary dependencies like `pytest`, `appium-python-client`, etc.
- **Change Sender Email**: If you are sending test reports via email, remember to update the sender email address in your configuration.

---

### ✨ **Contributing**:

We welcome contributions! If you'd like to improve the code or add new features, feel free to fork the repository and submit a pull request. 

---

### 🎉 **Enjoy Testing!**  
Start automating your Amazon app tests today and save valuable time. Let the automation magic happen! ✨

---

🔗 **Follow** the project to stay updated with new features and improvements.
