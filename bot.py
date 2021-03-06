import discord
import random
from requests_html import HTMLSession
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
    rollRequest = "Rolling " + a + " d" + b + "s..."
    rollResult = "";
    for x in range(a):
        rollResult += random.randint(1, b) + ", "

    embed = discord.Embed(title=rollRequest, description=rollResult, color=0x72e0d3)
    await context.send(embed)


@roll.error
async def roll_error(context, error):
    if isinstance(error, commands.BadArgument):
        await context.send()  # TODO: SEND REPLY ABOUT ERROR


@bot.command()
async def find(context, *, qry):
    session = HTMLSession()
    goog_search = qry.replace(" ", "+")
    goog_search = goog_search + "+d20pfsrd"
    goog_search = "https://www.google.com/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + goog_search

    r = session.get(goog_search)

    session.close()
    embed = discord.Embed(title="Search Results for " + qry, description=r.html.find('cite')[0].text, color=0x72e0d3)

    await context.send(embed=embed)  # TODO: ALLOW MULTI-WORD QUERIES WITHOUT QUOTATION MARKS. THEN SPEECH2TEXT

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
    embed.add_field(name="Number of Servers", value='{num}'.format(num=len(bot.guilds)))

    # show our resources
    embed.add_field(name="Reference", value="[Roll20](https://roll20.net/compendium/)")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite for Bot", value="[Invite link](https://bit.ly/dnd-bot)")

    # show our github
    embed.add_field(name="Source Code", value="[GitHub Repo](https://github.com/chicklightning/dnd-bot)")

    await context.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(context):
    embed = discord.Embed(title="D&D Bot", description="For all your nerd needs.", color=0x72e0d3)

    embed.add_field(name="dnd", value="Use to call the bot! Follow this with any of the commands below.", inline=False)
    # embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    # embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    # embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="dnd info", value="Gives a little info about the bot and its authors.", inline=False)
    embed.add_field(name="dnd help", value="Gives this message.", inline=False)
    embed.add_field(name="dnd find <search term>", value="Finds a relevant article from D20 Pathfinder SRD.", inline=False)
    embed.add_field(name="dnd roll <number of die> <number of sides", value="Will roll x number of d\"y\" die.", inline=False)

    await context.send(embed=embed)

bot.run(os.getenv('TOKEN', token))
