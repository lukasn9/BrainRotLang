import re
import sys

keyword_mapping = {
    "no cap": "False",
    "literally nothing": "None",
    "big cap": "True",
    "sigma male": "and",
    "rizzing up": "as",
    "gyatt": "assert",
    "sussy imposter": "async",
    "four": "await",
    "bussing": "break",
    "biggest bird": "class",
    "monday left me broken": "continue",
    "kai cenat": "def",
    "grimace shake": "del",
    "livvy dunne": "elif",
    "goofy ahh": "else",
    "freddy fazbear": "except",
    "john pork": "finally",
    "skibidi": "for",
    "backrooms": "from",
    "baby gronk": "global",
    "sisyphus": "if",
    "quandale dingle": "import",
    "shadow wizard money gang": "in",
    "poggers": "is",
    "fanum tax": "lambda",
    "delulu": "nonlocal",
    "rizz": "not",
    "the ocky way": "or",
    "uwu": "pass",
    "t-pose": "raise",
    "based": "return",
    "did you pray today": "try",
    "ambatukam": "while",
    "blud": "with",
    "thug shaker": "yield",
    "not the mosquito again": "not in",
    "ayo the pizza here": "print",
    "nair waxing": "input",
    "lightskin stare": "len",
    "garten of banban": "range",
    "pizza tower": "open",
    "fortnite battle pass": "sum",
    "goated with the sauce": "type"
}

def translate_custom_code(custom_code):
    for custom, python in keyword_mapping.items():
        if custom:
            custom_code = re.sub(rf'\b{re.escape(custom)}\b', python, custom_code)
    return custom_code

def execute_custom_code(custom_code):
    try:
        python_code = translate_custom_code(custom_code)
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

    try:
        with open(f"{file_name}.brl", "r") as file:
            custom_code = file.read()

        execute_custom_code(custom_code)
    except FileNotFoundError:
        print(f"Error: File '{file_name}.brl' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()