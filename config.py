import os

"""
load_env function reads the .env file and sets environment variables.
"""

def load_env():
    if os.path.exists('.env'):
        try:
            with open('.env', 'r') as f:
                for line in f:
                    if line.strip():
                        key, value = line.strip().split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        os.environ[key] = value 
        except Exception as e:
            print(f"Error loading .env file: {e}")

load_env()


"""
CONFIG VARIABLES
USERNAME_MIN_LENGTH is the minimum length for usernames.
USERNAME_MAX_LENGTH is the maximum length for usernames.
MIN_PASSWORD_LENGTH is the minimum length for user passwords.
MAX_PASSWORD_LENGTH is the maximum length for user passwords.
GAME_MIN_SCORE is the minimum score a game or review can have.
GAME_MAX_SCORE is the maximum score a game or review can have.

SECRET_KEY is used for session management and CRSF protection.
"""

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 10
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 16
GAME_MIN_SCORE = 0
GAME_MAX_SCORE = 10

SECRET_KEY = os.getenv("SECRET_KEY")
