import telebot

# Replace with your bot token
BOT_TOKEN = "7364291801:AAFjE844_Y-vrKp0WcMVPH2U_T-0vqi_KGQ"

# Create a TeleBot object
bot = telebot.TeleBot(BOT_TOKEN)

# User data dictionary (replace with a database later)
user_data = {}

# Function to handle "/start" command
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    if user_id not in user_data:
        user_data[user_id] = {"taps": 0}
    bot.send_message(message.chat.id, "Welcome to the Tap-to-Earn Bot!")

# Function to handle "/tap" command
@bot.message_handler(commands=["tap"])
def tap(message):
    user_id = message.chat.id
    if user_id in user_data:
        user_data[user_id]["taps"] += 1
        bot.send_message(message.chat.id, "Tapped! You have " + str(user_data[user_id]["taps"]) + " taps.")
    else:
        bot.send_message(message.chat.id, "Please use /start to begin.")

# Function for other messages (optional)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You can tap using /tap command.")

# Start the bot
bot.polling()
