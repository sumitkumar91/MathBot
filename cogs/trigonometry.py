from utils import send_message
from discord.ext import commands
import math

class Trigonometry(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="sin")
    async def sin(self, ctx, angle: float):
        result = math.sin(math.radians(angle))
        response = result
        await send_message(ctx.message, response)

    @commands.command(name="cos")
    async def cos(self, ctx, angle: float):
        result = math.cos(math.radians(angle))
        response = result
        await send_message(ctx.message, response)

    @commands.command(name="tan")
    async def tan(self, ctx, angle: float):
        if angle % 90 == 0 and (angle // 90) % 2 == 1:
            response = "Tangent is undefined at this angle."
        else:
            result = math.tan(math.radians(angle))
            response = result
        await send_message(ctx.message, response)

    @commands.command(name="csc")
    async def csc(self, ctx, angle: float):
        if angle % 180 == 0:
            response = "Cosecant is undefined at this angle."
        else:
            result = 1 / math.sin(math.radians(angle))
            response = result
        await send_message(ctx.message, response)

    @commands.command(name="sec")
    async def sec(self, ctx, angle: float):
        if angle % 90 == 0 and (angle // 90) % 2 == 1:
            response = "Secant is undefined at this angle."
        else:
            result = 1 / math.cos(math.radians(angle))
            response = result
        await send_message(ctx.message, response)

    @commands.command(name="cot")
    async def cot(self, ctx, angle: float):
        if angle % 180 == 0:
            response = "Cotangent is undefined at this angle."
        else:
            result = 1 / math.tan(math.radians(angle))
            response = result
        await send_message(ctx.message, response)


async def setup(client):
    await client.add_cog(Trigonometry(client))