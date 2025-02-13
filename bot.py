import os
from dotenv import load_dotenv
from nextcord.ext import commands

def main():
    client = commands.Bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # load all cogs
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()
Responses: {"?h": "Server IP: ge.terohost.com:3176", "!site": "Oops, we don't have a website!", "!owner": "@SauskeUchiha#6149 is the Owner", "!h": "{user} you can use command: !ip, !site, !owner. For help contact: SauskeUchiha#6149. Created by Dhruv"}
