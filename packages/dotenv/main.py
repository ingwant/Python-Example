from dotenv import load_dotenv, dotenv_values
import os


# Get env path from porject folder
dotenv_path = None
for dirpath, dirnames, files in os.walk("."):
    if ".env" in files:
        dotenv_path = os.path.join(dirpath, ".env")
        break

# Method 2 ========================================================
# load environment variables from .env by dotenv_values()
config = dotenv_values(dotenv_path=dotenv_path)
user = config.get("USER")
password = config.get("PASSWORD")
print(user)
print(password)

