import os
import json
import random
import discord
import asyncio
import time

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send(
        'Hello, please type !commands to see the list of commands!')


#Commands
  if message.content.startswith('!commands'):
    await message.channel.send(
        '!carboncalculator asks you for the amount of calories you burned in a run and outputs the carbon emissions you saved by not driving!'
    )
    await message.channel.send(
        '!caloriecalculator sends you a link to a website that helps you find the optimal amount of calories and macronutrients you need every day!'
    )
    await message.channel.send(
        '!calorietracker sends you a link to a website that helps you track the amount of calories you eat each day!'
    )
    await message.channel.send(
        '!workoutvideosbeginner gives you links to our beginner workout videos!'
    )
    await message.channel.send(
        '!workoutvideosintermediate gives you links to our intermediate workout videos!'
    )
    await message.channel.send(
        '!workoutvideosadvanced gives you links to our advanced workout videos!'
    )
    await message.channel.send(
        '!workoutvideosmusclegrowth gives you links to our muscle growth workout videos!'
    )
    await message.channel.send(
        '!resources gives you helpful resources to help you towards your fitness goals!'
    )
    await message.channel.send(
        '!website gives you a link to the GoGreenz website!')
    await message.channel.send(
        '!nearme helps you find parks and grocery stores near your location!')
    await message.channel.send(
        '!weeklychallenges shows you the weekly challenges to help you toward your health and wellness goals!'
    )
    await message.channel.send(
        '!login increases your login streak by 1! You can compete to maintain this login streak with friends!'
    )

  #Calorie Calculator and Tracker
  if message.content.startswith('!caloriecalculator'):
    await message.channel.send(
        'https://www.calculator.net/macro-calculator.html')

  if message.content.startswith('!calorietracker'):
    await message.channel.send(
        'https://www.webmd.com/diet/healthtool-food-calorie-counter')

  #Beginner Workout Videos
  if message.content.startswith('!workoutvideosbeginner'):
    beginner_videos = [
      'https://www.youtube.com/watch?v=SRb-XN_Yeww',
      'https://www.youtube.com/watch?v=q_JAxNc__kA',
      'https://www.youtube.com/watch?v=ramrjR8pCZ0'
    ]
    selected_video_beginner = random.choice(beginner_videos)
    await message.channel.send(f'Here is your beginner workout video: {selected_video_beginner}')
    await message.channel.send('For another beginner workout video, try the !workoutvideosbeginner command again.')

  #Intermediate Workout Videos
  if message.content.startswith('!workoutvideosintermediate'):
      intermediate_videos = [
            'https://www.youtube.com/watch?v=PLeRIznGpbA',
            'https://www.youtube.com/watch?v=6k8npknseG4',
            'https://www.youtube.com/watch?v=q8h9a0eSkEc'
        ]

      # Select a random video from the list
      selected_video_intermediate = random.choice(intermediate_videos)
      await message.channel.send(f'Here is your intermediate workout     video: {selected_video_intermediate}')
      await message.channel.send('For another intermediate workout video, try the !workoutvideosintermediate command again.')

  #Advanced Workout Videos
  if message.content.startswith('!workoutvideosadvanced'):
    advanced_videos = [
      'https://www.youtube.com/watch?v=RcLz_atcq8w',
      'https://www.youtube.com/watch?v=_Zem0_qsDg0',
      'https://www.youtube.com/watch?v=e3-zpBc_hg8'
    ]
    selected_video_advanced = random.choice(advanced_videos)
    await message.channel.send(f'Here is your advanced workout video: {selected_video_advanced}')
    await message.channel.send('For another advanced workout video, try the !workoutvideosadvanced command again.')

  
  #Muscle Growth Workout Videos
  if message.content.startswith('!workoutvideosmusclegrowth'):
    muscle_growth_videos = [
      'https://www.youtube.com/watch?v=gnTzk1yUHB4',
      'https://www.youtube.com/watch?v=c6VQvQJfD8Q',
      'https://www.youtube.com/watch?v=vc1E5CfRfos'
    ]
    selected_video_muscle_growth = random.choice(muscle_growth_videos)
    await message.channel.send(f'Here is your muscle growth workout video: {selected_video_muscle_growth}')
    await message.channel.send('For another muscle growth workout video, try the !workoutvideosmusclegrowth command again.')

  #Resources
  if message.content.startswith('!resources'):
    await message.channel.send(
        'WebMD - Health news, advice, and expertise on various health topics: '
        + 'https://www.webmd.com/')
    await message.channel.send(
        'MyFitnessPal Blog - Nutrition tips, workout ideas, and success stories: '
        + 'https://blog.myfitnesspal.com/')
    await message.channel.send(
        'To see all our resources, visit our website: ' +
        'https://sites.google.com/view/gogreenz/home'
    )

  #Website
  if message.content.startswith('!website'):
    await message.channel.send(
        'Here is the link to the GoGreenz website: ' +
        'https://sites.google.com/view/gogreenz/home'
    )

  #Near Me
  if message.content.startswith('!nearme'):
    await message.channel.send(
        'Parks Near You: ' +
        'https://www.google.com/maps/search/parks+near+me/')
    await message.channel.send(
        'Grocery Stores Near You: ' +
        'https://www.google.com/maps/search/grocery+stores+near+me/')

 
    #Carbon Calculator
  if message.content.startswith('!carboncalculator'):
    await message.channel.send(
        'Please enter the number of calories burned from your run, bike, etc:')

    def check(m):
      return m.author == message.author and m.channel == message.channel

    try:
      response = await client.wait_for('message', check=check, timeout=60.0)
      calories_burned = float(response.content)

      # Calculate carbon emissions saved (adjust the conversion factor as needed)
      emissions_saved = calories_burned * 0.03  # Assuming 0.03 kg CO2 emissions per calorie

      # Calculate equivalent miles not driven (adjust the conversion factor as needed)
      miles_not_driven = emissions_saved / 0.2  # Assuming 0.2 kg CO2 emissions per mile

      await message.channel.send(f'Calories Burned: {calories_burned} kcal')
      await message.channel.send(
          f'Carbon Emissions Saved: {emissions_saved:.2f} kg CO2')
      await message.channel.send(
          f'Equivalent Miles Not Driven: {miles_not_driven:.2f} miles')

    except asyncio.TimeoutError:
      await message.channel.send('You took too long to respond.')

    except ValueError:
      await message.channel.send(
          'Invalid input. Please enter a valid number of calories.')


  # Weekly Challenges
# Load completed challenges from a JSON file
  def load_completed_challenges():
      if os.path.exists('completed_challenges.json'):
          with open('completed_challenges.json', 'r') as file:
              return json.load(file)
      else:
          return {}
  
  # Save completed challenges to a JSON file
  def save_completed_challenges(completed_challenges):
      with open('completed_challenges.json', 'w') as file:
          json.dump(completed_challenges, file)



  if message.content.startswith('!weeklychallenges'):
      # Load completed challenges
      completed_challenges = load_completed_challenges()

      challenge_messages = [
          'Challenge 1: Drink 8 glasses of water every day.',
          'Challenge 2: Take a 30-minute walk every day.',
          'Challenge 3: Do 20 minutes of stretching exercises.'
      ]

      challenge_prompts = []
      for idx, challenge in enumerate(challenge_messages, start=1):
          challenge_prompt = await message.channel.send(challenge)
          challenge_prompts.append(challenge_prompt)
          await challenge_prompt.add_reaction('\U00002705')  # Unicode for checkmark emoji

          # Check if this challenge is already completed
          if f'challenge_{idx}' in completed_challenges.get(str(message.author.id), []):
              await challenge_prompt.add_reaction('\U00002705')  # Add checkmark reaction

      # Function to check if a challenge is completed
      def challenge_completed(reaction, user):
          return user == message.author and str(reaction.emoji) == '\U00002705'

      challenges_completed = 0
      for idx, challenge_prompt in enumerate(challenge_prompts, start=1):
          try:
              # Wait for the specific challenge to be completed (checkmark reaction)
              await client.wait_for('reaction_add', timeout=60.0, check=challenge_completed)
              challenges_completed += 1

              # Store completed challenge
              if str(message.author.id) not in completed_challenges:
                  completed_challenges[str(message.author.id)] = []
              completed_challenges[str(message.author.id)].append(f'challenge_{idx}')

          except asyncio.TimeoutError:
              # Timeout occurred, challenge not completed
              pass

      if challenges_completed == len(challenge_messages):
          await message.channel.send('Congratulations! You completed all the challenges! 🎉')
      else:
          await message.channel.send('You did not complete all the challenges in time. Keep trying!')

      # Save completed challenges
      save_completed_challenges(completed_challenges)

      # Remove reactions from the messages
      for challenge_prompt in challenge_prompts:
          await challenge_prompt.clear_reactions()


  #Login 
  def load_login_data():
      try:
          with open('login_data.json', 'r') as file:
              return json.load(file)
      except (FileNotFoundError, json.JSONDecodeError):
          # If the file doesn't exist or is empty/invalid, return an empty dictionary
          return {}

  # Save user login data to a JSON file
  def save_login_data(login_data):
      with open('login_data.json', 'w') as file:
          json.dump(login_data, file)
        
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
        
client.run(os.environ['TOKEN'])
