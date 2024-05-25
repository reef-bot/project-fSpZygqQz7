```python
# main.py

import discord
from discord.ext import commands
from moderation import Moderation
from machine_learning import MachineLearning
from reporting_system import ReportingSystem
from dashboard import Dashboard

# Bot token
TOKEN = "your_discord_bot_token_here"

# Bot prefix
PREFIX = "!"

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot instance
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Initialize components
moderation = Moderation(bot)
machine_learning = MachineLearning()
reporting_system = ReportingSystem()
dashboard = Dashboard()

# Bot events
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await moderation.moderate_message(message)

# Run the bot
bot.run(TOKEN)
```