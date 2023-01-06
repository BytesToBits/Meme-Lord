from core.MemeBot import MemeBot, disnake, commands

class About(commands.Cog):
    def __init__(self, bot:MemeBot):
        self.bot = bot
    
    @commands.slash_command(
        name="about",
        description="Some information about our lord and savior.",
        dm_permission=True
    )
    async def about_cmd(self, inter:disnake.CommandInteraction):
        return await inter.send(embed=disnake.Embed(
            title="About: Meme Lord",
            description="**Meme Lord** is a fun meme-generator bot developed by [BytesToBits](https://bytestobits.dev/). With the use of slash commands, you can easily create the meme of your choice! Simply use </meme:1044315118487478332> followed by the type :)\nIf you ever wish to suggest new memes to be added, do not hesitate! Join the support server and ask.",
            color=disnake.Color.red()
        )
        .add_field(name="🛡️ **Support Server** 🛡️", value="[Join BytesToBits](https://discord.com/invite/u4qdg3EM8J)")
        .add_field(name="📜 **Guilds** 📜", value=str(len(self.bot.guilds)))
        )

def setup(bot):
    bot.add_cog(About(bot))