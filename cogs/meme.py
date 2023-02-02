from io import BytesIO

from core.MemeBot import MemeBot, disnake, commands
from core.images.memes import *
from core.videos.memes import *

class MemeMain(commands.Cog):
    def __int__(self, bot:MemeBot):
        self.bot = bot
    
    @commands.slash_command(
        name="meme",
        description="Meme Commands"
    )
    async def meme(self, _): return

    @meme.sub_command(
        name="fate",
        description="Un la Fate el Decida",
        options=[
            disnake.Option(
                name="thread_text",
                description="text of the thread",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="scissors_text",
                description="text of the lady holding scissors",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="right",
                description="text of the lady on the right",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def fate_cmd(self, inter:disnake.CommandInteraction, thread_text:str, scissors_text:str, right:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: fate(thread_text, scissors_text, right))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="megamind",
        description="No brain?",
        options=[
            disnake.Option(
                name="text",
                description="hmmm",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def megamind_cmd(self, inter:disnake.CommandInteraction, text:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: megamind(text))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="monke",
        description="Return to monke.",
        options=[
            disnake.Option(
                name="third_monke_name",
                description="The name of Monke DREI.",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="third_monke_text",
                description="The text of Monke DREI.",
                type=disnake.OptionType.string,
                required=False
            ),
            disnake.Option(
                name="first_monke",
                description="EIN.",
                type=disnake.OptionType.string,
                required=False
            ),
            disnake.Option(
                name="second_monke",
                description="ZWEI.",
                type=disnake.OptionType.string,
                required=False
            ),
        ]
    )
    async def monke_command(self, inter:disnake.CommandInteraction, third_monke_name:str, third_monke_text:str="", first_monke:str="", second_monke:str=""):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: monke(first_monke, second_monke, third_monke_name, third_monke_text))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="obama",
        description="Mr President?",
        options=[
            disnake.Option(
                name="receiver",
                description="Text of the obama who receivers the medal.",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="giver",
                description="Text of the obama who gives the medal.",
                type=disnake.OptionType.string,
                required=True
            ),
        ]
    )
    async def obama_cmd(self, inter:disnake.CommandInteraction, receiver:str, giver:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: obama(receiver, giver))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="wtfdidyoujustdo",
        description="Wtf",
        options=[
            disnake.Option(
                name="user",
                description="Deported",
                type=disnake.OptionType.user,
                required=True
            ),
            disnake.Option(
                name="amount",
                description="how bad did they do (default: 10)",
                type=disnake.OptionType.integer,
                required=False,
                min_value=1,
                max_value=100
            ),
            disnake.Option(
                name="duration",
                description="how long should they suffer for (default: 80)",
                type=disnake.OptionType.integer,
                required=False,
                min_value=80,
                max_value=160
            )
        ]
    )
    async def wtfDidYouJustDo_cmd(self, inter:disnake.CommandInteraction, user:disnake.Member, amount=10, duration=80):
        amount = int(amount)
        duration = int(duration)

        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: wtfdidyoujustdo(user.display_avatar.with_size(512), amount, duration))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="worldwide",
        description="Mr World Wide.",
        options=[
            disnake.Option(
                name="text",
                description="whomst the chosen one?",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="member",
                description="whomst the chosen one vol 2?",
                type=disnake.OptionType.user,
                required=True
            )
        ]
    )
    async def worldwide_cmd(self, inter:disnake.CommandInteraction, text:str, member:disnake.User):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: worldwide(text, member.display_avatar))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="stat",
        description="What gives out the most energy?",
        options=[
            disnake.Option(
                name="stat",
                description="WHAT?",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def stat_cmd(self, inter:disnake.CommandInteraction, stat:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: stats(stat))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="what",
        description="what",
        options=[
            disnake.Option(
                name="main",
                description="huh",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="image",
                description="Just put one",
                type=disnake.OptionType.attachment,
                required=True
            ),
            disnake.Option(
                name="sub",
                description="huh vol 2",
                type=disnake.OptionType.string,
                required=False
            )
        ]
    )
    async def what_cmd(self, inter:disnake.CommandInteraction, main:str, image:disnake.Attachment, sub:str=""):
        await inter.response.defer(with_message=True)

        image = BytesIO(await image.read())

        FILE = await inter.bot.loop.run_in_executor(None, lambda: what(image, main, sub))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="we-are-not-the-same",
        description="I am a command. You're a user. We are not the same.",
        options=[
            disnake.Option(
                name="top_text",
                description="Top",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="bottom_text",
                description="Bottom",
                type=disnake.OptionType.string,
                required=True
            ),
        ]
    )
    async def we_are_not_the_same_cmd(self, inter:disnake.CommandInteraction, top_text:str, bottom_text:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: we_are_not_the_same(top_text, bottom_text))
        return await inter.edit_original_message(file=FILE)
    
    @meme.sub_command(
        name="stuff",
        description="He is admini",
        options=[
            disnake.Option(
                name="text",
                description="Text",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def stuff(self, inter:disnake.CommandInteraction, text:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: stuff_admini(text))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="our",
        description="🔨",
        options=[
            disnake.Option(
                name="image",
                description="Gib",
                type=disnake.OptionType.attachment
            ),
            disnake.Option(
                name="user",
                description="Or gib",
                type=disnake.OptionType.user
            )
        ]
    )
    async def our(self, inter:disnake.CommandInteraction, image:disnake.Attachment=None, user:disnake.Member=None):
        if not image and not user: return await inter.send("You must specify an image or a user!", ephemeral=True)

        await inter.response.defer(with_message=True)
        image = BytesIO(await image.read() if image else await user.display_avatar.read())

        FILE = await inter.bot.loop.run_in_executor(None, lambda: communist(image))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="insanity",
        description="ITS INSANE",
        options=[
            disnake.Option(
                name="image",
                description="provide an example of insanity",
                type=disnake.OptionType.attachment,
                required=True
            ),
            disnake.Option(
                name="description",
                description="Describe what da hell",
                type=disnake.OptionType.string,
                required=False
            )
        ]
    )
    async def insanity_cmd(self, inter:disnake.CommandInteraction, image:disnake.Attachment, description:str="A common example of insanity"):
        await inter.response.defer(with_message=True)

        image = BytesIO(await image.read())

        FILE = await inter.bot.loop.run_in_executor(None, lambda: insanity(image, description))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="at-home",
        description="We have it at home.",
        options=[
            disnake.Option(
                name="image",
                description="what's at home",
                type=disnake.OptionType.attachment,
                required=True
            ),
            disnake.Option(
                name="thing",
                description="what's at home",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def at_home(self, inter:disnake.CommandInteraction, image:disnake.Attachment, thing:str):
        await inter.response.defer(with_message=True)

        image = BytesIO(await image.read())

        FILE = await inter.bot.loop.run_in_executor(None, lambda: thing_at_home(image, thing))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="mass",
        description="wat the mass of you",
        options=[
            disnake.Option(
                name="thing",
                description="no thing indeed",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def mass(self, inter:disnake.CommandInteraction, thing:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: mass(thing))
        return await inter.edit_original_message(file=FILE)
    
    @meme.sub_command(
        name="jason",
        description="interesting",
        options=[
            disnake.Option(
                name="topic",
                description="why is jason important",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="description",
                description="why is jason important but detailed",
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )
    async def jason(self, inter:disnake.CommandInteraction, topic:str, description:str):
        await inter.response.defer(with_message=True)

        FILE = await inter.bot.loop.run_in_executor(None, lambda: jason(topic, description))
        return await inter.edit_original_message(file=FILE)

    @meme.sub_command(
        name="out-of-context",
        description="do not tell them",
        options=[
            disnake.Option(
                name="text",
                description="what is out of context?",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="attachment",
                description="Just put one",
                type=disnake.OptionType.attachment,
                required=True
            )
        ]
    )
    async def out_of_context(self, inter:disnake.CommandInteraction, text:str, attachment:disnake.Attachment):
        await inter.response.defer(with_message=True)

        is_image = "image" in attachment.content_type

        if is_image:
            attachment = BytesIO(await attachment.read())
        else:
            filename = f"temp/{inter.author.id}-{attachment.filename}"
            await attachment.save(filename)

        FILE, clear = await inter.bot.loop.run_in_executor(None, lambda: out_of_context(attachment if is_image else filename, text, is_image))
        await inter.edit_original_message(file=FILE)
        clear()

    @meme.sub_command(
        name="how",
        description="How",
        options=[
            disnake.Option(
                name="text",
                description="huh",
                type=disnake.OptionType.string,
                required=True
            ),
            disnake.Option(
                name="attachment",
                description="How???",
                type=disnake.OptionType.attachment,
                required=True
            )
        ]
    )
    async def how_cmd(self, inter:disnake.CommandInteraction, text:str, attachment:disnake.Attachment):
        await inter.response.defer(with_message=True)

        if not "image" in attachment.content_type and not "video" in attachment.content_type:
            return await inter.send("Please upload only videos or images!", ephemeral=True)

        if attachment.size > 5242880:
            return await inter.send("The maximum attachment size is 5MB! Try again.", ephemeral=True)

        is_image = "image" in attachment.content_type

        if is_image:
            attachment = BytesIO(await attachment.read())
        else:
            filename = f"temp/{inter.author.id}-{attachment.filename}"
            await attachment.save(filename)

        FILE, clear = await inter.bot.loop.run_in_executor(None, lambda: how(attachment if is_image else filename, text, is_image))
        await inter.edit_original_message(file=FILE)
        clear()


def setup(bot):
    bot.add_cog(MemeMain(bot))