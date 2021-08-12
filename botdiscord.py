import discord
import random
from  keep_alive import  keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} заебланился на серваЧОК'.format(client))
rep_word = ["niga","nigga","negr","нига","нигга","негр"]

otvetochka = ["+rep","chill chill","it so fucking good","i like it","nice cock"]
img = ['cs.jpg','standoff.jpg','leon.jpg']

@client.event
async  def on_message(message):
  if message.author == client.user:
    return

  msg = message.content


  if any(word in msg for word in rep_word):
    await message.channel.send(random.choice(otvetochka))
  if message.content.startswith("ава бравл"):
    await  message.channel.send('ава бравл',file = discord.File('leon.jpg'))
  if message.content.startswith("ава стэндофф"):
    await  message.channel.send('ава стэндофф',file = discord.File('standoff.jpg'))

  if message.content.startswith("ава кс"):
    await message.channel.send('ава кс',file= discord.File(random.choice(img)))
  if message.content.startswith('погода'+ ''):
   if message.content.startswith(msg):
    await message.channel.send('https://sinoptik.com.ru/'+msg,)


keep_alive()
client.run('TOKEN')
