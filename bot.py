import discord
from discord.ext import commands
import requests
from os import path
import wikipedia
#add steam api
client = discord.Client()

#start nuke code rug seminar earth olive split lunar book agree blur push spare spell defense
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

#start spambot
async def spam(message, cms):
    count = 0
    while count < 1000:
        msg = await client.send_message(message.channel,"BOT: {}".format(cms))
        if message.content.startswith('!spamstop'):
            count = 1000
        count += 1  # This is the same as count = count + 1
#end

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        msg = await client.send_message(message.channel, "`!nuke - Deletes all messages\n!exec - executes basic python commands\n!spam message - this spams a message 100 times \n!spamstop - stops the spam\n!chuck generates a random chuck norris joke\n!wiki subjects - searches wikipedia for a subject \n!cowsay message - puts your message but says it as a cow.`")

    elif message.content.startswith('!nuke'):
        if message.author.id == client.user.id:
            await nuke(message)

    elif message.content.startswith('!kick'):
        if message.author.id == client.user.id:
            name = message.content[len('!kick'):].strip()
            await client.send_message(message.channel, "user {} will be kicked".format(name))

    elif message.content.startswith('!spam'):
        if message.author.id == client.user.id:
            cms = message.content[len('!spam'):].strip()
            await spam(message = message,cms = cms)

    elif message.content.startswith('!chuck'):
        if message.author.id == client.user.id:
            chuckPull = requests.get("http://api.icndb.com/jokes/random")
            if chuckPull.status_code == 200:
                await client.send_message(message.channel,chuckPull.json()["value"]["joke"])
                
    elif message.content.startswith('!trumpt'):
       if message.author.id == client.user.id:
          trumpPull = request.get("placeholder")
          await client.send_message(message.channel,"Trump thinks\n\n"+chuckPull.json()["message"]+"\n\n His nickname for you is "+chuckPull.json()["nickname"])
            

#Add a option for users to add as many sentences as they want
    elif message.content.startswith("!wiki"):
        if message.author.id == client.user.id:
            search = message.content[len('!wiki'):].strip()
            msg = await client.send_message(message.channel,wikipedia.summary("{}".format(search), sentences=5))

    elif message.content.startswith('!exec'):
        if message.author.id == client.user.id:
            exe = message.content[len('!exec'):].strip()
            msg = await client.send_message(message.channel,eval(exe))

    elif message.content.startswith("!cowsay"):
        if message.author.id == client.user.id:
            cowsay = message.content[len('!cowsay'):].strip()
            await client.delete_message(message)
            msg = await client.send_message(message.channel,
"""
```
______
< {} >
 ------
\    ^__^
  \  (oo)\____
    (__)\     )\/
        ||---w||
        ||    || Sir Loin```""".format(cowsay))
@client.event
async def on_ready():
  print('Logged in as: %s#%s' % (client.user.name, client.user.id))

if __name__ == '__main__':
    client.run('x@x.x', 'x')
