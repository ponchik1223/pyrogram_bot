from pyrogram.types import Message
from pyrogram import Client, filters
import database.config as config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from datetime import datetime
import database.database as database

app = Client(name="my_pg_bot", api_id=config.api_id, api_hash=config.api_hash)


def goodbye():
    return "Скоро вернусь с новым материалом!"

async def filter_text(_, __, message):
    return message.text == 'Хорошего дня'

filter_data = filters.create(filter_text)

@app.on_message(filters.private & filters.text & (~filters.outgoing & ~filters.chat(chats='me')) & filter_data)
async def message_text(client: Client, message: Message):
    await app.send_message(message.chat.id, goodbye())
    if flag_goodbye is True:
        print('os')
        scheduler.remove_job("goodbye")
        flag_goodbye = False

@app.on_message(filters.private & filters.text & (~filters.outgoing & ~filters.chat(chats='me')))
async def main_photo(client: Client, message: Message):
     await app.send_photo(message.chat.id,"./c0266aa63ff5aa3948dab0a43e920424.jpg")
     result_list = {
         "user_id": message.from_user.id,
         "name_user": message.from_user.first_name,
         "user_register": datetime.utcnow()

     }
     await database.new_user(result_list)


# отправляю через бота в наш с ним чат инфу
async def job_welcome_10():
    await app.send_message(chat_id=447247770, text="Hi!")
    scheduler.remove_job("welcome")

async def job_material_90():
    await app.send_message(chat_id=447247770, text="Hi2!")
    scheduler.remove_job("material")

async def job_closer_2_hour():
    await app.send_message(chat_id=447247770, text=goodbye())
    scheduler.remove_job("goodbye")

scheduler = AsyncIOScheduler()
scheduler.add_job(job_welcome_10, "interval", seconds=10*60, id="welcome")
scheduler.add_job(job_material_90, "interval", seconds=90*60, id="material")
scheduler.add_job(job_closer_2_hour,"interval", second=2*60*60, id="goodbye")

scheduler.start()

app.run()
