import re
import sys
import json

def translate_custom_code(custom_code, keyword_mapping):
    for custom, python in keyword_mapping.items():
        if custom:
            custom_code = re.sub(rf'\b{re.escape(custom)}\b', python, custom_code)
    return custom_code

def execute_custom_code(custom_code, keyword_mapping):
    try:
        python_code = translate_custom_code(custom_code, keyword_mapping)
        if len(sys.argv) > 2 and sys.argv[2] == "debug":
            print("Translated Python Code:\n", python_code)
        exec(python_code)
    except Exception as e:
        print(f"Error executing code: {e}")

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python translator.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]

    with open("syntax.json", "r") as file:
        keyword_mapping = json.load(file)

    try:
        with open(f"{file_name}.brl", "r") as file:
            custom_code = file.read()

        execute_custom_code(custom_code, keyword_mapping)
    except FileNotFoundError:
        print(f"Error: File '{file_name}.brl' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()