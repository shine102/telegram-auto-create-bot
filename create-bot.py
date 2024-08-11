from telethon import TelegramClient, sync
import re
import asyncio

# Thay bằng giá trị của bạn
api_id = 'xxxxxxxxx'
api_hash = 'xxxxxxxxxxxxxxxxx'
phone_number = 'xxxxxxxxxxxxxxxxxx'

# Tạo một Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Bắt đầu client
client.start(phone=phone_number)

# Hàm để tạo bot mới
async def create_bot():
    async with client:
        # Bắt đầu cuộc hội thoại với BotFather
        botfather = await client.get_entity("BotFather")
        await client.send_message(botfather, "/newbot")

        # Đợi BotFather trả lời
        await asyncio.sleep(2)  # Thời gian chờ

        response = await client.get_messages(botfather, limit=1)
        print(response[0].message)

        # Gửi tên cho bot mới
        await client.send_message(botfather, "MyNewBot")

        # Đợi BotFather trả lời
        await asyncio.sleep(2)  # Thời gian chờ
        response = await client.get_messages(botfather, limit=1)
        print(response[0].message)

        # Gửi username cho bot mới (phải kết thúc bằng 'bot')
        await client.send_message(botfather, "lam_test_new_1_bot")

        # Đợi BotFather trả lời
        await asyncio.sleep(2)  # Thời gian chờ
        response = await client.get_messages(botfather, limit=1)
        print(response[0].message)

        # Tìm kiếm token bot trong phản hồi
        token_match = re.search(r"token:\s+([0-9a-zA-Z:_-]+)", response[0].message)
        if token_match:
            bot_token = token_match.group(1)
            print(f"Mã token của bot mới của bạn: {bot_token}")
        else:
            print("Không tìm thấy mã token của bot!")

# Chạy hàm tạo bot
client.loop.run_until_complete(create_bot())
