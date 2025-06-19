from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from keyboards.menu import main_menu
from utils.wallet import get_or_create_wallet
from database.db import init_db, get_user, save_user, get_ref_count

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    ref = message.get_args()
    wallet = get_or_create_wallet(user_id)
    save_user(user_id, wallet, ref)
    welcome = f"📡 WELCOME TO TPBOT v2.0\n\n"               f"人人都是科学家 | 一级交易自动化\n"               f"✅ 成熟策略\n🚗 零基础驱动高频交易\n🤖 智能执行 | 无经验掌控市场节奏\n\n"               f"钱包地址: `{wallet}`"
    await message.answer(welcome, parse_mode='Markdown', reply_markup=main_menu())

@dp.message_handler(lambda m: m.text == "💰 钱包")
async def show_wallet(message: types.Message):
    user_id = message.from_user.id
    user = get_user(user_id)
    await message.answer(f"🎒 您的钱包地址：\n`{user[1]}`", parse_mode='Markdown')

@dp.message_handler(lambda m: m.text == "📈 策略")
async def show_strategy(message: types.Message):
    await message.answer("📊 当前提供以下策略：\n1️⃣ 高频突破\n2️⃣ 智能震荡\n3️⃣ 趋势回撤")

@dp.message_handler(lambda m: m.text == "📦 仓位")
async def show_position(message: types.Message):
    await message.answer("🧾 当前仓位：\n策略：高频突破\n投入：1000 USDT\n收益：+13.4%")

@dp.message_handler(lambda m: m.text == "👨‍💻 客服")
async def support(message: types.Message):
    await message.answer("📞 请联系管理员：@admin")

@dp.message_handler(lambda m: m.text == "🎁 邀请返佣")
async def invite(message: types.Message):
    uid = message.from_user.id
    ref_link = f"https://t.me/{(await bot.get_me()).username}?start={uid}"
    count = get_ref_count(uid)
    await message.answer(f"🎁 你的邀请链接：\n{ref_link}\n已邀请：{count} 人")

@dp.message_handler(lambda m: m.text == "❌ 关闭菜单")
async def close(message: types.Message):
    await message.delete()

if __name__ == '__main__':
    init_db()
    executor.start_polling(dp, skip_updates=True)