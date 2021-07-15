from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext import commands

PREFIX = "+"
OWNER_IDS = [808309036364595202]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(
			command_prefix=PREFIX, 
			owner_ids=OWNER_IDS
			)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("THE ICED BOT IS CONNECTED")

	async def on_disconnect(self):
		print("THE ICED BOT IS DISCONNECTED")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(860876301921288193) 
			print("bot ready")

			channel = self.get_channel(862152877312049194)
			await channel.send("Now Online!")

			embed = Embed(title="Now Online!", description="Iced is now online.",
			              colour=0xFF0000, timestamp=datetime.utcnow())
			fields = [("Iced Bot", "The epic multi-purpose-bot", True),
			         ("AKA, #chadbot", "Brings you the full package for your server!", True),
			         ("Share and enjoy Iced", "Devs: Tindi Brown, VGO8, SIR F BOMBS special thanks to Sidhath SK!", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_author(name="Tindi Brown", icon_url=self.guild.icon_url)
			await channel.send(embed=embed) 
			embed.set_footer(text= "This is a footer") 

		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()