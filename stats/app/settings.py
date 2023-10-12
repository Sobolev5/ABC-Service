import os
import logging
from rich.logging import RichHandler
from dotenv import load_dotenv
load_dotenv()

# COMMON
DEBUG = os.getenv("DEBUG") == "1"
APP_UID = os.getenv("APP_UID", __name__)

# POSTGRES
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_URI = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# KAFKA
KAFKA_URI = os.getenv("KAFKA_URI")

# LOGGING
logging.basicConfig(format='%(filename)s (%(lineno)d): %(message)s', level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger("rich")

# TESTS
POSTGRES_URI_TEST_ASYNC = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/test"
POSTGRES_URI_TEST_SYNC = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/test"