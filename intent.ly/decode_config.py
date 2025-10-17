import os
import re
import base64
import json

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "tm-demo.smarterclick.co.uk.js")
new_file_path = os.path.join(script_dir, "config-decoded.json")

try:
    with open(file_path, "r") as f:
        content = f.read()

    match = re.search(r"o:'([^']*)'", content)

    if match:
        base64_config = match.group(1)
        decoded_config_str = base64.b64decode(base64_config).decode("utf-8")

        # Pretty-print the JSON
        decoded_json = json.loads(decoded_config_str)

        with open(new_file_path, "w") as f:
            json.dump(decoded_json, f, indent=4)

        print(f"Decoded config saved to {new_file_path}")
    else:
        print("Could not find base64 config string.")

except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
