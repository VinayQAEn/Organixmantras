import os
import sys

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

from PageObject.Loginpage import Loginpage

print("Loginpage module imported successfully.")

