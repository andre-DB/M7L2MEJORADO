import discord
from discord.ext import commands
from model import get_class
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# crear carpeta si no existe
if not os.path.exists("imagenes"):
    os.makedirs("imagenes")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            
            file_name = attachment.filename
            file_path = f"imagenes/{file_name}"

            # guardar imagen en carpeta
            await attachment.save(file_path)

            # usar modelo (debe devolver clase y probabilidad)
            clase, prob = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=file_path
            )

            porcentaje = round(prob * 100, 2)

            # mensaje según resultado
            if clase.lower() == "real":
                mensaje = f"Tu imagen ha sido analizada y es {porcentaje}% real!"
            else:
                mensaje = f"Tu imagen ha sido analizada y es {porcentaje}% hecha por IA!"

            await ctx.send(mensaje)

    else:
        await ctx.send("No recibí ninguna imagen. Intenta otra vez.")

bot.run("TOKEN")