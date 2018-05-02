import discord
import random
import token
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='dnd ')


@bot.event
async def on_ready():
    print('Logged in as ', end='')
    print(bot.user.name, end='')
    print(' with bot id ', end='')
    print(bot.user.id, end='')
    print('.\n', end='')
    print('Listening for contexts.')


@bot.command()
async def roll(context, a: int, b: int):
    await context.send(a + b)


@roll.error
async def roll_error(context, error):
    if isinstance(error, commands.BadArgument):
        await context.send()  # TODO: SEND REPLY ABOUT ERROR


@bot.command()
async def find(context, a: int, b: int):
    await context.send()  # TODO: SEND REPLY TO QUERY FROM ROLL20


@find.error
async def find_error(context, error):
    if isinstance(error, commands.BadArgument):
        await context.send()  # TODO: SEND REPLY ABOUT ERROR


@bot.command()
async def info(context):
    embed = discord.Embed(title="D&D Bot", description="For all your nerd needs.", color=0x72e0d3)

    # give info about you here
    embed.add_field(name="Authors", value="[chicklightning](https://github.com/chicklightning) and [sweetkevindan](https://github.com/kevSweet)")

    # Shows the number of servers the bot is member of
    embed.add_field(name="Number of Servers", value="{len(self.bot.servers)}")

    # show our resources
    embed.add_field(name="Reference", value="[Roll20](https://roll20.net/compendium/)", inline=False)

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite Others to Use This Bot", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=441011381068627969&permissions=55296&scope=bot)", inline=False)

    # show our github
    embed.add_field(name="Source Code", value="[GitHub Repo](https://github.com/chicklightning/dnd-bot)", inline=False)

    await context.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(context):
    embed = discord.Embed(title="D&D Bot", description="For all your nerd needs.", color=0x72e0d3)

    embed.add_field(name="dnd", value="Use to call the bot! Follow this with any of the commands below.", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await context.send(embed=embed)

bot.run(os.getenv('TOKEN', token))
