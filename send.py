import discord
from discord import app_commands
import serial
port = input('Enter the port number of the Arduino: COM')


MY_GUILD = discord.Object(id=GUILD)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

ser = serial.Serial(f'COM{port}', 115200, timeout=1)

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@client.tree.command()
@app_commands.describe(speed='Pump Speed', duration='Pump Strength')
async def pump(
    interaction: discord.Interaction,
    # This makes it so the first parameter can only be between 0 and 100.
    speed: app_commands.Range[int, 0, 100],
    # This makes it so the second parameter must be over 0, with no maximum limit.
    duration: app_commands.Range[int, 0, None],
):
    """Turns on the pump"""
    await interaction.response.send_message(f'pumping at {speed} percent for {duration} seconds')
    ser.write(str.encode(f'pump {speed}, {duration}'))

@client.tree.command()
@app_commands.describe(duration='Vent Duration')
async def vent(
    interaction: discord.Interaction,
    duration: app_commands.Range[int, 0, None],
):
    """Vents to atmosphere"""
    await interaction.response.send_message(f'venting for {duration} seconds')
    ser.write(str.encode(f'vent {duration}'))

@client.tree.command()
async def pressure(interaction: discord.Interaction):
    ser.flushInput()
    line = ser.readline()  # read a byte
    string = line.decode()
    stripped_string = string.strip()
    """Gets the current pressure"""
    await interaction.response.send_message(f'current pressure is {stripped_string} (atmospheric pressure is 493')

@client.tree.command()
async def stop(interaction: discord.Interaction):
    """Stops the pump"""
    await interaction.response.send_message('stopping pump')
    ser.write(str.encode('stop'))


for i in range(50):
    line = ser.readline()   # read a byte
    print(line)
client.run('TOKEN')
