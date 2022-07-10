import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
