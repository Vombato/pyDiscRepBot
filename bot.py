from dotenv import find_dotenv, load_dotenv
import discord
import json
import random
import os
import pymongo as mongo


load_dotenv(find_dotenv())

bot_token = os.environ.get('TOKEN')
guild_id_1 = os.environ.get('GUILD_1')
guild_id_2 = os.environ.get('GUILD_2')

bot = discord.Bot()

def get_rand_quote():
    with open("quotes.json", "rb") as file:
        data = json.load(file)
    
    return "*"+random.choice(data["quotes"])+"* - Sen. Mauritio Reputatio"

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[guild_id_1, guild_id_2])
async def citazione(ctx):
    await ctx.respond(get_rand_quote())


def main() -> None:
    bot.run(bot_token)


if __name__ == '__main__':
    main()
