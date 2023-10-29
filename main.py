import telebot
import os
from dotenv import load_dotenv, find_dotenv
from buttons import back_but, detail_of_work_but, popular_questions, send_welcome_but, about_me_but
from phrase import sendWelcomePhrase1, aboutMePhrase1, myExperience, myEducation, instLink, applyVisitPhrase1, applyVisitPhrase2,backPhrase, thanksPhrase, clientName, clientPhone, usrname, separator, popularQuestionsPhrase, answer0, answer1, answer2, answer3, detailWorkPhrase, cosmeticUsePhrase, aboutTimePhrase, myInstrumentPhrase





load_dotenv(find_dotenv('.conf'), verbose=True)
TOKEN:str = os.getenv('TOKEN') #type: ignore
MY_ID:str = os.getenv('MY_ID') #type: ignore 

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    buttons, banchButtons = send_welcome_but()
    bot.send_message(message.chat.id, sendWelcomePhrase1, reply_markup=buttons)


@bot.message_handler(content_types='text') #type: ignore
def menu_worker(message):
    buttons, banchButtons = send_welcome_but()
    backbutton, backbanchButtons  = back_but() 
    popularbuttons, popularBanchButtons = popular_questions()
    
    if message.text == banchButtons[0].text:
       buttons, banchButtons = about_me_but()
       bot.send_message(message.chat.id, aboutMePhrase1, reply_markup=buttons)
    elif message.text == banchButtons[3].text:
        detailbuttons, detailbanchButtons = detail_of_work_but()
        bot.send_message(message.chat.id, detailWorkPhrase, reply_markup=detailbuttons)
    elif message.text == banchButtons[1].text:
       question = bot.send_message(message.chat.id, applyVisitPhrase1, reply_markup=backbutton)
       bot.register_next_step_handler(question, name_registration)
    elif message.text == banchButtons[2].text:
        bot.send_message(message.chat.id, popularQuestionsPhrase, reply_markup=popularbuttons)
    elif message.text == popularBanchButtons[0].text:
        bot.send_message(message.chat.id, answer0)
    elif message.text == popularBanchButtons[1].text:
        bot.send_message(message.chat.id, answer1)
    elif message.text == popularBanchButtons[2].text:
        bot.send_message(message.chat.id, answer2)
    elif message.text == popularBanchButtons[3].text:
        bot.send_message(message.chat.id, answer3)
 
    

    else:
         bot.send_message(message.chat.id, backPhrase, reply_markup=buttons)


def name_registration(message):
    button, banchButton  = back_but()
    buttons, banchButtons = send_welcome_but()
    if message.text == banchButton[0].text:
        bot.clear_step_handler(message)
        bot.send_message(message.chat.id,backPhrase ,reply_markup=buttons)
    else:
       question = bot.send_message(message.chat.id, applyVisitPhrase2, reply_markup=button)
       bot.register_next_step_handler(question, phone_registration)
       bot.send_message(MY_ID, separator)
       bot.send_message(MY_ID, usrname + f'{message.from_user.username}')
       bot.send_message(MY_ID, clientName + f'{message.text}')




def phone_registration(message):
    button, banchButton  = back_but()
    buttons, banchButtons = send_welcome_but()
    if message.text == banchButton[0].text:
        bot.clear_step_handler(message)
        bot.send_message(message.chat.id,backPhrase ,reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, thanksPhrase, reply_markup=buttons)
        bot.send_message(MY_ID, clientPhone + f'{message.text}')



@bot.callback_query_handler(func=lambda call:True)
def about_me_menu(call):
    buttons, banchButtons = about_me_but()
    detailButtons, detailBunchButtons = detail_of_work_but()
    if call.data == banchButtons[0].callback_data:
        bot.send_photo(call.message.chat.id,open('./images/me.jpg','rb'))
        bot.send_message(call.message.chat.id, myExperience, reply_markup=buttons)
    elif call.data == banchButtons[1].callback_data: 
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=myEducation, reply_markup=buttons)
    elif call.data == banchButtons[2].callback_data:
        bot.send_message(call.message.chat.id, instLink, reply_markup=buttons)
    elif call.data ==  detailBunchButtons[0].callback_data:
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=cosmeticUsePhrase, reply_markup=detailButtons)
    elif call.data == detailBunchButtons[1].callback_data:
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=aboutTimePhrase, reply_markup=detailButtons)
    elif call.data == detailBunchButtons[2].callback_data:
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=myInstrumentPhrase, reply_markup=detailButtons)
    elif call.data == banchButtons[3].callback_data:
        bot.send_media_group(call.message.chat.id,
                             [telebot.types.InputMediaPhoto(open('./images/photo1.jpg', 'rb')), 
                              telebot.types.InputMediaPhoto(open('./images/photo2.jpg', 'rb')), 
                              telebot.types.InputMediaPhoto(open('./images/photo3.jpg', 'rb')),
                              telebot.types.InputMediaPhoto(open('./images/photo4.jpg', 'rb')),
                              telebot.types.InputMediaPhoto(open('./images/photo5.jpg', 'rb')), 
                             ])













bot.infinity_polling()



