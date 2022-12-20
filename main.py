
import telebot
import os
import random
import requests

bot_token = '5881010706:AAEd4FLdnL5VCO3Xmd_uElxn_3_7LFlUqJY'

bot = telebot.TeleBot('5881010706:AAEd4FLdnL5VCO3Xmd_uElxn_3_7LFlUqJY')


school, number, name = '', '', ''

@bot.message_handler(commands=['start', 'help'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id,
                         "Привет, выбери, что нужно сделать:\nотправить домашку /send\n /get\nхочешь фото с котиками?) /cats")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")




@bot.message_handler(commands=['send'])
def send_hw(message):
    bot.send_message(message.from_user.id, "Из какой ты школы?\nНапиши: 57 или Наша школа")
    bot.register_next_step_handler(message, get_school)


def get_school(message):
    global school
    school = message.text
    if school == "57":
        bot.send_message(message.from_user.id, "Напиши свою фамилию и имя")
        bot.register_next_step_handler(message, get_name)
    if school == "Наша школа" or school == "Наша":
        bot.send_message(message.from_user.id, "Из какого ты класса? Напиши: 5 или 6")
        bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number
    number = message.text
    bot.send_message(message.from_user.id, "Напиши свою фамилию и имя")
    if number == "5":
        bot.register_next_step_handler(message, get_name)
    if number == "6":
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Пришли одно фото своей домашки или файл пдф")
    bot.register_next_step_handler(message, get_photo)


def get_photo(message):
    try:
        fileID = message.photo[-1].file_id
    except TypeError:
        fileID = message.document.file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    extension = file_info.file_path[-4:]
    save_photo_in_user_folder(downloaded_file, extension)


def save_photo_in_user_folder(photo, extension):
    global name
    os.chdir('./домашки')
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)
    with open(str(random.randint(1e5, 1e8)).zfill(8) + extension, 'wb') as new_file:
        new_file.write(photo)
    os.chdir("..")
    os.chdir('..')


@bot.message_handler(commands=['cats'])
def cat(message):
    if message.text == "/cats":
        response = requests.get("https://cataas.com/cat")
        if response.status_code == 200:
            with open('c.png', 'wb') as out_file:
                out_file.write(response.content)
            photo = open("c.png", 'rb')
            bot.send_photo(message.from_user.id, photo, caption = 'Лови' )
        else:
            bot.send_message(message.from_user.id, "Технические шоколадки, извини")

bot.polling(none_stop=True, interval=0)



