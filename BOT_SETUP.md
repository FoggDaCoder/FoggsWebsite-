# 🤖 Fogg Bot - Discord Bot Setup

This is your Discord bot with moderation and fun commands!

## Commands Available

- `!ping` - Check bot latency
- `!kick @member [reason]` - Kick a member from the server
- `!ban @member [reason]` - Ban a member from the server
- `!mute @member [reason]` - Mute a member for 10 minutes
- `!warn @member [reason]` - Issue a warning to a member
- `!help` - View all available commands

## Setup Instructions

### Step 1: Create Your Bot on Discord Developer Portal

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and name it **"Fogg Bot"**
3. Go to the **"Bot"** section
4. Click **"Add Bot"**
5. Under the **TOKEN** section, click **"Copy"** to copy your bot token
6. **Paste it in the `.env` file** (replace `your_bot_token_here`)

### Step 2: Configure Bot Permissions

1. Go to **OAuth2 → URL Generator**
2. Under **Scopes**, select: `bot`
3. Under **Permissions**, select:
   - Kick Members
   - Ban Members
   - Moderate Members
   - Send Messages
   - Embed Links

4. Copy the **generated URL** at the bottom
5. Open the URL in your browser to **invite the bot to your server**

### Step 3: Install Dependencies

Run this command in your terminal:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Bot

```bash
python bot.py
```

You should see: `Fogg Bot#XXXX has connected to Discord!`

### Step 5: Test the Bot

In your Discord server, type:
```
!ping
!help
```

## File Structure

```
/workspaces/FoggsWebsite-/
├── bot.py              # Main bot file
├── .env                # Your bot token (KEEP SECRET!)
├── requirements.txt    # Python dependencies
├── index.html          # Bot website home page
└── about.html          # Bot features page
```

## Important Notes

⚠️ **NEVER share your bot token!** It's like a password for your bot.

If you accidentally share it:
1. Go back to Discord Developer Portal
2. Click "Regenerate" under the TOKEN section
3. Update your `.env` file with the new token

## Troubleshooting

**Bot won't start:**
- Make sure `.env` file has your bot token
- Make sure bot is online in Discord Developer Portal
- Run `pip install -r requirements.txt`

**Commands not working:**
- Make sure bot has permissions in the server
- Make sure you're using the correct prefix `!`

**Need help?**
- Check [discord.py Documentation](https://discordpy.readthedocs.io/)
