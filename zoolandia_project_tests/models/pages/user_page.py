from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()
user_login = os.getenv("USER_LOGIN")
user_pass = os.getenv("USER_PASSWORD")
user_name = os.getenv("USER_NAME")


@dataclass
class User:
    login: user_login
    password: user_pass
    name: user_name


test_user = User(login=user_login, password=user_pass, name=user_name)
