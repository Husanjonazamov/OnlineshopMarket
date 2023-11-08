from pprint import pprint

from telebot.types import Message

from ...bot import bot
from ...filters import Filter
from ...utils.user import User as BUser
from ...keyboards import send_location, vhome, button_phone, bhome
from ...utils import State


@bot.message_handler(func=Filter(text="Ro`yxatdan o`tish📝"))
def add_handler(msg: Message):
    user_id = msg.chat.id
    user = BUser.get_user(user_id)
    role = user.profile.role
    if auth_user is None:
            bot.send_message(user_id, "Bosh sahifa✅", reply_markup=markup)
            State.set_state(user_id, "home")
            user = User.objects.get(user_id=user_id)
            user.is_login = True
            user.profile = auth_user
            user.save()

    bot.send_message(user_id, "Ism kiriting", reply_markup=bhome)



@bot.message_handler(func=Filter(state="name"))
def handler(msg: Message):
    user_id = msg.chat.id
    State.set_data(user_id, "name", msg.text)
    State.set_state(user_id, "number")
    bot.send_message(user_id, "Telefon nomerni kiriting\npastdagi Telefon raqamni yuborish tugmasini bosing",
                     reply_markup=button_phone, parse_mode="markdown")


