import os

env_message = os.environ.get("MESSAGE", "No message specified")
print(env_message)
