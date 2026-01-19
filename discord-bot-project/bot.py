import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents - required for accessing certain Discord features
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
intents.members = True  # Required for member-related features

# Create bot instance with command prefix "!"
bot = commands.Bot(command_prefix='!', intents=intents)


# Event: Bot is ready and connected
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guild(s)')

    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name='for !help'
        )
    )


# Event: Handle errors in commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found. Use `!help` to see available commands.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')
    else:
        await ctx.send(f'An error occurred: {error}')


# Command: !ping - Check bot latency
@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')


# Command: !hello - Greet the user
@bot.command(name='hello', help='Get a friendly greeting')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}! Welcome to the server!')


# Command: !serverinfo - Display server information
@bot.command(name='serverinfo', help='Display information about the server')
async def serverinfo(ctx):
    guild = ctx.guild

    # Create an embed for better formatting
    embed = discord.Embed(
        title=f'{guild.name} Server Info',
        color=discord.Color.blue()
    )

    # Set server icon as thumbnail if available
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    # Add server information fields
    embed.add_field(name='Server ID', value=guild.id, inline=True)
    embed.add_field(name='Owner', value=guild.owner.mention if guild.owner else 'Unknown', inline=True)
    embed.add_field(name='Created On', value=guild.created_at.strftime('%Y-%m-%d'), inline=True)
    embed.add_field(name='Members', value=guild.member_count, inline=True)
    embed.add_field(name='Text Channels', value=len(guild.text_channels), inline=True)
    embed.add_field(name='Voice Channels', value=len(guild.voice_channels), inline=True)
    embed.add_field(name='Roles', value=len(guild.roles), inline=True)
    embed.add_field(name='Boost Level', value=guild.premium_tier, inline=True)
    embed.add_field(name='Boosts', value=guild.premium_subscription_count, inline=True)

    await ctx.send(embed=embed)


# Command: !avatar - Display a user's avatar with fun details
@bot.command(name='avatar', aliases=['av', 'pfp'], help='Display a user\'s avatar')
async def avatar(ctx, member: discord.Member = None):
    # Default to command author if no member specified
    member = member or ctx.author

    # Fun auras based on account age and randomness
    auras = [
        ('✨ Legendary', discord.Color.gold()),
        ('🔮 Mystic', discord.Color.purple()),
        ('🌊 Chill', discord.Color.blue()),
        ('🔥 Fiery', discord.Color.red()),
        ('🌿 Earthy', discord.Color.green()),
        ('🌸 Soft', discord.Color.pink()),
        ('⚡ Electric', discord.Color.yellow()),
        ('🌙 Nocturnal', discord.Color.dark_purple()),
        ('❄️ Frosty', discord.Color.from_rgb(150, 200, 255)),
        ('🎭 Chaotic', discord.Color.orange()),
    ]

    # Pick aura based on user ID for consistency
    aura_name, aura_color = auras[member.id % len(auras)]

    # Calculate account age
    account_age = (discord.utils.utcnow() - member.created_at).days

    # Determine account badge
    if account_age > 2000:
        badge = '🏛️ Ancient'
    elif account_age > 1000:
        badge = '👴 Veteran'
    elif account_age > 365:
        badge = '🎖️ Seasoned'
    elif account_age > 90:
        badge = '🌱 Growing'
    else:
        badge = '🆕 Fresh'

    embed = discord.Embed(
        title=f'{member.display_name}\'s Avatar',
        color=aura_color
    )

    # Set the avatar as a large image
    avatar_url = member.display_avatar.with_size(1024)
    embed.set_image(url=avatar_url)

    # Add fun details
    embed.add_field(name='Aura', value=aura_name, inline=True)
    embed.add_field(name='Account Age', value=f'{badge} ({account_age} days)', inline=True)
    embed.add_field(name='Created', value=member.created_at.strftime('%b %d, %Y'), inline=True)

    # Add join date if in a server
    if ctx.guild and member.joined_at:
        embed.add_field(name='Joined Server', value=member.joined_at.strftime('%b %d, %Y'), inline=True)

    embed.set_footer(text=f'Requested by {ctx.author.display_name}')

    await ctx.send(embed=embed)


# Run the bot
if __name__ == '__main__':
    if TOKEN is None:
        print('Error: DISCORD_TOKEN not found in environment variables.')
        print('Please create a .env file with your bot token.')
        print('See .env.example for the required format.')
    else:
        bot.run(TOKEN)
