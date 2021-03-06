#!/usr/bin/env python
import os
import sys

#if __name__ == "__main__":
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bucksell.settings")
#
#    from django.core.management import execute_from_command_line
#
#    execute_from_command_line(sys.argv)
#!/usr/bin/env python
from os.path import abspath, dirname, join
from site import addsitedir
import sys
# adding external lib folder to the path.
path = addsitedir(abspath(join(dirname(__file__), '../libs')), set())
if path: sys.path = list(path) + sys.path

# updating python sys path to include project applications.

sys.path.insert(0, abspath(join(dirname(__file__), 'apps')))
sys.path.insert(0, abspath(join(dirname(__file__), 'external_apps')))
sys.path.insert(0, abspath(join(dirname(__file__), '../libs')))

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)