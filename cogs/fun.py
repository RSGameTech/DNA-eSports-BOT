import discord
import random
import asyncio
from discord.ext import commands


class fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot

    #Q&A

    @commands.command()
    async def qna(self, ctx, *, question):
        response = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
                    ]
        embed = discord.Embed(
                title="Q&A",
                description=f"Question: {question}\nAnswer: {random.choice(response)}"
                )
        await ctx.send(embed=embed)

    #F

    @commands.command()
    async def f(self, ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{ctx.author.mention} has paid the respect")
        else:
            embed = discord.Embed(
                    title="F",
                    description=
                    f"{ctx.author.mention} has paid the respect for {user.mention}"
                    )
            await ctx.send(embed=embed)

    #Virus

    @commands.command()
    async def virus(self, ctx, user: discord.Member = None, *, virus: str = "trojan"):
        m = await ctx.send("starting")
        await asyncio.sleep(0.5)
        user = user or ctx.author
        virus = (
            f"`[▓▓▓                    ] / {virus}-virus.exe Packing files.`",
            f"`[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..`",
            f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..`",
            f"`Successfully downloaded {virus}-virus.exe`",
            "`Injecting virus.   |`",
            "`Injecting virus..  /`",
            "`Injecting virus... -`",
            f"`Successfully Injected {virus}-virus.exe into {user.name}`",
        )
        for i in virus:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

def setup(bot):
    bot.add_cog(fun(bot))
    print("Fun file is loaded!")
