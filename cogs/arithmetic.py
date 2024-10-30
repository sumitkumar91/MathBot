from utils import send_message
from discord.ext import commands

class Arithmetic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="add")
    async def add(self, ctx, a: float, b: float):
        result = a + b
        response = result
        await send_message(ctx.message, response)

    @commands.command(name="subtract")
    async def subtract(self, ctx, a: float, b: float):
        result = a - b
        response = result
        await send_message(ctx.message, response)

    @commands.command(name="multiply")
    async def multiply(self, ctx, a: float, b: float):
        result = a * b
        response = result
        await send_message(ctx.message, response)

    @commands.command(name="divide")
    async def divide(self, ctx, a: float, b: float):
        if b == 0:
            response = "Division by zero is undefined."
            await send_message(ctx.message, response)
        else:
            result = a / b
            response = result
        await send_message(ctx.message, response)


async def setup(client):
    await client.add_cog(Arithmetic(client))