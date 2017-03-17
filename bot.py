import discord
from time import sleep
from discord.ext import commands

client = discord.Client()

#start nuke code
async def nuke(message):
  def __retry(message):
    cnt = 0
    while 1:
      sleep(1)
      try:
        cnt += 1
        if cnt >= 3:
          break
        client.delete_message(message)
        break
      except:
        continue

  counter = 0
  async for message in client.logs_from(message.channel, limit=500):
    if message.author == client.user:
      try:
        await client.delete_message(message)
      except:
        __retry(message)
      counter += 1
      if counter == 25:
        sleep(5)
        counter = 0
#end
@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        msg = await client.send_message(message.channel, "`!nuke - Deletes all messages.`")

    elif message.content.startswith('!nuke'):
        if message.author.id == client.user.id:
            await nuke(message)

    elif message.content.startswith('!kick'):
        if message.author.id == client.user.id:
            name = message.content[len('!kick'):].strip()
            await client.send_message(message.channel, "user {} will be kicked".format(name))
            await client.kick(name)
@client.event
async def on_ready():
  print('Logged in as: %s#%s' % (client.user.name, client.user.id))

if __name__ == '__main__':
    client.run('EMAIL', 'PASSWORD')
