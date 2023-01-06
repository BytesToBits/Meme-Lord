from typing import Final

class Bot:
    OWNER: Final = 123456789012345678
    TOKEN: Final = "bot_token"
    DEV_TOKEN: Final = "dev_bot_token" # Required to run it with the --dev flag ;c
    ID: Final = 123456789012345678 # bot client id
    GUILDS: Final = [] # leave empty if you want the bot to be global. it's passed as the "test_guilds" in bot initialization
    DEV_EXTRA_GUILDS: Final = [862481678722793493]