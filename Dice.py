from discord.ext import commands
import random


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send("Hello " + member.name + "!")

    @commands.group()
    async def flip(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid command. Try again!")

    @flip.command(name = "coin")
    async def flip_a_coin(self, ctx):
        coin = random.randint(0, 1)
        if coin == 0:
            await ctx.send("You got heads!")
        else:
            await ctx.send("You got tails!")

    @flip.command(name = "dice")
    async def flip_a_dice(self, ctx):
        dice = random.randint(1, 6)
        await ctx.send("You got " + str(dice))

    @flip.command(name = "custom")
    async def flip_custom(self, ctx, sides: int = 1):
        await ctx.send(random.randint(1, sides))


async def setup(bot):
    await bot.add_cog(Dice(bot))
