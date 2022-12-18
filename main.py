
#from datetime import date
import telebot
#import gspread

bot_token = 'token'
#googlesheet_id = 'some_spreadsheet_id'

bot = telebot.TeleBot('5881010706:AAEd4FLdnL5VCO3Xmd_uElxn_3_7LFlUqJY')
#gc = gspread.service_account()

@bot.message_handler(commands=['start','help'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, выбери, что нужно сделать:\nотправить домашку /send\nполучить домашку /get\nхочешь фото с котиками?) /cats")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.message_handler(commands=['cats'])
def cats(message):
    bot.send_animation()

@bot.message_handler(commands=['send'])
def send_hw(message):
    bot.send_message(message.from_user.id, "Из какой ты школы?\nНапиши: 57 или Наша школа")
    bot.register_next_step_handler(message, get_school)

def get_school(message):
    global school
    school = message.text
    if message.text == "57":
        bot.register_next_step_handler(message, get_name)
    if message.text == "Наша школа" or message.text == "Наша":
        bot.send_message(message.from_user.id, "Из какого ты класса? Напиши: 5 или 6")
        bot.register_next_step_handler(message, get_number)

#сделать тут иф
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Напиши свою фамилию и имя")
    bot.register_next_step_handler(message, get_photo)
    #файл на диске должен называться имя и фамилия. Запомнить переменную

def get_number(message):
    global number
    number = message.text
    if message.text == "5":
        bot.register_next_step_handler(message, get_name)
    if message.text == "6":
        bot.register_next_step_handler(message, get_name)

def get_photo(message):
    

    def save_photo_in_user_folder(message):
        directory_for_all_users_photos = "D:\img"

    user_id = message.from_user.id
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    if not os.path.isdir(str(user_id)):
        os.mkdir(str(user_id))
    os.chdir(str(user_id))
    with open("image_def_folder.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)


#def get_photo(message):




#@bot.message_handler(commands=["get"])


#@bot.message_handler(commands=["cats"])
#if __name__ == '__main__':
    #executor.start_polling(dp)

bot.polling(none_stop=True, interval=0)





#научиться добавлять фото и отправлять их в табличку


