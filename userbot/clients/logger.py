# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import MAN2, MAN3, MAN4, MAN5, MAN6, MAN7, MAN8, MAN9, MAN10, MAN11, MAN12, MAN13, MAN14, MAN15, MAN16, MAN17, MAN18, MAN19, MAN20, bot, branch, tgbot
from userbot.utils import checking

MSG_ON = """
🔥 **xMan-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def man_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            ManUBOT = await tgbot.get_me()
            BOT_USERNAME = ManUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            ManUBOT = await tgbot.get_me()
            BOT_USERNAME = ManUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN2:
            await checking(MAN2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN3:
            await checking(MAN3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN4:
            await checking(MAN4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN5:
            await checking(MAN5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN6:
            await checking(MAN6)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN6.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN7:
            await checking(MAN7)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN7.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN8:
            await checking(MAN8)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN8.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN9:
            await checking(MAN9)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN9.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN10:
            await checking(MAN10)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN10.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN11:
            await checking(MAN11)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN11.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN12:
            await checking(MAN12)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN12.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN13:
            await checking(MAN13)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN13.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN14:
            await checking(MAN14)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN14.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN15:
            await checking(MAN15)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN15.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN16:
            await checking(MAN16)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN16.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN17:
            await checking(MAN17)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN17.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN18:
            await checking(MAN18)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN18.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN19:
            await checking(MAN19)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN19.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MAN20:
            await checking(MAN20)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MAN20.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
