import discord
import random as r
#statement generator section cos I did now know how to make it run from different file lmao

#print("Welcome to Random Peekz Statement Generator! Kneel before zoomer of boomers!")
#x = int(input("How long do you want your random peekz statement to be?"))
pre = ["I mean ", "Man ", "??? ", "lol ", "Maaaaaaaaaaaaan ","It’s like ","LOL? ","Dno about u guys but "]
opening_statement=["FNC ","G2 ","Jankos ","Rekkles ","Europe ","China "]
flame =["is overrated ","is bad ","is an idiot ","doesn't even look strong ", "is busted ", "is playing broken champions "]
closing_statement=["first seed or 2nd seek doesn't rly matter ", "and this is the only reason g2 even won a fight ","and overall everyone is inting "]
peekz_special=["xd","KEKW ","man ","lmao ","btw shut the fuck up ", "man don't speak ","XD ", "HAHA ", "CBA ","fucking simp ", ":) ", "smh ", "so i dno "]





#bot section
TOKEN='NzY0NjM4OTk2NjcxMzY1MTIw.X4JLjw.5Vgh4P2mKPVEio3-tnU_C4OiMHo'
from discord.ext import commands
client = commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def quote(ctx):
    os = r.choice(opening_statement)
    f = r.choice(flame)
    cs = r.choice(closing_statement)
    ps = r.choice(peekz_special)
    p = r.choice(pre)
    mood = r.randint(0, 100)
    total = p + os + f + "and " + cs + ps

    if mood == 0:
        for i in total.split():
            await ctx.send(i)
    elif mood in range(1, 20):

        await ctx.send(p)
        await ctx.send(os)
        await ctx.send(f)
        await ctx.send("and")
        await ctx.send(cs)
        await ctx.send(ps)

    else:
        await ctx.send(total)









client.run(TOKEN)

