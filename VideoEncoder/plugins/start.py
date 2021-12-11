# VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from database.add import add_user_to_database
from pyrogram import Client, filters
from translation import Translation
from .. import (audio, crf, doc_thumb, preset, resolution, sudo_users, tune,
                upload_doc)
from ..utils.utils import output

@Client.on_message(filters.command('settings'))
async def vset(app, message):
    await add_user_to_database(app, message)
    text = f'''<b>Encode Settings</b>
Tune: <code>{tune}</code> | <code>Preset: {preset}</code>
Audio: <code>{audio}</code> | <code>CRF: {crf}</code>
Resolution: <code>{resolution}</code>

<b>Upload Settings</b>
Upload Mode: <code>{'Document' if (upload_doc) else 'Video' }</code>
Doc thumb: <code>{'True' if (doc_thumb) else 'False'}</code>

'''
    await message.reply(text=text, reply_markup=Translation.BUTTONS)

@Client.on_message(filters.command('logs'))
async def logs(app, message):
    await add_user_to_database(app, message)
    file = 'VideoEncoder/utils/logs.txt'
    await message.reply_document(file, caption='#Logs')
