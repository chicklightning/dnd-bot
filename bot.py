import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='dnd ')


@bot.event
async def on_ready():
    print('Logged in as ')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def roll(context, a: int, b: int):
    await context.send(a + b)


@bot.command()
async def find(context, a: int, b: int):
    await context.send()  # TODO: SEND REPLY TO QUERY FROM ROLL20


@bot.command()
async def info(context):
    embed = discord.Embed(title="D&D Bot", description="You fuckin' nerd(s).", color=0x72e0d3)

    # give info about you here
    embed.add_field(name="Authors", value="chicklightning and sweetkevindan")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Number of Servers", value="{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite Others to Use This Bot", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=441011381068627969&permissions=55296&scope=bot)")

    await context.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(context):
    embed = discord.Embed(title="D&D Bot", description="You fuckin' nerd(s).", color=0x72e0d3)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await context.send(embed=embed)


bot.run('NDE0MzIyMDQ1MzA0OTYzMDcy.DWl2qw.nTxSDf9wIcf42te4uSCMuk2VDa0')