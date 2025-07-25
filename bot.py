#Start the Discord intent
from discord.ext import commands,tasks
from discord.utils import get
import discord
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
client = discord.Client(intents=intents)

#Load environment variables
from dotenv import dotenv_values
secrets=dotenv_values(".env")

# Available commands that are going to be read by the bot
AVAILABLE_COMMANDS = ["!baño", "!nopucmes", "!help", "!tocate", "!ducha", "!cafe", "!volvi", "!focus","!desayuno","!mirienda","!matcha","!ban","!cosorro","!joder","!frio"]
ALT_COMMANDS = ["!tócate", "!duchita", "!café", "!cafecito", "!volví","!desayunito","!merienda","!besito","!BAN","!frío","!pablotequeremos"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Que dise surmano, ya está er tío listo pal cancaneo!")
    channel = bot.get_channel(int(secrets["COMMANDS_CHANNEL_ID"]))
    await channel.send("Que dise surmano, ya está er tío listo pal cancaneo!")
    print('/pomodoro create focus_length:55 break_length:12 timer_channel:#"Estudio" notification_channel:#🍅pomodoros manager_role:@Illo-bot inactivity_threshold:6 voice_alerts:True name:Pomos')
    random_kick_event.start()
    
## Función para mutear a todo aquel que se mueva al canal de estudio, incluidos admins
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel:
        ## Mute si entras al canal de estudio desde 0
        if not before.channel and str(after.channel.id) == secrets['STUDY_CHANNEL_ID']:
            await member.edit(mute=True)
            return
        ## Unmute si entras a algún canal de descanso desde 0
        if not before.channel and (str(after.channel.id) == secrets['BREAK_CHANNEL_ID'] or str(after.channel.id) == secrets['PETIT_COMITE_CHANNEL_ID']):
            await member.edit(mute=False)
            return
        ## Mute si entras al canal de estudio desde alguno de descanso
        if (str(before.channel.id) == secrets['BREAK_CHANNEL_ID'] or str(before.channel.id) == secrets['PETIT_COMITE_CHANNEL_ID']) and str(after.channel.id) == secrets['STUDY_CHANNEL_ID']:
            await member.edit(mute=True)
            return
        ## Unmute si entras a algún canal de descanso desde el estudio
        if str(before.channel.id) == secrets['STUDY_CHANNEL_ID'] and (str(after.channel.id) == secrets['BREAK_CHANNEL_ID'] or str(after.channel.id) == secrets['PETIT_COMITE_CHANNEL_ID']):
            await member.edit(mute=False)
            return

@tasks.loop(minutes=1.0)
async def random_kick_event():
    member_secret = get(bot.get_all_members(), id=int(secrets['USER']))
    wait_time = random.randint(2000,30000)
    await asyncio.sleep(wait_time)
    if member_secret.voice and member_secret.voice.channel:
        try:
            print(f"Mandando al usuario {member_secret} al carajo")
            await member_secret.move_to(None)
        except Exception as e:
            print(f"An unexpected error occurred {e}")
    else:
        print(f"El usuario {member_secret} no está conectao, pisha")

    

@random_kick_event.before_loop
async def before_random_kick():
    """Ensures the bot is fully ready before starting the loop."""
    await bot.wait_until_ready()

@bot.event
async def on_message(message):
    if message.author == bot.user or not message.content.startswith('!') and not bot.user.mentioned_in(message):
        return
    if message.content.lower().split(' ', 1)[0] not in AVAILABLE_COMMANDS and message.content.lower().split(' ', 1)[0] not in ALT_COMMANDS and message.content.startswith('!'):
        await message.channel.send("Estás más perdío que el barco del arroz... los comandos disponibles son:" + str(AVAILABLE_COMMANDS) + " que no tentera!")
        channel = bot.get_channel(int(secrets["PETITIONS_CHANNEL_ID"]))
        await channel.send(message.content)
        return
    if message.content.lower().split(' ', 1)[0].startswith('!baño'):
        await message.channel.send("Ojú, " + str(message.author) + " tú también necesitas ir al baño? No vaya a tardá más que yo, EN?")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!nopucmes'):
        await message.channel.send("No puedo má con mi vía por favoooooo!")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!volví') or message.content.lower().split(' ', 1)[0].startswith('!volvi'):
        await message.channel.send("Menos mal que has vuelto " + str(message.author) + "... ya te estábamo eshando de meno")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!ducha') or message.content.lower().split(' ', 1)[0].startswith('!duchita'):
        await message.channel.send(str(message.author) + " se va a dar una ducha, no vaya a tarda mucho, ojitocuidao")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!help'):
        await message.channel.send("Estás más perdío que el barco del arroz... los comandos disponibles son: " + str(AVAILABLE_COMMANDS) + " que no tentera!")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!tocate') or message.content.lower().split(' ', 1)[0].startswith('!tócate'):
        await message.channel.send("Disfruta de tu cuerpo... TÓCATE ESTHER! A practicar descansos activos")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!cafe') or message.content.lower().split(' ', 1)[0].startswith('!café') or message.content.lower().split(' ', 1)[0].startswith('!cafecito'):
        await message.channel.send("CAFEINAAAAAA!!!!")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!focus'):
        await message.channel.send("Cushame, callarze ya que estoy malito de los nervios, me lio a puñalás y me quedo zolo...")
        return   
    if message.content.lower().split(' ', 1)[0].startswith('!desayuno') or message.content.lower().split(' ', 1)[0].startswith('!desayunito'):
        await message.channel.send("Por fin te vas a desayunar, " +str(message.author) + ", llevamos media hora escuchándo como te ruge la barriga...")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!merienda') or message.content.lower().split(' ', 1)[0].startswith('!mirienda'):
        await message.channel.send("Nos paese genial que te vaya a merendá.... pero tráete argo pa compartí con tus coleguita no?")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!matcha'):
        await message.channel.send("MATCHAAA MATCHAAAA queremos MATCHAAA MATCHAAAAAA💃💃")
        return
    if message.content.lower().split(' ', 1)[0].startswith('!besito'):
        await message.channel.send('y yo le dije \"NO!!\", me giré y me monté en mi bus')
        return
    if message.content.lower().split(' ', 1)[0].startswith('!ban') or message.content.lower().split(' ', 1)[0].startswith('!BAN'):
        await message.channel.send('Seré tu amante BAN dido BANdido, corazón corazón malherido🎶🎶')
        return
    if message.content.lower().split(' ', 1)[0].startswith('!cosorro'):
        await message.channel.send('AY COSORRO, por la viejita, que arguien me ayude... !nopucmes')
        return
    if message.content.lower().split(' ', 1)[0].startswith('!joder'):
        await message.channel.send('Joé shikillo yastabien no? Qué jartura...')
        return
    if message.content.lower().split(' ', 1)[0].startswith('!frio') or message.content.lower().split(' ', 1)[0].startswith('!frío'):
        await message.channel.send('https://i.pinimg.com/originals/a6/fb/bb/a6fbbb147c557a0bdcc78dacc529fe4f.gif')
        return
    if message.content.lower().split(' ', 1)[0].startswith('!pablotequeremos'):
        await message.channel.send('YO SI QUE OS QUIERO A USTEDE, CRIATURILLAS!!!')
        channel = bot.get_channel(int(secrets["PETITIONS_CHANNEL_ID"]))
        await channel.send(message.content)
        return
    if bot.user.mentioned_in(message):
        await message.channel.send('Que quiere ' + str(message.author) + '???')
        return

bot.run(secrets["BOT_TOKEN"])