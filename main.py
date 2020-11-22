import json
from modules.dc_wrapper import DiscordWrapper


def main():
    with open("modules/files/discord_token.json") as f:
        discord_token = json.load(f)
        # {"token":"token_string"}
    DiscordWrapper.client.run(discord_token["token"])


if __name__ == "__main__":
    main()
