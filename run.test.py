import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system('pytest')
os.system('coverage run -m --omit="*/tests*" unittest discover')
os.system('coverage report')

