import discord
from discord.ext import commands,tasks
import os, math




#token

TOKEN =  'ODU3MjQzMTg0MTk1NTY3NjI2.YNMv7Q.eouOmtXJfIwofFDtMiZPZx8I4ss'

#bot

client = commands.Bot(command_prefix='?')

#Startup info

@client.event

async def on_ready():
    print("Polaczono z botem: {}".format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

#zmienne wymagane
art_str = str(input())


@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')

@client.command()
async def prefix(ctx):
    await ctx.send('My prefix is ?<command>')

@client.command()
async def halp(ctx):
    await ctx.send('Lista komend: \n    helloworld - funkcja testowa bota\n    halp - pomoc\n    rigcz_start - daje ci początkową liczbe rigczu')

@client.command()
async def rigcz_start(ctx):
    await ctx.send('Dodawanie profilu rigczowego. Masz na start 1 rigcz. {} '.format(ctx.author.name))
    nazwa = ctx.author.name
    nazwafile = nazwa + ".txt"
    rigcz_file = open(nazwafile, mode="a+")
    rigcz_file.write("1")
    rigcz_file.close()

@client.command()
async def rigcz(ctx, parameter, y_s):
    name = ctx.author.name
    f = open(file=name + ".txt", mode="r+")
    if parameter == "Dodaj" or "dodaj":
        x = str(f.read())
        x1 = str(x)
        y = int(str(x1))
        z = str(y_s)
        z1 = int(str(z))
        suma = y + z1
        chain = str(int(suma))
        await ctx.send(f"Twój rigcz to teraz {chain}")
        f.close()
        os.system("del " + name + ".txt")
        f1 = open(file=name + ".txt", mode="a+")
        f1.write(chain)

    elif parameter == "Odejmij" or "odejmij":
        x = str(f.read())
        x1 = str(x)
        y = int(str(x1))
        z = str(y_s)
        z1 = int(str(z))
        suma = y - z1
        chain = str(int(suma))
        await ctx.send(f"Twój rigcz to teraz {chain}")
        f.close()
        os.system("del " + name + ".txt")
        f1 = open(file=name + ".txt", mode="a+")
        f1.write(chain)

    elif parameter == "Pomnóż" or "pomnóż":
        x = str(f.read())
        x1 = str(x)
        y = int(str(x1))
        z = str(y_s)
        z1 = int(str(z))
        suma = y * z1
        chain = str(int(suma))
        await ctx.send(f"Twój rigcz to teraz {chain}")
        f.close()
        os.system("del " + name + ".txt")
        f1 = open(file=name + ".txt", mode="a+")
        f1.write(chain)

    elif parameter == "Podziel" or "podziel":
        x = str(f.read())
        x1 = str(x)
        y = int(str(x1))
        z = str(y_s)
        z1 = int(str(z))
        suma = y * z1
        chain = str(int(suma))
        await ctx.send(f"Twój rigcz to teraz {chain}")
        f.close()
        os.system("del " + name + ".txt")
        f1 = open(file=name + ".txt", mode="a+")
        f1.write(chain)



@client.command()
async def rigcz_stan(ctx, nick):
    name = nick + ".txt"
    wartosc = open(file=name, mode="r")
    Stan = wartosc.read()
    await ctx.send(f"Stan twojego rigczu wynosi: {Stan}")
    wartosc.close()





#konwersja liczb na znaki
#x = str(input("Podaj liczbe: "))
#y = int(str(x))
#print(y)
#z = y * 2
#print(z)



@client.command()
async def ilosc(ctx):
    nazwa = ctx.author.name + ".txt"
    file = open(file=nazwa, mode="a+")
    rigcz = file.readlines()
    await ctx.send(f"Twój rigcz wynosi: {rigcz}")







client.run(TOKEN)
