import discord
from discord.ext import commands
from discord import Intents
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot with intents
intents = Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="!help for commands"))

# PING COMMAND
@bot.command(name='ping', help='Check the bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="🏓 Pong!", description=f"Bot latency: {latency}ms", color=0x5865F2)
    await ctx.send(embed=embed)

# KICK COMMAND
@bot.command(name='kick', help='Kick a member from the server')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    embed = discord.Embed(title="👢 Member Kicked", description=f"{member.mention} has been kicked.\nReason: {reason}", color=0xFF0000)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to kick members!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Usage: !kick @member [reason]")

# BAN COMMAND
@bot.command(name='ban', help='Ban a member from the server')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    embed = discord.Embed(title="🚫 Member Banned", description=f"{member.mention} has been banned.\nReason: {reason}", color=0xFF0000)
    await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to ban members!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Usage: !ban @member [reason]")

# MUTE COMMAND
@bot.command(name='mute', help='Mute a member')
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.timeout(discord.utils.utcnow() + discord.Timedelta(minutes=10), reason=reason)
    embed = discord.Embed(title="🔇 Member Muted", description=f"{member.mention} has been muted for 10 minutes.\nReason: {reason}", color=0xFFA500)
    await ctx.send(embed=embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to mute members!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Usage: !mute @member [reason]")

# WARN COMMAND
@bot.command(name='warn', help='Issue a warning to a member')
@commands.has_permissions(moderate_members=True)
async def warn(ctx, member: discord.Member, *, reason="No reason provided"):
    embed = discord.Embed(title="⚠️ Member Warned", description=f"{member.mention} has been warned.\nReason: {reason}", color=0xFFFF00)
    await ctx.send(embed=embed)
    
    # Send DM to warned member
    try:
        await member.send(f"⚠️ You have been warned in {ctx.guild.name}\nReason: {reason}")
    except:
        pass

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to warn members!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Usage: !warn @member [reason]")

# HELP COMMAND
@bot.command(name='help', help='View all available commands')
async def help(ctx):
    embed = discord.Embed(title="🤖 Fogg Bot Commands", description="Here are all available commands:", color=0x5865F2)
    embed.add_field(name="!ping", value="Check the bot latency", inline=False)
    embed.add_field(name="!kick @member [reason]", value="Kick a member from the server", inline=False)
    embed.add_field(name="!ban @member [reason]", value="Ban a member from the server", inline=False)
    embed.add_field(name="!mute @member [reason]", value="Mute a member for 10 minutes", inline=False)
    embed.add_field(name="!warn @member [reason]", value="Issue a warning to a member", inline=False)
    embed.add_field(name="!help", value="View this message", inline=False)
    await ctx.send(embed=embed)

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Error: DISCORD_TOKEN not found in .env file!")
