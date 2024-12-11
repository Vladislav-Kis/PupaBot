from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import utils


def list_of_users(list_user):
    markup = InlineKeyboardBuilder()
    for i in range(len(list_user)):
        markup.button(text=f'{utils.dict_of_users[list_user[i]]['FirstName']} '
                           f'{utils.dict_of_users[list_user[i]]['LastName']}',
                      callback_data=f'{list_user[i]}:id_for_list')
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)
def back_to_list_user_but():
    markup = InlineKeyboardBuilder()
    markup.button(text=f'Назад', callback_data=f'back_to_list_user')
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)
