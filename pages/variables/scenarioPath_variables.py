from utilities.logger import config

playstore_features = config.get('scenario_paths', {}).get('login_playstore')
amazon_install_features = config.get('scenario_paths', {}).get('install_amazon')
amazon_signin_features = config.get('scenario_paths', {}).get('signin_amazon')