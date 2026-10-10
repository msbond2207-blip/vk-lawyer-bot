import os
import json
import time
from datetime import datetime

from vkbottle.bot import Bot, Message
from vkbottle import Keyboard
from vkbottle import KeyboardButtonColor, Text

TOKEN = "vk1.a.ecbtcW2hykGmDFJUGeXZkZ7OTO6M9PCUgV-_dsfhp0ni-1Ao5Bx_stngT_jTw7MFaJnfohMqNhTgOTVjQGOjIeJqryWXipmHvsLLQjIDyPUgVMG4w5NbczMQJPUADosV2fGNaLyYWrQxv306SdzQNK5rK1DI9sHdN0Ojb4ZECtdnh9irdW1H6SaLBPmrntcOpjUtnG5EhSJQa_B-xuD8uA"
ADMIN_ID = 758865307

CASES_FILE = "cases.json"
STATS_FILE = "stats.json"
REVIEWS_FILE = "reviews.json"
CALLS_FILE = "calls.json"
PRICE_FILE = "price.json"
PROFILE_FILE = "profile.json"
PORTFOLIO_FILE = "portfolio.json"

bot = Bot(token=TOKEN)


def load(file, default):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


admin_mode = {}
user_state = {}


# ============================================================
# 🛡 ЗАЩИТА ОТ СПАМА
# ============================================================
spam_tracker = {}
SPAM_LIMIT = 8
SPAM_WINDOW = 60


def check_spam(uid):
    now = time.time()
    if uid not in spam_tracker:
        spam_tracker[uid] = []
    spam_tracker[uid] = [t for t in spam_tracker[uid] if now - t < SPAM_WINDOW]
    if uid == ADMIN_ID:
        return True
    if len(spam_tracker[uid]) >= SPAM_LIMIT:
        return False
    spam_tracker[uid].append(now)
    return True


DEFAULT_PRICE = (
    "💰 ПРАЙС-ЛИСТ НА УСЛУГИ\n"
    "👨‍⚖️ Адвокат Kai Schwartz\n"
    "━━━━━━━━━━━━━━━━━\n\n"
    "📞 КОНСУЛЬТАЦИЯ\n"
    "• Консультация — БЕСПЛАТНО\n"
    "• Защита на допросе — БЕСПЛАТНО\n\n"
    "🆘 ЭКСТРЕННЫЙ ВЫЗОВ\n"
    "• Выезд при КПЗ — 5.000.000 $\n"
    "• Выезд при ТСР — 7.000.000 $\n\n"
    "📄 ДОКУМЕНТЫ\n"
    "• Иск на физ. лицо — 3.000.000 $\n"
    "• Иск на юр. лицо — 4.000.000 $\n"
    "• Иск на гос. служащего — 5.000.000 $\n"
    "• Ходатайство по делу — 2.000.000 $\n\n"
    "⚖️ ВЕДЕНИЕ ДЕЛА\n"
    "• Активное участие — 10.000.000 $\n\n"
    "━━━━━━━━━━━━━━━━━\n"
    "🕐 Работаю КРУГЛОСУТОЧНО\n"
    "📞 Связь:\n"
    "• VK: @samp2207\n"
    "• TG: @kendyfan\n"
    "• Тел. в игре: 1113998"
)

DEFAULT_PROFILE = (
    "👨‍⚖️ ОБО МНЕ\n"
    "━━━━━━━━━━━━━━━━━\n"
    "Меня зовут Kai Schwartz\n"
    "🏛 Адвокат Arizona Mobile 1\n\n"
    "💼 Специализация:\n"
    "• Уголовные дела\n"
    "• Защита при задержании\n"
    "• Гражданские иски\n"
    "• Обжалование решений гос. структур\n\n"
    "🕐 График работы: КРУГЛОСУТОЧНО\n\n"
    "📞 Связь:\n"
    "• VK: @samp2207\n"
    "• TG: @kendyfan\n"
    "• 📱 Тел. в игре: 1113998"
)


def main_keyboard(uid=None):
    kb = Keyboard(one_time=False)
    kb.add(Text("📝 Заполнить анкету"), color=KeyboardButtonColor.PRIMARY)
    kb.row()
    kb.add(Text("🆘 ЭКСТРЕННЫЙ ВЫЗОВ"), color=KeyboardButtonColor.NEGATIVE)
    kb.row()
    kb.add(Text("💰 Прайс-лист"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("📁 Обо мне"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("🏆 Примеры работ"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("📊 Статистика"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("⭐ Оставить отзыв"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("📖 Читать отзывы"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("📄 Обращение в прокуратуру"), color=KeyboardButtonColor.PRIMARY)
    if uid == ADMIN_ID:
        kb.row()
        kb.add(Text("🔙 Вернуться в админ-панель"), color=KeyboardButtonColor.POSITIVE)
    return kb.get_json()


def admin_keyboard():
    kb = Keyboard(one_time=False)
    kb.add(Text("📋 Список дел"), color=KeyboardButtonColor.PRIMARY)
    kb.add(Text("🆘 Журнал вызовов"), color=KeyboardButtonColor.PRIMARY)
    kb.row()
    kb.add(Text("⚙️ Взять дело"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("✅ Закрыть дело"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("➕ Добавить в портфолио"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("🗑 Удалить дело"), color=KeyboardButtonColor.NEGATIVE)
    kb.row()
    kb.add(Text("✏️ Изменить прайс"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("✏️ Изменить резюме"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("📊 Моя статистика"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("⭐ Все отзывы"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("📤 Экспорт дел"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("👤 Режим клиента"), color=KeyboardButtonColor.SECONDARY)
    return kb.get_json()


def cancel_keyboard():
    kb = Keyboard(one_time=True)
    kb.add(Text("❌ Отмена"), color=KeyboardButtonColor.NEGATIVE)
    return kb.get_json()


def evidence_keyboard():
    kb = Keyboard(one_time=True)
    kb.add(Text("📸 Скриншоты"))
    kb.add(Text("🎥 Видео"))
    kb.row()
    kb.add(Text("👥 Свидетели"))
    kb.add(Text("❌ Доказательств нет"))
    return kb.get_json()


def close_result_keyboard(case_id):
    kb = Keyboard(one_time=True)
    kb.add(Text("✅ Выиграно #" + str(case_id)), color=KeyboardButtonColor.POSITIVE)
    kb.add(Text("❌ Проиграно #" + str(case_id)), color=KeyboardButtonColor.NEGATIVE)
    return kb.get_json()


# ============================================================
# 🚀 /start
# ============================================================
@bot.on.message(text=["/start", "начать", "Начать"])
async def start_handler(message: Message):
    uid = message.from_id
    user_state.pop(uid, None)
    if uid == ADMIN_ID:
        admin_mode[uid] = "admin"
        await message.answer(
            "👨‍⚖️ Панель адвоката Kai Schwartz\n\nТы — админ.",
            keyboard=admin_keyboard()
        )
    else:
        await message.answer(
            "👋 Здравствуйте, я адвокат Kai Schwartz на Arizona Mobile 1.\n\nВыберите действие 👇",
            keyboard=main_keyboard(uid)
        )


@bot.on.message(text="👤 Режим клиента")
async def switch_to_client(message: Message):
    uid = message.from_id
    if uid != ADMIN_ID:
        return
    admin_mode[uid] = "client"
    await message.answer("👤 Режим клиента включён.", keyboard=main_keyboard(uid))


@bot.on.message(text="🔙 Вернуться в админ-панель")
async def switch_to_admin(message: Message):
    uid = message.from_id
    if uid != ADMIN_ID:
        return
    admin_mode[uid] = "admin"
    await message.answer("👨‍⚖️ Ты снова в админ-панели.", keyboard=admin_keyboard())


# ============================================================
# ✅❌ ИТОГ ДЕЛА — обработка нажатий
# ============================================================
@bot.on.message(text=lambda m: m.text is not None and m.text.startswith("✅ Выиграно #"))
async def won_case(message: Message):
    if message.from_id != ADMIN_ID:
        return
    parts = message.text.split("#")
    if len(parts) < 2:
        return
    case_id = parts[1].strip()
    stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
    stats["won"] = stats.get("won", 0) + 1
    save(STATS_FILE, stats)
    cases = load(CASES_FILE, {})
    if case_id in cases:
        cases[case_id]["status"] = "closed"
        save(CASES_FILE, cases)
    await message.answer("🏆 Дело #" + case_id + " записано как ВЫИГРАННОЕ!", keyboard=admin_keyboard())


@bot.on.message(text=lambda m: m.text is not None and m.text.startswith("❌ Проиграно #"))
async def lost_case(message: Message):
    if message.from_id != ADMIN_ID:
        return
    parts = message.text.split("#")
    if len(parts) < 2:
        return
    case_id = parts[1].strip()
    stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
    stats["lost"] = stats.get("lost", 0) + 1
    save(STATS_FILE, stats)
    cases = load(CASES_FILE, {})
    if case_id in cases:
        cases[case_id]["status"] = "closed"
        save(CASES_FILE, cases)
    await message.answer("❌ Дело #" + case_id + " записано как проигранное.", keyboard=admin_keyboard())


# ============================================================
# ❌ ОТМЕНА
# ============================================================
@bot.on.message(text="❌ Отмена")
async def cancel_handler(message: Message):
    uid = message.from_id
    user_state.pop(uid, None)
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer("❌ Отменено.", keyboard=kb)


# ============================================================
# 📝 АНКЕТА
# ============================================================
@bot.on.message(text="📝 Заполнить анкету")
async def form_start(message: Message):
    uid = message.from_id
    user_state[uid] = {"step": "nickname", "data": {}}
    await message.answer("1️⃣ Введите ваш игровой ник:", keyboard=cancel_keyboard())


@bot.on.message(text="🆘 ЭКСТРЕННЫЙ ВЫЗОВ")
async def emergency_start(message: Message):
    uid = message.from_id
    user_state[uid] = {"step": "em_nick", "data": {}}
    await message.answer("🆘 ЭКСТРЕННЫЙ ВЫЗОВ\n\n1️⃣ Ваш игровой ник:", keyboard=cancel_keyboard())


@bot.on.message(text="💰 Прайс-лист")
async def price_handler(message: Message):
    uid = message.from_id
    price = load(PRICE_FILE, {"text": DEFAULT_PRICE})["text"]
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer(price, keyboard=kb)


@bot.on.message(text="📁 Обо мне")
async def about_handler(message: Message):
    uid = message.from_id
    text = load(PROFILE_FILE, {"text": DEFAULT_PROFILE})["text"]
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer(text, keyboard=kb)


@bot.on.message(text="🏆 Примеры работ")
async def portfolio_handler(message: Message):
    uid = message.from_id
    portfolio = load(PORTFOLIO_FILE, [])
    if not portfolio:
        text = "🏆 Пока нет примеров работ."
    else:
        text = "🏆 ПРИМЕРЫ ВЫИГРАННЫХ ДЕЛ\n━━━━━━━━━━━━━━━━━\n\n"
        for i, c in enumerate(portfolio, 1):
            text += (
                "⚖️ Дело #" + str(i) + " — " + c["case_type"] + "\n"
                "👤 Клиент: " + c["client"] + "\n"
                "🏆 Результат: " + c["result"] + "\n"
                "💬 " + c["description"] + "\n"
                "💰 Гонорар: " + c["fee"] + " $\n"
                "━━━━━━━━━━━━━━━━━\n\n"
            )
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer(text, keyboard=kb)


@bot.on.message(text=["📊 Статистика", "📊 Моя статистика"])
async def stats_handler(message: Message):
    uid = message.from_id
    s = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
    won = s.get("won", 0)
    lost = s.get("lost", 0)
    if (won + lost) > 0:
        winrate = round(won / (won + lost) * 100)
    else:
        winrate = 0
    if s.get("ratings"):
        avg_rating = round(sum(s["ratings"]) / len(s["ratings"]), 1)
    else:
        avg_rating = "—"
    text = (
        "📊 СТАТИСТИКА АДВОКАТА\n"
        "👨‍⚖️ Kai Schwartz\n"
        "━━━━━━━━━━━━━━━━━\n\n"
        "📁 Всего дел: " + str(s.get("total", 0)) + "\n"
        "✅ Выиграно: " + str(won) + "\n"
        "❌ Проиграно: " + str(lost) + "\n"
        "🆘 Экстренных: " + str(s.get("emergency", 0)) + "\n\n"
        "🏆 Винрейт: " + str(winrate) + "%\n"
        "⭐ Рейтинг: " + str(avg_rating) + " / 5.0"
    )
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer(text, keyboard=kb)


@bot.on.message(text="⭐ Оставить отзыв")
async def review_start(message: Message):
    uid = message.from_id
    user_state[uid] = {"step": "rev_rate", "data": {}}
    kb = Keyboard(one_time=True)
    kb.add(Text("5"), color=KeyboardButtonColor.POSITIVE)
    kb.add(Text("4"), color=KeyboardButtonColor.POSITIVE)
    kb.add(Text("3"), color=KeyboardButtonColor.PRIMARY)
    kb.row()
    kb.add(Text("2"), color=KeyboardButtonColor.NEGATIVE)
    kb.add(Text("1"), color=KeyboardButtonColor.NEGATIVE)
    await message.answer("⭐ Оцените работу адвоката от 1 до 5:", keyboard=kb.get_json())


@bot.on.message(text="📖 Читать отзывы")
async def read_reviews(message: Message):
    uid = message.from_id
    reviews = load(REVIEWS_FILE, [])
    if not reviews:
        text = "📖 Пока нет отзывов."
    else:
        text = "📖 ОТЗЫВЫ ОБ АДВОКАТЕ\n━━━━━━━━━━━━━━━━━\n\n"
        for r in reviews[-10:]:
            stars = "⭐" * r["rating"]
            text += stars + " (" + str(r["rating"]) + "/5)\n"
            text += "📅 " + r["date"] + "\n"
            text += "💬 " + r["text"] + "\n"
            text += "━━━━━━━━━━━━━━━━━\n\n"
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer(text, keyboard=kb)


# ============================================================
# 📄 ОБРАЩЕНИЕ В ПРОКУРАТУРУ
# ============================================================
@bot.on.message(text="📄 Обращение в прокуратуру")
async def appeal_start(message: Message):
    uid = message.from_id
    user_state[uid] = {"step": "ap_name", "data": {}}
    await message.answer(
        "📄 ОБРАЩЕНИЕ В ПРОКУРАТУРУ\n"
        "━━━━━━━━━━━━━━━━━\n\n"
        "Заполним по шагам.\n\n"
        "1️⃣ Введите ваше имя и фамилию (Name Surname):",
        keyboard=cancel_keyboard()
    )


# ============================================================
# 👨‍⚖️ АДМИН-КОМАНДЫ
# ============================================================
@bot.on.message(text="📋 Список дел")
async def list_cases(message: Message):
    if message.from_id != ADMIN_ID:
        return
    cases = load(CASES_FILE, {})
    if not cases:
        await message.answer("📭 Заявок пока нет.", keyboard=admin_keyboard())
        return
    text = "📋 Список дел:\n\n"
    for cid, c in cases.items():
        if c["status"] == "new":
            emoji = "🆕"
        elif c["status"] == "in_work":
            emoji = "⚙️"
        elif c["status"] == "closed":
            emoji = "✅"
        else:
            emoji = "❔"
        text += emoji + " #" + cid + " — " + c["nickname"] + " — " + c["position"] + "\n"
    await message.answer(text, keyboard=admin_keyboard())


@bot.on.message(text="🆘 Журнал вызовов")
async def calls_log(message: Message):
    if message.from_id != ADMIN_ID:
        return
    calls = load(CALLS_FILE, {})
    if not calls:
        await message.answer("📭 Вызовов не было.", keyboard=admin_keyboard())
        return
    text = "🆘 Журнал вызовов:\n\n"
    for cid, c in calls.items():
        text += "#" + cid + " " + c["nickname"] + " — " + c["place"] + " (" + c["time"] + ")\n"
    await message.answer(text, keyboard=admin_keyboard())


@bot.on.message(text="⭐ Все отзывы")
async def all_reviews(message: Message):
    if message.from_id != ADMIN_ID:
        return
    reviews = load(REVIEWS_FILE, [])
    if not reviews:
        await message.answer("Отзывов пока нет.", keyboard=admin_keyboard())
        return
    text = "⭐ Все отзывы:\n\n"
    for r in reviews[-20:]:
        stars = "⭐" * r["rating"]
        text += stars + " (" + str(r["rating"]) + "/5) — " + r["date"] + "\n" + r["text"] + "\n\n"
    await message.answer(text, keyboard=admin_keyboard())


@bot.on.message(text="⚙️ Взять дело")
async def take_case_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "take_id", "data": {}}
    await message.answer("Введите номер дела:", keyboard=cancel_keyboard())


@bot.on.message(text="✅ Закрыть дело")
async def close_case_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "close_id", "data": {}}
    await message.answer("Введите номер дела для закрытия:", keyboard=cancel_keyboard())


@bot.on.message(text="➕ Добавить в портфолио")
async def add_portfolio_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "pf_type", "data": {}}
    await message.answer("Тип дела:", keyboard=cancel_keyboard())


@bot.on.message(text="🗑 Удалить дело")
async def delete_case_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "del_id", "data": {}}
    await message.answer("Введите номер дела для удаления:", keyboard=cancel_keyboard())


@bot.on.message(text="✏️ Изменить прайс")
async def edit_price_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "edit_price", "data": {}}
    await message.answer("Отправь новый текст прайс-листа:", keyboard=cancel_keyboard())


@bot.on.message(text="✏️ Изменить резюме")
async def edit_profile_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "edit_profile", "data": {}}
    await message.answer("Отправь новый текст резюме:", keyboard=cancel_keyboard())


@bot.on.message(text="📤 Экспорт дел")
async def export_cases(message: Message):
    if message.from_id != ADMIN_ID:
        return
    cases = load(CASES_FILE, {})
    if not cases:
        await message.answer("📭 Дел нет.", keyboard=admin_keyboard())
        return
    text = "📤 ЭКСПОРТ ВСЕХ ДЕЛ\n━━━━━━━━━━━━━━━━━\n\n"
    for cid, c in cases.items():
        text += (
            "#" + cid + " [" + c["status"] + "]\n"
            "👤 " + c["nickname"] + " — " + c["position"] + "\n"
            "📌 " + c["reason"] + "\n"
            "⚖️ " + c["demands"] + "\n"
            "🤝 " + c["help_needed"] + "\n"
            "📎 " + c["evidence"] + "\n"
            "📞 " + c["contact"] + "\n"
            "🔗 vk.com/id" + str(c["vk_id"]) + "\n"
            "🕒 " + c["date"] + "\n"
            "━━━━━━━━━━━━━━━━━\n"
        )
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    for chunk in chunks:
        await message.answer(chunk)
    await message.answer("✅ Экспорт завершён.", keyboard=admin_keyboard())


# ============================================================
# 🎯 УНИВЕРСАЛЬНЫЙ ОБРАБОТЧИК
# ============================================================
@bot.on.message()
async def universal_handler(message: Message):
    uid = message.from_id

    if not check_spam(uid):
        return

    if message.text:
        text = message.text.strip()
    else:
        text = ""

    if uid not in user_state:
        return

    state = user_state[uid]
    step = state["step"]
    data = state["data"]

    def get_kb():
        if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
            return admin_keyboard()
        return main_keyboard(uid)

    # ========== ОБРАЩЕНИЕ В ПРОКУРАТУРУ ==========
    if step == "ap_name":
        data["name"] = text
        state["step"] = "ap_vk"
        await message.answer("2️⃣ Вставьте ссылку на ваш VK:", keyboard=cancel_keyboard())
    elif step == "ap_vk":
        data["vk"] = text
        state["step"] = "ap_phone"
        await message.answer("3️⃣ Введите ваш игровой номер телефона:", keyboard=cancel_keyboard())
    elif step == "ap_phone":
        data["phone"] = text
        state["step"] = "ap_target"
        kb = Keyboard(one_time=True)
        kb.add(Text("👤 Гражданин"), color=KeyboardButtonColor.PRIMARY)
        kb.add(Text("👮 Сотрудник"), color=KeyboardButtonColor.PRIMARY)
        kb.row()
        kb.add(Text("❌ Отмена"), color=KeyboardButtonColor.NEGATIVE)
        await message.answer("4️⃣ На кого жалуетесь?", keyboard=kb.get_json())
    elif step == "ap_target":
        data["target_type"] = text
        state["step"] = "ap_target_name"
        if text == "👮 Сотрудник":
            await message.answer("5️⃣ Организация и ник (пример: LSPD, John_Doe):", keyboard=cancel_keyboard())
        else:
            await message.answer("5️⃣ Введите ник гражданина:", keyboard=cancel_keyboard())
    elif step == "ap_target_name":
        data["target_name"] = text
        state["step"] = "ap_situation"
        await message.answer("6️⃣ Опишите ситуацию:", keyboard=cancel_keyboard())
    elif step == "ap_situation":
        data["situation"] = text
        state["step"] = "ap_laws"
        await message.answer("7️⃣ Какие статьи нарушены?", keyboard=cancel_keyboard())
    elif step == "ap_laws":
        data["laws"] = text
        state["step"] = "ap_request"
        await message.answer("8️⃣ Что просите у прокуратуры?", keyboard=cancel_keyboard())
    elif step == "ap_request":
        data["request"] = text
        state["step"] = "ap_video"
        await message.answer("9️⃣ Ссылка на видео (или «нет»):", keyboard=cancel_keyboard())
    elif step == "ap_video":
        data["video"] = text
        state["step"] = "ap_passport"
        await message.answer("🔟 Доказательство личности (/showpass или /stats+/time):", keyboard=cancel_keyboard())
    elif step == "ap_passport":
        data["passport"] = text
        today = datetime.now().strftime("%d.%m.%Y")
        bbcode = (
            "[CENTER][IMG width=\"231px\" size=\"400x400\"]https://i.imgur.com/OR5H8NN.png[/IMG]\n"
            "[B][SIZE=5]PROSECUTOR'S OFFICE OF STATE OF ARIZONA[/SIZE][/B]\n"
            "[/CENTER]\n"
            "[HR][/HR]\n"
            "[RIGHT][FONT=book antiqua][COLOR=rgb(239, 239, 239)]Генеральной прокуратуре штата Arizona.[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]От гражданина " + data["name"] + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]С электронным адресом \"" + data["vk"] + "\"[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]С номером телефона \"" + data["phone"] + "\"[/COLOR][/FONT][/RIGHT]\n"
            "[CENTER]\n"
            "[B][SIZE=5]Обращение[/SIZE][/B]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]Я " + data["name"] + ", житель Штата Arizona подаю обращение в прокуратуру на " + data["target_type"] + " " + data["target_name"] + ".[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]" + data["situation"] + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]Какие пункты каких законов были по вашему мнению: " + data["laws"] + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]В связи с выше указанной ситуацией, я прошу Прокуратуру штата Аризона " + data["request"] + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]Видео доказательства: " + data["video"] + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]Основной документ удостоверяющий личность: " + data["passport"] + "[/COLOR][/FONT]\n"
            "[/CENTER]\n"
            "[RIGHT][FONT=book antiqua][COLOR=rgb(239, 239, 239)]Дата : " + today + "[/COLOR][/FONT]\n"
            "[FONT=book antiqua][COLOR=rgb(239, 239, 239)]Подпись : " + data["name"] + "[/COLOR][/FONT][/RIGHT]\n"
        )
        user_state.pop(uid, None)
        await message.answer("✅ Обращение готово! Скопируйте и вставьте на форум:", keyboard=main_keyboard(uid))
        await message.answer(bbcode)
        if ADMIN_ID:
            try:
                adm_text = (
                    "📄 НОВОЕ ОБРАЩЕНИЕ\n"
                    "👤 " + data["name"] + "\n"
                    "🔗 " + data["vk"] + "\n"
                    "📞 " + data["phone"] + "\n"
                    "🎯 " + data["target_type"] + " " + data["target_name"] + "\n"
                    "📌 " + data["situation"] + "\n"
                    "⚖️ " + data["laws"] + "\n"
                    "🙏 " + data["request"] + "\n"
                    "🎥 " + data["video"] + "\n"
                    "🪪 " + data["passport"] + "\n"
                    "🔗 vk.com/id" + str(uid)
                )
                await bot.api.messages.send(user_id=ADMIN_ID, message=adm_text, random_id=0)
            except Exception:
                pass

    # ========== АНКЕТА ==========
    elif step == "nickname":
        data["nickname"] = text
        state["step"] = "position"
        await message.answer("2️⃣ Ваша должность:", keyboard=cancel_keyboard())
    elif step == "position":
        data["position"] = text
        state["step"] = "reason"
        await message.answer("3️⃣ Причина обращения:", keyboard=cancel_keyboard())
    elif step == "reason":
        data["reason"] = text
        state["step"] = "demands"
        await message.answer("4️⃣ Исковые требования:", keyboard=cancel_keyboard())
    elif step == "demands":
        data["demands"] = text
        state["step"] = "help"
        await message.answer("5️⃣ В чём помощь адвоката?", keyboard=cancel_keyboard())
    elif step == "help":
        data["help_needed"] = text
        state["step"] = "evidence"
        await message.answer("6️⃣ Есть доказательства?", keyboard=evidence_keyboard())
    elif step == "evidence":
        data["evidence"] = text
        state["step"] = "contact"
        await message.answer("7️⃣ Контакт для связи:", keyboard=cancel_keyboard())
    elif step == "contact":
        data["contact"] = text
        cases = load(CASES_FILE, {})
        case_id = str(len(cases) + 1)
        cases[case_id] = {
            "nickname": data["nickname"],
            "position": data["position"],
            "reason": data["reason"],
            "demands": data["demands"],
            "help_needed": data["help_needed"],
            "evidence": data["evidence"],
            "contact": data["contact"],
            "vk_id": uid,
            "status": "new",
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        save(CASES_FILE, cases)
        stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
        stats["total"] = stats.get("total", 0) + 1
        save(STATS_FILE, stats)
        user_state.pop
