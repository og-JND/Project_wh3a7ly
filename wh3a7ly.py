import discord
import responses

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

f = open('sensitive_shit.txt', 'r')
TOKEN = f.readline()

@client.event
async def on_ready():
    print("Wh3a7ly_v1.0 is now operational.")

@client.event
async def on_message(message):
    channel = message.channel
    author = message.author.global_name
    message_content = message.content
    greeting = responses.sendResponse(message_content, author)
    if (message.author != client.user):
        await channel.send(greeting)
    # print(f"{channel_name = }")
    # print(f"{message_content = }")
    # print(f"{author = }")
    


client.run(TOKEN)