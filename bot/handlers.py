from telebot import types
from .google_sheets import get_google_sheet_value, append_date_to_sheet
from .utils import check_date_format
from .payment import create_payment


def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton("Кнопка 1")
        btn2 = types.KeyboardButton("Кнопка 2")
        btn3 = types.KeyboardButton("Кнопка 3")
        btn4 = types.KeyboardButton("Кнопка 4")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, "Привет! Выбери действие:", reply_markup=markup
        )

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        if message.text == "Кнопка 1":
            bot.send_message(
                message.chat.id,
                "Текст + ссылка на Яндекс карты: https://yandex.ru/maps/?text=Ленина%1",
            )
        elif message.text == "Кнопка 2":
            payment_url = create_payment(2.00, "RUB", "Оплата 2 рубля")
            bot.send_message(
                message.chat.id, f"Текст + ссылка на оплату 2 р: {payment_url}"
            )
        elif message.text == "Кнопка 3":
            with open("images/img1.jpg", "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption="Текст + картинка")
        elif message.text == "Кнопка 4":
            value = get_google_sheet_value("A2")
            bot.send_message(message.chat.id, f"Значение A2: {value}")
        else:
            input_date = message.text
            if check_date_format(input_date):
                append_date_to_sheet(input_date)
                bot.send_message(message.chat.id, "Дата верна")
            else:
                bot.send_message(message.chat.id, "Дата введена неверно")
