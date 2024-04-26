import discord
from discord.ext import commands

intents = discord.Intents.default().all()

bot = commands.Bot(command_prefix = "!", intents = intents)


@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)
    print("Bot id:", bot.user.id)


@bot.command(name = "ping")
async def ping(ctx, times: int = 1):
    for i in range(times):
        await ctx.send(f"Pong!")


@bot.group(name = "mod")
async def mod_group(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid subcommand")


@mod_group.command()
async def tag(ctx, member):
    await ctx.send(member)


@bot.command(name = "info")
async def info(ctx):
    server_name = ctx.guild.name
    member_count = ctx.guild.member_count
    server_roles = ctx.guild.roles
    server_roles_str = ""
    for role in server_roles:
        server_roles_str += f"{role.name}\n"

    message = f"Server Name: {server_name} \nMembers: {member_count} \nServer Roles: {server_roles_str}\n"

    embed = discord.Embed(title = "Server info", description = "Information about the server", color = 0x00ff00)
    embed.add_field(name = "Server Name", value = server_name, inline = False)
    embed.add_field(name = "Members", value = member_count, inline = False)
    embed.add_field(name = "Server Roles", value = server_roles_str, inline = False)

    await ctx.send(embed = embed)
