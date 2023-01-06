from datetime import datetime
import os
from disnake.ext import commands
import disnake

from .info import Bot

class MemeBot(commands.InteractionBot):
    def __init__(self, dev_mode=False):
        self.info = Bot
        self.dev_mode = dev_mode
        self.start_time = datetime.utcnow()

        guilds = self.info.GUILDS
        if dev_mode: guilds += self.info.DEV_EXTRA_GUILDS

        super().__init__(test_guilds=guilds or None, intents=disnake.Intents.default())

        COG_TREE = filter(lambda dir: not "__pycache__" in dir[0] ,os.walk("cogs"))

        for cog_branch in COG_TREE:
            dir = cog_branch[0]
            self.load_extensions(dir)
            print(f"Loaded Cogs ({dir}):", ', '.join(cog_branch[-1]))
        
        self.add_slash_command(commands.InvokableSlashCommand(self.shutdown, name="shutdown", description="Shut down the bot"))

        self.run(self.info.TOKEN if not dev_mode else self.info.DEV_TOKEN)

    async def on_ready(self):
        print("--------------------------------------")
        print("BOT HAS LOGGED IN AS", str(self.user))
        print("BOT ID:", self.user.id)
        print("GUILDS:", len(self.guilds))
        print("--------------------------------------")

    async def shutdown(self, inter:disnake.CommandInteraction):
        if not inter.author.id == self.info.OWNER: return await inter.send("You cannot execute this command!", ephemeral=True)

        await inter.send("Bot shutting down...")
        for slash_command in self.slash_commands:
            self.remove_slash_command(slash_command.name)

        await self._sync_application_commands()
            
        await self.close()