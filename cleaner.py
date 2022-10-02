# Author:	Zile42O
# Version:	1.0
# Lib:		Telethon
# Lang:		Python3

from telethon import TelegramClient
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.tl.types import UserStatusLastMonth
from telethon.tl.types import UserStatusRecently
from telethon.tl.types import UserStatusLastWeek
import asyncio
import datetime
import sys

api_id = 1337 # Your API_ID
api_hash = "" # Your APP_ID

async def clear_chat(client):
	group = sys.argv[1]
	deleted_accounts = 0
	async for user in client.iter_participants(group):
		if not user.bot and not user.status == UserStatusRecently() and not user.status == UserStatusLastMonth() and not user.status == UserStatusLastWeek():
			try:
				deleted_accounts += 1
				#comment this line bellow if you don't need debug
				print(f"Debug: {str(user.first_name)} Last seen: {str(user.status)}")
				await client(EditBannedRequest(group, user, ChatBannedRights(
				   until_date=datetime.timedelta(minutes=1),
				   view_messages=True
				   )))
			except Exception as exc:
				print(f"Failed to kick one inactive account because: {str(exc)}")
	if deleted_accounts:
		print(f"Kicked {deleted_accounts} Inactive Accounts")
	else:
		print(f"No inactive accounts found in {group}")

with TelegramClient("check_inactive_accs", api_id, api_hash) as client:
	asyncio.get_event_loop().run_until_complete(clear_chat(client))