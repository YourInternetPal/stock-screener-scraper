from dotenv import load_dotenv
import os


load_dotenv()
REQUIRED_DATA = os.environ['REQUIRED_DATA'].split(",")
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(",")