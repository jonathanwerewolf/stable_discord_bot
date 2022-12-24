from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate

load_dotenv()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    description="Runs models on Replicate!",
    intents=intents,
)


@bot.command()
async def dream(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("stability-ai/stable-diffusion")
    images = model.predict(prompt=prompt, num_outputs=4)

    await msg.edit(content=f"“{prompt}”\n{images[0]}\n{images[1]}\n{images[2]}\n{images[3]}")

@bot.command()
async def pokemon(ctx, *, prompt):
    """Generate an pokemon from a text prompt using the text-to-pokemon model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("lambdal/text-to-pokemon")
    images = model.predict(prompt=prompt, num_outputs=4)

    await msg.edit(content=f"“{prompt}”\n{images[0]}\n{images[1]}\n{images[2]}\n{images[3]}")

@bot.command()
async def tile(ctx, *, prompt):
    """Generate an tileable image from a text prompt using the material_stable_diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("tommoore515/material_stable_diffusion")
    images = model.predict(prompt=prompt, num_outputs=4)

    await msg.edit(content=f"“{prompt}”\n{images[0]}\n{images[1]}\n{images[2]}\n{images[3]}")

bot.run(os.environ["DISCORD_TOKEN"])
