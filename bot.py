import os
import json
from datetime import datetime

from vkbottle.bot import Bot, Message
from vkbottle import Keyboard
from vkbottle import KeyboardButtonColor, Text

TOKEN = "vk1.a.ecbtcW2hykGmDFJUGeXZkZ7OTO6M9PCUgV-_dsfhp0ni-1Ao5Bx_stngT_jTw7MFaJnfohMqNhTgOTVjQGOjIeJqryWXipmHvsLLQjIDyPUgVMG4w5NbczMQJPUADosV2fGNaLyYWrQxv306SdzQNK5rK1DI9sHdN0Ojb4ZECtdnh9irdW1H6SaLBPmrntcOpjUtnG5EhSJQa_B-xuD8uA"
ADMIN_ID = 758865307
RESET_PASSWORD = "kaischwartz22072011"

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
    kb.add(Text("✅ Выиграно"), color=KeyboardButtonColor.POSITIVE)
    kb.row()
    kb.add(Text("❌ Проиграно"), color=KeyboardButtonColor.NEGATIVE)
    kb.add(Text("🗑 Удалить дело"), color=KeyboardButtonColor.NEGATIVE)
    kb.row()
    kb.add(Text("➕ Добавить в портфолио"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("✏️ Изменить прайс"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("✏️ Изменить резюме"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("📊 Моя статистика"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("⭐ Все отзывы"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("📤 Экспорт дел"), color=KeyboardButtonColor.SECONDARY)
    kb.row()
    kb.add(Text("👤 Режим клиента"), color=KeyboardButtonColor.SECONDARY)
    kb.add(Text("🔄 Сбросить статистику"), color=KeyboardButtonColor.NEGATIVE)
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


@bot.on.message(text="❌ Отмена")
async def cancel_handler(message: Message):
    uid = message.from_id
    user_state.pop(uid, None)
    if uid == ADMIN_ID and admin_mode.get(uid) == "admin":
        kb = admin_keyboard()
    else:
        kb = main_keyboard(uid)
    await message.answer("❌ Отменено.", keyboard=kb)


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
    won = s["won"]
    lost = s["lost"]
    if (won + lost) > 0:
        winrate = round(won / (won + lost) * 100)
    else:
        winrate = 0
    if s["ratings"]:
        avg_rating = round(sum(s["ratings"]) / len(s["ratings"]), 1)
    else:
        avg_rating = "—"
    text = (
        "📊 СТАТИСТИКА АДВОКАТА\n"
        "👨‍⚖️ Kai Schwartz\n"
        "━━━━━━━━━━━━━━━━━\n\n"
        "📁 Всего дел: " + str(s["total"]) + "\n"
        "✅ Выиграно: " + str(won) + "\n"
        "❌ Проиграно: " + str(lost) + "\n"
        "🆘 Экстренных: " + str(s["emergency"]) + "\n\n"
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


@bot.on.message(text="✅ Выиграно")
async def won_case_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "result_won", "data": {}}
    await message.answer("🏆 Введите номер выигранного дела:", keyboard=cancel_keyboard())


@bot.on.message(text="❌ Проиграно")
async def lost_case_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "result_lost", "data": {}}
    await message.answer("❌ Введите номер проигранного дела:", keyboard=cancel_keyboard())


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


@bot.on.message(text="🔄 Сбросить статистику")
async def reset_stats_start(message: Message):
    if message.from_id != ADMIN_ID:
        return
    user_state[message.from_id] = {"step": "reset_pass", "data": {}}
    await message.answer(
        "🔐 Введите секретный пароль для сброса:",
        keyboard=cancel_keyboard()
    )


@bot.on.message()
async def universal_handler(message: Message):
    uid = message.from_id
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

    if step == "reset_pass":
        if text == RESET_PASSWORD:
            save(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
            save(REVIEWS_FILE, [])
            save(CASES_FILE, {})
            save(CALLS_FILE, {})
            user_state.pop(uid, None)
            await message.answer(
                "✅ СТАТИСТИКА СБРОШЕНА!\n\n"
                "📁 Всего дел: 0\n"
                "✅ Выиграно: 0\n"
                "❌ Проиграно: 0\n"
                "🆘 Экстренных: 0\n"
                "⭐ Отзывов: 0\n\n"
                "Все данные обнулены.",
                keyboard=admin_keyboard()
            )
        else:
            user_state.pop(uid, None)
            await message.answer(
                "❌ НЕВЕРНЫЙ ПАРОЛЬ!\n\nСброс отменён.",
                keyboard=admin_keyboard()
            )
        return

    if step == "nickname":
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
        stats["total"] += 1
        save(STATS_FILE, stats)
        user_state.pop(uid, None)
        await message.answer("✅ Анкета #" + case_id + " отправлена!", keyboard=get_kb())
        if ADMIN_ID:
            try:
                adm_text = (
                    "🔔 АНКЕТА #" + case_id + "\n"
                    "👤 " + data["nickname"] + "\n"
                    "💼 " + data["position"] + "\n"
                    "📌 " + data["reason"] + "\n"
                    "⚖️ " + data["demands"] + "\n"
                    "🤝 " + data["help_needed"] + "\n"
                    "📎 " + data["evidence"] + "\n"
                    "📞 " + data["contact"] + "\n"
                    "🔗 vk.com/id" + str(uid)
                )
                await bot.api.messages.send(user_id=ADMIN_ID, message=adm_text, random_id=0)
            except Exception:
                pass
    elif step == "em_nick":
        data["nickname"] = text
        state["step"] = "em_place"
        await message.answer("2️⃣ Где вы находитесь?", keyboard=cancel_keyboard())
    elif step == "em_place":
        data["place"] = text
        state["step"] = "em_sit"
        await message.answer("3️⃣ Что случилось?", keyboard=cancel_keyboard())
    elif step == "em_sit":
        data["situation"] = text
        calls = load(CALLS_FILE, {})
        call_id = str(len(calls) + 1)
        calls[call_id] = {
            "nickname": data["nickname"],
            "place": data["place"],
            "situation": data["situation"],
            "vk_id": uid,
            "time": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "status": "new"
        }
        save(CALLS_FILE, calls)
        stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
        stats["emergency"] += 1
        save(STATS_FILE, stats)
        user_state.pop(uid, None)
        await message.answer("🔴 ВЫЗОВ ПРИНЯТ!", keyboard=get_kb())
        if ADMIN_ID:
            try:
                adm_text = (
                    "🔴 ВЫЗОВ #" + call_id + "\n"
                    "👤 " + data["nickname"] + "\n"
                    "📍 " + data["place"] + "\n"
                    "⚡ " + data["situation"] + "\n"
                    "🔗 vk.com/id" + str(uid)
                )
                await bot.api.messages.send(user_id=ADMIN_ID, message=adm_text, random_id=0)
            except Exception:
                pass
    elif step == "rev_rate":
        try:
            r = int(text)
            if 1 <= r <= 5:
                state["data"]["rating"] = r
                state["step"] = "rev_text"
                await message.answer("✍️ Напишите отзыв:", keyboard=cancel_keyboard())
            else:
                await message.answer("Введите число от 1 до 5.")
        except ValueError:
            await message.answer("Введите число от 1 до 5.")
    elif step == "rev_text":
        reviews = load(REVIEWS_FILE, [])
        reviews.append({
            "vk_id": uid,
            "rating": state["data"]["rating"],
            "text": text,
            "date": datetime.now().strftime("%d.%m.%Y")
        })
        save(REVIEWS_FILE, reviews)
        stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
        stats["ratings"].append(state["data"]["rating"])
        save(STATS_FILE, stats)
        user_state.pop(uid, None)
        await message.answer("✅ Спасибо за отзыв!", keyboard=get_kb())
        if ADMIN_ID:
            try:
                stars = "⭐" * state["data"]["rating"]
                adm_text = (
                    "⭐ ОТЗЫВ\n"
                    + stars + " (" + str(state["data"]["rating"]) + "/5)\n"
                    "От: vk.com/id" + str(uid) + "\n"
                    + text
                )
                await bot.api.messages.send(user_id=ADMIN_ID, message=adm_text, random_id=0)
            except Exception:
                pass
    elif step == "take_id":
        cases = load(CASES_FILE, {})
        if text in cases:
            cases[text]["status"] = "in_work"
            save(CASES_FILE, cases)
            user_state.pop(uid, None)
            await message.answer("⚙️ Дело #" + text + " в работе!", keyboard=admin_keyboard())
        else:
            await message.answer("❌ Дело не найдено.", keyboard=cancel_keyboard())
    elif step == "result_won":
        case_id = text.strip()
        cases = load(CASES_FILE, {})
        stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
        stats["won"] += 1
        save(STATS_FILE, stats)
        if case_id in cases:
            cases[case_id]["status"] = "closed"
            save(CASES_FILE, cases)
        user_state.pop(uid, None)
        await message.answer("🏆 Дело #" + case_id + " ВЫИГРАНО!", keyboard=admin_keyboard())
    elif step == "result_lost":
        case_id = text.strip()
        cases = load(CASES_FILE, {})
        stats = load(STATS_FILE, {"total": 0, "won": 0, "lost": 0, "emergency": 0, "ratings": []})
        stats["lost"] += 1
        save(STATS_FILE, stats)
        if case_id in cases:
            cases[case_id]["status"] = "closed"
            save(CASES_FILE, cases)
        user_state.pop(uid, None)
        await message.answer("❌ Дело #" + case_id + " проиграно.", keyboard=admin_keyboard())
    elif step == "pf_type":
        data["case_type"] = text
        state["step"] = "pf_client"
        await message.answer("Ник клиента:")
    elif step == "pf_client":
        data["client"] = text
        state["step"] = "pf_result"
        await message.answer("Результат:")
    elif step == "pf_result":
        data["result"] = text
        state["step"] = "pf_desc"
        await message.answer("Описание:")
    elif step == "pf_desc":
        data["description"] = text
        state["step"] = "pf_fee"
        await message.answer("Гонорар ($):")
    elif step == "pf_fee":
        data["fee"] = text
        portfolio = load(PORTFOLIO_FILE, [])
        portfolio.append(data)
        save(PORTFOLIO_FILE, portfolio)
        user_state.pop(uid, None)
        await message.answer("✅ Добавлено в портфолио!", keyboard=admin_keyboard())
    elif step == "del_id":
        cases = load(CASES_FILE, {})
        if text in cases:
            del cases[text]
            save(CASES_FILE, cases)
            user_state.pop(uid, None)
            await message.answer("🗑 Дело #" + text + " удалено.", keyboard=admin_keyboard())
        else:
            await message.answer("❌ Дело не найдено.", keyboard=cancel_keyboard())
    elif step == "edit_price":
        save(PRICE_FILE, {"text": text})
        user_state.pop(uid, None)
        await message.answer("✅ Прайс обновлён!", keyboard=admin_keyboard())
    elif step == "edit_profile":
        save(PROFILE_FILE, {"text": text})
        user_state.pop(uid, None)
        await message.answer("✅ Резюме обновлено!", keyboard=admin_keyboard())


if __name__ == "__main__":
    print("🤖 VK-бот запущен!")
    bot.run_forever()
