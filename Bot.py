import telebot

TOKEN = "8075930976:AAGyz3Pm-Nj4o-o00B8VTVzr2ZtrO_uTKN0"
bot = telebot.TeleBot(TOKEN)

catalog = {
    "1": {"name": "Футболка", "price": "1000 руб"},
    "2": {"name": "Кепка", "price": "500 руб"},
    "3": {"name": "Худи", "price": "2000 руб"}
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Я бот-магазин. Напиши /catalog чтобы посмотреть товары.")

@bot.message_handler(commands=['catalog'])
def show_catalog(message):
    text = "📦 Наш каталог:\n"
    for key, item in catalog.items():
        text += f"{key}. {item['name']} — {item['price']}\n"
    text += "\n✏️ Введите номер товара, чтобы заказать."
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text in catalog)
def handle_selection(message):
    item = catalog[message.text]
    bot.send_message(
        message.chat.id,
        f"✅ Вы выбрали: {item['name']} за {item['price']}. Мы скоро с вами свяжемся!"
    )

bot.polling()
