import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Wh3a7ly_v1.0 is now operational.")

@client.event
async def on_message(message):
    channel_name = message.channel.name
    author = message.author.global_name
    message_content = message.content
    print(f"{channel_name = }")
    print(f"{message_content = }")
    print(f"{author = }")


client.run('MTE1NDU1NjMyOTY0MjQ0Njg5OA.GWdisd.SSX7NShc9L4U69B9aF4n5aRTm06N0m7fLoP0e0')