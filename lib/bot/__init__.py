from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from time import sleep
from glob import glob
import asyncio

PREFIX = "+"
OWNER_IDS = [808309036364595202]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
class Ready():
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f"{cog} cog ready")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])
class Bot(BotBase):
	def __init__(self):
		
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()
		self.bot = Bot
		self.cogs_ready = Ready()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

	def run(self, version):
		self.VERSION = version
		self.setup()
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
			while not self.cogs_ready.all_ready():
				await asyncio.sleep(0.5)

			
			self.ready = True
			self.guild = self.get_guild(860876301921288193)
			print("bot ready")

		else:
			print("bot reconnected")

	# async def on_message(self,message):
	# 	if message.content == "+hello":
	# 		await message.channel.send('Hey there')
	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f" {cog} cog loaded")

		print("setup complete")

bot = Bot()

