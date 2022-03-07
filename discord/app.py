from asyncio.log import logger
import datetime
import gc
import discord
from discord.ext import tasks
import json

gc.set_threshold(1000, 100, 20)

with open("config.json", "r") as file:
    settings = json.load(file)


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)
        self.show_per_min.start()

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")

    @tasks.loop(hours=1)
    async def show_per_min(self):
        channel = client.get_channel(id=settings["channelID"][0])
        await channel.send(f"{datetime.datetime.now()}")


client = MyClient()
client.run(settings["token"])
