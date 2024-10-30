from discord import Message

async def send_message(message: Message, response: str) -> None:
    if message.content[0] == '?':
        await message.author.send(response)
    else:
        await message.channel.send(response)
