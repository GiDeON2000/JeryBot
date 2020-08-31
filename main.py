import discord
from discord.ext import commands
from pymongo import MongoClient
from asyncio import sleep


#MongoDB init
cluster = MongoClient('mongodb+srv://gideon:upitob32@cluster0.gy3lr.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster["ABD"]
collection = db["Users"]


bot = commands.Bot(command_prefix='+')

# on_ready, выполняет весь свой код при запуске бота
@bot.event
async def on_ready():
	for guild in bot.guilds:
  		for member in guild.members:
  			if collection.count_documents({"_id": member.id}) == 0:
  				collection.insert_one({
  				"_id": member.id,
  				"name": member.name,
  				"rep": 0,
  				"lvl": 0,
  				"xp": 0,
  				"warn": 0
  				})
	print('I am ready')


#cogs loads
@bot.command()
async def load(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}')
    await ctx.send('loaded')

@bot.command()
async def reload(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}')
    Bot.unload_extensions(f'cogs.{extensions}')
    await ctx.send('reloaded')

@bot.command()
async def unload(ctx, extensions):
    Bot.unload_extension(f'cogs.{extensions}')
    await ctx.send('unloaded')

#add cogs
#bot.load_extension()
bot.load_extension("cogs.rep")

# bot.run 
bot.run('NzQ5OTcwODE2NTc3MzA2NzU1.X0zuwA.l3MdFLB69barpdQmKZOYXAvDlYE')