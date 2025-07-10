import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM5MjI3MTUwNjgwMDY0NDE5OQ.GZQjgb.dXwn8mzPG4UUmUQLvqjKNEy9OZZS-xHWBvJVgo') # Replace with your own token.

'''First, we've imported the discord.py package that we just installed and 
created our own class MyClient which we will use to interact with the Discord API. 
We create this class by extending from the base class discord.Client. 
This base class already has methods to respond to common events. 
For example, the on_ready() function above will be called when the Discord bot's login is successful.
discord.py works around the concept of events. 
There are other types of events (e.g., messages) that we will see later, 
but for now here's the definition of events from their website:
An event is something you listen for and then respond to. 
For example, when a message happens, you will receive an event about it that you can respond to.'''


intents = discord.Intents.default()
intents.message_content = True

'''The next two lines of code sets the intents that will be passed into a given instance of MyClient. 
These are the settings for what our Discord bot can access. Since we've assigned the default() behavior for our bot, 
we'll need to explicitly allow it to interact with messages (i.e., message_content=True):
'''

client = MyClient(intents=intents)
client.run('MTM5MjI3MTUwNjgwMDY0NDE5OQ.GZQjgb.dXwn8mzPG4UUmUQLvqjKNEy9OZZS-xHWBvJVgo') # Replace with your own token

'''Finally, our last two lines of code instantiates the MyClient class and calls run, which is the main way to start the client. 
The client will use the given token (which you should have saved from before) to authenticate itself to the Discord backend servers.
'''

