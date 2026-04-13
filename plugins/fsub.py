# (c) @Sanchit0102 & ᯏ 𝚮𝚼𝚸𝚬꧊᱂ ! श्रेष्ठ # Dont Remove Credit

# ===================== [ importing Requirements ] ===================== #

from pyrogram import enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import DS_AUTH_CHANNEL, DS_BOT_USERNAME

# ===================== [ Force Sub Def ] ===================== #


async def checkSub(bot, message):
    userid = message.from_user.id
    try:
        user =await bot.get_chat_member(DS_AUTH_CHANNEL, userid)
        if user.status == enums.ChatMemberStatus.BANNED:
            await message.reply_text("**<i>Sorry, You're Banned. Contact my [𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥!!]('https://t.me/exzmc') to get unbanned.**</i>", disable_web_page_preview=True)
            return False
        return True
    except UserNotParticipant:
        invite_link = await bot.export_chat_invite_link(DS_AUTH_CHANNEL)
        join_button = InlineKeyboardMarkup([
            [
            InlineKeyboardButton('⛔️ 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ⛔️', url=invite_link)
            ],[
            InlineKeyboardButton('♻️ 𝗥𝗘𝗙𝗥𝗘𝗦𝗛 ♻️', url=f'https://t.me/{DS_BOT_USERNAME}?start=True')
            ]
        ])
        await message.reply_text("**<i>Please Join My Updates Channel to use this Bot!**\n**Due to Overload, Only Channel Subscribers can use this Bot!</i>**", reply_markup=join_button)
        return False
    except Exception as e:
        print(e)
        await message.reply_text("Something went wrong. Contact my [𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥!!]('https://t.me/exzmc').")
        return False
    

# ===================== [🔺 End Of Force Sub 🔺] ===================== #
