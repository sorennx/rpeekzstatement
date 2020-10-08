import random as r
print("Welcome to Random Peekz Statement Generator! Kneel before zoomer of boomers!")
#x = int(input("How long do you want your random peekz statement to be?"))
pre = ["I mean ", "Man ", "? ", "lol ", "Maaaaaaaaaaaaan "]
opening_statement=["FNC ","G2 ","Jankos ","Rekkles ","Europe ","China "]
flame =["is overrated ","is bad ","is an idiot ","doesn't even look strong ", "is busted ", "is playing broken champions "]
closing_statement=["first seed or 2nd seek doesn't rly matter ", "and this is the only reason g2 even won a fight ","and overall everyone is inting "]
peekz_special=["xd","KEKW ","man ","lmao ","btw shut the fuck up ", "man don't speak ","XD ", "HAHA ", "CBA ",",fucking simp ", ":) ", "smh ", "so i dno "]

os = r.choice(opening_statement)
f = r.choice(flame)
cs = r.choice(closing_statement)
ps = r.choice(peekz_special)
p = r.choice(pre)
mood = r.randint(0,4)

total = p + os +f+"and "+cs+ps
if mood == 0:
    for i in total.split():
        print(i)
else:
    print(total)
