import discord
from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://gideon:upitob32@cluster0.gy3lr.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster["ABD"]
collection = db["Users"]

class Reputation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['rep', 'реп'])
	async def plus_reputation_for_member(self, ctx, member: discord.Member):
		if not member:
			emb = discord.Embed(title='Error', color=0x7265EF,
				description='Mention the person you want to give your reputation to!')
		else:
			for x in collection.find({"_id": member.id}):
				reps = x["rep"] = x["rep"] + 1
				collection.update_one({"_id": member.id}, {"$set": {"rep": reps}})
				emb = discord.Embed(description=f'+1 rep for {member.mention}', color=0x0000FF)
				await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Reputation(bot))