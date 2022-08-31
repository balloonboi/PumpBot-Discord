import discord
from discord.ext import commands
import serial
port = input('Enter the port number of the Arduino: COM')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='p!', intents=intents)

client = MyClient(intents=intents)

ser = serial.Serial(f'COM{port}', 115200, timeout=1)

@bot.command()
async def pump(ctx, a: int, b: int):
    await ctx.send(f'pumping at {a} percent for {b} seconds')
    ser.write(str.encode(f'pump {a}, {b}'))

@bot.command()
async def pressure(ctx):
        ser.flushInput()
        line = ser.readline()  # read a byte
        string = line.decode()
        stripped_string = string.strip()
        await ctx.send(f'current pressure is {stripped_string} (atmospheric pressure is 493)')

@bot.command()
async def vent(ctx, a: int):
    await ctx.send(f'venting to atmosphere for {a} seconds')
    ser.write(str.encode(f'vent {a}'))

#@bot.command()
#async def fuckingexplode(ctx):
#    await ctx.send('kaboom')
#    ser.write(str.encode(f'pump 100, 999999999'))


bot.run('TOKEN-HERE')


