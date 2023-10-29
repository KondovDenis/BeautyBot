from telebot import types
from typing import Tuple, List




def popular_questions() -> Tuple[types.ReplyKeyboardMarkup, List[types.KeyboardButton]]:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text= 'Какой тональный крем выбрать ?')
    button2 = types.KeyboardButton(text= 'Правильный уход за кожей до и после макияжа')
    button3 = types.KeyboardButton(text= 'Как правильно выбрать красную помаду ?')
    button4 = types.KeyboardButton(text= 'Почему макияж держится не долго ?')
    button5 = types.KeyboardButton(text='Назад ⬅️') 
    keyboard.add(button1, button2, button3, button4, button5)
    arr_butt = [button1, button2, button3, button4, button5]
    return keyboard, arr_butt



def detail_of_work_but() -> Tuple[types.InlineKeyboardMarkup, List[types.InlineKeyboardButton]]:
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='Как используется косметика', callback_data='detail1')
    item2 = types.InlineKeyboardButton(text='Cколько времени занимает сеанс', callback_data='detail2')
    item3 = types.InlineKeyboardButton(text='Какие инструменты я использую', callback_data='detail3')
    markup.add(item1, item2, item3)
    arr_butt = [item1, item2, item3]
    return markup, arr_butt

def send_welcome_but() -> Tuple[types.ReplyKeyboardMarkup, List[types.KeyboardButton]]: 
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Популярные вопросы клиентов')
    button2 = types.KeyboardButton(text='Обо мне 👩‍⚕️')
    button3 = types.KeyboardButton(text = 'Детали моей работы')
    button4 = types.KeyboardButton(text='Записаться на услуги')
    keyboard.add(button2, button3, button4, button1)
    arr_butt = [button2, button4, button1, button3]
    return keyboard, arr_butt 

def back_but() -> Tuple[types.ReplyKeyboardMarkup, List[types.KeyboardButton]]:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text='Назад ⬅️')
    keyboard.add(button)
    arr_butt = [button]
    return keyboard, arr_butt

def about_me_but() -> Tuple[types.InlineKeyboardMarkup, List[types.InlineKeyboardButton]]:
    markup=types.InlineKeyboardMarkup(row_width=1)
    item1=types.InlineKeyboardButton(text='Опыт работы', callback_data='menu1')
    item2=types.InlineKeyboardButton(text='Образование', callback_data='menu2')
    item3=types.InlineKeyboardButton(text='Instagram', callback_data='menu3', url='https://www.instagram.com/fallensky99')
    item4=types.InlineKeyboardButton(text='Фото работ', callback_data='menu4')
    arr_markup = [item1, item2, item3, item4]
    markup.add(item1,item2,item3,item4)
    return markup, arr_markup
