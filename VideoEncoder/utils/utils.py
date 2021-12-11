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

import asyncio
import mimetypes

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



output = InlineKeyboardMarkup([
    [InlineKeyboardButton("🤖 Update Channel", url="https://t.me/tellybots_4u"),
     InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")]
])


async def get_file_mimetype(filename):
    mimetype = mimetypes.guess_type(filename)[0]
    if not mimetype:
        proc = await asyncio.create_subprocess_exec('file', '--brief', '--mime-type', filename, stdout=asyncio.subprocess.PIPE)
        stdout, _ = await proc.communicate()
        mimetype = stdout.decode().strip()
    return mimetype or ''

video_duration_cache = {}
video_duration_lock = asyncio.Lock()


async def convert_to_jpg(original, end):
    proc = await asyncio.create_subprocess_exec('ffmpeg', '-y', '-i', original, end)
    await proc.communicate()
