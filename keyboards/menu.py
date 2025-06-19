from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📈 策略"), KeyboardButton("📦 仓位"))
    kb.add(KeyboardButton("💰 钱包"), KeyboardButton("👨‍💻 客服"))
    kb.add(KeyboardButton("🎁 邀请返佣"), KeyboardButton("❌ 关闭菜单"))
    return kb