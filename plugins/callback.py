#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR

from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation

@Clinton.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)


@Clinton.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)

    elif update.data == "home":
        await update.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit(
            text=Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            # disable_web_page_preview=True
        )
    elif "close" in update.data:
        await update.message.delete(True)
              
