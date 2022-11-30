FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/muhammadhanif71/xMan-Userbot /home/man-userbot/ \
    && chmod 777 /home/xman-userbot \
    && mkdir /home/xman-userbot/bin/

WORKDIR /home/xman-userbot/

CMD [ "bash", "start" ]
