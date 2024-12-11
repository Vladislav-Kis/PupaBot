import io
import os
import ffmpeg
from aiogram.types import Message, CallbackQuery
import main
import speech_recognition as sr
from google.cloud import speech
from pydub import AudioSegment
#AudioSegment.converter = r'C:\Users\v.kiselev\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe'
from Keyboards import Inline
#{1068762338: {'FirstName': 'Alexsandr', 'LastName': 'Konstantinov'}, 960251316: {'FirstName': 'Purp1e_13', 'LastName': None}}
dict_of_users = {}
list_id_users = []
list_for_callback = []

async def start(message: Message):
    pass
async def get_users(message: Message):
    await main.bot.send_chat_action(message.chat.id, action="typing")
    await message.answer(text='Список пользователей', reply_markup=Inline.list_of_users(list_id_users))
async def write_to_user_text(message: Message):
    if dict_of_users[message.chat.id]['Status'] and message.chat.id != -1002449681126:
        await main.bot.send_message(text=f'{message.text}', chat_id=f'{dict_of_users[message.chat.id]['Status']}')
        await main.bot.delete_message(message.chat.id, message.message_id)
    else:
        await message.answer(text='Я пока не работаю с текстом')

async def get_chat_id(message: Message):
    await message.answer(f'Chat id: {message.chat.id}', parse_mode='html')
async def write_to_user(callback: CallbackQuery):
    await main.bot.send_chat_action(callback.message.chat.id, action="typing")
    id = int(callback.data.split(':')[0])
    dict_of_users[callback.message.chat.id]['Status'] = id
    await callback.message.edit_text(text=f'Написать {dict_of_users[id]['FirstName']} {dict_of_users[id]['LastName']}',
                                     reply_markup=Inline.back_to_list_user_but())
async def back_to_list_user(callback: CallbackQuery):
    await main.bot.send_chat_action(callback.message.chat.id, action="typing")
    dict_of_users[callback.message.chat.id]['Status'] = None
    await callback.message.edit_text(text='Список пользователей', reply_markup=Inline.list_of_users(list_id_users))

async def voice_handler(message: Message):
    global dict_of_users
    await main.bot.send_chat_action(message.chat.id, action="typing")
    id = message.from_user.id
    if id not in dict_of_users.keys():
        dict_of_users = {id: {'FirstName': message.from_user.first_name,
                              'LastName': message.from_user.last_name,
                              'Status': None},
                         **dict_of_users}
    if id not in list_id_users:
        list_id_users.append(id)
        list_for_callback.append(f'{id}:id_for_list')
    print(dict_of_users)
    if message.content_type == 'voice':
        file_id = message.voice.file_id
        file = await main.bot.get_file(file_id)
        file_path = file.file_path
        await main.bot.download_file(file_path, "Resources/audio.mp3")
        mp3_file_path = "Resources/audio.mp3"

        def convert_audio(input_file, output_file, bitrate='192k'):
            try:
                ffmpeg.input(input_file).output(output_file, audio_bitrate=bitrate).run(quiet=True)
            except ffmpeg.Error as e:
                print(f"Ошибка при работе с FFmpeg: {e.stderr.decode()}")
        output_path = 'Resources/audio1.mp3'
        convert_audio(mp3_file_path, output_path)
        def convert_mp3_to_text(mp3_path):
            try:
                if not os.path.exists(mp3_path):
                    raise FileNotFoundError(f"Файл {mp3_path} не найден.")
                wav_path = mp3_path.replace(".mp3", ".wav")
                audio = AudioSegment.from_mp3(mp3_path)
                audio.export(wav_path, format="wav")
                recognizer = sr.Recognizer()
                with sr.AudioFile(wav_path) as source:
                    audio_data = recognizer.record(source)
                recognized_text = recognizer.recognize_google(audio_data, language="ru-RU")
                os.remove(wav_path)
                return recognized_text if recognized_text else "Текст не распознар."
            except sr.UnknownValueError:
                return "Текст не распознан. Возможно, аудиофайл пустой или содержит шум."
            except Exception as e:
                return f"Ошибка: {str(e)}"

        recognized_text = convert_mp3_to_text(output_path)
        if recognized_text == "Текст не распознан.":
            await message.answer("Сообщение: Текст из аудио не удалось распознать.")
        else:
            print(len(recognized_text), recognized_text)
            if len(recognized_text) > 4000:
                out = [(recognized_text[i:i+1000]) for i in range(0, len(recognized_text), 1000)]
                for i in range(len(out)):
                    await message.answer(out[i])
            else:
                await message.answer(recognized_text)

        os.remove(output_path)
