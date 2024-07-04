import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise RuntimeError('BOT_TOKEN environment variable is not set.')


# DB_PARAMS = {
#     'host': os.getenv('db_host'),
#     'database': os.getenv('db_name'),
#     'port': int(os.getenv('db_port')),
#     'user': os.getenv('db_user'),
#     'password': os.getenv('db_pwd')
# }

# if not all(DB_PARAMS.values()):
#     raise RuntimeError('Database parameters environment variables are not set.')