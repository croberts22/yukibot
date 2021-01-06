import os
from discord.ext import commands
from dotenv import load_dotenv


# - Environment Setup

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot = commands.Bot(command_prefix='!')
preamble = '📣 **Before posting, please check <#{channel}> for previously answered questions.**\n\n'


# - Events

@bot.event
async def on_ready():
    print('Logged in as {0.user}.'.format(bot))


# - Commands

@bot.command(name='yuki', help='Introduces herself!')
async def hi_yuki(ctx):
    """
    Let's you know who this bot is.
    :param ctx: The current context.
    :return: A friendly message. ^_^
    """
    await ctx.send('Hi! I\'m {0.user}!'.format(bot))


@bot.command(name='caniwatch', help='Prints a message on whether or not you can watch anime on MyAniList.')
async def can_i_watch(ctx):
    """
    Prints a message on whether or not you can watch anime on MyAniList.
    :param ctx: The current context.
    :return: A message on whether or not you can watch anime on MyAniList.
    """
    question = '**Q:** Can I watch anime or read manga on MyAniList?'
    answer = '**A: No.** MyAniList is a __tracking__ app that __tracks your content__ and synchronizes it with the ' \
             'AniList website. If you want to watch anime, please check out Crunchyroll, Funimation, and HIDIVE. '
    message = generate_message(ctx, question, answer)
    await ctx.send(message)


@bot.command(name='canyouaddthis', help='Prints a message on whether or not we can add new shows on AniList.')
async def can_you_add_this(ctx):
    """
    Prints a message on whether or not we can add new shows on AniList.
    :param ctx: The current context
    :return: A message on whether or not we can add new shows on AniList.
    """
    question = '**Q:** Why don\'t you have _<insert title here>_ in MyAniList? I have my 18+ toggle on but I still ' \
               'can\'t find _<insert title here>_. Can\'t you just add it? '
    answer = '**A:** We do not own the contents of what gets displayed in the app, AniList.co does.** MyAniList is a ' \
             'third-party app that is __not owned by them__. Please contact the team at AniList.co, or join their ' \
             'Discord (`https://discord.gg/uDaxJf7`) to request a series be added. '
    message = generate_message(ctx, question, answer)
    await ctx.send(message)


@bot.command(name='notanilist', help='Prints a message on whether or not MyAniList is AniList (spoilers: it\'s not).')
async def are_we_anilist(ctx):
    """
    Prints a message on whether or not MyAniList is AniList (spoilers: it's not).
    :param ctx: The current context.
    :return: A message declaring we aren't AniList.
    """
    question = '**Q:** Is this the official AniList / AniChart Discord server?\n'
    answer = '**A: NO.** This is an **unofficial** server for the **unofficial** iOS app, MyAniList. If you want to ' \
             'join AniList\'s Discord, you may do so here: `https://discord.gg/uDaxJf7`'
    message = generate_message(ctx, question, answer)
    await ctx.send(message)


# - Helper Functions

def generate_message(ctx, question, answer):
    """
    Concatenates strings together to make a message.
    :param ctx: The current context.
    :param question: The question to display.
    :param answer: The answer to show.
    :return: A concatenated string.
    """
    return preamble.format(channel=rules_channel(ctx).id) + question + answer


def rules_channel(ctx):
    """
    Iterates through the current context and finds the #rules channel object.
    Note that this function will throw an exception if the context does _not_
    Have a channel by the name of #rules. Here, we assume all contexts available to
    the bot will have visibility to the #rules channel.
    :param ctx: The current context.
    :return: Returns the #rules channel.
    """
    return [channel for channel in ctx.guild.channels if channel.name == 'rules'][0]


# - Execution

bot.run(TOKEN)
