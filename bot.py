#Start the Discord intent
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Load environment variables
from dotenv import dotenv_values
secrets=dotenv_values(".env")

# Available commands that are going to be read by the bot
AVAILABLE_COMMANDS = ["!baño", "!nopucmes", "!help", "!tocate", "!ducha", "!cafe", "!volvi"]
ALT_COMMANDS = ["!tócate", "!duchita", "!café", "!cafecito", "!volví"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Que dise surmano, ya está er tío listo pal cancaneo!")
    channel = bot.get_channel(int(secrets["COMMANDS_CHANNEL_ID"]))
    await channel.send("Que dise surmano, ya está er tío listo pal cancaneo!")
    print('/pomodoro create focus_length:55 break_length:12 timer_channel:#"Estudio" notification_channel:#🍅pomodoros manager_role:@Illo-bot inactivity_threshold:6 voice_alerts:True name:Pomos')
@bot.event
async def on_message(message):
    if message.author == bot.user or not message.content.startswith('!') and not bot.user.mentioned_in(message):
        return
    if message.content.split(' ', 1)[0] not in AVAILABLE_COMMANDS and message.content.split(' ', 1)[0] not in ALT_COMMANDS and message.content.startswith('!'):
        await message.channel.send("Estás más perdío que el barco del arroz... los comandos disponibles son:" + str(AVAILABLE_COMMANDS) + " que no tentera!")
        channel = bot.get_channel(int(secrets["PETITIONS_CHANNEL_ID"]))
        await channel.send(message.content)
        return
    if message.content.split(' ', 1)[0].startswith('!baño'):
        await message.channel.send("Ojú, " + str(message.author) + " tú también necesitas ir al baño? No vaya a tardá más que yo, EN?")
        return
    if message.content.split(' ', 1)[0].startswith('!nopucmes'):
        await message.channel.send("No puedo má con mi vía por favoooooo!")
        return
    if message.content.split(' ', 1)[0].startswith('!volví') or message.content.split(' ', 1)[0].startswith('!volvi'):
        await message.channel.send("Menos mal que has vuelto " + str(message.author) + "... ya te estábamo eshando de meno")
        return
    if message.content.split(' ', 1)[0].startswith('!ducha') or message.content.split(' ', 1)[0].startswith('!duchita'):
        await message.channel.send(str(message.author) + " se va a dar una ducha, no vaya a tarda mucho, ojitocuidao")
        return
    if message.content.split(' ', 1)[0].startswith('!help'):
        await message.channel.send("Estás más perdío que el barco del arroz... los comandos disponibles son: " + str(AVAILABLE_COMMANDS) + " que no tentera!")
        return
    if message.content.split(' ', 1)[0].startswith('!tocate') or message.content.split(' ', 1)[0].startswith('!tócate'):
        await message.channel.send("Disfruta de tu cuerpo... TÓCATE ESTHER! A practicar descansos activos")
        return
    if message.content.split(' ', 1)[0].startswith('!cafe') or message.content.split(' ', 1)[0].startswith('!café') or message.content.split(' ', 1)[0].startswith('!cafecito'):
        await message.channel.send("CAFEINAAAAAA!!!!")
        return
    if bot.user.mentioned_in(message):
        await message.channel.send('Que quiere ' + str(message.author) + '???')
        return

bot.run(secrets["BOT_TOKEN"])