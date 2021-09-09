from telethon import TelegramClient
import time
import os


# Place your own values from my.telegram.org

api_id = 1234567 # your api id, make sure it is a number
api_hash = '<api hash>'
client = TelegramClient('<your name>', api_id, api_hash)

async def main():
    async for message in client.iter_messages('me'):
        if message.photo or message.file:
            await message.download_media(file=f'{os.getcwd()}/messages/{message.id}/{message.id}')
            with open(f'messages/{message.id}/{message.id}.json', 'w') as file:
                file.write(f'{{\n\t"message_id": "{message.id}",\n\t"datetime": "{message.date}",\n\t"message": "{message.message}"\n}}')
        else:
            with open(f'messages/{message.id}.json', 'w') as file:
                file.write(f'{{\n\t"message_id": "{message.id}",\n\t"datetime": "{message.date}",\n\t"message": "{message.message}"\n}}')
        
        time.sleep(1)


with client:
    client.loop.run_until_complete(main())