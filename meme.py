import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM5MjI3MTUwNjgwMDY0NDE5OQ.GZQjgb.dXwn8mzPG4UUmUQLvqjKNEy9OZZS-xHWBvJVgo') # Replace with your own token

''' requests package allows us to make HTTP requests to any URL. 
In this case we're calling the GET method to the URL that will give us the meme data.
json package allows us to read JSON data. 
This is useful since most data passed around on the web is in the JSON format, 
like the JSON response we saw above.'''

