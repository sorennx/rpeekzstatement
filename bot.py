import discord
import random as r
#statement generator section cos I did now know how to make it run from different file lmao
#general/guild
pre = ["I mean ", "Man ", "??? ", "lol ", "Maaaaaaaaaaaaan ","It’s like ","LOL? ","Dno about u guys but ", "As always "]
peekz_special=["xd","KEKW ","man ","lmao ","btw shut the fuck up ", "man don't speak ","XD ", "HAHA ", "CBA ","fucking simp ", ":) ", "smh ", "so i dno "]
#league stuff
l_opening_statement=["FNC ","G2 ","Jankos ","Rekkles ","Europe ","China "]
l_flame =["is overrated ","is bad ","is an idiot ","doesn't even look strong ", "is busted ", "is playing broken champions ","is so fucking bad"]
l_closing_statement=["first seed or 2nd seek doesn't rly matter ", "and this is the only reason g2 even won a fight ","and overall everyone is inting "]





#bot section
TOKEN='NzY0NjM4OTk2NjcxMzY1MTIw.X4JLjw.5iNq4zSrA4we6_4QU-xXnfKKbDs'
from discord.ext import commands
client = commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=['lquote'])
async def lolquote(ctx):
    #l stands for League of Legends related quotes
    l_os = r.choice(l_opening_statement)
    l_f = r.choice(l_flame)
    l_cs = r.choice(l_closing_statement)
    l_ps = r.choice(peekz_special)
    l_p = r.choice(pre)
    mood = r.randint(0, 100)
    total = l_p + l_os + l_f + "and " + l_cs + l_ps

    if mood == 0:
        for i in total.split():
            await ctx.send(i)
    elif mood in range(1, 20):

        await ctx.send(l_p)
        await ctx.send(l_os)
        await ctx.send(l_f)
        await ctx.send("and")
        await ctx.send(l_cs)
        await ctx.send(l_ps)

    else:
        await ctx.send(total)

@client.command()
async def gquote(ctx):
    print("hello")







client.run(TOKEN)

