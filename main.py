import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.getenv("TOKEN")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

seen_users = []

@client.event
async def on_message(message):
    user_name = message.author.name
    message_values = ["Hello {}, Welcome to our server", "{}, Hi please read our rules before continue chating."]

    if message.author == client.user:
        return

    if user_name not in seen_users:
        random_index = random.randint(0, len(message_values)-1)
        res = message_values[random_index]
        await message.channel.send(res.format(user_name))
        seen_users.append(user_name)
        

client.run(token)

