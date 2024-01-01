import sys
print(sys.path)

import os
from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe_project.settings'
execute_from_command_line(["manage.py", "runserver"])
