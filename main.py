from discord.ext import commands

from discord.voice_client import VoiceClient

from os import listdir
from os.path import isfile, join


cogs_dir = "cogs"
bot = commands.Bot(command_prefix="!!")
# TOKEN = ("NDA1MTg3NDk0Nzk2MDY2ODE2.DWTb6A.D8AlplcKCQ0Cac0d3CzdHNasUcg")
TOKEN = ("NDE5MjM3MjkwODQyMzkwNTM5.DXtMuA.EWP1gmopU6dK-T-3XGAFMDRWMhQ") #testbot token

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()




bot.run(TOKEN)
