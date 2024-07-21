import telebot
import random 
from config import token

from logic import Pokemon
from logic import Fighter, Wizard
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        i = random.randint(1,3)
        if i == 1: 
            pokemon = Pokemon(message.from_user.username)
        elif i == 2: pokemon = Fighter(message.from_user.username)
        elif i == 3: pokemon = Wizard(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img()[0])
        bot.send_photo(message.chat.id, pokemon.show_img()[1])
        bot.send_photo(message.chat.id, pokemon.show_img()[2])
        bot.send_photo(message.chat.id, pokemon.show_img()[3])

    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def go(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        bot.reply_to(message, Pokemon.pokemons[message.from_user.username].feed())

@bot.message_handler(commands=['attack'])
def go(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        username = message.reply_to_message.from_user.username
        pokemon1 = Pokemon.pokemons[username]
        pokemon2= Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, pokemon2.attack(pokemon1))
bot.infinity_polling(none_stop=True)

