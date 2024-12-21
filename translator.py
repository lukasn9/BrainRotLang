import re
import sys

keyword_mapping = {
    "delulu": "False",
    "backrooms": "None",
    "gigachad": "True",
    "ratio": "and",
    "bird": "as",
    "uwu": "assert",
    "grindset": "async",
    "monday_left_me_broken": "await",
    "ambatukam": "break",
    "sigma_male": "class",
    "literally_hitting_the_griddy": "continue",
    "shadow_wizard_money_gang": "def",
    "poof": "del",
    "butwhatif": "elif",
    "only_in_ohio": "else",
    "not_the_mosquito_again": "except",
    "whopper_whopper_whopper_whopper": "finally",
    "baby_gronk": "for",
    "sin_city": "from",
    "the_ocky_way": "global",
    "kiki_do_you_love_me": "if",
    "grabdat": "import",
    "insidey": "in",
    "izzit": "is",
    "pibby_glitch": "lambda",
    "no_insidey": "nonlocal",
    "nahfam": "not",
    "thisorthat": "or",
    "fanum_tax": "pass",
    "goated_with_the_sauce": "raise",
    "gibback": "return",
    "givashot": "try",
    "thug_shaker": "while",
    "togetha": "with",
    "handover": "yield",
    "poggers": "+",
    "": "-",
    "fortnite_battle_pass": "*",
    "sliceyslice": "/",
    "chunkydive": "//",
    "leftoverbit": "%",
    "supahpowah": "**",
    "sussy_no_imposter": "==",
    "sussy_imposter": "!=",
    "smolr": "<",
    "biggr": ">",
    "smolorequal": "<=",
    "bigorequal": ">=",
    "setdat": "=",
    "plusandset": "+=",
    "minusandset": "-=",
    "starmultiset": "*=",
    "slicenset": "/=",
    "": "or",
    "": "not",
    "": "is",
    "": "in",
    "": "not in",
    "": "print",
    "": "input",
    "": "len",
    "": "range",
    "": "open",
    "": "sum",
    "": "type",
    "shadowwizardgang": "#"
}

def translate_custom_code(custom_code):
    for custom, python in keyword_mapping.items():
        custom_code = re.sub(rf'\b{custom}\b', python, custom_code)
    return custom_code

def execute_custom_code(custom_code):
    python_code = translate_custom_code(custom_code)
    exec(python_code)

file_name = sys.argv[1]
file_name, file_extension = file_name.split(".")

with open(f"{file_name}.brl") as file:
    custom_code = file.read()

execute_custom_code(custom_code)