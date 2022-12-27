# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, MAN2, MAN3, MAN4, MAN5,MAN6, MAN7, MAN8, MAN9, MAN10, MAN11, MAN12, MAN13, MAN14, MAN15, MAN16, MAN17, MAN18, MAN19, MAN20):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if MAN2 is not None:
            id2 = await MAN2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if MAN3 is not None:
            id3 = await MAN3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if MAN4 is not None:
            id4 = await MAN4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if MAN5 is not None:
           id5 = await MAN5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    try:
        if MAN6 is not None:
            id6 = await MAN6get_me()
            user_ids.append(id6.id)
    except BaseException:
        pass

    try:
        if MAN7 is not None:
            id7 = await MAN7.get_me()
            user_ids.append(id7.id)
    except BaseException:
        pass

    try:
        if MAN8 is not None:
            id8 = await MAN8.get_me()
            user_ids.append(id8.id)
    except BaseException:
        pass

    try:
        if MAN9 is not None:
            id9 = await MAN9.get_me()
            user_ids.append(id9.id)
    except BaseException:
        pass

    try:
        if MAN10 is not None:
            id10 = await MAN10.get_me()
            user_ids.append(id10.id)
    except BaseException:
        pass

    try:
        if MAN11 is not None:
            id11 = await MAN11.get_me()
            user_ids.append(id11.id)
    except BaseException:
        pass

    try:
        if MAN12 is not None:
            id12 = await MAN12.get_me()
            user_ids.append(id12.id)
    except BaseException:
        pass

    try:
        if MAN13 is not None:
            id13 = await MAN13.get_me()
            user_ids.append(id13.id)
    except BaseException:
        pass

    try:
        if MAN14 is not None:
            id14 = await MA14.get_me()
            user_ids.append(id14.id)
    except BaseException:
        pass

    try:
        if MAN15 is not None:
            id15 = await MAN15.get_me()
            user_ids.append(id15.id)
    except BaseException:
        pass

    try:
        if MAN16 is not None:
            id16 = await MAN16.get_me()
            user_ids.append(id16.id)
    except BaseException:
        pass

    try:
        if MAN17 is not None:
            id17 = await MAN17.get_me()
            user_ids.append(id17.id)
    except BaseException:
        pass

    try:
        if MAN18 is not None:
            id18 = await MAN18.get_me()
            user_ids.append(id18.id)
    except BaseException:
        pass

    try:
        if MAN19 is not None:
            id19 = await MAN19.get_me()
            user_ids.append(id19.id)
    except BaseException:
        pass

    try:
        if MAN20 is not None:
            id20 = await MAN20.get_me()
            user_ids.append(id20.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTAyNzE3NDAzMQ==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        MAN_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        MAN_USER = client.first_name
    man_mention = f"[{MAN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, MAN_USER, man_mention
