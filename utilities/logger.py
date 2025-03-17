import json
import logging
from datetime import datetime
import pytest
import base64
from pages.variables.root_path_variables import root_path


# Function to set up logger
def setup_logger():
    current_time = datetime.now().strftime('%m-%d-%Y_%I-%M-%S_%p')
    log_file_path = f"{root_path}\\utilities\\logs\\{current_time}.log"
    logging.basicConfig(
        format='%(asctime)s: %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG,
        filename=log_file_path
    )
    logger = logging.getLogger("AppiumTestLogger")
    return logger


# Log capture function for pytest tests
def log_common():
    @pytest.fixture(autouse=True)
    def attach_logs(request):
        if hasattr(request.node, "log_capture"):
            request.node.log_capture = request.node.funcargs.get("log_capture")


# Function to capture adb logcat logs
def capture_logcat():
    try:
        # Run adb logcat command and capture output in real-time
        logcat_process = subprocess.Popen(
            ["adb", "logcat"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Continuously read and capture the output
        logs = ""
        for stdout_line in iter(logcat_process.stdout.readline, ""):
            logs += stdout_line
            # Check if the line contains base64-encoded data
            if "data={" in stdout_line and "iVBORw0KGgoAAAANS" in stdout_line:
                decoded_data = decode_base64(stdout_line)
                save_decoded_data(decoded_data)

        logcat_process.stdout.close()
        logcat_process.wait()

        if logs:
            return logs
        else:
            return "No logs captured."

    except Exception as e:
        return f"Failed to capture logcat: {str(e)}"


# Function to decode base64 data and save it as a file
def decode_base64(data):
    # Extract base64 string from the log (you may need to adjust the exact substring to fit your log format)
    base64_string = data.split("data={")[-1]
    base64_string = base64_string.split("iVBORw0KGgoAAAANS")[0]  # Adjust as needed to get the base64 part

    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(base64_string)
        return decoded_data
    except Exception as e:
        return f"Failed to decode base64 data: {str(e)}"


# Function to save the decoded base64 data to an image file
def save_decoded_data(decoded_data):
    try:
        # Save the decoded data (e.g., as a PNG image)
        file_path = f"{root_path}\\utilities\\logs\\screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        with open(file_path, 'wb') as file:
            file.write(decoded_data)
        print(f"Base64-encoded image saved to: {file_path}")
    except Exception as e:
        print(f"Failed to save decoded data: {str(e)}")


# Function to capture logs based on specific adb command
def capture_adb_logs(command):
    try:
        # Run any given adb command
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.stderr:
            raise Exception(f"Error running ADB command: {result.stderr}")
        return result.stdout
    except Exception as e:
        return f"Failed to capture ADB logs: {str(e)}"


# Function to capture Appium-related logs (if needed)
import subprocess
import threading


def get_appium_logs():
    try:
        logcat_process = subprocess.Popen(
            ["adb", "logcat", "-v", "time"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        logs = []

        def read_logs():
            for line in iter(logcat_process.stdout.readline, ""):
                logs.append(line)

        # Read logs in a separate thread
        log_thread = threading.Thread(target=read_logs, daemon=True)
        log_thread.start()

        # Let it run for 20 seconds (adjust if needed)
        log_thread.join(timeout=20)

        logcat_process.terminate()  # Stop logcat

        return "".join(logs) if logs else "No logs captured."

    except Exception as e:
        return f"Failed to capture Appium logs: {str(e)}"


# Function to load configuration from a JSON file
def load_config():
    try:
        with open("C:\\Users\\166928\\PycharmProjects\\Mobile_App_Automation\\MobileAppAutomation\\config.json") as f:
            return json.load(f)
    except Exception as e:
        return f"Failed to load config: {str(e)}"


# Load configuration
config = load_config()
