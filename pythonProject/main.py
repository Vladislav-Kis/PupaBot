import asyncio, utils, ffmpeg
import os.path, json
import speech_recognition
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
bot = Bot(token='7825909832:AAGfEhdd59enr0mH2xrYDssKYNf-MCwF_Dw')

def convert_keys_to_str(d):
    return {str(k): v for k, v in d.items()}
def convert_keys_to_int(d):
    return {int(k): v for k, v in d.items()}

async def async_on_exit():
    copy_dict = utils.dict_of_users
    copy_list_for_callback = utils.list_for_callback

    copy_info_file = 'Resources/CopyData.txt'
    if not os.path.exists(copy_info_file):
        with open(copy_info_file, 'w') as file:
            json.dump({'copy_dict': convert_keys_to_str(copy_dict),
                            'copy_list_for_callback': copy_list_for_callback}, file)
    # for i in range(len(chat.id_admin_chats)):
    #     try:
    #         await bot.delete_message(chat_id=chat.id_admin_chats[i],
    #                        message_id=chat.id_message_in_chat[chat.id_admin_chats[i]][0])
    #     except Exception as e:
    #         print('Не удалилось', e)
    print('Бот выключен')

async def main():
    global bot
    copy_info_file = 'Resources/CopyData.txt'
    if os.path.exists(copy_info_file):
        with open(copy_info_file, 'r') as file:
            data = json.load(file)
            utils.dict_of_users = convert_keys_to_int(data['copy_dict'])
            utils.list_for_callback = data['copy_list_for_callback']
        os.remove(copy_info_file)
    for i in range(len(utils.list_for_callback)):
            utils.list_id_users.append(int(utils.list_for_callback[i].split(':')[0]))
    dp = Dispatcher()
    dp.message.register(utils.start, Command(commands='start'))
    dp.message.register(utils.get_users, Command(commands='getusers'))
    dp.message.register(utils.get_chat_id, Command(commands='getid'))
    dp.callback_query.register(utils.write_to_user, lambda c: c.data in utils.list_for_callback)
    dp.callback_query.register(utils.back_to_list_user, F.data.in_(['back_to_list_user']))
    dp.message.register(utils.voice_handler, F.voice)
    #dp.message.register(utils.write_to_user_text, F.text)
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print('Бот остановлен пользователем')
    finally:
        await async_on_exit()
        await bot.session.close()

if __name__ == '__main__':
    print("starting")
    asyncio.run(main())
