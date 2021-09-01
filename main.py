from typing import Text
import telebot
from telebot import types
from telebot import util



token = '1990132177:AAHoDmxp8-RyCl-0ZN5z6wSBaRG4FDpeET4'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)







@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('නමෝ බුද්ධාය ')
    full_name = message.from_user.full_name
    user_name = message.from_user.username
    markup = telebot.types.InlineKeyboardMarkup()
    
    
    markup.add(telebot.types.InlineKeyboardButton(text='🗂ත්‍රිපිටක සූචි හා ශබ්දකෝෂ', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂දහම් පාසල් හා පිරිවෙන්', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි අට්ඨකථා', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි ඉගෙනුම', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂අභිධර්ම', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂ඉපැරිණි පොත්', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි භාෂාව', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂පින්තූර වගු සටහන්', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂බුද්ධ ජයන්ති ත්‍රිපිටකය', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂භාවනා කමටහන්', callback_data=10))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂භික්ෂු විනය', callback_data=11))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂මෘදුකාංග', callback_data=12))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂රේරුකානේ චන්ද්‍රවිමල හිමි', callback_data=13))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂වෙනත්', callback_data=14))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂වෙනත් ත්‍රිපිටක', callback_data=15))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂සිංහල අට්ඨකථා', callback_data=16))
    markup.add(telebot.types.InlineKeyboardButton(text='🗂සූත්‍ර', callback_data=17))

    
    
    markup.add(telebot.types.InlineKeyboardButton(text='☸️The Buddhist Group☸️', url="https://t.me/the_buddhist_group"))
    markup.add(telebot.types.InlineKeyboardButton(text='Contact Creator', url="https://t.me/harshithalakruwan")) 

    
    
    
    bot.send_message(message.chat.id, "ආයුබෝවන්" +full_name+ "මෙම bot මගින් බෞද්ධ පොත් ලබාගත හැක. ඔබට අවශ්‍ය පොත් වර්ගය තෝරන්න.",reply_markup=markup,parse_mode="Markdown")






@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == '100':
        print('නමෝ බුද්ධාය ')

        full_name = call.message.from_user.full_name
        user_name = call.message.from_user.username
    
        markup = telebot.types.InlineKeyboardMarkup()

        markup.add(telebot.types.InlineKeyboardButton(text='🗂අභිධර්ම', callback_data=1)) 
        markup.add(telebot.types.InlineKeyboardButton(text='🗂ඉපැරිණි පොත්', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂ත්‍රිපිටක සූචි හා ශබ්දකෝෂ', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂දහම් පාසල් හා පිරිවෙන්', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි අට්ඨකථා', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි ඉගෙනුම', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂පාලි භාෂාව', callback_data=7))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂පින්තූර වගු සටහන්', callback_data=8))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂බුද්ධ ජයන්ති ත්‍රිපිටකය', callback_data=9))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂භාවනා කමටහන්', callback_data=10))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂භික්ෂු විනය', callback_data=11))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂මෘදුකාංග', callback_data=12))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂රේරුකානේ චන්ද්‍රවිමල හිමි', callback_data=13))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂වෙනත්', callback_data=14))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂වෙනත් ත්‍රිපිටක', callback_data=15))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂සිංහල අට්ඨකථා', callback_data=16))
        markup.add(telebot.types.InlineKeyboardButton(text='🗂සූත්‍ර', callback_data=17))

    
    
        markup.add(telebot.types.InlineKeyboardButton(text='☸️The Buddhist Group☸️', url="https://t.me/the_buddhist_group"))
        markup.add(telebot.types.InlineKeyboardButton(text='Contact Creator', url="https://t.me/harshithalakruwan")) 

    
    
    
        bot.send_message(call.message.chat.id, "ආයුබෝවන්" +full_name+ "මෙම bot මගින් බෞද්ධ පොත් ලබාගත හැක. ඔබට අවශ්‍ය පොත් වර්ගය තෝරන්න. ",reply_markup=markup,parse_mode="Markdown")

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)






    elif call.data == '3':
        print('🗂අභිධර්ම')
        markup = telebot.types.InlineKeyboardMarkup()


        markup.add(telebot.types.InlineKeyboardButton(text='🔙 ආපසු මුල් පිටුව‍ට', callback_data=100))


        bot.forward_message(call.message.chat.id, -1001582189590, 5)
        bot.forward_message(call.message.chat.id, -1001582189590, 5)
        bot.forward_message(call.message.chat.id, -1001582189590, 6)
        bot.forward_message(call.message.chat.id, -1001582189590, 7)
        bot.forward_message(call.message.chat.id, -1001582189590, 8)
        bot.forward_message(call.message.chat.id, -1001582189590, 9)

        bot.send_message(call.message.chat.id,"ඇතුලත් කර ඇති අභිධර්ම පොත් අවසානයි",reply_markup=markup)

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


     
    
    


    















    
    
    














bot.polling(none_stop=True)