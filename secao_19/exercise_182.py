# Import the os module
import os

# Import math module as an alias called my_math
import math as my_math

#Import everything from random module. All names will be accessed 
# directly without random.name 
from random import *

import requests
r = requests.get('https://rspiolirf.netlify.com')
print(r.text)

#%%
print(sys.stdout)