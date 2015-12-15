import pip
from subprocess import call
print("pip install --upgrade pip")
for dist in pip.get_installed_distributions():
    print("pip install --upgrade " + dist.project_name)

