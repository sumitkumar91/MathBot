from utils import send_message
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="help")
    async def help(self, ctx):
        response = (
            "**Available Commands:**\n"
            "- **!add a b** - Adds two numbers.\n"
            "- **!subtract a b** - Subtracts the second number from the first.\n"
            "- **!multiply a b** - Multiplies two numbers.\n"
            "- **!divide a b** - Divides the first number by the second.\n"
            "- **!sin angle** - Computes the sine of the given angle.\n"
            "- **!cos angle** - Computes the cosine of the given angle.\n"
            "- **!tan angle** - Computes the tangent of the given angle.\n"
            "- **!csc angle** - Computes the cosecant of the given angle.\n"
            "- **!sec angle** - Computes the secant of the given angle.\n"
            "- **!cot angle** - Computes the cotangent of the given angle.\n"
            "- **!differentiation expression [var]** - Differentiates the given expression with respect to the specified variable (default is x).\n"
            "- **!integrate expression [var] [lower] [upper]** - Integrates the given expression with respect to the specified variable (default is x). Optionally, specify lower and upper limits.\n"
            "- **!helpcalculus** - Displays help for calculus commands.\n"
            "- **!quiz** - Starts a quiz.\n"
            "\n You can use '?' instead of '!' to recieve response in your DM.\n"
        )
        await send_message(ctx.message, response)

    @commands.command(name="helpcalculus")
    async def helpcalculus(self, ctx):
            response = (
                "**Calculus Commands Help**\n\n"
                "**Differentiation**\n"
                "To differentiate an expression with respect to a variable, use:\n"
                "`!differentiation <expression> <variable>`\n"
                "- Example: `!differentiation sin(x) x`\n"
                "- Example: `!differentiation x**2 + 3*x + 5 x`\n\n"
        
                "**Integration**\n"
                "To integrate an expression with respect to a variable, use:\n"
                "`!integrate <expression> <variable> [lower bound] [upper bound]`\n"
                "- For indefinite integration (no bounds):\n"
                "  Example: `!integrate x**2 + 3*x x`\n"
                "- For definite integration (with bounds):\n"
                "  Example: `!integrate x**2 + 3*x x 0 5`\n\n"
        
                "Use `**` for exponents (e.g., `x**2` for x squared) and standard trigonometric "
                "functions like `sin(x)`, `cos(x)`, `tan(x)`, etc."
            )
            await send_message(ctx.message, response)

async def setup(client):
    await client.add_cog(Help(client))