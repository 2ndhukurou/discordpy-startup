# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import ffmpeg
import os
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'みせられないよ'
sound_path = "./sound"
# 接続に必要なオブジェクトを生成
client = commands.Bot(command_prefix='+')
voice_client = None

# 起動時に動作する処理
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def join(ctx):
    print('#voicechannelを取得')
    vc = ctx.author.voice.channel
    print('#voicechannelに接続')
    await vc.connect()

@client.command()
async def bye(ctx):
    print('#切断')
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    if message.content.startswith('+'):
        origin_name = message.content.lstrip('+')
        print(message.content)
        name = 'sound/' + origin_name + '.ogg'
        if os.path.exists(name):
            source = discord.FFmpegPCMAudio(name)
            message.guild.voice_client.play(source)
        else:
            pass

    else:
        pass
    await client.process_commands(message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
