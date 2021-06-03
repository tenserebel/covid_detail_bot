import discord 
import asyncio
import requests
from discord.ext import commands

client = commands.Bot(command_prefix=">")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def covid(ctx, *, countryName = None):
    try:

        if countryName is None:
            embed=discord.Embed(title="This command is used like this: ```>covid [country]```", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


        else:
            url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
            stats = requests.get(url)
            json_stats = stats.json()
            country = json_stats["country"]
            totalCases = json_stats["cases"]
            todayCases = json_stats["todayCases"]
            totalDeaths = json_stats["deaths"]
            todayDeaths = json_stats["todayDeaths"]
            recovered = json_stats["recovered"]
            active = json_stats["active"]
            critical = json_stats["critical"]
            casesPerOneMillion = json_stats["casesPerOneMillion"]
            deathsPerOneMillion = json_stats["deathsPerOneMillion"]
            totalTests = json_stats["totalTests"]
            testsPerOneMillion = json_stats["testsPerOneMillion"]

            embed2 = discord.Embed(title=f"**COVID-19 Details Of {country}**!", description="This Information Isn't Live Always, Hence It May Not Be Accurate!", colour=0x00FF00, timestamp=ctx.message.created_at)
            embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
            embed2.add_field(name="**Today Cases**", value=todayCases, inline=True)
            embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
            embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
            embed2.add_field(name="**Recovered**", value=recovered, inline=True)
            embed2.add_field(name="**Active**", value=active, inline=True)
            embed2.add_field(name="**Critical**", value=critical, inline=True)
            embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
            embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
            embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
            embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

            embed2.set_thumbnail(url="https://epicentre.msf.org/sites/default/files/styles/crop_media_block_text_img_lr/public/2020-04/Covid-19_virus.jpg?itok=6cltV3eU")
            await ctx.send(embed=embed2)

    except:
        embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0xff0000, timestamp=ctx.message.created_at)
        embed3.set_author(name="Error!")
        await ctx.send(embed=embed3)
      
client.run("ODQ2ODM4Mzc3MzYxMTc4Njg0.YK1Vsg.g0h0ZSuZ74kAiN616C2I72sgWCA")   