from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [808309036364595202]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

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

		else:
			print("bot reconnected")

	async def on_message(self, message):
		print('message')

bot = Bot()