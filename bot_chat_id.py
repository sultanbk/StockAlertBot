import asyncio
import telegram

async def main():
    try:
        bot = telegram.Bot(token="OPD0JPCUa-NMcXzUdo9lDMobs")
        print("Bot created successfully")
        
        # Get bot info to verify token
        bot_info = await bot.get_me()
        print(f"Bot name: {bot_info.first_name}")
        print(f"Bot username: @{bot_info.username}")
        
        updates = await bot.get_updates()
        print(f"Number of updates: {len(updates)}")
        
        if len(updates) == 0:
            print("No updates found. Try sending a message to your bot first.")
            return
            
        for i, u in enumerate(updates):
            print(f"Update {i + 1}:")
            if u.message:
                print(f"  Chat ID: {u.message.chat.id}")
                print(f"  From: {u.message.from_user.first_name}")
                print(f"  Text: {u.message.text}")
            else:
                print("  No message in this update")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
