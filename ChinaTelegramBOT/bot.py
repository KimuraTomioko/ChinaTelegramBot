from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import InputFile
import os

def start(update, context):
    button_about = KeyboardButton("📌О компании")
    button_services = KeyboardButton("📝Наши услуги")
    button_prices = KeyboardButton("💰Наши цены")
    button_ransom = KeyboardButton("📦Выкуп")
    button_selfransom = KeyboardButton("🛍Самовыкуп")
    button_scheme_of_work = KeyboardButton("😉Схема работы")
    button_connect_with_us = KeyboardButton("📨Связаться с нами")
    button2 = KeyboardButton("🗃Упаковка")
    button_actual_uan = KeyboardButton("🤔 Актуальный курс юаня")
    reply_keyboard = [[button_about], [button_services, button_prices], [button_ransom, button_selfransom], [button_scheme_of_work, button_connect_with_us], [button2], [button_actual_uan]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Поздравляем! Вы подписались на ChinaTrendsBot - Доставка из Китая. Используйте /off чтобы приостановить подписку.", reply_markup=markup)

def off(update, context):
    reply_keyboard = [['Start']]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ваша подписка деактивирована. Вы всегда можете включить ее снова с помощью команды /start.", reply_markup=markup)

def on(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ваша подписка снова активирована!")

def handle_message(update, context):
    if update.message.text == 'Start':
        start(update, context)
    elif update.message.text == '📌О компании':
        about_company(update, context)
    elif update.message.text == '📝Наши услуги':
        our_services(update, context)
    elif update.message.text == '💰Наши цены':
        our_prices(update, context)
    elif update.message.text == "📦Выкуп":
        ransom(update, context)
    elif update.message.text == 'Go Back':
        go_back(update, context)
    elif update.message.text == '💰Сколько стоят наши услуги':
        our_service_prices(update, context)
    elif update.message.text == '💶За что я плачу?':
        what_do_i_pay(update, context)
    elif update.message.text == '💸Варианты логистики':
        delivery_price(update, context)
    elif update.message.text == '💳Способы оплат':
        payment_methods(update, context)
    #elif update.message.text == 'В рублях (₽)':
        #payment_in_rubles(update, context)
    #elif update.message.text == 'В юанях (¥)':
        #payment_in_yuan(update, context)
    elif update.message.text == "🛍Самовыкуп":
        self_ransom(update, context)
    elif update.message.text == "😉Схема работы":
        scheme_of_work(update, context)
    elif update.message.text == "📨Связаться с нами":
        connect_with_us(update, context)
    elif update.message.text == "📝Бланк заказа":
        blank(update, context)
    elif update.message.text == "🗃Упаковка":
        package(update, context)
    elif update.message.text == "🔥Обычная упаковка":
        default_package(update, context)
    elif update.message.text == "🔥Картонные уголки":
        cardboard_corners_package(update, context)
    elif update.message.text == "🔥Деревянная упаковка":
        wood_package(update, context)
    elif update.message.text == "🤔 Актуальный курс юаня":
        current_yuan_exchange_rate(update, context)

def about_company(update, context):
    message = "ChinaTrends - Ваш надежный партнёр по закупкам товаров из Китая!\n\nУ нас два офиса: в России (Ростов-на-Дону) и в Китае два склада (ИУ и Гуанджоу)🏠\n\nЕсть свой фулфилмент в Москве📦\n\nПомогаем нашим клиентам в оплате товаров в Китае, по оптимальному курсу💲\n\nНайдём любой запрос в требуемые сроки👌🏻"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def our_services(update, context):
    message = "Наша компания готова предложить комплексное решение по работе с Китаем для Вас и Вашего бизнеса.\nЧем можем быть полезны для Вас: \n🔴 Закупить товар с различных китайских сайтов и напрямую с фабрики 🔴\nДоговориться о цене с поставщиком\n🔴 Выбить для вас скидку.\n🔴 Проверить на своём складе на качество и отсутствие брака (в случае обнаружения вернуть или обменять)\n🔴 Упаковать и доставить до вашего адреса.\n🔴 По вашему тех заданию упаковать и отправить товар на склады Маркетплейсов сразу в Москве.\n\nВесь спектр услуг по работе с Китаем под ключ 🔑"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def our_prices(update, context):
    button1 = KeyboardButton("💰Сколько стоят наши услуги")
    button2 = KeyboardButton("💶За что я плачу?")
    button3 = KeyboardButton("💸Варианты логистики")
    button4 = KeyboardButton("💳Способы оплат")
    button5 = KeyboardButton("Go Back")
    reply_keyboard = [[button1, button2], [button3, button4], [button5]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="ℹ️ Выберите нужный пункт", reply_markup=markup)

def what_do_i_pay(update, context):
    message = "У нас нет скрытых платежей в компании и мы сразу говорим за что вы будете платить, что бы в будущем не возникло недопонимания👇🏻\n\n❗️Вы платите за товар\n❗️За доставку до нашего склада (иногда бесплатно и мы будем просить это у продавцов)\n❗️За нашу комиссию до 10%\n❗️За страховку 2 - 3 % от стоимости товара\n❗️За упаковку (от 5$ за место обычная упаковка, или от 10 $ за место усиленная упаковка (обрешётка))\n❗️За доставку до Москвы из Китая\n❗️За доставку до вашего города (если нужно получать в другом городе).\n❗️ За разгрузку товара в Москве - 300₽ за 1 место.\n⚠️За доставку вашего товара на фулфилмент, если понадобится данная услуга."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def our_service_prices(update, context):
    message = "Наша комиссия за услуги составляет от 5 до 10 % от суммы перевода продавцу.\n\nВ эту сумму входит:\n💎 Общение с фабрикой\n💎 Выкуп товара\n💎 Выборочная проверка товара на брак\n💎 Консолидация и переупаковка товара\n💎 Хранение на нашем складе до момента отправки\n\n👌🏻Минимальная сумма заказа - 50 000 рублей.\n👌🏻Ограничении‌ по максимальному весу на перевозку нет, а минимальный 10кг😉\n\nГрадация комиссии:\nОт 50 000 до 500 000 = 10%\nОт 500 000 до 1 000 000 = 7%\nОт 1 000 000 = 5%\n\nИсключения: сложные заказы и заказы, где очень много ссылок. Более подробную информацию можно получить у менеджера в телеграмм канале."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def delivery_price(update, context):
   #photo_path = "Delevery_price.jpg"  # Путь к вашей картинке
   #context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo_path, 'rb'))
    message = "Тариф для логистики лучше выбирать исходя из Ваших потребностей и мы сможем подобрать удобный вариант.\n\nВ среднем из практики есть самые распространённые тарифы. Стоит учитывать что отчет логистики начинается с момента отправки Вашего груза в РФ, а не с момента оплаты Вашего товара, так как может понадобиться время на его производство, а так же внутреннюю логистику по Китаю.\n\nЖД 30-45 дней от 1,5$ за кг\nДолгое Авто 25-30 дней от 2$ за кг\nБыстрое Авто 18-25 дней от 3$ за кг\nАвиа Доставка 10-12 дней от 7 $ за кг\n\nТарифы рассчитываются индивидуально исходя из данных, ВЕС, ТОВАР, ГАБАРИТЫ, НАИМЕНОВАНИЕ ТОВАРА, (ФОТО) для того чтоб рассчитать, таможенную ставку."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def payment_methods(update, context):
    message = '💴 Оплата в рублях возможна на нашу банковскую карту Сбербанк и Тинькофф.\n 💴 Расчётный счёт - так же принимаем средства на р/с. Комиссия 10% от суммы принятия, вывод денег несколько дней на нашу банковскую карту и далее уже по курсу дня мы выводим средства в Китай (обмениваем на юань). Сможем предоставить отгрузочные документы (торг 12, акт оказания услуг, расходная накладная), подготовим, подпишем и вышлем вам.\n 💴 Наличными при личной встрече, либо с нашим представителем в вашем городе.\n 💴 Возможна оплата через криптовалюту: принимаем (USDT… )\n 💴 Юань принимаем с вашего кошелька Alipay на наш Alipay.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

'''def payment_in_rubles(update, context):
    message = "❕Оплата в рублях возможна на нашу банковскую карту Сбербанк и Тинькофф.\n\n❕Расчётный счёт - у нас есть партнёры которые готовы принять оплату на р/с. Их комиссия 12% от суммы принятия, вывод денег 7 дней на нашу банковскую карту и далее уже по курсу дня мы выводим средства в Китай (обмениваем на юань). Сможем предоставить отгрузочные документы (торг 12), подпишем и вышлем вам. Подготовка накладных на вашей стороне, с нас подпись и отправка. \n\n❕Но! Важно чтобы суммы к оплате были не меньше 75-80 тысяч рублей, в противном случае принять оплату на р/с партнёры не смогут."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def payment_in_yuan(update, context):
    message = "Юани мы готовы принимать на нашу Китайскую карту, например переводом с вашего Alipay на наш Alipay👌🏻"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)'''

def ransom(update, context):
    button1 = KeyboardButton("📝Бланк заказа")
    # button2 = KeyboardButton("🗃Упаковка")
    button3 = KeyboardButton("Go Back")
    reply_keyboard = [[button1], [button3]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Наша компания может выкупить интересующий Вас товар, на любой площадке, сайте или просто по WeChat. Вы можете скинуть нам информацию для выкупа любым удобным для вас способом:\n🔺Заполнить наш бланк заказа. Можно скачать наш бланк чуть ниже.\n🔺Можете заполнить Гугл Таблицу в удобном для Вас виде и прислать нам ссылку.\n🔺Можете создать свои‌ бланк заказа и присылать нашему менеджеру.\n🔺Можете прислать нам ссылки в соц. сетях и мы так же сможем выкупить ваш товар.\n🔺Если у вас есть другои‌ способ, так же готовы его рассмотреть. ( фото товара, наименование…).", reply_markup=markup)    

from telegram import InputFile

def blank(update, context):
    message = 'Мини-инструкция по заполнению бланка внутри 🙂'
    # Путь к бланку
    xlsx_file_path = 'Blank_ChinaTrends.xlsx'
    with open(xlsx_file_path, 'rb') as file:
        xlsx_file = InputFile(file)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        context.bot.send_document(chat_id=update.effective_chat.id, document=xlsx_file)

def package(update, context):
    button1 = KeyboardButton("🔥Обычная упаковка")
    button2 = KeyboardButton("🔥Картонные уголки")
    button3 = KeyboardButton("🔥Деревянная упаковка")
    button4 = KeyboardButton("Go Back")
    reply_keyboard = [[button1], [button2], [button3], [button4]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Примеры того, как выглядит упаковка😌", reply_markup=markup)

def default_package(update, context):
    photo1_default = 'photo1_default.jpg'
    photo2_default = 'photo2_default.jpg'
    photo3_default = 'photo3_default.jpg'
    photo4_default = 'photo4_default.jpg'
    message = 'Обычная: \n🤓Это картонная коробка + пакет (защитит от влаги) мешок + скотч. \n😎 Идеально подойдёт для одежды, тканей и товаров, которые не повредятся при перевозке даже при падении с высоты (например при падении с фуры) \n💰Цена: от 3$'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo1_default, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo2_default, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo3_default, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo4_default, 'rb'))

def cardboard_corners_package(update, context):
    photo1_cardboard = 'photo1_cardboard.jpg'
    photo2_cardboard = 'photo2_cardboard.jpg'
    photo3_cardboard = 'photo3_cardboard.jpg'
    photo4_cardboard = 'photo4_cardboard.jpg'
    message = 'Картонные уголки: \n🤓Это картонная коробка + картонные уголки по всему периметру + пакет (защитит от влаги) мешок + скотч. 😎Идеально подойдёт для товаров, которые готовы выдержать не большие падения. Например для блокнотов и книг, для значков, наборов, не дорогих электронных товаров. Рекомендуем, если хотите сохранить картонные заводские коробки товаров.\n 💰Цена: от 7$'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo1_cardboard, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo2_cardboard, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo3_cardboard, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo4_cardboard, 'rb'))

def wood_package(update, context):
    photo1_wood = 'photo1_wood.jpg'
    photo2_wood = 'photo2_wood.jpg'
    photo3_wood = 'photo3_wood.jpg'
    photo4_wood = 'photo4_wood.jpg'
    photo5_wood = 'photo5_wood.jpg'
    message = 'Деревянная обрешётка:\n 🤓Это картонная коробка + пакет (защитит от влаги) мешок + скотч + деревянный короб\n 😎 Идеально подойдёт для хрупких товаров и тех, где важно сохранить внешний в д продукта (продажный вид)\n 💰Цена: от 8$'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo1_wood, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo2_wood, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo3_wood, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo4_wood, 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo5_wood, 'rb'))

def self_ransom(update, context):
    message = "Вы можете самостоятельно выкупить товар в Китае на наш склад и мы организуем его логистику в РФ🚚\n\nСхема очень проста:\n1. Мы даём вам адрес склада и присваиваем порядковый код 2. Вы выкупаете заказы( либо можем мы оплатить поставщику) и просите указать продавца ваш код на посылке 3. Как все посылки будут доставлены (можете сверяться на сайте 1688/Таобао или в поисковике Baidu.com по трек номеру), вы присылаете нам списком все трек номера для поиска и сборки 4. Мы все находим, присылаем вам общее фото и согласовываем отправку 5. Товар пакуется и отправляется к вам🏎\n\nЕсли вам нужна проверка на брак и фотоотчёт, то это услуга стоит 5% от стоимости заказа, но минимум 200¥🤝"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message) 

def scheme_of_work(update, context):
    message = "Наша работа будет построена следующим образом:\n❕Вы заполняете бланк заказа для выкупа товара любым удобным для вас способом\n❕Мы говорим вам стоимость заказа с учетом выкупа + нашей комиссии;\n❕Вы оплачиваете нам эту сумму;\n❕Мы выкупаем товар и он едет к нам на склад;\n❕По приходу товара на наш склад мы делаем выборочную проверку качества товара;\n❕Далее мы с вами выбираем упаковку и вид доставки, чтобы вложиться в нужные для Вас сроки;\n❕Товар взвешивается, переупаковывается и отправляется в Москву;\n❕Вы оплачиваете доставку либо после поступления товара в Москву, либо сразу перед отправлением из Китая;\n❕Как только товар поступает в Москву наши сотрудники с вами свяжутся для уточнения деталей (Отправки в другой город, если да, то какой ТК и на чье имя, или будет самостоятельный забор в Москве)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message) 

def connect_with_us(update, context):
    message = "Наши социальные сети:\n💎 Вконтакте Сообщество в VK (https://vk.com/china_trends_ru)\n\n💎 В телеграмме Наш ТГ канал (https://t.me/china_trends)\n\n💎 Наш сайт\n\n💎 Отзывы о нашей компании Отзывы о Нас (https://t.me/otziv_china_trends)\n\n💎 Наш менеджер Менеджер (https://t.me/china_trends_manager)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

import requests

import requests

def current_yuan_exchange_rate(update, context):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    yuan_to_rub_rate = data['Valute']['CNY']['Value']

    markup_amount = 0.7
    final_rate = yuan_to_rub_rate + markup_amount
    message = f"❗️Курсы меняются каждый день. Пожалуйста, перед оплатой, уточняйте актуальный курс\n Текущий курс ЮАНЯ к рублю: {final_rate:.2f}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    
def go_back(update, context):
    button_about = KeyboardButton("📌О компании")
    button_services = KeyboardButton("📝Наши услуги")
    button_prices = KeyboardButton("💰Наши цены")
    button_ransom = KeyboardButton("📦Выкуп")
    button_selfransom = KeyboardButton("🛍Самовыкуп")
    button_scheme_of_work = KeyboardButton("😉Схема работы")
    button_connect_with_us = KeyboardButton("📨Связаться с нами")
    button_actual_uan = KeyboardButton("🤔 Актуальный курс юаня")
    reply_keyboard = [[button_about], [button_services, button_prices], [button_ransom, button_selfransom], [button_scheme_of_work, button_connect_with_us], [button_actual_uan]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Начальное меню", reply_markup=markup)

def admin():
    pass

def main():
    updater = Updater(token='6364323743:AAFKSSmVGzx8TAH-gZz05ms6y1NySOVstsk', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('off', off))
    dispatcher.add_handler(CommandHandler('on', on))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))
    dispatcher.add_handler(CommandHandler('what_do_i_pay', what_do_i_pay))  # Добавляем обработчик для кнопки "💶За что я плачу?"
    dispatcher.add_handler(CommandHandler('delivery_price', delivery_price))
    dispatcher.add_handler(CommandHandler('our_service_prices', our_service_prices))
    dispatcher.add_handler(CommandHandler('blank', blank))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


