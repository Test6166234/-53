import telebot
import os

TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"
bot = telebot.TeleBot('8542656922:AAE2aAq2lK2E_mY_jGGEJQ427faoL9uFOR0')

CARS = [
    {
        "name": "Audi A8",
        "engine": "3.0L V6",
        "speed": "250 км/ч",
        "fuel": "Бензин",
        "photo": "cars/AudiA8.jpg"
    },
    {
        "name": "BMW 7 Series",
        "engine": "3.0L Turbo",
        "speed": "250 км/ч",
        "fuel": "Бензин",
        "photo": "cars/BMW7Series.jpg"
    },
    {
        "name": "Honda Accord",
        "engine": "2.0L",
        "speed": "210 км/ч",
        "fuel": "Бензин",
        "photo": "cars/HondaAccord.jpg"
    },
    {
        "name": "Honda Fit",
        "engine": "1.5L",
        "speed": "180 км/ч",
        "fuel": "Бензин",
        "photo": "cars/HondaFit.jpg"
    },
    {
        "name": "Hyundai Accent",
        "engine": "1.6L",
        "speed": "190 км/ч",
        "fuel": "Бензин",
        "photo": "cars/HyundaiAccent.jpg"
    },
    {
        "name": "Hyundai Sonata",
        "engine": "2.5L",
        "speed": "220 км/ч",
        "fuel": "Бензин",
        "photo": "cars/HyundaiSonata.jpg"
    },
    {
        "name": "Kia Rio",
        "engine": "1.6L",
        "speed": "185 км/ч",
        "fuel": "Бензин",
        "photo": "cars/KiaRio.jpg"
    },
    {
        "name": "Mazda 6",
        "engine": "2.5L",
        "speed": "225 км/ч",
        "fuel": "Бензин",
        "photo": "cars/Mazda6.jpg"
    },
    {
        "name": "Mercedes S-Class",
        "engine": "3.0L",
        "speed": "250 км/ч",
        "fuel": "Бензин",
        "photo": "cars/MercedesSClass.jpg"
    },
    {
        "name": "Nissan Note",
        "engine": "1.6L",
        "speed": "170 км/ч",
        "fuel": "Бензин",
        "photo": "cars/NissanNote.jpg"
    },
    {
        "name": "Range Rover Vogue",
        "engine": "4.4L V8",
        "speed": "230 км/ч",
        "fuel": "Бензин",
        "photo": "cars/RangeRoverVogue.jpg"
    },
    {
        "name": "Toyota Camry",
        "engine": "2.5L",
        "speed": "210 км/ч",
        "fuel": "Бензин",
        "photo": "cars/ToyotaCamry.jpg"
    },
    {
        "name": "Toyota Corolla",
        "engine": "1.8L",
        "speed": "195 км/ч",
        "fuel": "Бензин",
        "photo": "cars/ToyotaCorolla.jpg"
    },
    {
        "name": "Volkswagen Passat",
        "engine": "2.0L Turbo",
        "speed": "230 км/ч",
        "fuel": "Бензин",
        "photo": "cars/VolswagenPassat.jpg"
    }
]

user_index = {}

def keyboard():
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("⬅️ Назад", "➡️ Вперед")
    return kb

@bot.message_handler(commands=["start"])
def start(message):
    user_index[message.chat.id] = 0
    send_car(message.chat.id)

def send_car(chat_id):
    idx = user_index[chat_id]
    car = CARS[idx]

    text = (
        f"🚗 {car['name']}\n"
        f"🔧 Двигатель: {car['engine']}\n"
        f"⚡ Скорость: {car['speed']}\n"
        f"⛽ Топливо: {car['fuel']}"
    )

    if os.path.exists(car["photo"]):
        bot.send_photo(chat_id, open(car["photo"], "rb"), caption=text, reply_markup=keyboard())
    else:
        bot.send_message(chat_id, text + "\n(Фото не найдено)", reply_markup=keyboard())

@bot.message_handler(func=lambda m: m.text == "➡️ Вперед")
def next_car(message):
    user_index[message.chat.id] = (user_index[message.chat.id] + 1) % len(CARS)
    send_car(message.chat.id)

@bot.message_handler(func=lambda m: m.text == "⬅️ Назад")
def prev_car(message):
    user_index[message.chat.id] = (user_index[message.chat.id] - 1) % len(CARS)
    send_car(message.chat.id)

bot.infinity_polling(skip_pending=True)
