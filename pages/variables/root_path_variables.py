import json
def load_config():
    with open(f"C://Users//166928//PycharmProjects//Mobile_App_Automation//MobileAppAutomation//config.json") as f:
        return json.load(f)

config = load_config()


root_path = config.get('folder_paths', {}).get('root_path')