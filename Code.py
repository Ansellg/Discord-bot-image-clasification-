import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def clafisicate(ctx):
    if ctx.message.attachments:
        for att in ctx.message.attachments:
            file_name = att.filename
            file_url = att.url
            await att.save(f"./{file_name}")
            await ctx.send(f"File is saved with the name {file_name}")
            await ctx.send(f"{file_url}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{att.filename}"))
    else:   
        await ctx.send('You forgot to add a image or i cant detect version. Please use JPEG files')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run(#ENTER DISCORD BOT CODE HERE)
