from utils import send_message
from discord.ext import commands
import asyncio
import html
import random
import requests

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="quiz")
    async def quiz(self, ctx):
        url = "https://opentdb.com/api.php?amount=1&category=19&difficulty=easy"
        response = requests.get(url)
        data = response.json()



        if data["response_code"] == 0:
            question = data["results"][0]["question"]
            correct_answer = data["results"][0]["correct_answer"]
            incorrect_answers =data["results"][0]["incorrect_answers"]
            options = [correct_answer] + incorrect_answers
            random.shuffle(options)
            print(options)

            response = "Q. " + question + "\n\n"

            for i in range(len(options)):
                response += chr(65 + i) + ". " + options[i] + "\n"

            response += "\nYou have 60 seconds to answer"

            response = html.escape(response)
        
            await send_message(ctx.message, response)

            def check(msg):
                valid_options = []
                for i in range(len(options)):
                    valid_options.append(chr(65 + i))
                print(valid_options)
                return (msg.author == ctx.author and msg.channel == ctx.channel)

            try:
                user_answer = await self.client.wait_for('message', check=check, timeout=60.0)
                user_index = ord(user_answer.content.strip().upper()) - 65
                if 0 <= user_index < len(options):
                    user_selected = options[user_index]

                if user_selected == correct_answer:
                    final_response = html.escape("Well done! You chose the correct option\n")
                else:
                    final_response = html.escape(f"Incorrect \nThe correct answer is {correct_answer}")

                await send_message(ctx.message, final_response)

            except asyncio.TimeoutError:
                final_response = (f"Time's up! The correct answer is {correct_answer}")
                await send_message(ctx.message, final_response)
        else:
            await ctx.send("Sorry, I couldn't retrieve a question at the moment. Please try again later.")

async def setup(client):
    await client.add_cog(Quiz(client))