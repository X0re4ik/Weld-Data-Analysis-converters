import os
from dotenv import load_dotenv

load_dotenv('.env')

USERNAME    = os.environ["DATABASE_USERNAME"]
PASSWORD    = os.environ["DATABASE_PASSWORD"]

HOSTNAME    = os.environ["DATABASE_HOST_NAME"]
PORT        = os.environ["DATABASE_PORT"]
DATABASE    = os.environ["DATABASE_NAME"]

DB_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'