
from discord.ext.commands import Cog
from discord.ext.commands import command
import random
import py8fact as facts

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="Hi", aliases=['hello'], hidden=True)
    async def hello(self, ctx):
        await ctx.send('Hey there!')

    @command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        response = ['as i see yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')
    @command()
    async def dice(self, ctx):
        
        await ctx.send(f'you rolled a {random.randint(1, 6)}')
    @command(aliases=['fact'])
    async def fact(self, ctx):
	await ctx.send(facts.random_fact())
    @command()
    async def randomno(self, ctx):
        await ctx.send(f'Your random number is {random.randint(1, 1000000)}')


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")



def setup(bot):
	bot.add_cog(Fun(bot))
