# Hugo - UserBot
# Copyright (C) TeamHugoX
#
# This file is a part of < https://github.com/TeamHugoX/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHugoX/Hugo/blob/main/LICENSE/>.
"""
**༄** Commands Available -

• `{i}whichsong`
   Reply to a song file, to recognise the song.
"""

from os import remove

from shazamio import Shazam

from . import eor, get_string, mediainfo, hugo_cmd

shazam = Shazam()


@hugo_cmd(pattern="whichsong$")
async def song_recog(event):
    reply = await event.get_reply_message()
    if not (reply and mediainfo(reply.media) == "audio"):
        return await eor(event, get_string("whs_1"), time=5)
    xx = await eor(event, get_string("com_5"))
    path_to_song = "./temp/shaazam_cache/unknown.mp3"
    await reply.download_media(path_to_song)
    await xx.edit(get_string("whs_2"))
    try:
        res = await shazam.recognize_song(path_to_song)
    except Exception as e:
        return await eor(xx, str(e), time=10)
    remove(path_to_song)
    try:
        x = res["track"]
        await xx.edit(get_string("whs_4").format(x["title"]))
    except KeyError:
        return await eor(xx, get_string("whs_3"), time=5)