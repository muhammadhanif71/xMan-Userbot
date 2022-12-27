# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz

import sys

from telethon.utils import get_peer_id

from userbot import BOT_TOKEN
from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    man2,
    man3,
    man4,
    man5,
    man6,
    man7,
    man8,
    man9,
    man10,
    man11,
    man12,
    man13,
    man14,
    man15,
    man16,
    man17,
    man18,
    man19,
    man20,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    STRING_11,
    STRING_12,
    STRING_13,
    STRING_14,
    STRING_15,
    STRING_16,
    STRING_17,
    STRING_18,
    STRING_19,
    STRING_20,  
    STRING_SESSION,
    blacklistman,
    bot,
    call_py,
    tgbot,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nxMan-Ubot v{}, Copyright © 2021-2022 PayXr <https://github.com/grey423>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCilik-Ubot v{}, Copyright © 2021-2022 PayXr <https://github.com/grey423>"


async def man_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multiman():
    if 1027174031 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001601365018 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1027174031 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(man_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            man2.start()
            LOOP.run_until_complete(man_client(man2))
            user = man2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            man3.start()
            LOOP.run_until_complete(man_client(man3))
            user = man3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            man4.start()
            LOOP.run_until_complete(man_client(man4))
            user = man4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            man5.start()
            LOOP.run_until_complete(man_client(man5))
            user = man5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_6:
        try:
            man6.start()
            LOOP.run_until_complete(man_client(man6))
            user = man6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            man7.start()
            LOOP.run_until_complete(man_client(man7))
            user = man7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            man8.start()
            LOOP.run_until_complete(man_client(man8))
            user = man8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            man9.start()
            LOOP.run_until_complete(man_client(man9))
            user = man9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_10:
        try:
            man10.start()
            LOOP.run_until_complete(man_client(man10))
            user = man10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_11:
        try:
            man11.start()
            LOOP.run_until_complete(man_client(man11))
            user = man11.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_11 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_12:
        try:
            man12.start()
            LOOP.run_until_complete(man_client(man12))
            user = man12.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_12 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_13:
        try:
            man13.start()
            LOOP.run_until_complete(man_client(man13))
            user = man13.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_13 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_14:
        try:
            man14.start()
            LOOP.run_until_complete(man_client(man14))
            user = man14.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_14 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_15:
        try:
            man15.start()
            LOOP.run_until_complete(man_client(man15))
            user = man15.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_15 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_16:
        try:
            man16.start()
            LOOP.run_until_complete(man_client(man16))
            user = man16.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_16 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_17:
        try:
            man17.start()
            LOOP.run_until_complete(man_client(man17))
            user = man17.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_17 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_18:
        try:
            man18.start()
            LOOP.run_until_complete(man_client(man18))
            user = man18.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_18 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_19:
        try:
            man19.start()
            LOOP.run_until_complete(man_client(man19))
            user = man19.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_19 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_20:
        try:
            man20.start()
            LOOP.run_until_complete(man_client(man20))
            user = man20.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_20 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistman:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))            

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1 
    if not STRING_10:
        failed += 1
    if not STRING_11:
        failed += 1
    if not STRING_12:
        failed += 1
    if not STRING_13:
        failed += 1
    if not STRING_14:
        failed += 1
    if not STRING_15:
        failed += 1
    if not STRING_16:
        failed += 1
    if not STRING_17:
        failed += 1
    if not STRING_18:
        failed += 1
    if not STRING_19:
        failed += 1 
    if not STRING_20:
        failed += 1         
    return failed
