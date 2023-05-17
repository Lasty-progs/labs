import telebot
from telebot import types
import psycopg2
import datetime

nums = int(datetime.datetime.utcnow().isocalendar()[1])



conn = psycopg2.connect(database="telegram", user="postgres", password="1", host="localhost", port="5432")
cursor = conn.cursor()
token="5952402956:AAGBSwyXLC_kzt9dixm1vzH1NsOxo5-U4JM"
bot = telebot.TeleBot(token)


week_day=['Понедельник','Вторник','Среду','Четверг','Пятницу']

def weekday (a=0):
    week_number = nums + 1
    return week_number % 2
    
week = weekday()

def days(message, day):
    cursor.execute("select * from schedule_for_the_day({});".format(day))
    records = cursor.fetchall()

    if records:
        for i in records:
            string = ' | '.join(map(str, i))
            bot.send_message(message.chat.id, string)
    else:
        bot.send_message(message.chat.id, "Занятий нет")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()


    days = ("Хочу узнать о МТУСИ","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота",
            "Расписание на текущую неделю","Расписание на следующую неделю","/help")
    temp = []

    # Create buttons panel 
    for i in days:
        temp.append(i)
        if len(temp) > 2:
            keyboard.add(types.KeyboardButton(temp.pop(0)),types.KeyboardButton(temp.pop(0)),types.KeyboardButton(temp.pop(0)))
        if temp and temp[0] == "Хочу узнать о МТУСИ":
            keyboard.add(types.KeyboardButton(temp.pop(0)))


    bot.send_message(message.chat.id, 'Здравствуйте! Выберите команду из списка.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):

    temp = """Команды:
    понедельник - расписание на понедельник
    вторник - расписание на вторник
    среда - расписание на среду
    четверг - расписание на четверг
    пятница - расписание на пятницу
    суббота - расписание на субботу
    расписание на текущую неделю - расписание на текущую неделю
    расписание на следующую неделю - расписание на следующую неделю
    /week - определение недели(четная/нечетная)"""

    bot.send_message(message.chat.id,temp)


@bot.message_handler(commands=['week'])
def start_message(message):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "Четная")
    if (nums % 2) != 0:
        bot.send_message(message.chat.id, "Нечетная")


@bot.message_handler(content_types=['text'])
def answer(message):
    
    if message.text.lower()== 'хочу узнать о мтуси' or message.text.lower()== 'mtuci':
        bot.send_message(message.chat.id, "Тогда тебе сюда - https://mtuci.ru/")

    elif message.text.lower() == 'понедельник':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[0]),parse_mode= "Markdown")
        days(message,1+week*7)
    elif message.text.lower() == 'вторник':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[1]),parse_mode= "Markdown")
        days(message,2+week*7)
    elif message.text.lower() == 'среда':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[2]),parse_mode= "Markdown")
        days(message,3+week*7)
    elif message.text.lower() == 'четверг':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[3]),parse_mode= "Markdown")
        days(message,4+week*7)
    elif message.text.lower() == 'пятница':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[4]),parse_mode= "Markdown")
        days(message,5+week*7)
    elif message.text.lower() == 'суббота':
        bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[4]),parse_mode= "Markdown")
        days(message,6+week*7)
    
    elif message.text.lower() == 'расписание на текущую неделю':
        # bot.send_message(message.chat.id, "Был нажат расписание на текущую неделю")
        for i in range(1,6):
            bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[i-1]),parse_mode= "Markdown")
            bot.send_message(message.chat.id, "------------------------------")
            days(message,i+week*7)
            bot.send_message(message.chat.id, "------------------------------")

    elif message.text.lower() == 'расписание на следующую неделю':
        # bot.send_message(message.chat.id, "Был нажат расписание на следующую неделю")
        for i in range(1,6):
            bot.send_message(message.chat.id, "*Расписание на {}:*".format(week_day[i-1]),parse_mode= "Markdown")
            bot.send_message(message.chat.id, "------------------------------")
            days(message,i+((week+1)%2)*7)
            bot.send_message(message.chat.id, "------------------------------")
    else:
        bot.send_message(message.chat.id, "Я Вас не понимаю")

bot.polling(none_stop=True, interval=0)
