# This script converts YAML files to JSON format.
# Usage: python yaml2json.py file1.yaml file2.yaml ...
# It reads each YAML file specified in the command line arguments,
# converts its content to JSON, and saves it with the same name but with a .json extension.


import yaml
import json
from sys import argv

for yaml_path in argv[1:]:
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    
    json_path = yaml_path.replace('.yaml', '.json')
    with open(json_path, 'w') as json_file:
        json.dump(yaml_data, json_file, indent=4)
    
    print(f"Converted {yaml_path} to {json_path}")



