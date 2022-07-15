import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    print(msg.from_user.first_name, " (", msg.from_user.username, ")", ": \"", msg.text, "\"", sep='')
    print("Ответ:", bot.reply_to(msg, "Введите выражение, например: 1 * (2 + 3) / 4 ^ 5").text, "\n")


@bot.message_handler(content_types=['text'])
def get_text_messages(msg):
    print(msg.from_user.first_name, " (", msg.from_user.username, ")", ": \"", msg.text, "\"", sep='')
    try:
        print("Ответ:", bot.reply_to(msg, eval(compile(str(msg.text).replace("^", "**"), "str", "eval"))).text, "\n")
    except ZeroDivisionError:
        print("Ответ:", bot.reply_to(msg, "Ошибка: Деление на ноль.").text, "\n")
    except NameError:
        print("Ответ:", bot.reply_to(msg, "Ошибка: Введите выражение, например: 1 * (2 + 3) / 4 ^ 5").text, "\n")
    except Exception as err_name:
        print("Error:", type(err_name), err_name)


bot.polling(none_stop=True)
