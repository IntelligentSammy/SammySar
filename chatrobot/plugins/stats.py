
#    Copyright (C) DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from chatrobot.plugins.sql.checkuser_sql import get_all_users

@chatbot_cmd("stats", is_args=False)
@god_only
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(f"<b>I have <u>{len(starkisnoob)}</u> Users In Database.</b>", parse_mode="HTML")

@chatbot_cmd("alive", is_args=False)
@god_only
async def stark(event):
    await event.reply("<b><u>Yeah,🔸 **MADE IN 🇮🇳, MADE WITH 😻**\n\n"

pm_caption += "🔹 **Black PearL** : [Repo](https://github.com/IntelligentSammy/Blackpearl)\n"

pm_caption += "🔸 **Telethon Version:** `1.15.0` \n"

pm_caption += "🔹 **Python:** `3.7.4` \n"

pm_caption += f"🔸 **PearL Uptime** : `{uptime}` \n"

pm_caption += f"🔹 **Fork By:**  {DEFAULTUSER} \n"

pm_caption += f"🔸 **Plugin Version** : `1.0`\n"

pm_caption += "🔹 **SupportGroup** : [Join](https://t.me/BlackPearlChat)\n"

pm_caption += "🔸 ༺ ──•◈•───•◈•──༻\n\n"

pm_caption += "🔹 **[Deploy✔️](https://heroku.com/deploy?template=https://github.com/IntelligentSammy/BlackPearl)** \n"</b></u>", parse_mode="HTML")

@chatbot_cmd("repo", is_args=False)
async def stark(event):
    await event.reply("<b><u>My Repo is Here :</b></u> <code>https://github.com/MrSammyXD</code>", parse_mode="HTML")
