import re
import sys

PIP_SLUG_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
pip_slug = "{{cookiecutter.pip_slug}}"
if not re.match(PIP_SLUG_REGEX, pip_slug):
    print(f"ERROR: The pip slug ({pip_slug}) is not a valid Pip name. Please do not use a _ and use - instead")
    # Exit to cancel project
    sys.exit(1)

MODULE_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{cookiecutter.module_name}}"
if not re.match(MODULE_NAME_REGEX, module_name):
    print(f"ERROR: The module name ({module_name}) is not a valid Python module name. Please do not use a - and use _ instead")
    # Exit to cancel project
    sys.exit(1)