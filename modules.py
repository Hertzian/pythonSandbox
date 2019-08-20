# A module is basically a file containing a ser of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# pip modules
# import camelcase

# custom modules
# import validator
# from validator import validate_email

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()

camel = camelcase.CamelCase()

text = 'Hello there world'
print(camel.hump(text))

email = 'test@test.com'
if validator.validate_email(email):
    print('email is valid')
else:
    print('Not an email')