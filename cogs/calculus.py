from utils import send_message
from discord.ext import commands
from sympy import symbols, diff, sympify, integrate

class Calculus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="differentiation")
    async def differentiate(self, ctx, expression: str, var: str = 'x'):
        try:
            variable = symbols(var)
            parsed_expression = sympify(expression)
            result = diff(parsed_expression, variable)
            response = str(result)
        except Exception as e:
            response = "An error occurred while differentiating the expression. Please check your input."
        await send_message(ctx.message, response)

    @commands.command(name="integrate")
    async def integrate(self, ctx, expression: str, var: str = 'x', lower: float = None, upper: float = None):
        try:
            variable = symbols(var)
            parsed_expression = sympify(expression)
            if lower is not None and upper is not None:
                result = integrate(parsed_expression, (variable, lower, upper))
                response = str(result)
            else:
                result = integrate(parsed_expression, variable)
                response = str(result)
        except Exception as e:
            response = "An error occurred while integrating the expression. Please check your input."
        await send_message(ctx.message, response)

async def setup(client):
    await client.add_cog(Calculus(client))