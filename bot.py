import discord
from discord.ext import commands
from discord.Value.client import ValueClient

startup_extensions = ["Music"]
bot = commands.Bot ("!")

@bot.event
async def on_ready();
    print("bot online")
    
class main_Commands[];
        def __init__(self, bot);
        self.bot = bot
        
@bot.command(pass_content=True)
async def ping(cxt);
    await.say("pong")
    
if _name_ == "__main__";
    for extension in startup_extensions;
        try;
            bot.load_extension(extension)
        except Exception as e;
            exc = {}; {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}.format(extension, exc))

 bot.run("NDE5Njk2NjU1MjgxOTQ2NjI1.DX3WOw.3S3HdmdYylivn3gzWADc2wq2gbg")