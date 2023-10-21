import discord
import os
import json
import time

client = discord.Client(intents=discord.Intents.all())

# Load user login data from a JSON file
def load_login_data():
    if os.path.exists('login_data.json'):
        with open('login_data.json', 'r') as file:
            return json.load(file)
    else:
        return {}

# Save user login data to a JSON file
def save_login_data(login_data):
    with open('login_data.json', 'w') as file:
        json.dump(login_data, file)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!login'):
        login_data = load_login_data()

        # Get the current time
        current_time = time.time()

        # Check if user has a login record
        user_id = str(message.author.id)
        last_login_time = login_data.get(user_id, 0)

        # Calculate the time difference in hours
        time_difference_hours = (current_time - last_login_time) / 3600

        if time_difference_hours >= 24:
            # User can log in (time difference is more than 24 hours)
            login_data[user_id] = current_time
            save_login_data(login_data)

            # Increase login streak for the user
            login_streak = login_data.get(user_id + '_streak', 0)
            login_streak += 1
            login_data[user_id + '_streak'] = login_streak
            save_login_data(login_data)

            await message.channel.send(f'Login successful! Your login streak is now {login_streak}.')
        else:
            # User cannot log in (less than 24 hours since last login)
            wait_time_hours = 24 - time_difference_hours
            await message.channel.send(f'You can log in again in {wait_time_hours:.2f} hours.')

client.run(os.environ['DISCORD_TOKEN'])
