import os

from dotenv import load_dotenv

load_dotenv()

app_port = os.getenv("APP_PORT")
host = os.getenv("HOST")
password_db = os.getenv("PASSWORD_DB")
localhost = os.getenv("LOCALHOST")
name_db = os.getenv("NAME_DB")
postgres_user = os.getenv("POSTGRES_USER")
port_db = os.getenv("PORT_DB")
