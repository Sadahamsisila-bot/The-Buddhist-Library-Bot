from typing import Text
import telebot
from telebot import types
from telebot import util



token = '1990132177:AAHoDmxp8-RyCl-0ZN5z6wSBaRG4FDpeET4'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)



abhidharma_msg = open('abhidharma.txt','rb').read()




@bot.message_handler(content_types=['new_chat_members'])
def bot_func(message):

    welcome_sticker = open('sticker.webp','rb')
    bot.reply_to(message,"ආයුබෝවන්! තෙරුවන් සරණයි!")


@bot.message_handler(commands=['start','poth','books'])
def send_welcome(message):
    print('නමෝ බුද්ධාය ')
    
    full_name = message.from_user.full_name
    user_name = message.from_user.username
    


    print('Bot started by'+full_name)


    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(text='➕Add to group', url ="http://t.me/buddhist_books_bot?startgroup=true"))
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

    
    
    markup.add(telebot.types.InlineKeyboardButton(text='☸️Buddhist Groups☸️', callback_data=18))
    markup.add(telebot.types.InlineKeyboardButton(text='Contact Creator', url="https://t.me/harshithalakruwan")) 

    
    
    
    bot.send_message(message.chat.id, "ආයුබෝවන් " +full_name+ " මෙම bot මගින් බෞද්ධ පොත් ලබාගත හැක. ඔබට අවශ්‍ය පොත් වර්ගය තෝරන්න.",reply_markup=markup,parse_mode="Markdown")
    bot.send_message(1451642747, "Bot started by " +full_name+ " user name @" +user_name,parse_mode="Markdown")






@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == '100':
        print('නමෝ බුද්ධාය ')
        

        full_name = call.message.from_user.full_name
        user_name = call.message.from_user.username


        print('Bot started by'+full_name)
    
        markup = telebot.types.InlineKeyboardMarkup()
        
        markup.add(telebot.types.InlineKeyboardButton(text='➕Add to group', url ="http://t.me/buddhist_books_bot?startgroup=true")) 

        btn01 = telebot.types.InlineKeyboardButton(text='🗂අභිධර්ම', callback_data=1) 
        btn02 = telebot.types.InlineKeyboardButton(text='🗂ඉපැරිණි පොත්', callback_data=2)
        btn03 = telebot.types.InlineKeyboardButton(text='🗂ත්‍රිපිටක සූචි හා ශබ්දකෝෂ', callback_data=3)
        btn04 = telebot.types.InlineKeyboardButton(text='🗂දහම් පාසල් හා පිරිවෙන්', callback_data=4)
        btn05 = telebot.types.InlineKeyboardButton(text='🗂පාලි අට්ඨකථා', callback_data=5)
        btn06 = telebot.types.InlineKeyboardButton(text='🗂පාලි ඉගෙනුම', callback_data=6)
        btn07 = telebot.types.InlineKeyboardButton(text='🗂පාලි භාෂාව', callback_data=7)
        btn08 = telebot.types.InlineKeyboardButton(text='🗂පින්තූර වගු සටහන්', callback_data=8)
        btn09= telebot.types.InlineKeyboardButton(text='🗂බුද්ධ ජයන්ති ත්‍රිපිටකය', callback_data=9)
        btn010 = telebot.types.InlineKeyboardButton(text='🗂භාවනා කමටහන්', callback_data=10)
        btn011 = telebot.types.InlineKeyboardButton(text='🗂භික්ෂු විනය', callback_data=11)
        btn012 = telebot.types.InlineKeyboardButton(text='🗂මෘදුකාංග', callback_data=12)
        btn013 = telebot.types.InlineKeyboardButton(text='🗂රේරුකානේ චන්ද්‍රවිමල හිමි', callback_data=13)
        btn014 = telebot.types.InlineKeyboardButton(text='🗂වෙනත්', callback_data=14)
        btn015 = telebot.types.InlineKeyboardButton(text='🗂වෙනත් ත්‍රිපිටක', callback_data=15)
        btn016 = telebot.types.InlineKeyboardButton(text='🗂සිංහල අට්ඨකථා', callback_data=16)
        btn017 = telebot.types.InlineKeyboardButton(text='🗂සූත්‍ර', callback_data=17)

    
        markup.add(btn01,btn02)
        markup.add(btn03,btn04)
        markup.add(btn05,btn06)
        markup.add(btn07,btn08)
        markup.add(btn09,btn010)
        markup.add(btn011,btn012)
        markup.add(btn013,btn014)
        markup.add(btn015,btn016)
        markup.add(btn017)

        markup.add(telebot.types.InlineKeyboardButton(text='☸️Buddhist Groups☸️', callback_data=18))
        markup.add(telebot.types.InlineKeyboardButton(text='Contact Creator', url="https://t.me/harshithalakruwan")) 

          
    
    
        bot.send_message(call.message.chat.id, "ආයුබෝවන්" +full_name+ "මෙම bot මගින් බෞද්ධ පොත් ලබාගත හැක. ඔබට අවශ්‍ය පොත් වර්ගය තෝරන්න. ",reply_markup=markup,parse_mode="Markdown")

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)






    elif call.data == '1':
        print('🗂අභිධර්ම')
        markup = telebot.types.InlineKeyboardMarkup()


        btn1 = telebot.types.InlineKeyboardButton(text='1️⃣', callback_data=101)
        btn2 = telebot.types.InlineKeyboardButton(text='2️⃣', callback_data=102)
        btn3 = telebot.types.InlineKeyboardButton(text='3️⃣', callback_data=103)
        btn4 = telebot.types.InlineKeyboardButton(text='4️⃣', callback_data=104)
        btn5 = telebot.types.InlineKeyboardButton(text='5️⃣', callback_data=105)
        btn6 = telebot.types.InlineKeyboardButton(text='6️⃣', callback_data=106)
        btn7 = telebot.types.InlineKeyboardButton(text='7️⃣', callback_data=107)
        btn8 = telebot.types.InlineKeyboardButton(text='8️⃣', callback_data=108)
        btn9 = telebot.types.InlineKeyboardButton(text='9️⃣', callback_data=109)
        btn10 = telebot.types.InlineKeyboardButton(text='🔟', callback_data=110)
        btn11 = telebot.types.InlineKeyboardButton(text='1️⃣1️⃣', callback_data=111)
        btn12 = telebot.types.InlineKeyboardButton(text='1️⃣2️⃣', callback_data=112)
        btn13 = telebot.types.InlineKeyboardButton(text='1️⃣3️⃣', callback_data=113)
        btn14 = telebot.types.InlineKeyboardButton(text='1️⃣4️⃣', callback_data=114)
        btn15 = telebot.types.InlineKeyboardButton(text='1️⃣5️⃣', callback_data=115)
        btn16 = telebot.types.InlineKeyboardButton(text='1️⃣6️⃣', callback_data=116)
        btn17 = telebot.types.InlineKeyboardButton(text='1️⃣7️⃣', callback_data=117)
        btn18 = telebot.types.InlineKeyboardButton(text='1️⃣8️⃣', callback_data=118)
        btn19 = telebot.types.InlineKeyboardButton(text='1️⃣9️⃣', callback_data=119)
        btn20 = telebot.types.InlineKeyboardButton(text='2️⃣0️⃣', callback_data=120)
        btn21 = telebot.types.InlineKeyboardButton(text='2️⃣1️⃣', callback_data=121)
        btn22 = telebot.types.InlineKeyboardButton(text='2️⃣2️⃣', callback_data=122)
        btn23 = telebot.types.InlineKeyboardButton(text='2️⃣3️⃣', callback_data=123)
        btn24 = telebot.types.InlineKeyboardButton(text='2️⃣4️⃣', callback_data=124)
        btn25 = telebot.types.InlineKeyboardButton(text='2️⃣5️⃣', callback_data=125)
        btn26 = telebot.types.InlineKeyboardButton(text='2️⃣6️⃣', callback_data=126)
        btn27 = telebot.types.InlineKeyboardButton(text='2️⃣7️⃣', callback_data=127)
        btn28 = telebot.types.InlineKeyboardButton(text='2️⃣8️⃣', callback_data=128)
        btn29 = telebot.types.InlineKeyboardButton(text='2️⃣9️⃣', callback_data=129)
        btn30 = telebot.types.InlineKeyboardButton(text='3️⃣0️⃣', callback_data=130)
        btn31 = telebot.types.InlineKeyboardButton(text='3️⃣1️⃣', callback_data=131)
        btn32 = telebot.types.InlineKeyboardButton(text='3️⃣2️⃣', callback_data=132)
        btn33 = telebot.types.InlineKeyboardButton(text='3️⃣3️⃣', callback_data=133)
        btn34 = telebot.types.InlineKeyboardButton(text='3️⃣4️⃣', callback_data=134)
        btn35 = telebot.types.InlineKeyboardButton(text='3️⃣5️⃣', callback_data=135)
        btn36 = telebot.types.InlineKeyboardButton(text='3️⃣6️⃣', callback_data=136)
        btn37 = telebot.types.InlineKeyboardButton(text='3️⃣7️⃣', callback_data=137)
        btn38 = telebot.types.InlineKeyboardButton(text='3️⃣8️⃣', callback_data=138)
        btn39 = telebot.types.InlineKeyboardButton(text='3️⃣9️⃣', callback_data=139)
        btn40 = telebot.types.InlineKeyboardButton(text='4️⃣0️⃣', callback_data=140)
        btn41 = telebot.types.InlineKeyboardButton(text='4️⃣1️⃣', callback_data=141)
        btn42 = telebot.types.InlineKeyboardButton(text='4️⃣2️⃣', callback_data=142)
        btn43 = telebot.types.InlineKeyboardButton(text='4️⃣3️⃣', callback_data=143)
        btn44 = telebot.types.InlineKeyboardButton(text='4️⃣4️⃣', callback_data=144)
        btn45 = telebot.types.InlineKeyboardButton(text='4️⃣5️⃣', callback_data=145)
        btn46 = telebot.types.InlineKeyboardButton(text='4️⃣6️⃣', callback_data=146)
        btn47 = telebot.types.InlineKeyboardButton(text='4️⃣7️⃣', callback_data=147)
        btn48 = telebot.types.InlineKeyboardButton(text='4️⃣8️⃣', callback_data=148)
        btn49 = telebot.types.InlineKeyboardButton(text='4️⃣9️⃣', callback_data=149)
        btn50 = telebot.types.InlineKeyboardButton(text='5️⃣0️⃣', callback_data=150)
        btn51 = telebot.types.InlineKeyboardButton(text='5️⃣1️⃣', callback_data=151)
        btn52 = telebot.types.InlineKeyboardButton(text='5️⃣2️⃣', callback_data=152)
        btn53 = telebot.types.InlineKeyboardButton(text='5️⃣3️⃣', callback_data=153)
        
        
        btn54 = telebot.types.InlineKeyboardButton(text='🔙 ආපසු මුල් පිටුව‍ට', callback_data=100)
        



        




        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
        markup.add(btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18)
        markup.add(btn19,btn20,btn21,btn22,btn23,btn24,btn25,btn26,btn27)
        markup.add(btn28,btn29,btn30,btn31,btn32,btn33,btn34,btn35,btn36)
        markup.add(btn37,btn38,btn39,btn40,btn41,btn42,btn43,btn44,btn45)
        markup.add(btn46,btn47,btn48,btn49,btn50,btn51,btn52,btn53)

        markup.add(btn54)


        

        bot.send_message(call.message.chat.id,abhidharma_msg,reply_markup=markup)

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == '101':
        print("1️⃣අත්ථසාලිනි අත්ථයෝජනා- ඤාණකිත්ති හිමි")
        bot.forward_message(call.message.chat.id,-1001582189590,5 )

    elif call.data == '102':
        print("2️⃣අභිධම්ම මාතිකා")
        bot.forward_message(call.message.chat.id,-1001582189590,6 )

    elif call.data == '103':
        print("3️⃣අභිධම්ම හා සුත්තන්ත මාතිකා සන්නය- විමලසාර හිමි")
        bot.forward_message(call.message.chat.id,-1001582189590,7 )

    elif call.data == '104':
        print("4️⃣අභිධම්මත්ථ විකාසිනී - අභිධම්මාවතාර ටීකා")
        bot.forward_message(call.message.chat.id,-1001582189590,8 )

    elif call.data == '105':
        print("5️⃣අභිධම්මත්ථ විභාවිනී - අභිධම්මත්ථ සංගහ ටීකා 1933")
        bot.forward_message(call.message.chat.id,-1001582189590,9 )

    elif call.data == '106':
        print("6️⃣අභිධම්මමාතිකා පාළි ව්‍යාඛ්‍යානය- සද්ධම්මපාල රත්නායක")
        bot.forward_message(call.message.chat.id,-1001582189590,11 )

    elif call.data == '107':
        print("7️⃣අභිධම්මාවතාරය සන්නය- ඇම් අනෝමදස්සී හිමි")
        bot.forward_message(call.message.chat.id,-1001582189590,12 )

    elif call.data == '108':
        print("8️⃣අභිධර්ම කෝෂය ")
        bot.forward_message(call.message.chat.id,-1001582189590,13 )

    elif call.data == '109':
        print("9️⃣අභිධර්ම චන්ද්‍රිකාව- මාතර ධර්මවංශ හිමි  ")
        bot.forward_message(call.message.chat.id,-1001582189590,14 )

    elif call.data == '110':
        print("🔟අභිධර්ම ප්‍රකාශය  ")
        bot.forward_message(call.message.chat.id,-1001582189590,15 )

    elif call.data == '111':
        print("1️⃣1️⃣අභිධර්ම ප්‍රකාශය 01- දොඩම්පහළ කවිධජ හිමි ")
        bot.forward_message(call.message.chat.id,-1001582189590,16 )

    elif call.data == '112':
        print("1️⃣2️⃣අභිධර්ම ප්‍රකාශය v2  ")
        bot.forward_message(call.message.chat.id,-1001582189590,17 )

    elif call.data == '113':
        print("1️⃣3️⃣අභිධර්ම ප්‍රවේශනය  ")
        bot.forward_message(call.message.chat.id,-1001582189590,18 )

    elif call.data == '114':
        print("1️⃣4️⃣අභිධර්ම ප්‍රවේශය   ")
        bot.forward_message(call.message.chat.id,-1001582189590,19 )

    elif call.data == '115':
        print("1️⃣5️⃣අභිධර්ම මධු බින්දුව  ")
        bot.forward_message(call.message.chat.id,-1001582189590,20 )

    elif call.data == '116':
        print("1️⃣6️⃣අභිධර්ම රූප සටහන්  ")
        bot.forward_message(call.message.chat.id,-1001582189590,21 )

     
    
    


    














    
    
    














bot.polling()
