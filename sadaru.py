import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("사다리")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!사다리타기"):
        team = message.content[7:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "---->" + teamname[i])

client.run("NjUyNTExMDAwODA0OTgyNzk0.XepggQ.zzb0lGE-FrQBCnz6iu3JdVHgT90")


