import discord
import random
from discord.ext import commands
import requests
from os import path
import wikipedia
import urllib
import os
import ruamel.yaml
import json


apikey = {"UVvWJFG638ebIoQtfQNDmx9bDYDeIh4quOBeAFvP"}
#add steam api
client = discord.Client()
listVIP = ['191063904384712706']
#start meme generator
async def meme(message):
    image = random.randint(0, 11)
    image += 1
    if image >= 12:
        video = random.randint(0,5)
        video += 1
        if video == 1:
            video = "https://www.youtube.com/watch?v=8JQHm7Jsxiw"
            await client.send_message(message.channel, video)
            
        elif video == 2:
            video = ''
            await client.send_message(message.channel, video)
            
        elif video == 3:
            video = ''
            await client.send_message(message.channel, video)
            
        elif video == 4:
            video = ''
            await client.send_message(message.channel, video)
            
        elif video == 5:
            video = ''
            await client.send_message(message.channel, video)
            
        elif video == 6:
            video = ''
            await client.send_message(message.channel, video)
    elif image < 12:
        file = '{}.jpg'.format(image)
        await client.send_file(message.channel, file)
#end
#start insult generator
async def insult(message):
    config = ruamel.yaml.load(open(os.path.dirname(__file__) + 'insults.yml'))
    pref = 'Thou'
    col1 = random.choice(config['column1'])
    col2 = random.choice(config['column2'])
    col3 = random.choice(config['column3'])
    msg = await client.send_message(message.channel, pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '.')
#end

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
        if message.author.id == client.user.id or message.author.id == listVIP[0]:
            msg = await client.send_message(message.channel, "'Owners Commands\n!nuke - Deletes all messages\n!exec - executes basic python commands\n!spam message - this spams a message 100 times \n!spamstop - stops the spam\n!chuck generates a random chuck norris joke\n!wiki subjects - searches wikipedia for a subject \n!cowsay message - puts your message but says it as a cow.`")
        elif message.author.id != client.user.id:
            msg = await client.send_message(message.channel, "'User Commands\n!help - Display helps message\n!chuck - displays random chuck norris joke\n!insult - makes an insult\n!trump name - trump gives his opinion'")

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
            chuckPull = requests.get("http://api.icndb.com/jokes/random")
            if chuckPull.status_code == 200:
                await client.send_message(message.channel,chuckPull.json()["value"]["joke"])
                
    elif message.content.startswith('!swtoritem'):
        itemsearch = message.content[len('!swtoritem'):].strip()
        apikey = 
        swtorPull = request.get("http://swtordata.com:80/api/v2/items?query={}".format(itemsearch), X-Api-Key = apikey)
        if swtorPull.status_code == 404:
            await client.send_message(message.channel,"BOT: ERROR 404 - Item not found")
        elif swtorPull.status_code == 200:
            await client.send_message(message.channel,swtorPull.json()["display_name"])
    
    elif message.content.startswith('!trump'):
            name = message.content[len('!trump'):].strip()
            trumpPull = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={}".format(name))
            await client.send_message(message.channel,"Trump thinks \nTRUMP: "+trumpPull.json()["message"]+" \ntheir nickname is "+trumpPull.json()["nickname"])

#fix memes
    elif message.content.startswith('!meme'):
            await meme(message=message)

    elif message.content.startswith('!insult'):
            await insult(message)

#Add a option for users to add as many sentences as they want
    elif message.content.startswith("!wiki"):
        if message.author.id == client.user.id or message.author.id == listVIP[0]:
            search = message.content[len('!wiki'):].strip()
            msg = await client.send_message(message.channel,wikipedia.summary("{}".format(search), sentences=5))

    elif message.content.startswith('!exec'):
        if message.author.id == client.user.id:
            exe = message.content[len('!exec'):].strip()
            msg = await client.send_message(message.channel,eval(exe))

    elif message.content.startswith('!sh'):
        if message.author.id == client.user.id:
            cmd = message.content[len('!sh'):].strip()
            msg = await client.send_message(message.channel,os.system("{}".format(cmd)  ))

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
    client.run('x', 'x')
