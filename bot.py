import discord 
import responses
import traceback

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    token = 'MTE1MzQxNzkzNjI5MjI4MjQyOA.GMpSri.TTSgFwqIhFqDwl_TXDYCWjsFZn8wTHR59bEp7Q'
    intents = discord.Intents.default()
    intents.message_content=True
    intents.reactions = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #print(f"{username} said: '{user_message}' ({channel})")

        try:
            if user_message and user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
    client.run(token)